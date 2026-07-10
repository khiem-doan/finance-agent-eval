"""Paired clustered bootstrap of the frontier score difference + subset
representativeness check. Zero new model calls: grades already on disk."""
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
REPO = Path(__file__).resolve().parent.parent

sub = json.loads((REPO / "analysis" / "frontier_subset.json").read_text(encoding="utf-8"))
companies = json.loads((REPO / "data" / "task_companies.json").read_text(encoding="utf-8"))

rows = sub["per_task"] if isinstance(sub, dict) and "per_task" in sub else sub
print("frontier_subset keys:", list(sub.keys()) if isinstance(sub, dict) else "list")
sample = rows[0]
print("per-task row keys:", list(sample.keys()))

def company_of(idx):
    v = companies.get(str(idx), companies.get(idx, f"task-{idx}"))
    if isinstance(v, dict):
        v = v.get("company") or v.get("name") or json.dumps(v, sort_keys=True)
    return str(v)

# Build paired diffs per task: gpt55_strict - fable5_strict
diffs_by_cluster = defaultdict(list)
n = 0
for r in rows:
    idx = r["idx"]
    d = int(r["gpt55_strict"]) - int(r["fable5_strict"])
    diffs_by_cluster[company_of(idx)].append(d)
    n += 1
clusters = list(diffs_by_cluster.values())
point = sum(sum(c) for c in clusters) / n
print(f"\nPAIRED DIFFERENCE (gpt55 - fable5), n={n} tasks, {len(clusters)} company clusters")
print(f"point estimate: {point:+.4f} ({point*100:+.1f} points)")

rng = random.Random(20260710)
means = []
for _ in range(2000):
    resample = [rng.choice(clusters) for _ in range(len(clusters))]
    vals = [d for c in resample for d in c]
    means.append(sum(vals) / len(vals))
means.sort()
lo, hi = means[int(0.025 * len(means))], means[int(0.975 * len(means))]
print(f"95% clustered bootstrap CI of the difference: [{lo*100:+.1f}, {hi*100:+.1f}] points")

out = {
    "note": ("Paired task-by-task strict-score difference (gpt55 - fable5) on the "
             "identical 20, company-clustered bootstrap (2,000 resamples, seed "
             "20260710). Also: subset-vs-full representativeness for the two "
             "models with full-50 runs. Zero new model calls; computed from "
             "grades already on disk by analysis/paired_frontier_ci.py."),
    "n_tasks": n,
    "n_clusters": len(clusters),
    "resamples": 2000,
    "point_pts": round(point * 100, 1),
    "ci95_lo_pts": round(lo * 100, 1),
    "ci95_hi_pts": round(hi * 100, 1),
    "representativeness": [],
}

# Representativeness: subset-20 score vs full graded basis for full-50 runs
subset_idx = {r["idx"] for r in rows}
print(f"\nREPRESENTATIVENESS CHECK (subset of {len(subset_idx)} vs full graded basis)")
for tag in ["gpt55-full", "nano-full"]:
    recs = {}
    for line in (REPO / "runs" / tag / "grades.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r["idx"]] = r  # latest record per idx wins
    full = list(recs.values())
    on_subset = [r for r in full if r["idx"] in subset_idx]
    fs = sum(r["strict_score"] for r in full) / len(full)
    ss = sum(r["strict_score"] for r in on_subset) / len(on_subset)
    print(f"{tag}: subset {sum(r['strict_score'] for r in on_subset)}/{len(on_subset)} = {ss*100:.1f}% | "
          f"full graded {sum(r['strict_score'] for r in full)}/{len(full)} = {fs*100:.1f}% | gap {abs(fs-ss)*100:.1f} pts")
    out["representativeness"].append({
        "run": tag,
        "subset_passed": sum(r["strict_score"] for r in on_subset),
        "subset_n": len(on_subset),
        "subset_pct": round(ss * 100, 1),
        "full_passed": sum(r["strict_score"] for r in full),
        "full_n": len(full),
        "full_pct": round(fs * 100, 1),
        "gap_pts": round(abs(fs - ss) * 100, 1),
    })

(REPO / "analysis" / "paired_ci.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8")
print("\nwrote analysis/paired_ci.json")
