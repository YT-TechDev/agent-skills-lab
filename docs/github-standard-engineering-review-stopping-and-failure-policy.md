# GitHub Standard Engineering Review — Stopping and Failure Policy

## Status and policy boundary

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: stopping, retry, and failure behavior definition
- production package: not implemented
- production readiness: not established

This document defines intended behavior for:

- normal completion;
- clarification pauses;
- decline or redirect endings;
- bounded retries;
- read-only fallback behavior;
- terminal evidence failures;
- unstable-head handling;
- stopping behavior for same-PR re-review; and
- decision effects under the existing verdict rules.

This document does not implement:

- a production Skill;
- connector retry code;
- polling automation;
- a workflow engine;
- a final output renderer; or
- production installation behavior.

Standard Review remains a read-only review of one established current GitHub pull request. Standard Review and Deep Review remain separate. Existing evidence statuses, exact verdict names, decision precedence, and the ten-phase review workflow are reused unchanged. This document fills the previously deferred detailed stopping and failure behavior without creating a production Skill package.

## Ending classes

Standard Review recognizes these distinct ending classes. They are not verdict names and must not be presented as replacements for the existing verdicts.

1. **Normal review completion**: one current PR target is established, sufficient current evidence is gathered or limitations are classified, and the existing decision rules produce a verdict.
2. **Clarification pause before target-state establishment**: Standard Review intent exists, but the repository, PR, ref, or other mandatory target identity remains ambiguous before target-state establishment. The review pauses for the smallest missing clarification and does not fabricate a merge-readiness verdict.
3. **Decline or redirect for non-trigger or out-of-scope requests**: the request is not Standard Review, is implementation-only, merge-only, release-only, Deep-Review-only, or otherwise outside the trigger policy. No Standard Review merge-readiness verdict is produced.
4. **Bounded recovery continuation**: a recoverable access, coverage, freshness, or contradiction problem is addressed through the bounded recovery ladder while preserving the same claim and read-only scope.
5. **Verdict-ready stop after current evidence is sufficient**: current evidence is sufficient under the existing decision rules, including sufficient classification of any limitations, and continued inspection would not materially change the Standard Review judgment.
6. **Terminal evidence failure after recovery is exhausted**: bounded recovery cannot establish material evidence needed for a trustworthy judgment. The remaining limitation is classified and the existing decision rules determine the verdict effect.
7. **User-requested cancellation or material scope replacement**: the user cancels the review or replaces the target or job. The current review unit ends without fabricated conclusions; any new request is re-evaluated under the trigger policy.

A verdict is produced only for one established current PR target. Non-trigger requests do not receive a Standard Review merge-readiness verdict. Unresolved target ambiguity before target-state establishment results in clarification rather than a fabricated verdict. Implementation-only, merge-only, release-only, and Deep-Review-only requests are separated or redirected under the trigger policy.

## Failure classification

Failures are classified by the effect on the claim being evaluated. Tool failure must be distinguished from evidence that proves a repository condition.

| Failure class | Default action |
| --- | --- |
| Transient access failure | Retry once at workflow level when plausibly temporary. |
| Permanent authorization/access failure | Fallback if a legitimate read-only path exists; otherwise classify as evidence limitation and stop recovery for that claim. |
| Target-not-found or target-mismatch failure | Clarify when target identity may be wrong; stop when confirmed against the provided target and no corrected target or fallback exists. |
| Unsupported capability | Fallback if a supported read-only alternative exists; otherwise classify as evidence limitation or decline/redirect when the request requires an unsupported job. |
| Incomplete coverage | Fallback or narrow by page, file, job, log, or evidence unit; then classify remaining limitation. |
| Stale or conflicting state | Restart the affected phase or refresh mutable state before decision selection. |
| Unstable target/head | Restart once from target-state establishment; stop on a second head change in one invocation. |
| Unavailable required evidence | Retry/fallback when bounded recovery permits; otherwise classify as a material evidence limitation. |
| Contradictory material evidence | Reconcile by authority, SHA/ref, freshness, specificity, and completeness; classify unresolved material contradiction as a verification gap. |
| User-input insufficiency | Clarify for the smallest missing target or material context; stop without verdict if required target identity is not supplied. |
| Scope-boundary failure | Decline/redirect or separate the request under the trigger policy. |

Examples:

- inaccessible CI status is not failed CI;
- inaccessible review-thread state is not proof that threads are resolved;
- a 404 may mean not found or inaccessible, so Standard Review must not infer which without evidence; and
- a confirmed missing required artifact differs from inability to inspect that artifact.

## Bounded recovery ladder

For each failed capability or claim, Standard Review applies this workflow-level recovery order:

1. validate target identity, ref, SHA, path, and request parameters;
2. perform at most one immediate retry for a plausibly transient failure;
3. use at most one materially different read-only fallback when available;
4. narrow the request by page, file, job, log, or evidence unit when that can improve completeness without changing the claim;
5. request the smallest sanitized user-provided evidence only when permitted by the input and tool policies; and
6. classify the remaining evidence limitation and stop recovery for that claim.

Connector-internal retries are outside this workflow-level budget. The workflow must not loop indefinitely. Repeating the same failed request with no changed condition is prohibited. Permanent authorization failures, confirmed unsupported capabilities, and confirmed target-not-found failures do not receive an automatic retry unless corrected target information or a legitimate fallback exists. User or platform constraints may shorten the recovery path. Recovery must remain read-only.

## Retry and polling limits

- One immediate workflow-level retry is allowed per failed capability or claim.
- One materially different fallback path is allowed when available.
- One final mutable-state refresh occurs before decision selection.
- Open-ended polling for CI, reviews, threads, comments, or head changes is prohibited.
- Sleep/wait loops are not part of a single invocation.
- Repeated refresh after state remains unchanged is prohibited unless new user-provided information materially changes the request.

A current required check that remains pending after the final refresh is handled by the existing decision rules. Standard Review must not wait indefinitely for it.

## Head-change and unstable-target behavior

The first detected head change invalidates prior SHA-specific conclusions. Previous-head findings may be retained only as historical context. Standard Review restarts from target-state establishment, re-enumerates changed files, and re-inspects newly changed scope. At most one workflow restart caused by a head change is permitted in one invocation.

If the head changes again before final decision, Standard Review stops with an unstable-target material verification gap and applies the existing decision rules. It must never issue a positive verdict from evidence tied only to a previous head. A verified blocker tied to a previous head must be re-verified against the current head before it can determine the current verdict.

## Pagination, truncation, and coverage failure

Standard Review must handle paginated changed-file lists, paginated comments and reviews, truncated diffs, unavailable per-file patches, binary files, oversized files, missing logs, unavailable artifacts, repeated pagination tokens or page loops, and connector result caps without inventing coverage.

When evidence is material to the judgment, Standard Review must exhaust accessible pages and use per-file or narrower read-only fallbacks when available. It must preserve the exact inaccessible scope, including which file, page, job, log, artifact, thread, or evidence unit could not be inspected.

Material incomplete coverage is classified as `PARTIAL` or `UNKNOWN` under the evidence policy and prevents a positive verdict unless a verified blocker already determines `NOT MERGE READY`. Immaterial unavailable evidence may remain a disclosed limitation without automatically changing the verdict.

## Material versus immaterial failure

A failure is material when it can affect:

- target-state integrity;
- an applicable governing requirement;
- correctness;
- required validation;
- type safety or error handling where applicable;
- public API or compatibility;
- required review, approval, or thread state;
- required escalation;
- complete relevant change-scope coverage; or
- verdict selection.

An immaterial failure affects none of the material applicable criteria. Materiality requires evidence-based reasoning. Convenient availability does not make evidence material, and inconvenience does not make failure immaterial. Positive verdicts require all material failures to be resolved or shown not applicable. Immaterial limitations must not be promoted into blockers.

## Interaction with evidence statuses

Existing meanings are used unchanged:

- successful current retrieval may support `VERIFIED`;
- incomplete but meaningful retrieval may support `PARTIAL`;
- confirmed absence after sufficient accessible inspection may support `MISSING`;
- inability to determine after bounded recovery supports `UNKNOWN`; and
- supported non-applicability supports `NOT APPLICABLE`.

Tool failure alone does not establish `MISSING`. `UNKNOWN` on a material criterion is a material verification gap. `PARTIAL` on a material criterion is a material verification gap unless a verified blocker already decides the verdict. `MISSING` for a confirmed required artifact is a blocker. Status labels do not replace materiality or requirement reasoning.

## Decision effects

Standard Review reuses the existing verdict precedence exactly:

1. target-state integrity cannot be established → `UNABLE TO VERIFY`
2. verified current blocker exists → `NOT MERGE READY`
3. no blocker, but unresolved material verification gap exists → `UNABLE TO VERIFY`
4. no blocker/gap, with genuine notes → `MERGE READY WITH NON-BLOCKING NOTES`
5. no blocker/gap/qualification → `MERGE READY`

A verified current blocker remains decisive when an unrelated evidence source later fails; the unrelated failure remains a disclosed coverage limitation. A tool failure must not erase a verified blocker. A material failure must prevent positive verdicts. An immaterial failure does not automatically prevent a positive verdict. `UNABLE TO VERIFY` is not a tool-error synonym; it results from material unresolved verification limits under the decision rules.

## Stopping after a verified blocker

One verified current blocker is sufficient to determine `NOT MERGE READY`. Standard Review should not stop solely because the first blocker was found when the remaining accessible relevant scope can still be inspected reasonably. It should continue enough inspection to avoid an obviously misleading or under-scoped review.

A hard access failure may end further inspection once the blocker is secure and remaining limitations are recorded. Standard Review must never claim uninspected areas are satisfactory. Focused correction direction remains limited to current verified blockers. This balanced continuation must not turn Standard Review into an exhaustive Deep Review.

## CI, review, and discussion stopping behavior

- Failed required CI is a blocker.
- Required CI still pending after final refresh applies the existing blocker rule when completion is confirmed required.
- Inaccessible required CI state is a material verification gap.
- Optional CI state is evaluated against governing evidence.
- Unavailable required review or approval state is a material verification gap.
- Confirmed missing required approval is a blocker.
- Unavailable required thread state is a material verification gap.
- Confirmed unresolved material blocking thread is a blocker.
- Lack of comments is not approval.
- No polling occurs beyond the bounded final refresh.

## Requirement and contradiction failure

Contradictions are reconciled under the evidence policy using claim-specific authority, SHA/ref, freshness, specificity, and completeness. If a material governing requirement remains contradictory after bounded recovery, classify it as a material verification gap. Standard Review must not invent a requirement or silently choose the most convenient source. User summaries and PR prose do not override repository-owned requirements.

## Same-PR re-review stopping behavior

A same-PR re-review must refresh current head and mutable state, compare previous and current heads, use prior findings only as a re-evaluation checklist, and verify every claimed fix. Newly failed evidence receives the same retry and fallback budgets. The one-head-change restart budget applies to the current invocation.

Unresolved prior blockers remain blockers when verified against current evidence. Newly inaccessible material evidence may produce `UNABLE TO VERIFY` only when no verified current blocker already determines `NOT MERGE READY`. A reported fix or passing check alone does not end re-review.

## User clarification and cancellation

Standard Review requests only the smallest missing target or material context. It must not request secrets, credentials, private AI URLs, or unrelated repository data. If the user does not provide required target identity, Standard Review stops at clarification without a merge-readiness verdict. If the user replaces the target or changes from Standard Review to another job, the current review unit ends and trigger behavior is re-evaluated. If the user cancels, Standard Review stops without fabricating conclusions.

## Logical failure record

Later output work may retain the following logical information:

- workflow phase;
- repository and PR target;
- relevant ref/head SHA;
- failed capability or inaccessible evidence;
- failure class;
- retry attempted;
- fallback attempted;
- resulting coverage limitation;
- evidence status;
- materiality;
- decision effect; and
- unresolved unknown.

This is not a final heading set, citation-rendering rule, machine-readable schema, user-facing ordering, or correction-prompt template.

## Stopping and failure matrix

| Condition | Recovery allowed | Stop condition | Evidence effect | Decision effect |
| --- | --- | --- | --- | --- |
| Missing repository/PR identity | Clarify for smallest target detail | Required target identity remains absent | No current PR target established | No merge-readiness verdict; clarification pause |
| Transient network/tool failure | Validate request and retry once | Retry and fallback are exhausted | `UNKNOWN` or `PARTIAL` for affected evidence | Material gap prevents positive verdict; immaterial limitation disclosed |
| Permanent authorization failure | Legitimate read-only fallback only | No authorized path exists | `UNKNOWN` for inaccessible evidence | Material gap prevents positive verdict |
| Target not found | Clarify or use corrected target/fallback | Confirmed target missing or inaccessible with no correction | Target-state integrity not established or limitation recorded | `UNABLE TO VERIFY` when target-state integrity fails |
| Unsupported capability | Supported read-only fallback if available | Capability remains unsupported | `UNKNOWN` or out-of-scope classification | Material gap, or decline/redirect if outside Standard Review |
| Truncated material diff | Per-file or narrower read-only fallback | Material diff remains incomplete | `PARTIAL` or `UNKNOWN` changed-scope coverage | Positive verdict prevented unless blocker already decides |
| Inaccessible material changed file | Retry/fallback/narrow file evidence | File remains inaccessible | `UNKNOWN` material file coverage | Positive verdict prevented unless blocker already decides |
| Unavailable required CI | Retry/fallback/final refresh | Required CI state remains inaccessible | `UNKNOWN` required validation state | `UNABLE TO VERIFY` absent verified blocker |
| Required CI still pending after final refresh | Final refresh only; no polling | Required completion remains pending | `VERIFIED` pending required check | Existing blocker rule applies |
| Unavailable required review/thread state | Retry/fallback/final refresh | Required state remains inaccessible | `UNKNOWN` collaboration state | Material gap prevents positive verdict |
| First head change | Restart once from target-state establishment | Restart begins on current head | Prior SHA-specific findings become historical | Recompute decision from current head only |
| Second head change in one invocation | No second restart | Head changes again before final decision | Unstable-target material verification gap | Existing rules select `UNABLE TO VERIFY` unless a verified current blocker exists |
| Contradictory material requirements | Reconcile by authority, SHA/ref, freshness, specificity, completeness | Material contradiction remains unresolved | `UNKNOWN` governing requirement | Material gap prevents positive verdict |
| Confirmed missing required artifact | Confirm absence through sufficient accessible inspection | Absence is established | `MISSING` required artifact | Blocker; `NOT MERGE READY` |
| Verified blocker plus unrelated tool failure | Record limitation; fallback if reasonable | Blocker remains verified and unrelated evidence fails | Verified blocker plus disclosed limitation | `NOT MERGE READY`; failure does not erase blocker |
| Immaterial optional evidence unavailable | Optional fallback if convenient and read-only | Optional evidence remains unavailable | Disclosed immaterial limitation | Does not automatically prevent positive verdict |
| User cancellation | None after cancellation | User cancels review | Review unit ended | No fabricated conclusion or verdict |
| Non-trigger or Deep-Review-only request | Clarify, separate, decline, or redirect | Request remains outside Standard Review | No Standard Review target/claim | No Standard Review verdict |

## Deferred specification

This document intentionally defers:

- exact verdict presentation contract;
- final output format;
- citation rendering format;
- correction-prompt contract;
- examples and golden cases beyond the compact matrix;
- evaluation implementation;
- production package structure;
- Skill frontmatter and final description;
- installation behavior; and
- Deep Review stopping/failure policy.
