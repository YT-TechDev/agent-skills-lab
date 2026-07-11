# GitHub Standard Engineering Review — Evaluation Plan

## 1. Status and boundary

- Canonical name: `github-standard-engineering-review`.
- Status: specification draft.
- Lifecycle stage: evaluation-plan definition.
- Production package: not implemented.
- Production readiness: not established.
- Executable evaluation harness: not implemented.

This document defines evaluation questions, evaluation layers, dimensions, acceptance rules, golden-case coverage, human execution, observation recording, result statuses, regression comparison, and promotion evidence before package work.

This document does not provide executable tests, automated scoring, connector mocks, fixture repositories, production behavior, installation, publication, Deep Review evaluation, or observed platform results. This Issue records no observed results.

## 2. Evaluation questions

The evaluation asks whether a future implementation:

1. triggers for valid one-PR Standard Review requests and avoids non-trigger requests;
2. handles clarification, redirect, decline, cancellation, and `NO VERDICT` endings correctly;
3. establishes target and current head, refreshes evidence before verdict selection, and handles unknown current head honestly;
4. collects complete material evidence for the target, diff, governing requirements, CI, review state, and relevant discussions;
5. assigns evidence statuses correctly without turning unknown, inaccessible, stale, or contradictory facts into verified facts;
6. detects verified current-head blockers;
7. avoids false blockers for optional work, inaccessible evidence, or satisfied requirements;
8. handles material verification gaps without hiding them or overstating readiness;
9. selects the exact required verdict or `NO VERDICT`;
10. complies with the required output contract for the selected ending;
11. respects retry, fallback, stopping, and unstable-head behavior;
12. recomputes same-PR re-review from current evidence rather than retaining historical conclusions;
13. avoids unsupported claims;
14. maintains the Standard Review versus Deep Review boundary;
15. remains compatible with applicable Project instructions without importing repository-specific rules into the reusable Skill;
16. fails gracefully when required target, evidence, or tool access is unavailable.

## 3. Evaluation layers

Keep these layers separate in every evaluation record:

1. **Specification conformance**: whether the written implementation instructions, prompts, or package draft match the current repository specifications.
2. **Observed ChatGPT Skill behavior**: what a user-visible run actually produced in a dated product surface.
3. **Tool and connector capability**: whether available GitHub, file, CI, review-thread, or other read-only access can provide required evidence.
4. **Repository static validation**: whether repository files satisfy static hygiene, link, artifact-boundary, and package-shape checks.

A connector limitation is not automatically a Skill logic failure. Mishandling a known limitation, fabricating missing facts, or selecting a verdict that the limitation cannot support may still be a Skill failure. Passing repository validation does not prove Skill behavior. Observed behavior must be dated and labeled as **Observed**, **Reproduced**, **Inferred**, **Unverified**, or **Changed since previous test**.

## 4. Evaluation-result statuses

These statuses classify evaluation assertions and cases only. They do not replace Standard Review evidence statuses or merge-readiness verdicts. Do not add numeric scores or confidence percentages.

- `PASS`: the applicable assertion or case met every required expectation with adequate evidence.
- `FAIL`: at least one required assertion was contradicted by observed output, inspected artifacts, or tool/access facts.
- `PARTIAL`: non-terminal coverage is incomplete, but the missing coverage is not itself a material inconclusive or verified failure for the assertion being recorded.
- `INCONCLUSIVE`: required evidence to decide the assertion was unavailable, ambiguous, stale, or contradictory, and no separate verified failure already decides the case.
- `NOT APPLICABLE`: the assertion or dimension does not apply to the case; this is not a pass.

## 5. Evaluation unit

Use a human-readable record, not a machine-readable schema. Each evaluation unit contains:

- implementation/version identifier;
- product surface/environment;
- test date and timezone;
- case ID;
- exact input;
- target/fictional fixture;
- available tools/connectors;
- expected trigger/ending;
- expected verdict or `NO VERDICT`;
- expected evidence/finding classifications;
- expected output obligations;
- observed user-visible output;
- tool/access facts;
- evidence references;
- per-dimension results;
- overall result;
- deviations;
- attribution;
- retest requirement.

## 6. Required evaluation dimensions

For every dimension, evaluate only applicable golden cases and record `NOT APPLICABLE` when the case does not exercise the dimension.

| # | Dimension | What is evaluated | Pass condition | Common failure examples | Applicable golden cases |
| --- | --- | --- | --- | --- | --- |
| 1 | Trigger precision | Whether the implementation starts, clarifies, redirects, declines, cancels, or continues correctly. | Valid review requests trigger; ambiguous, write-only, merge-only, Deep-Review-only, and cancellation cases do not emit a readiness verdict. | Running on implementation-only work; guessing a missing PR; issuing a verdict after cancellation. | TRG-01–TRG-05 |
| 2 | Target-state establishment | Repository, PR, and reviewed head handling. | Target and current head are established or explicitly unknown before evidence-dependent conclusions. | Reviewing an unstated PR; omitting reviewed head; treating unknown head as current. | TRG-01, TRG-02, GAP-01, GAP-06, RRV-01–RRV-03 |
| 3 | Evidence completeness and freshness | Material diff, requirements, CI, approval/thread, and re-review evidence coverage. | Current-head material evidence is inspected or recorded as a gap before verdict selection. | Using stale previous-head checks; omitting changed files; ignoring inaccessible CI. | POS-01–POS-03, BLK-01–BLK-05, GAP-01–GAP-06, RRV-01–RRV-03 |
| 4 | Governing requirement and applicability interpretation | Whether repository rules and optional criteria are classified correctly. | Required, optional, contradictory, and not-applicable criteria are distinguished. | Treating optional refactor as required; ignoring contradictory requirements. | POS-02, POS-03, GAP-05, BLK-04 |
| 5 | Blocker detection | Verified current-head merge blockers. | Expected blockers are surfaced with evidence and current-head association. | Missing correctness defect; ignoring failed required CI; omitting missing required approval. | BLK-01–BLK-05, RRV-03 |
| 6 | False-blocker avoidance | Avoidance of unsupported or optional blockers. | Inaccessible evidence, optional work, and satisfied criteria are not called blockers. | Blocking on optional Deep Review; calling inaccessible CI failed; retaining fixed blocker. | POS-02, POS-03, GAP-01–GAP-06, RRV-01 |
| 7 | Material verification-gap handling | Inaccessible, unknown, stale, or contradictory material evidence. | Gaps are classified as gaps and drive `UNABLE TO VERIFY` unless a verified blocker is already decisive. | Hiding a material gap; treating a gap as pass/fail; letting a gap override verified blocker precedence. | BLK-05, GAP-01–GAP-06, RRV-02 |
| 8 | Non-blocking-note quality | Optional notes and optional escalation. | Notes are evidence-based, clearly deferrable, and not disguised blockers. | Unrelated style opinions; mandatory wording for optional work; hidden blocker as note. | POS-02, POS-03 |
| 9 | Exact verdict selection | Required final verdict or `NO VERDICT`. | Exact expected verdict string or `NO VERDICT` is used; aliases do not pass. | “Looks good” instead of `MERGE READY`; `UNABLE TO VERIFY` for clarification; positive verdict despite blocker. | All cases |
| 10 | Output-contract compliance | Required sections, headings, compatible sections, evidence adjacency, and omissions. | Output matches the selected verdict and contains no empty or incompatible sections. | Two verdicts; missing limitations; blockers section under `MERGE READY`; evidence far from claim. | All cases, especially POS-01–POS-03, BLK-01–BLK-05, GAP-01–GAP-06 |
| 11 | Retry and stopping compliance | Bounded retries, fallback, and terminal stopping. | The implementation retries only within policy, records fallback, and stops when required. | Infinite retry; silent fallback; continuing after terminal evidence failure. | GAP-01–GAP-06 |
| 12 | Unstable-head handling | Head changes and refresh limits. | Unstable head is detected, bounded, and produces required stopping behavior. | Reviewing moving target as stable; claiming current verdict after repeated head changes. | GAP-06 |
| 13 | Same-PR re-review consistency | Reconfirmation, refresh, historical verdict handling, and recomputation. | Same PR is reconfirmed, head refreshed, old blockers re-verified, new scope inspected, and current verdict recomputed. | Retaining fixed blocker; trusting claimed fix; using delta instead of full review. | RRV-01–RRV-03 |
| 14 | Unsupported-claim avoidance | Claims about evidence, tests, approvals, safety, scope, and execution. | Every material readiness claim is supported by current evidence or labeled unknown. | Claiming files inspected without evidence; claiming risk-free; claiming CI passed from old head. | All cases |
| 15 | Standard Review versus Deep Review boundary | Review scope and escalation. | Deep Review-only requests are redirected; optional escalation does not claim audit completion. | Performing or claiming full security/privacy/architecture audit; making Deep Review required without evidence. | TRG-04, POS-03 |
| 16 | Correction and re-verification usefulness | Focused fix guidance and retest requirement. | Required corrections identify smallest useful fix and re-verification need. | Vague “fix issues”; unrelated next task under blockers; no retest requirement. | BLK-01–BLK-05, GAP-01–GAP-06, RRV-02, RRV-03 |
| 17 | Graceful failure | Behavior when target, evidence, or tools are unavailable. | The output explains the limitation, avoids unsupported conclusions, and requests the smallest missing evidence. | Fabricating connector results; failing closed without guidance; issuing readiness despite missing target. | TRG-02, GAP-01–GAP-06 |
| 18 | Project-instruction compatibility | Respect for applicable Project instructions. | Project instructions are applied when relevant and not treated as portable Skill defaults. | Ignoring explicit repo review rules; embedding this repository’s workflow as universal. | At least one selected case with Project instructions; TRG-01 or POS/BLK/GAP cases may be adapted for this check. |

## 7. Explicit acceptance rules

- Valid Standard Review requests trigger.
- Ambiguous targets clarify.
- Implementation-only, merge-only, and Deep-Review-only requests do not implicitly trigger Standard Review.
- Cancellation and target replacement emit `NO VERDICT`.
- Expected blockers are surfaced and associated with the current head.
- Inaccessible evidence is not converted into a blocker.
- Optional work is not treated as required.
- Failed, pending, and inaccessible required CI remain distinct.
- Missing approval and inaccessible approval state remain distinct.
- The exact expected verdict or `NO VERDICT` is required.
- Aliases do not pass.
- Output sections must match the selected verdict.
- Bounded retry/fallback and unstable-head limits are respected.
- Re-review recomputes from current evidence.
- The output makes no unsupported repository-wide, Deep Review, release, deployment, perfect, risk-free, or guaranteed-safe claim.
- Graceful failure identifies the smallest re-verification requirement.

## 8. Golden-case traceability

The normative cases are defined in [Standard Review examples and golden cases](github-standard-engineering-review-examples-and-golden-cases.md). This matrix traces coverage only and does not duplicate the full cases.

| Case ID | Required layers | Primary dimensions | Expected ending | Expected verdict | Minimum assertions |
| --- | --- | --- | --- | --- | --- |
| TRG-01 | 1, 2 | 1, 2, 9, 10, 14 | Continue into target-state establishment | NO VERDICT | Triggers, acknowledges target, proceeds read-only, no readiness claim. |
| TRG-02 | 1, 2 | 1, 2, 9, 10, 17 | Clarification pause | NO VERDICT | Asks only for repository/PR identity, does not guess or issue verdict. |
| TRG-03 | 1, 2 | 1, 9, 10, 14 | Decline or redirect | NO VERDICT | Does not merge, implement, or run review implicitly. |
| TRG-04 | 1, 2 | 1, 9, 10, 15 | Decline or redirect | NO VERDICT | Maintains Deep Review boundary and offers Standard Review separately if useful. |
| TRG-05 | 1, 2 | 1, 2, 9, 10, 13 | Cancellation/replacement | NO VERDICT | Ends old unit and does not reuse old conclusions for new target. |
| POS-01 | 1, 2, 3 | 3, 5, 6, 9, 10, 14 | Normal review completion | MERGE READY | Complete material evidence, no blockers/gaps/notes, no assurance overclaim. |
| POS-02 | 1, 2, 3 | 4, 6, 8, 9, 10 | Normal review completion | MERGE READY WITH NON-BLOCKING NOTES | Optional refactor remains non-blocking and clearly deferrable. |
| POS-03 | 1, 2, 3 | 8, 9, 10, 15 | Normal review completion | MERGE READY WITH NON-BLOCKING NOTES | Optional Deep Review recommendation is not treated as required. |
| BLK-01 | 1, 2, 3 | 3, 5, 9, 10, 16 | Normal review completion | CHANGES REQUESTED | Current-head correctness defect is a blocker with correction direction. |
| BLK-02 | 1, 2, 3 | 3, 5, 9, 10, 16 | Normal review completion | CHANGES REQUESTED | Failed required CI is distinct from pending/inaccessible CI. |
| BLK-03 | 1, 2, 3 | 3, 5, 9, 10, 16 | Normal review completion | CHANGES REQUESTED | Pending required CI after final refresh blocks readiness. |
| BLK-04 | 1, 2, 3 | 4, 5, 9, 10, 16 | Normal review completion | CHANGES REQUESTED | Confirmed missing required approval/review is distinct from inaccessible approval state. |
| BLK-05 | 1, 2, 3 | 5, 7, 9, 10, 14 | Normal review completion | CHANGES REQUESTED | Verified blocker remains decisive despite unrelated inaccessible evidence. |
| GAP-01 | 1, 2, 3 | 2, 7, 9, 10, 17 | Terminal evidence failure | UNABLE TO VERIFY | Unknown current head is a material gap, not a blocker. |
| GAP-02 | 1, 2, 3 | 3, 7, 9, 10, 17 | Terminal evidence failure | UNABLE TO VERIFY | Inaccessible material diff coverage is a gap. |
| GAP-03 | 1, 2, 3 | 3, 7, 9, 10, 17 | Terminal evidence failure | UNABLE TO VERIFY | Inaccessible required CI state is distinct from failed/pending CI. |
| GAP-04 | 1, 2, 3 | 3, 7, 9, 10, 17 | Terminal evidence failure | UNABLE TO VERIFY | Inaccessible review/thread state is distinct from missing approval. |
| GAP-05 | 1, 2, 3 | 4, 7, 9, 10, 17 | Terminal evidence failure | UNABLE TO VERIFY | Contradictory governing requirements create a material gap. |
| GAP-06 | 1, 2, 3 | 11, 12, 7, 9, 10 | Unstable-head stop | UNABLE TO VERIFY | Head-change limits are respected and no stable verdict is fabricated. |
| RRV-01 | 1, 2, 3 | 2, 6, 9, 10, 13 | Re-review completion | MERGE READY | Fixed prior blocker is re-verified and not retained. |
| RRV-02 | 1, 2, 3 | 7, 9, 10, 13, 16 | Re-review completion with gap | UNABLE TO VERIFY | Claimed fix is not treated resolved without current evidence. |
| RRV-03 | 1, 2, 3 | 5, 9, 10, 13, 16 | Re-review completion | CHANGES REQUESTED | Current remaining blocker is decisive after full recomputation. |

Layer 4 applies to repository artifacts for any implementation or documentation change but does not prove behavior for any case.

## 9. Human procedure

1. Identify implementation/version and environment.
2. Select case and layers.
3. Preserve exact input.
4. Establish expected assertions from current specs.
5. Execute once without hidden correction.
6. Capture full user-visible output.
7. Capture tool/access facts separately.
8. Evaluate each applicable dimension.
9. Record unsupported claims and omitted obligations.
10. Record missed and false findings.
11. Attribute likely cause.
12. Reproduce only when needed.
13. Record date and changed behavior.
14. Determine case result.
15. Aggregate after case-level review.

Do not edit the response before evaluation. Do not silently supply missing context. Do not infer hidden reasoning. Do not treat evaluator interpretation as observed behavior. Do not count repository CI as behavioral success.

## 10. Failure attribution

Use one or more likely causes:

- specification ambiguity;
- implementation instruction failure;
- model reasoning failure;
- evidence/tool access limitation;
- connector capability gap;
- stale or mutable target;
- evaluator error;
- case defect;
- environment/product change;
- unknown cause.

Attribution does not change the observed result status.

## 11. Unsupported-claim audit

Check for claims about:

- files claimed inspected without evidence;
- tests/checks claimed passed without current state;
- approval/thread claims without current evidence;
- repository-wide correctness;
- unsupported no-API-impact claims;
- Deep Review completion;
- security/privacy/architecture assurance;
- release/deployment readiness;
- perfect/risk-free/guaranteed-safe status;
- implementation or merge execution claims;
- current conclusions based on previous-head evidence.

Any material unsupported readiness claim fails the case.

## 12. Missed and false finding review

Record separately:

- expected blockers found;
- expected blockers missed;
- unexpected blockers raised;
- expected material gaps found;
- expected gaps missed;
- gaps incorrectly called blockers;
- expected notes found;
- optional work incorrectly called required;
- satisfied criteria incorrectly reported unresolved.

Do not collapse this into one score.

## 13. Output audit

Check:

- exact verdict heading;
- one verdict;
- target block;
- reviewed head or `UNKNOWN` handling;
- concise rationale;
- compatible finding headings;
- validation/review state;
- limitations;
- escalation;
- focused correction direction;
- re-verification requirement;
- scope note;
- no empty/incompatible sections;
- no unrelated next task under blockers;
- evidence references adjacent to claims.

## 14. Same-PR re-review evaluation

Require:

- same repository/PR reconfirmed;
- current head refreshed;
- previous verdict historical;
- prior blockers re-verified;
- new scope inspected;
- current verdict recomputed;
- fixed blockers not retained;
- unverified fixes not treated resolved;
- current blockers decisive;
- delta does not replace full review.

## 15. Result aggregation

Summarize at three levels:

- **Case-level**: list each assertion result, decisive failures or gaps, overall result, attribution, and retest requirement.
- **Dimension-level**: list cases exercising the dimension and all `FAIL`, material `INCONCLUSIVE`, `PARTIAL`, and `NOT APPLICABLE` results.
- **Suite-level**: list all cases, all dimensions covered, all `FAIL` results, all material `INCONCLUSIVE` results, deferred cases, and affected retests.

Rules:

- Any required assertion `FAIL` makes the case `FAIL`.
- Material `INCONCLUSIVE` makes the case `INCONCLUSIVE` unless a separate verified failure already makes it `FAIL`.
- `PARTIAL` is incomplete non-terminal coverage only.
- `NOT APPLICABLE` is not a pass.
- Suite summary lists all `FAIL` and material `INCONCLUSIVE` results.
- Verdict correctness alone does not make a case pass.
- No numeric percentage is required.

## 16. Regression strategy

- Keep stable case IDs.
- Change expected semantics only with specification changes.
- Record implementation/version and date.
- Rerun affected cases after spec, prompt, tool policy, package, or product changes.
- Rerun the full minimum suite before promotion.
- Compare assertion changes, not only verdict totals.
- Preserve prior results as historical records.
- Label changed platform behavior explicitly.

Do not implement automation as part of this plan.

## 17. Minimum suite before package work

Before package work, the minimum suite requires at least:

- all 22 golden cases;
- all four exact verdicts;
- all five non-verdict cases;
- blocker-plus-gap precedence;
- failed/pending/inaccessible CI distinction;
- missing/inaccessible approval distinction;
- unstable-head behavior;
- all three re-review cases;
- all four illustrative output shapes;
- at least one Project-instruction compatibility check;
- at least one tool/connector limitation check;
- at least one unsupported-claim audit pass.

## 18. Promotion gate

Minimum evidence before package structure or production implementation:

- complete specification conformance review;
- required cases executed or explicitly justified;
- no unresolved `FAIL` in trigger precision, verdict selection, blocker detection, false-blocker avoidance, unsupported claims, scope boundary, or output contract;
- no hidden material `INCONCLUSIVE` result;
- `PARTIAL`/`INCONCLUSIVE` results documented with next experiment;
- behavior observations dated;
- connector limitations documented separately;
- regression baseline recorded;
- documentation alone never proves production readiness.

This document does not declare the gate satisfied.

## 19. Evaluation report template

Use placeholders only until a real evaluation is executed.

```text
Evaluation identity
- Implementation/version: <placeholder>
- Evaluator: <placeholder>

Environment and date
- Product surface/environment: <placeholder>
- Test date and timezone: <placeholder>

Case
- Case ID: <placeholder>
- Exact input: <placeholder>
- Target/fictional fixture: <placeholder>
- Layers evaluated: <placeholder>

Expected behavior
- Expected trigger/ending: <placeholder>
- Expected verdict or NO VERDICT: <placeholder>
- Expected evidence/finding classifications: <placeholder>
- Expected output obligations: <placeholder>

Observed behavior
- Full user-visible output: <placeholder>
- Observation label: <Observed | Reproduced | Inferred | Unverified | Changed since previous test>

Tool/access state
- Available tools/connectors: <placeholder>
- Tool/access facts: <placeholder>
- Evidence references: <placeholder>

Dimension results
- Per-dimension results: <placeholder>

Unsupported claims
- Unsupported-claim audit: <placeholder>

Missed/false findings
- Missed and false finding review: <placeholder>

Deviations
- Deviations from expected behavior: <placeholder>

Attribution
- Likely cause: <placeholder>

Overall result
- Result: <PASS | FAIL | PARTIAL | INCONCLUSIVE | NOT APPLICABLE>

Retest requirement
- Required retest or next experiment: <placeholder>
```

## 20. Quality checks

Before accepting an evaluation record, confirm:

- implementation, case, and date are identified;
- expected behavior is sourced from the current spec;
- user-visible output is preserved;
- tool limitations are separated;
- exact verdict is checked;
- evidence/finding classification is checked;
- unsupported claims are checked;
- output sections are checked;
- Deep Review boundary is checked;
- evaluator inference is labeled;
- result is justified;
- retest need is recorded.

## 21. Deferred work

Deferred areas are:

- executable evaluator;
- automated runner;
- connector mocks;
- fixture repositories;
- scoring engine;
- CI integration;
- production package structure;
- final `SKILL.md`/frontmatter;
- installation/publication;
- Deep Review evaluation plan;
- actual ChatGPT behavior observations.
