# Benchmark defect catalog (primary-source adjudicated, 2026-07-13)

Six candidate-defect tasks from the full-50 frontier runs were adjudicated against primary SEC filings by six independent agents. **Four are confirmed benchmark key/spec defects** (the model was right or defensible and the benchmark's own answer key or task spec is wrong); two are genuine model failures. Two additional key defects (idx 0, 14) were already documented. This is a partial adjudication: the remaining unflagged failures (idx 5, 13, 24, 31, 35, 46, 49) are not yet primary-source-verified.

## Confirmed benchmark defects (unscoreable, excluded from the clean-subset)

### idx 11 - TSMC Q1 2025 guidance (KEY DEFECT)
The key states guidance of $25.0-25.4B at NT$32.9/USD and grades the task a "-1.0% miss." TSMC's official Q4 2024 release (pr.tsmc.com/english/news/3201, Jan 16 2025; SEC 6-K) states the real guidance verbatim: "$25.0 billion and $25.8 billion" at "1 US dollar to 32.8 NT dollars." The key mislabeled the range *midpoint* ($25.4B) as the *top* and mistyped the FX rate; its own headline figure NT$833,120M = 25.4 x 32.8 proves it. Actual Q1 2025 revenue (news/3219, news/3222) was US$25.53B, a beat. **The model's answer ($25.0-25.8B @ NT$32.8) matches the filing; the key does not.**

### idx 28 - Spirit Airlines FY2024 unit metrics (KEY DEFECT)
The key's TRASM ($0.93) and Adjusted CASM ex-fuel ($0.80) are each off by exactly 10x and internally self-contradictory (ex-fuel CASM listed *larger* than total CASM; an ~88% per-ASM margin for a carrier in Chapter 11). Spirit's FY2024 10-K (SEC EDGAR, save-20241231.htm, Comparative Operating Statistics p.70) reports TRASM 9.27 cents and Adjusted CASM ex-fuel 7.97 cents. **The model matches the filing digit-for-digit on all five metrics; two key values are arithmetically wrong.**

### idx 41 - Coca-Cola dividend payout vs competitors (SPEC DEFECT)
The question asks to "compare the FY24 dividend payout ratio of Coca-Cola to that of its competitors" and names no competitor set. The key silently requires Kraft Heinz and Smucker (GICS Packaged Foods, not beverage rivals) and strict-fails the model purely for not naming them. The model's own KO payout ratio (~79%) is correct against the filing and its competitor picks (PepsiCo, Keurig Dr Pepper, Monster) are at least as defensible. **The spec imposes an unstated grading requirement.**

### idx 42 - Uber 2024 revenue growth decomposition (SPEC DEFECT)
Both the key and the model are correct on the merits (Uber FY2024 10-K, uber-20241231.htm: revenue +18%, gross bookings +18%, take rate ~27.0% flat). The model's take-rate-vs-volume bridge is arithmetically exact and reaches the key's own conclusion. The failed checks penalize it only for not reciting the key's supplementary segment color, which the question ("what portion of growth was take-rate vs volume") never asks for. **The checks reward verbatim reproduction, not correctness.**

### idx 0 - US Steel / Nippon (KEY DEFECT, pre-known)
Reference anchored to the Dec-2023 unsolicited-offer framing, never updated for the actual 2025-06-18 merger close; five models penalized against the stale key.

### idx 14 - US Steel inventory turnover (KEY DEFECT, pre-known)
The reference "Avg. Inventory: $2,168" is actually FY2024 *ending* inventory, mislabeled as an average; the correct average-of-two-years turnover differs from the keyed figure.

## Adjudicated as genuine model failures (kept as fails)

### idx 47 - Lemonade FY2024 vs guidance (mixed: 1 spec defect, but task fails)
The flagged "at high end" vs "within range" check IS a spec defect ($943.7M IFP is within the $940-944M range, $0.3M below the top). But the task strict-fails on independent, legitimate completeness grounds: the answer never mentions stock-based comp, capex, or weighted shares. **Kept as a genuine completeness failure.**

### idx 21 - Airbnb GBV per night (MODEL MISS)
The key ($160.44 / $163.51 / $166.23) is triple-verified correct across three separate Airbnb 10-Ks (FY22/23/24, EDGAR). The model's FY2022 figure ($160.32) is 12-21 cents off and not explainable as a rounding convention. **Kept as a genuine model miss.**

## Impact

Excluding the 6 confirmed-defect items (0, 11, 14, 28, 41, 42) as unscoreable, clean-subset strict accuracy rises: GPT-5.5 67.3% -> 76.7% (33/43), Claude Fable 5 62.0% -> 70.5% (31/44), GPT-5.6 Sol 53.1% -> 60.5% (26/43). Every model was strict-failed on all six defect items, so the raw scores systematically understate frontier performance. This is a conservative floor: seven further failures remain to be adjudicated.

**The point for the pitch:** four benchmark key/spec defects with SEC citations, surfaced in a six-task adjudication sample, on a specialist finance benchmark. No automated judge catches a wrong answer key; only source-backed human adjudication does. This is the product.
