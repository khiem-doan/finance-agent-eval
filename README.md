# Grading the Frontier on Finance Agent Work

Interactive results site for an independent evaluation of 8 models on the
Vals AI Finance Agent benchmark's 50 public tasks: an adapted copy of the
official harness, an independently validated LLM judge, a hand-classified
failure taxonomy with full trajectory evidence, and measured per-task costs.

Live site: https://khiem-doan.github.io/finance-agent-eval/

- `index.html` - the full interactive report (static, no build step; view source)
- `slides.pdf` - the 5-slide walkthrough deck
- `data/` - the evidence files every number on the site traces to: per-run
  summaries and cluster-bootstrap CIs, per-task costs, the identical-20-task
  frontier slice, judge cross-family/transport checks, a semantic diff of
  the benchmark's two public copies, the task-type taxonomy and failure-mode
  glossary, the per-trace failure instances behind the failure stack, the
  held-out task candidates (specs with SEC citations and atomic checks), the
  lab proposal content, the market-thesis source list, and the two frontier
  grading records (check-by-check judge output) behind the rubric scoreboards.

Built by Khiem Doan. External reference numbers (the benchmark paper's human
baseline, public leaderboard figures) are labeled as external wherever cited.
