# Sol lane judge validation: reconciliation (2026-07-13)

The GPT-5.6 Sol lane (runs/gpt56sol-subset20, 20 graded records) received the same
judge-validation protocol as the original 2026-07-02 trifecta, rerun end to end on
2026-07-13. Three legs completed the same night; the blind human leg's pack is
generated and sealed, with Khiem's verdicts to be appended below when graded.

## 1. Leg results

- **Cross-family re-judge (all 20 records):** gemini-2.5-flash re-graded every Sol
  record under the same rubrics. Strict agreement 17/20 (0.85), mean absolute
  partial difference 0.176. All three splits hand-adjudicated in section 3; the
  primary verdict was upheld in each. Artifact: judge_agreement_gpt56sol.json.
- **Transport recheck (6 stratified tasks: idx 3, 7, 25, 38, 43, 44):** gpt-5.4-mini
  re-graded via the direct OpenAI API against the original OpenRouter-transport
  grades. Strict agreement 6/6, exact-partial agreement 6/6 (including Delta idx
  38's 0.833 reproduced exactly). Artifact: judge_transport_check_gpt56sol.json.
- **Adversarial blind re-grade (10-task pack):** an independent grader (Claude
  Sonnet, fresh session, given ONLY handgrade_sheet_sol.md, never the key) graded
  all 10 tasks adversarially with quoted decisive evidence per check. Strict
  verdicts matched the sealed key 10/10. Check-level notes in section 4.
- **Blind human hand-grade:** the 10-task pack (5 judge-pass / 5 judge-fail,
  8 categories, order shuffled) was graded blind by Khiem Doan in the published
  Google Sheet on 2026-07-13, every check filled. Strict verdicts agreed with the
  sealed key 10/10, and with the adversarial grader 10/10: three-way unanimity on
  all ten strict verdicts.

## 2. Per-task table (adversarial vs sealed key)

| Task | Category | Question | Adversarial strict | Khiem strict | Judge strict (key) | Agree |
|---|---|---|---|---|---|---|
| 1 | Complex Retrieval | KKR Series D mandatory convertible terms | 0 | 0 | 0 (partial 0.818) | YES |
| 2 | Numerical Reasoning | Palantir 3-year revenue CAGR | 0 | 0 | 0 (partial 0.333) | YES |
| 3 | Numerical Reasoning | Microsoft % full-time employees in US | 1 | 1 | 1 | YES |
| 4 | Quantitative Retrieval | Airbnb 2024 average nights per booking | 1 | 1 | 1 | YES |
| 5 | Qualitative Retrieval | Shift4 vendor concentration risk | 1 | 1 | 1 | YES |
| 6 | Adjustments | Boeing net-income impact of +3pt refinancing | 0 | 0 | 0 (partial 0.000) | YES |
| 7 | Beat or Miss | Lyft Q4'24 Adjusted EBITDA margin vs guidance | 1 | 1 | 1 | YES |
| 8 | Quantitative Retrieval | TKO total consideration at transaction close | 0 | 0 | 0 (partial 0.000) | YES |
| 9 | Financial Modeling | Snap maximum dilutive shares from converts | 1 | 1 | 1 | YES |
| 10 | Market Analysis | Zillow acquisition strategy vs revenue mix | 0 | 0 | 0 (partial 0.333) | YES |

Adversarial-vs-key strict agreement: **10/10**. Human-vs-key strict agreement:
**10/10** (every check-level dropdown filled; task-level notes recorded below).
Three-way agreement (human, adversarial, sealed key): **10/10**.

Khiem's grading notes flagged three tasks for expert review while still scoring
them against the current key: task 2 (the CAGR-period definition), task 6 (the
refinancing methodology), and task 8 (the requested-basis wording). Those are the
same three ambiguities independently documented in sections 3 and 4 below: the
blind human leg surfaced them without seeing the key, the cross-family split, or
the adversarial notes.

## 3. Cross-family split adjudications (all three upheld)

**Split 1, idx 6 (Airbnb CFO): mini strict 1, gemini strict 0. UPHELD (mini).**
The agent answered "Ellie Mertz"; the reference names "Elinor Mertz." The primary
judge passed it as the same person under a standard short form (Airbnb's own
communications use Ellie Mertz). The Gemini judge failed the literal string. This
is an accepted-equivalents case: the entity is identical, only the name form
differs. Root cause class: semantic-equivalence handling, exactly the concept-level
criteria (canonical facts plus accepted equivalents) that expert-authored rubrics
pin explicitly.

**Split 2, idx 7 (TKO): mini strict 0, gemini strict 1. UPHELD (mini) under the key,
and the split itself is a finding.** Sol submitted a $4.00 billion close-date
valuation; the key expects the filing's stated $3.25 billion consideration. The
primary judge failed the answer and fired the contradiction gate. Given the SAME
rubric, the Gemini judge PASSED it (strict 1, partial 1.0), accepting the
close-date construction as answering "measured at transaction close." Under keyed
grading the primary verdict stands: the reference answer is unambiguous at $3.25B.
But two judge families reading the same rubric opposite ways is measured evidence
that the prompt phrase "measured at transaction close" admits a spot-price reading.
The training-pack fix already specified for this task (requested valuation basis as
its own atomic check) is exactly what removes this ambiguity.

**Split 3, idx 20 (Shift4): mini strict 1, gemini strict 0 (partial 0.5). UPHELD
(mini).** Both required facts are verbatim present in the agent answer: the
single-vendor North American processing disclosure and the vendor's backup systems
and alternative arrangements. The Gemini judge credited one check and not the
other; the primary judge's per-check reasoning quotes the satisfying sentence for
both. Root cause class: under-crediting a present fact.

Adjudication summary: 3 splits, primary upheld 3/3. One equivalence strictness
error against the answer, one under-credit against the answer, one leniency in the
answer's favor on the task whose prompt ambiguity is separately documented. No Sol
grade changes.

## 4. Adversarial check-level notes (strict verdicts all agreed)

- **Task 1 (KKR):** the adversarial grader marked 5 additional checks FAIL as
  "absent from the given text" and itself flagged that the sheet's 3,000-character
  clip cut the agent answer mid-word. The sealed key's judge, grading the full
  answer, scored those checks differently (partial 0.818, 9 of 11 checks passing,
  with the real misses being the assembled 51,750,000 total and the common-dividend
  restriction). DISCLOSURE: the pack's display clip means check-level counts are
  not comparable on this task; the strict verdicts (0 and 0) agree regardless, for
  overlapping reasons. The original 2026-07-02 protocol carried the same 3,000-char
  display clip.
- **Task 2 (Palantir):** the adversarial grader independently noted the reference
  pairs FY2022 with FY2024 while labeling it a 3-year CAGR, the same base-year
  convention issue documented in the Palantir deep-dive card. Verdict agreed 0.
- **Task 8 (TKO):** the adversarial grader independently flagged "measured at
  transaction close" as "genuinely ambiguous" while agreeing the reference is
  unambiguous at $3.25B and scoring 0. Third independent surface for the same
  basis-ambiguity lesson (primary judge's contradiction reasoning, the Gemini
  split, and now the blind adversarial note).
- **Task 10 (Zillow):** the adversarial grader treated the agent's "Aug. 2023" for
  Aryeo against the reference's July 31 as a contradiction; Zillow's own newsroom
  dated the announcement August 2, 2023, so agreement-vs-signing date granularity
  is a rubric-specification nuance. Verdict agreed 0 on independent grounds
  (a required revenue-decline element absent and a different strategic-thesis
  framing).

## 5. Methodology disclosure

Same protocol as the original 2026-07-02 validation: the blind pack was generated
by the same stratified sampler (seed 42, 5 judge-pass / 5 judge-fail, category cap,
shuffled order); the adversarial grader was a fresh Claude Sonnet session with
access to exactly one file (the blind sheet) and no knowledge of any verdict; the
cross-family judge is a different model family (Gemini) from the primary
(gpt-5.4-mini, OpenAI) and from the adversarial grader (Claude); the sealed key was
opened only after the adversarial verdicts were returned. The main-session model
(Claude Fable) performed the reconciliation and adjudications in this document; the
adversarial grades themselves came from the separate blind session. Costs:
cross-family ~$0.02, transport well under $1, adversarial $0 API (in-session
compute).

## 6. Ratification

- Adversarial leg: COMPLETE, 10/10 vs sealed key, recorded above.
- Cross-family and transport legs: COMPLETE, artifacts committed.
- Blind human leg: COMPLETE. Khiem Doan graded all 10 tasks blind in the
  published Google Sheet on 2026-07-13 (every check dropdown filled, per-task
  notes recorded) and confirmed in-session. Human-vs-key 10/10; three-way
  unanimity across human, adversarial, and sealed key on all ten strict verdicts.

**RATIFIED via the graded sheet plus in-session confirmation, Khiem Doan,
2026-07-13.** All ten verdicts final as graded. The three tasks he flagged for
expert review (2, 6, 8) stand as scored under the current key, with the flags
preserved above as rubric-specification findings, consistent with sections 3-4.
