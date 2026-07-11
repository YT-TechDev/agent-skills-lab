# GitHub Standard Engineering Review — Examples and Golden Cases

## 1. Status and boundary

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: examples and human-readable golden-case definition
- production package: not implemented
- production readiness: not established

This document contains repository-neutral illustrative examples, normative human-readable golden cases, expected trigger or ending behavior, expected evidence statuses and finding classifications, expected exact verdicts or `NO VERDICT`, expected output obligations, prohibited claims and behaviors, same-PR re-review expectations, and a compact traceability matrix.

This document does not provide executable tests, automated evaluation implementation, connector mocks, real repository fixtures, production Skill behavior, installation behavior, Deep Review examples, or observed/reproduced platform findings.

These are specification fixtures for human review. They do not claim current ChatGPT or connector behavior was validated.

## 2. Case conventions

Use only fictional, repository-neutral identifiers in these cases:

- repository: `example/widgets`
- PRs: `#42`, `#57`
- branches: `main`, `feature/widget-cache`
- short fictional SHAs such as `abc1234`, labeled illustrative
- fictional paths such as `src/cache.ts`
- fictional CI checks such as `test`, `typecheck`, or `repository-validation`

Do not use real private repositories, credentials, user data, connector IDs, API endpoints, AI task URLs, or conversation-sharing URLs.

Each case uses this compact format:

| Field | Meaning |
| --- | --- |
| Case ID and name | Stable case identifier and short name. |
| Purpose | What the case demonstrates. |
| Request or trigger situation | User request or review situation. |
| Target and reviewed head, or NOT ESTABLISHED | Repository, PR, and head identity when established. |
| Governing requirement/applicability | Requirement, policy, or applicability fact controlling the outcome. |
| Available evidence | Fictional evidence available to the reviewer. |
| Limited, inaccessible, stale, or conflicting evidence | Evidence limitations, or `NOT APPLICABLE`. |
| Expected evidence statuses | Expected status labels for decisive evidence. |
| Expected finding classification | Blocker, material gap, note, satisfied, or `NOT APPLICABLE`. |
| Expected ending class | Ending behavior under the stopping policy. |
| Expected verdict or NO VERDICT | Exact verdict name or `NO VERDICT`. |
| Decisive rationale | Why that ending and verdict follow. |
| Required output elements | Minimum output obligations for the case. |
| Prohibited claims or behaviors | Claims or actions the case must not produce. |
| Re-review delta when applicable | Same-PR re-review history treatment, or `NOT APPLICABLE`. |

Fields that do not apply are written as `NOT APPLICABLE` rather than omitted.

## 3. Normative interpretation rules

- Golden cases are normative examples of the current specification.
- Governing specification documents remain authoritative.
- A case does not create a new verdict or decision rule.
- All evidence is fictional but internally consistent.
- Each verdict is recomputed from the case evidence.
- Previous-head findings are historical until current-head re-verification.
- Unavailable evidence is not failed, passed, missing, approved, or resolved.
- A verified current blocker remains decisive despite unrelated gaps.
- Non-trigger and clarification cases do not emit a merge-readiness verdict.
- Output examples follow the existing output-format contract.

## 4. Normative golden cases

### TRG-01 — Complete Standard Review request

| Field | Case content |
| --- | --- |
| Case ID and name | TRG-01 — Complete Standard Review request |
| Purpose | Show an execution-ready Standard Review intake. |
| Request or trigger situation | User asks: "Review example/widgets PR #42 for merge readiness." |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; reviewed head NOT ESTABLISHED at intake. |
| Governing requirement/applicability | One current GitHub PR review; read-only access is available. |
| Available evidence | Repository and PR identity are provided; request is merge-readiness review. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Target identity VERIFIED; head NOT APPLICABLE at intake. |
| Expected finding classification | NOT APPLICABLE. |
| Expected ending class | Continue into target-state establishment. |
| Expected verdict or NO VERDICT | NO VERDICT |
| Decisive rationale | Trigger is yes, but readiness cannot be fabricated before inspection. |
| Required output elements | Acknowledge target, proceed read-only, no verdict heading. |
| Prohibited claims or behaviors | Do not claim merge readiness, checks, approvals, or reviewed files. |
| Re-review delta when applicable | NOT APPLICABLE |

### TRG-02 — Repository or PR identity unresolved

| Field | Case content |
| --- | --- |
| Case ID and name | TRG-02 — Repository or PR identity unresolved |
| Purpose | Show clarification before target-state establishment. |
| Request or trigger situation | User asks: "Can you review the PR?" with no current PR context. |
| Target and reviewed head, or NOT ESTABLISHED | NOT ESTABLISHED. |
| Governing requirement/applicability | Standard Review intent exists but execution-ready target identity is missing. |
| Available evidence | Review intent only. |
| Limited, inaccessible, stale, or conflicting evidence | Repository and PR identity UNKNOWN. |
| Expected evidence statuses | Target identity UNKNOWN. |
| Expected finding classification | NOT APPLICABLE. |
| Expected ending class | Clarification pause before target-state establishment. |
| Expected verdict or NO VERDICT | NO VERDICT |
| Decisive rationale | Target ambiguity causes clarification, not UNABLE TO VERIFY. |
| Required output elements | Ask only for repository and PR number or URL. |
| Prohibited claims or behaviors | Do not guess the PR or emit a verdict. |
| Re-review delta when applicable | NOT APPLICABLE |

### TRG-03 — Implementation-only or merge-only request

| Field | Case content |
| --- | --- |
| Case ID and name | TRG-03 — Implementation-only or merge-only request |
| Purpose | Show non-trigger redirect for write/action-only work. |
| Request or trigger situation | User asks: "Merge PR #42" or "Implement the fix for PR #42." |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; reviewed head NOT ESTABLISHED. |
| Governing requirement/applicability | Merge execution and implementation are outside Standard Review. |
| Available evidence | Request asks for write/action-only work, not review. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | NOT APPLICABLE. |
| Expected finding classification | NOT APPLICABLE. |
| Expected ending class | Decline or redirect to separate job. |
| Expected verdict or NO VERDICT | NO VERDICT |
| Decisive rationale | Standard Review must not run implicitly for merge-only or implementation-only requests. |
| Required output elements | State Standard Review can review if requested separately. |
| Prohibited claims or behaviors | Do not merge, implement, or issue a readiness verdict. |
| Re-review delta when applicable | NOT APPLICABLE |

### TRG-04 — Deep-Review-only request

| Field | Case content |
| --- | --- |
| Case ID and name | TRG-04 — Deep-Review-only request |
| Purpose | Show Deep Review boundary. |
| Request or trigger situation | User asks: "Perform a full security and architecture audit of PR #42." |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; reviewed head NOT ESTABLISHED. |
| Governing requirement/applicability | Deep Review is separate from Standard Review. |
| Available evidence | Request is Deep-Review-only. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | NOT APPLICABLE. |
| Expected finding classification | NOT APPLICABLE. |
| Expected ending class | Decline or redirect to separate Deep Review workflow. |
| Expected verdict or NO VERDICT | NO VERDICT |
| Decisive rationale | Standard Review cannot claim Deep Review completion. |
| Required output elements | Explain boundary and offer Standard Review separately if desired. |
| Prohibited claims or behaviors | Do not perform or claim full security, privacy, architecture, dependency, release, deployment, or Deep Review assurance. |
| Re-review delta when applicable | NOT APPLICABLE |

### TRG-05 — User cancellation or material target replacement

| Field | Case content |
| --- | --- |
| Case ID and name | TRG-05 — User cancellation or material target replacement |
| Purpose | Show review-unit termination without reused conclusions. |
| Request or trigger situation | During PR #42 review, user says: "Stop; review PR #57 instead." |
| Target and reviewed head, or NOT ESTABLISHED | Original: example/widgets PR #42; replacement: example/widgets PR #57; reviewed head NOT ESTABLISHED for replacement. |
| Governing requirement/applicability | Cancellation or material target replacement ends the current unit. |
| Available evidence | User cancellation/replacement is explicit. |
| Limited, inaccessible, stale, or conflicting evidence | Any prior PR #42 evidence is target-specific and historical. |
| Expected evidence statuses | Prior evidence STALE for replacement. |
| Expected finding classification | NOT APPLICABLE. |
| Expected ending class | User-requested cancellation or material scope replacement. |
| Expected verdict or NO VERDICT | NO VERDICT |
| Decisive rationale | The current review unit ends; a new target must be evaluated from intake. |
| Required output elements | Confirm cancellation/replacement and restart only if new request triggers. |
| Prohibited claims or behaviors | Do not reuse PR #42 conclusions for PR #57. |
| Re-review delta when applicable | PR #42 evidence is historical only. |

### POS-01 — Clean current-head review

| Field | Case content |
| --- | --- |
| Case ID and name | POS-01 — Clean current-head review |
| Purpose | Show unqualified positive verdict. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head abc1234 (illustrative). |
| Governing requirement/applicability | All material criteria apply or are supported NOT APPLICABLE. |
| Available evidence | Current diff for src/cache.ts inspected; repository-validation, test, and typecheck passed on abc1234; approval present; no unresolved threads. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Relevant criteria VERIFIED satisfied or NOT APPLICABLE. |
| Expected finding classification | Satisfied; no findings. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | MERGE READY |
| Decisive rationale | Complete material scope inspected and no blocker, material gap, or meaningful qualification found. |
| Required output elements | Verdict, target block, summary, validation/review state, scope note; no finding sections. |
| Prohibited claims or behaviors | Do not claim perfection, risk-free status, Deep Review, release, or deployment assurance. |
| Re-review delta when applicable | NOT APPLICABLE |

### POS-02 — Genuine optional improvement

| Field | Case content |
| --- | --- |
| Case ID and name | POS-02 — Genuine optional improvement |
| Purpose | Show non-blocking maintainability note. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head abc1234 (illustrative). |
| Governing requirement/applicability | No repository rule requires the improvement. |
| Available evidence | All required checks and review state satisfied; src/cache.ts has clear but repetitive helper naming. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Required criteria VERIFIED; optional improvement VERIFIED as non-required. |
| Expected finding classification | Non-blocking note. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | MERGE READY WITH NON-BLOCKING NOTES |
| Decisive rationale | The improvement is evidence-supported and safe to defer despite being sizable enough to mention. |
| Required output elements | Include one non-blocking note explaining safe deferral, validation/review state, scope note. |
| Prohibited claims or behaviors | Do not say the note must be fixed before merge or hide a blocker as a note. |
| Re-review delta when applicable | NOT APPLICABLE |

### POS-03 — Optional Deep Review recommendation

| Field | Case content |
| --- | --- |
| Case ID and name | POS-03 — Optional Deep Review recommendation |
| Purpose | Show optional escalation note without Deep Review claim. |
| Request or trigger situation | Standard Review for example/widgets PR #42 touching cache eviction policy. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head abc1234 (illustrative). |
| Governing requirement/applicability | Repository does not require Deep Review for this change. |
| Available evidence | Material Standard Review coverage, CI, approval, and threads satisfied; change touches performance-sensitive cache policy. |
| Limited, inaccessible, stale, or conflicting evidence | No required Deep Review evidence because it is optional. |
| Expected evidence statuses | Required criteria VERIFIED; Deep Review recommendation NOT APPLICABLE to readiness. |
| Expected finding classification | Non-blocking note / optional escalation. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | MERGE READY WITH NON-BLOCKING NOTES |
| Decisive rationale | Optional Deep Review may be worth surfacing but is not a merge requirement. |
| Required output elements | Include escalation section as optional recommendation and state Deep Review was not performed. |
| Prohibited claims or behaviors | Do not imply Deep Review occurred or is required. |
| Re-review delta when applicable | NOT APPLICABLE |

### BLK-01 — Verified correctness defect on current head

| Field | Case content |
| --- | --- |
| Case ID and name | BLK-01 — Verified correctness defect on current head |
| Purpose | Show code-evidence blocker. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head def5678 (illustrative). |
| Governing requirement/applicability | Cache invalidation must remove expired entries before returning cached values. |
| Available evidence | src/cache.ts lines 44-52 on def5678 return cached values before checking expiresAt; test expectation in tests/cache.test.ts lines 18-29 covers expiry. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Correctness defect VERIFIED failed. |
| Expected finding classification | Current blocker. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | Direct current-head code/test evidence proves incorrect behavior. |
| Required output elements | Blocking findings, validation/review state, focused correction direction, scope note. |
| Prohibited claims or behaviors | Do not treat this as optional because the fix is small; do not add unrelated next tasks. |
| Re-review delta when applicable | NOT APPLICABLE |

### BLK-02 — Failed required CI on current head

| Field | Case content |
| --- | --- |
| Case ID and name | BLK-02 — Failed required CI on current head |
| Purpose | Distinguish failed CI from MISSING. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head def5678 (illustrative). |
| Governing requirement/applicability | repository-validation is required by repository rule. |
| Available evidence | Check repository-validation ran against def5678 and failed. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Required CI VERIFIED failed, not MISSING. |
| Expected finding classification | Current blocker. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | A required current-head check failed. |
| Required output elements | Blocking finding for failed check, validation state, focused correction direction. |
| Prohibited claims or behaviors | Do not call the failed run MISSING or UNKNOWN. |
| Re-review delta when applicable | NOT APPLICABLE |

### BLK-03 — Required CI pending after final refresh

| Field | Case content |
| --- | --- |
| Case ID and name | BLK-03 — Required CI pending after final refresh |
| Purpose | Show pending required CI stopping behavior. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head def5678 (illustrative). |
| Governing requirement/applicability | test completion is required before merge. |
| Available evidence | test check exists on def5678 and remains pending after the one final refresh. |
| Limited, inaccessible, stale, or conflicting evidence | No further polling permitted. |
| Expected evidence statuses | Required CI VERIFIED pending after final refresh. |
| Expected finding classification | Current blocker under existing rules. |
| Expected ending class | Verdict-ready stop after current evidence is sufficient. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | Confirmed required completion has not occurred and Standard Review cannot poll indefinitely. |
| Required output elements | Blocking finding, validation state with final refresh, focused correction direction. |
| Prohibited claims or behaviors | Do not wait indefinitely or mark pending as failed. |
| Re-review delta when applicable | NOT APPLICABLE |

### BLK-04 — Confirmed missing required approval or specialist review

| Field | Case content |
| --- | --- |
| Case ID and name | BLK-04 — Confirmed missing required approval or specialist review |
| Purpose | Distinguish missing approval from no comments. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head def5678 (illustrative). |
| Governing requirement/applicability | Repository rule requires one maintainer approval for src/cache.ts changes. |
| Available evidence | Reviews inspected for def5678 show no approvals from required reviewers. |
| Limited, inaccessible, stale, or conflicting evidence | Lack of comments alone is not approval. |
| Expected evidence statuses | Required approval MISSING after sufficient inspection. |
| Expected finding classification | Current blocker. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | Confirmed absence of a required approval blocks readiness. |
| Required output elements | Blocking finding, review state, focused correction direction. |
| Prohibited claims or behaviors | Do not infer approval from silence; do not treat tool failure alone as MISSING. |
| Re-review delta when applicable | NOT APPLICABLE |

### BLK-05 — Verified blocker plus unrelated inaccessible evidence

| Field | Case content |
| --- | --- |
| Case ID and name | BLK-05 — Verified blocker plus unrelated inaccessible evidence |
| Purpose | Show blocker precedence over unrelated gap. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head def5678 (illustrative). |
| Governing requirement/applicability | Expired cache correctness requirement applies; optional generated-report artifact is material but unrelated. |
| Available evidence | src/cache.ts on def5678 has verified expiry defect. |
| Limited, inaccessible, stale, or conflicting evidence | coverage-report artifact inaccessible after bounded fallback. |
| Expected evidence statuses | Correctness VERIFIED failed; report UNKNOWN. |
| Expected finding classification | Current blocker plus material verification gap. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | A verified current blocker outranks an unrelated material gap, which remains disclosed. |
| Required output elements | One verdict only; blocking finding and limitation/gap disclosure. |
| Prohibited claims or behaviors | Do not emit UNABLE TO VERIFY as a second verdict or hide the limitation. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-01 — Repository and PR established, current head identity unavailable

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-01 — Repository and PR established, current head identity unavailable |
| Purpose | Show target-state failure after PR establishment. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head UNKNOWN. |
| Governing requirement/applicability | Current head identity is mandatory for current readiness. |
| Available evidence | Repository and PR exist. |
| Limited, inaccessible, stale, or conflicting evidence | Current head SHA cannot be retrieved after bounded retry/fallback. |
| Expected evidence statuses | Current head UNKNOWN. |
| Expected finding classification | Material verification gap / target-state integrity incomplete. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | Repository and PR are known, but current change identity is not established. |
| Required output elements | Target block shows head UNKNOWN and names unresolved target-state property. |
| Prohibited claims or behaviors | Do not use stale or previous-head evidence for readiness. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-02 — Material changed file or diff coverage inaccessible

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-02 — Material changed file or diff coverage inaccessible |
| Purpose | Show inaccessible diff coverage with established head. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head ghi9012 (illustrative). |
| Governing requirement/applicability | src/cache.ts is a material changed file. |
| Available evidence | Target, head, and file list are established; no blocker verified. |
| Limited, inaccessible, stale, or conflicting evidence | src/cache.ts diff and file content inaccessible after retry and file-level fallback. |
| Expected evidence statuses | Changed-file coverage PARTIAL or UNKNOWN as supported. |
| Expected finding classification | Material verification gap. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | Positive readiness requires material changed-file coverage. |
| Required output elements | Material gap, coverage/access limitation, re-verification direction; no unresolved target-state field. |
| Prohibited claims or behaviors | Do not describe inaccessible file as passed, failed, absent, or approved. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-03 — Required CI state inaccessible

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-03 — Required CI state inaccessible |
| Purpose | Distinguish inaccessible CI from failed CI. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head ghi9012 (illustrative). |
| Governing requirement/applicability | repository rule confirms test check state is material. |
| Available evidence | Code review finds no blocker. |
| Limited, inaccessible, stale, or conflicting evidence | Current test check state cannot be retrieved after bounded recovery. |
| Expected evidence statuses | Required CI UNKNOWN. |
| Expected finding classification | Material verification gap. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | Unavailable CI is not failed CI, passed CI, or MISSING CI. |
| Required output elements | Material gap and validation state naming inaccessible check. |
| Prohibited claims or behaviors | Do not call the check failed, passed, missing, or approved. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-04 — Required review or thread state inaccessible

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-04 — Required review or thread state inaccessible |
| Purpose | Distinguish inaccessible approval/thread state from missing or resolved. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head ghi9012 (illustrative). |
| Governing requirement/applicability | Repository rule requires approval and resolved material threads. |
| Available evidence | Changed files inspected; no code blocker verified. |
| Limited, inaccessible, stale, or conflicting evidence | Review/thread API page for current head inaccessible after fallback. |
| Expected evidence statuses | Required review/thread state UNKNOWN. |
| Expected finding classification | Material verification gap. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | Inaccessible review state is not approval, absence, or resolution. |
| Required output elements | Material gap, limitation, re-verification evidence needed. |
| Prohibited claims or behaviors | Do not infer approval from no comments or from tool failure. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-05 — Contradictory material governing requirements

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-05 — Contradictory material governing requirements |
| Purpose | Show unresolved governing-rule conflict. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; head ghi9012 (illustrative). |
| Governing requirement/applicability | Two repository-owned docs conflict about whether typecheck is required for docs-only PRs. |
| Available evidence | README says typecheck is required for every PR; CONTRIBUTING says docs-only PRs skip typecheck. |
| Limited, inaccessible, stale, or conflicting evidence | Authority, freshness, ref, and specificity do not resolve conflict. |
| Expected evidence statuses | Governing requirement UNKNOWN. |
| Expected finding classification | Material verification gap. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | The review cannot choose the convenient requirement. |
| Required output elements | Material gap naming conflicting sources and needed clarification. |
| Prohibited claims or behaviors | Do not pick one rule without evidence or emit a positive verdict. |
| Re-review delta when applicable | NOT APPLICABLE |

### GAP-06 — Head changes twice in one invocation

| Field | Case content |
| --- | --- |
| Case ID and name | GAP-06 — Head changes twice in one invocation |
| Purpose | Show unstable-head stopping. |
| Request or trigger situation | Standard Review for example/widgets PR #42. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; initial head abc1234, restarted at def5678, second change to ghi9012 (illustrative). |
| Governing requirement/applicability | Current-head association is mandatory. |
| Available evidence | First change triggers allowed restart. |
| Limited, inaccessible, stale, or conflicting evidence | Second head change occurs before final decision. |
| Expected evidence statuses | Target stability UNKNOWN; previous-head evidence STALE/HISTORICAL. |
| Expected finding classification | Material verification gap. |
| Expected ending class | Terminal unstable-target stop. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | Second head change exceeds allowed restart; previous-head evidence is historical only. |
| Required output elements | Material gap and re-verification direction for stable current head. |
| Prohibited claims or behaviors | Do not issue a positive verdict from previous-head evidence. |
| Re-review delta when applicable | Prior findings remain historical only. |

### RRV-01 — Prior blocker verified fixed and full current review passes

| Field | Case content |
| --- | --- |
| Case ID and name | RRV-01 — Prior blocker verified fixed and full current review passes |
| Purpose | Show re-review recomputation to positive. |
| Request or trigger situation | Same-PR re-review after user reports prior expiry bug fixed. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; new head jkl3456 (illustrative). |
| Governing requirement/applicability | Same PR must refresh head, verify prior blockers, inspect new changes, and recompute. |
| Available evidence | Prior blocker in src/cache.ts is resolved on jkl3456; full current scope, CI, approval, and threads satisfy requirements. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | Prior blocker VERIFIED resolved on current head; all material criteria VERIFIED/NOT APPLICABLE. |
| Expected finding classification | Satisfied; resolved prior finding appears only in delta/history. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | MERGE READY |
| Decisive rationale | Previous verdict is historical; current evidence now supports readiness. |
| Required output elements | Verdict, target block, validation state, optional re-review delta. |
| Prohibited claims or behaviors | Do not claim prior NOT MERGE READY still controls. |
| Re-review delta when applicable | Delta: prior blocker fixed; no current blockers or gaps. |

### RRV-02 — Fix reported but current evidence cannot verify it

| Field | Case content |
| --- | --- |
| Case ID and name | RRV-02 — Fix reported but current evidence cannot verify it |
| Purpose | Show previous-head blocker not automatically current. |
| Request or trigger situation | Same-PR re-review after user says the expiry bug is fixed. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; new head jkl3456 (illustrative). |
| Governing requirement/applicability | Current changed area must be inspectable to verify fix. |
| Available evidence | New head established; prior blocker belongs to previous head. |
| Limited, inaccessible, stale, or conflicting evidence | src/cache.ts current content inaccessible after bounded recovery. |
| Expected evidence statuses | Current fix evidence UNKNOWN; prior blocker HISTORICAL. |
| Expected finding classification | Material re-verification gap. |
| Expected ending class | Terminal evidence failure after recovery exhausted. |
| Expected verdict or NO VERDICT | UNABLE TO VERIFY |
| Decisive rationale | No current blocker is verified, but material current evidence is inaccessible. |
| Required output elements | Material gap, limitation, re-verification direction, optional delta. |
| Prohibited claims or behaviors | Do not automatically carry forward previous-head blocker or claim it is fixed. |
| Re-review delta when applicable | Delta: prior blocker unverified on current head. |

### RRV-03 — One prior blocker fixed, another remains

| Field | Case content |
| --- | --- |
| Case ID and name | RRV-03 — One prior blocker fixed, another remains |
| Purpose | Show mixed re-review result. |
| Request or trigger situation | Same-PR re-review after two prior blockers. |
| Target and reviewed head, or NOT ESTABLISHED | example/widgets PR #42; new head jkl3456 (illustrative). |
| Governing requirement/applicability | Each prior blocker must be re-evaluated on current head. |
| Available evidence | Prior expiry defect fixed; required test check still failed on jkl3456. |
| Limited, inaccessible, stale, or conflicting evidence | NOT APPLICABLE. |
| Expected evidence statuses | One blocker VERIFIED resolved; required CI VERIFIED failed. |
| Expected finding classification | Current blocker; resolved finding only in delta/history. |
| Expected ending class | Normal review completion. |
| Expected verdict or NO VERDICT | NOT MERGE READY |
| Decisive rationale | The remaining current blocker determines the verdict. |
| Required output elements | Blocking finding only for current failed CI; delta may mention resolved expiry bug. |
| Prohibited claims or behaviors | Do not list fixed blocker as current blocking. |
| Re-review delta when applicable | Delta: expiry blocker resolved; test blocker remains current. |

## 5. Traceability matrix

| Case ID | Trigger or ending | Decisive evidence state | Expected classification | Expected verdict |
| --- | --- | --- | --- | --- |
| TRG-01 | Continue into target-state establishment. | Target identity VERIFIED; head NOT APPLICABLE at intake. | NOT APPLICABLE. | NO VERDICT |
| TRG-02 | Clarification pause before target-state establishment. | Target identity UNKNOWN. | NOT APPLICABLE. | NO VERDICT |
| TRG-03 | Decline or redirect to separate job. | NOT APPLICABLE. | NOT APPLICABLE. | NO VERDICT |
| TRG-04 | Decline or redirect to separate Deep Review workflow. | NOT APPLICABLE. | NOT APPLICABLE. | NO VERDICT |
| TRG-05 | User-requested cancellation or material scope replacement. | Prior evidence STALE for replacement. | NOT APPLICABLE. | NO VERDICT |
| POS-01 | Normal review completion. | Relevant criteria VERIFIED satisfied or NOT APPLICABLE. | Satisfied; no findings. | MERGE READY |
| POS-02 | Normal review completion. | Required criteria VERIFIED; optional improvement VERIFIED as non-required. | Non-blocking note. | MERGE READY WITH NON-BLOCKING NOTES |
| POS-03 | Normal review completion. | Required criteria VERIFIED; Deep Review recommendation NOT APPLICABLE to readiness. | Non-blocking note / optional escalation. | MERGE READY WITH NON-BLOCKING NOTES |
| BLK-01 | Normal review completion. | Correctness defect VERIFIED failed. | Current blocker. | NOT MERGE READY |
| BLK-02 | Normal review completion. | Required CI VERIFIED failed, not MISSING. | Current blocker. | NOT MERGE READY |
| BLK-03 | Verdict-ready stop after current evidence is sufficient. | Required CI VERIFIED pending after final refresh. | Current blocker under existing rules. | NOT MERGE READY |
| BLK-04 | Normal review completion. | Required approval MISSING after sufficient inspection. | Current blocker. | NOT MERGE READY |
| BLK-05 | Normal review completion. | Correctness VERIFIED failed; report UNKNOWN. | Current blocker plus material verification gap. | NOT MERGE READY |
| GAP-01 | Terminal evidence failure after recovery exhausted. | Current head UNKNOWN. | Material verification gap / target-state integrity incomplete. | UNABLE TO VERIFY |
| GAP-02 | Terminal evidence failure after recovery exhausted. | Changed-file coverage PARTIAL or UNKNOWN as supported. | Material verification gap. | UNABLE TO VERIFY |
| GAP-03 | Terminal evidence failure after recovery exhausted. | Required CI UNKNOWN. | Material verification gap. | UNABLE TO VERIFY |
| GAP-04 | Terminal evidence failure after recovery exhausted. | Required review/thread state UNKNOWN. | Material verification gap. | UNABLE TO VERIFY |
| GAP-05 | Terminal evidence failure after recovery exhausted. | Governing requirement UNKNOWN. | Material verification gap. | UNABLE TO VERIFY |
| GAP-06 | Terminal unstable-target stop. | Target stability UNKNOWN; previous-head evidence STALE/HISTORICAL. | Material verification gap. | UNABLE TO VERIFY |
| RRV-01 | Normal review completion. | Prior blocker VERIFIED resolved on current head; all material criteria VERIFIED/NOT APPLICABLE. | Satisfied; resolved prior finding appears only in delta/history. | MERGE READY |
| RRV-02 | Terminal evidence failure after recovery exhausted. | Current fix evidence UNKNOWN; prior blocker HISTORICAL. | Material re-verification gap. | UNABLE TO VERIFY |
| RRV-03 | Normal review completion. | One blocker VERIFIED resolved; required CI VERIFIED failed. | Current blocker; resolved finding only in delta/history. | NOT MERGE READY |

## 6. Illustrative output examples

These examples are illustrative, not additional golden cases. They use fictional locators and avoid connector-specific syntax requirements.

### Example A — MERGE READY

## Verdict: MERGE READY

**Reviewed target**

- Repository: `example/widgets`
- PR: `#42` — `Cache widget lookups`
- Base ref: `main`
- Head ref: `feature/widget-cache`
- Reviewed head: `abc1234` (illustrative)
- Review mode: `initial`

No blocker or material verification gap was found within Standard Review scope. The material changed file `src/cache.ts` was inspected for the cache behavior in this PR, and required validation and review state are satisfied for `abc1234` (`src/cache.ts:10-74`, check `test` on `abc1234`, review `maintainer-approval-7`).

### Validation and review state

- Current CI: `test`, `typecheck`, and `repository-validation` passed on `abc1234` (checks `test-101`, `typecheck-102`, `repository-validation-103`).
- Review state: one required maintainer approval applies to `abc1234` (review `maintainer-approval-7`).
- Threads: no unresolved material review threads were found for `abc1234` (thread list `threads-42-a`).

Standard Review is a read-only merge-readiness review of this PR. It does not provide Deep Review, security, privacy, architecture, dependency, release, deployment, or risk-free assurance.

### Example B — MERGE READY WITH NON-BLOCKING NOTES

## Verdict: MERGE READY WITH NON-BLOCKING NOTES

**Reviewed target**

- Repository: `example/widgets`
- PR: `#42` — `Cache widget lookups`
- Base ref: `main`
- Head ref: `feature/widget-cache`
- Reviewed head: `abc1234` (illustrative)
- Review mode: `initial`

No blocker or material verification gap was found within Standard Review scope. One maintainability note is worth surfacing, but governing evidence does not require it before merge (`src/cache.ts:24-39`, check `test` on `abc1234`).

### Non-blocking notes

- `src/cache.ts` repeats the cache-key normalization expression in two small helper paths (`src/cache.ts:24-39`). This can be deferred because the repeated expression is covered by current tests, does not change API behavior, and no repository rule requires the refactor before merge.

### Validation and review state

- Current CI: `test`, `typecheck`, and `repository-validation` passed on `abc1234` (checks `test-201`, `typecheck-202`, `repository-validation-203`).
- Review state: required approval is present for `abc1234` (review `maintainer-approval-9`).
- Threads: no unresolved material review threads were found (thread list `threads-42-b`).

Standard Review is a read-only merge-readiness review of this PR. It does not provide Deep Review, security, privacy, architecture, dependency, release, deployment, or risk-free assurance.

### Example C — NOT MERGE READY

## Verdict: NOT MERGE READY

**Reviewed target**

- Repository: `example/widgets`
- PR: `#42` — `Cache widget lookups`
- Base ref: `main`
- Head ref: `feature/widget-cache`
- Reviewed head: `def5678` (illustrative)
- Review mode: `initial`

The PR has one verified current blocker: `src/cache.ts` can return an expired cached widget before checking expiry on the reviewed head (`src/cache.ts:44-52` on `def5678`).

### Blocking findings

- Expired cache entries can be returned. Governing requirement: cache lookup must not return entries after `expiresAt`. Current evidence: `getWidgetFromCache` returns the cached value before the expiry check (`src/cache.ts:44-52` on `def5678`), while the PR's test expectation requires expired entries to miss (`tests/cache.test.ts:18-29`). This blocks merge readiness because it violates the required cache behavior.

### Validation and review state

- Current CI: `test` failed on `def5678` in the expiry case (check `test-301`).
- Review state: required approval is present, but approval does not override the verified correctness blocker (review `maintainer-approval-11`).

### Focused correction direction

Change `src/cache.ts` so expiry is checked before returning the cached value, then re-run the relevant cache test and required CI for the current head.

Standard Review is a read-only merge-readiness review of this PR. It does not provide Deep Review, security, privacy, architecture, dependency, release, deployment, or risk-free assurance.

### Example D — UNABLE TO VERIFY

## Verdict: UNABLE TO VERIFY

**Reviewed target**

- Repository: `example/widgets`
- PR: `#42` — `Cache widget lookups`
- Base ref: `main`
- Head ref: `feature/widget-cache`
- Reviewed head: `ghi9012` (illustrative)
- Review mode: `initial`

The target and current head are established, but material changed-file coverage is incomplete: `src/cache.ts` could not be inspected after bounded retry and file-level fallback. No verified current blocker was found from accessible evidence.

### Material verification gaps

- Material changed file inaccessible. Governing requirement: Standard Review must inspect material changed files before a positive verdict. Current limitation: `src/cache.ts` is listed as changed for `ghi9012`, but its diff and current file content were inaccessible after retry and fallback (`changed-files-42`, `file-fetch-src-cache-ts`). This prevents a trustworthy readiness judgment.

### Validation and review state

- Current CI: `test` and `typecheck` passed on `ghi9012` (checks `test-401`, `typecheck-402`). Passing CI does not replace inspection of the inaccessible material file.
- Review state: required approval is present for `ghi9012` (review `maintainer-approval-13`).

### Coverage and access limitations

- `src/cache.ts` coverage is `UNKNOWN` for `ghi9012` after bounded recovery (`file-fetch-src-cache-ts`). This inaccessible evidence is not classified as a failure, absence, approval, or resolution.

### Re-verification direction

Re-run Standard Review when `src/cache.ts` diff or current file content is accessible for the same current head, or provide the smallest sanitized evidence needed to inspect that file.

Standard Review is a read-only merge-readiness review of this PR. It does not provide Deep Review, security, privacy, architecture, dependency, release, deployment, or risk-free assurance.

## 7. Semantic edge-case coverage

- Unavailable CI is not failed CI: `GAP-03`.
- Failed CI is not `MISSING`: `BLK-02`.
- No comments is not approval: `BLK-04`, `GAP-04`.
- Tool failure alone is not `MISSING`: `BLK-04`, `GAP-04`.
- Confirmed absence after sufficient inspection can be `MISSING`: `BLK-04`.
- A small required fix can still be blocking: `BLK-01`.
- A large optional improvement can still be non-blocking: `POS-02`.
- Passing CI does not replace code review: `GAP-02`, Example D.
- A previous-head blocker is historical until re-verified: `GAP-06`, `RRV-02`.
- A verified blocker outranks unrelated material gap: `BLK-05`.
- Positive verdicts require sufficient material coverage: `POS-01`, `POS-02`, `POS-03`.
- Target ambiguity causes clarification, not `UNABLE TO VERIFY`: `TRG-02`.
- Target-state failure after repository and PR establishment may cause `UNABLE TO VERIFY`: `GAP-01`.
- Cancellation and target replacement emit `NO VERDICT`: `TRG-05`.
- Standard Review does not claim security, privacy, architecture, dependency, release, deployment, or Deep Review assurance: `TRG-04`, all illustrative outputs.

## 8. Consistency checklist

- Trigger/ending class correct.
- Target-state assumptions explicit.
- Governing requirement/applicability explicit.
- Evidence provenance, freshness, and head association explicit.
- Status matches evidence.
- Finding classification consistent.
- Verdict precedence followed.
- Retry/stopping limits respected.
- Required output sections present.
- Prohibited claims absent.
- Deep Review boundary intact.
- Re-review verdict recomputed from current evidence.
- Repository-neutral and no sensitive data.
