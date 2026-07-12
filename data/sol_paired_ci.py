"""Paired clustered bootstrap: GPT-5.6 Sol vs each incumbent frontier on the
identical 20. Same method as paired_frontier_ci.py (company clusters, 2,000
resamples); zero new model calls. Writes analysis/sol_paired_ci.json.
The original paired_frontier_ci.py is untouched by design."""
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
REPO = Path(__file__).resolve().parent.parent

SUBSET = [0, 1, 3, 6, 7, 9, 15, 20, 23, 25, 29, 30, 32, 33, 37, 38, 43, 44, 45, 48]
TAGS = {"sol": "gpt56sol-subset20", "gpt55": "gpt55-full", "fable5": "fable5-subset20"}

companies = json.loads((REPO / "data" / "task_companies.json").read_text(encoding="utf-8"))


def company_of(idx):
    v = companies.get(str(idx), companies.get(idx, f"task-{idx}"))
    if isinstance(v, dict):
        v = v.get("company") or v.get("name") or json.dumps(v, sort_keys=True)
    return str(v)


def grades(tag):
    recs = {}
    for line in (REPO / "runs" / tag / "grades.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r["idx"]] = r  # latest record per idx wins
    return recs


g = {k: grades(t) for k, t in TAGS.items()}
out = {
    "note": ("Paired task-by-task strict-score difference (sol - incumbent) on the "
             "identical 20, company-clustered bootstrap (2,000 resamples, seed "
             "20260712). Zero new model calls; computed from grades already on "
             "disk by analysis/sol_paired_ci.py."),
    "n_tasks": len(SUBSET),
    "resamples": 2000,
    "seed": 20260712,
    "pairs": {},
}

for inc in ("gpt55", "fable5"):
    diffs_by_cluster = defaultdict(list)
    flips_sol_worse, flips_sol_better = [], []
    for idx in SUBSET:
        d = int(g["sol"][idx]["strict_score"]) - int(g[inc][idx]["strict_score"])
        diffs_by_cluster[company_of(idx)].append(d)
        if d < 0:
            flips_sol_worse.append(idx)
        elif d > 0:
            flips_sol_better.append(idx)
    clusters = list(diffs_by_cluster.values())
    n = len(SUBSET)
    point = sum(sum(c) for c in clusters) / n
    rng = random.Random(20260712)
    means = []
    for _ in range(2000):
        resample = [rng.choice(clusters) for _ in range(len(clusters))]
        vals = [d for c in resample for d in c]
        means.append(sum(vals) / len(vals))
    means.sort()
    lo, hi = means[int(0.025 * len(means))], means[int(0.975 * len(means))]
    agree = n - len(flips_sol_worse) - len(flips_sol_better)
    print(f"sol - {inc}: point {point*100:+.1f} pts, 95% clustered CI "
          f"[{lo*100:+.1f}, {hi*100:+.1f}], agreement {agree}/{n}, "
          f"flips sol-worse={flips_sol_worse} sol-better={flips_sol_better}, "
          f"{len(clusters)} clusters")
    out["pairs"][f"sol_vs_{inc}"] = {
        "point_pts": round(point * 100, 1),
        "ci95_lo_pts": round(lo * 100, 1),
        "ci95_hi_pts": round(hi * 100, 1),
        "agreement": f"{agree}/{n}",
        "n_clusters": len(clusters),
        "flips_sol_worse_idx": flips_sol_worse,
        "flips_sol_better_idx": flips_sol_better,
    }

(REPO / "analysis" / "sol_paired_ci.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8")
print("wrote analysis/sol_paired_ci.json")
