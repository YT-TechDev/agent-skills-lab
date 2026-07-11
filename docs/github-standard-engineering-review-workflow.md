# GitHub Standard Engineering Review — Workflow

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: repository inspection and review workflow definition
- production package: not implemented
- production readiness: not established

This document defines the ordered review phases, repository-inspection sequence, evidence-refresh points, material-criterion evaluation sequence, same-PR re-review flow, and preparation of decision inputs for the existing verdict rules.

This document does not claim production implementation, connector implementation, an automatic workflow engine, hidden context assembly, a final output renderer, production installation behavior, or production readiness.

## Workflow principles

- One invocation reviews one current pull request.
- Target identity is resolved before review work begins.
- Current repository-native evidence is preferred when accessible.
- The current head SHA, or equivalent change identity, is established before code analysis.
- Governing requirements are inspected before implementation judgment.
- Complete relevant change scope is inspected before any positive verdict.
- Criteria are evaluated by materiality and applicability rather than by a universal checklist requirement.
- Important conclusions retain provenance and evidence status.
- Mutable state is refreshed before final verdict selection.
- Evidence from different head SHAs is not silently combined.
- Implementation, merge, release, and Deep Review remain separate from Standard Review.
- Standard Review performs no write action.
- Unavailable evidence is never fabricated.

## Ordered logical phases

Standard Review uses exactly these ten logical phases:

1. request and target intake
2. target-state establishment
3. governing-requirement discovery
4. change-scope discovery
5. implementation and criterion inspection
6. validation, CI, review, and discussion inspection
7. evidence reconciliation and coverage check
8. current-state refresh
9. decision-rule application
10. verdict-package preparation

These are logical phases, not connector-specific calls. A connector, browser, local checkout, or user-provided sanitized excerpt may expose evidence differently, but the workflow order and evidence discipline remain the same.

## Phase 1 — request and target intake

The review begins by confirming Standard Review intent under the trigger policy. The reviewer resolves exactly one repository and exactly one pull request, identifies user constraints, identifies whether the request is a same-PR re-review, and requests only the smallest missing clarification needed to proceed.

The reviewer must never guess between multiple possible repositories, pull requests, branches, or review targets. Requests that combine Standard Review with implementation, merge execution, release work, or Deep Review are separated so the Standard Review portion remains one read-only PR review.

The workflow continues only when one unambiguous pull request target is available.

## Phase 2 — target-state establishment

Before implementation analysis, inspect the current target state:

- repository identity;
- pull request number and state;
- base and head refs;
- head SHA or equivalent change identity;
- changed-file list; and
- complete diff or per-file patches.

Check repository, pull request, ref, SHA, and path consistency. Target/head conflicts are surfaced rather than reconciled silently. Evidence associated with a previous head is historical evidence only unless verified against the current head.

Apply the target-state integrity gate defined by the decision rules. Retry limits and terminal failure behavior remain deferred to later specification.

## Phase 3 — governing-requirement discovery

Before judging implementation, inspect governing requirements when relevant and accessible, including:

- `AGENTS.md` or equivalent repository instructions;
- contribution or review rules;
- linked Issues;
- acceptance criteria;
- repository documentation defining intended behavior;
- public API or compatibility commitments owned by the repository;
- required checks, approvals, escalation, or specialist review; and
- PR non-goals and user constraints.

Apply evidence-policy contradiction handling when requirements conflict or cannot be reconciled. PR prose and user summaries guide inspection, but they do not override governing repository evidence.

## Phase 4 — change-scope discovery

Enumerate every changed file and classify relevant changes, such as code, tests, documentation, configuration, CI, fixtures, generated output, binary or oversized content, or other categories. Not every category is required for every pull request.

Identify changed public surfaces and likely runtime, type-safety, error-handling, compatibility, documentation, and maintenance implications. Compare actual changes with Issue and PR scope, and identify unrelated or accidental scope.

Preserve coverage limitations for inaccessible, truncated, binary, and oversized files or patches. A positive verdict requires sufficient inspection of the complete relevant changed-file and diff scope.

## Phase 5 — implementation and criterion inspection

Inspect the complete relevant change scope against applicable decision-rule criteria:

- correctness;
- acceptance criteria;
- repository conventions;
- type safety where applicable;
- error handling where applicable;
- documentation impact;
- public API impact;
- compatibility impact;
- maintainability;
- unnecessary complexity; and
- scope coherence.

Trace findings to current evidence, distinguish direct evidence from inference, and classify each material criterion as a blocker, material verification gap, non-blocking note, satisfied criterion, or `NOT APPLICABLE`.

Avoid preference-based blockers and avoid Deep Review claims. Relevant unchanged context may be inspected to understand the diff, but Standard Review must not become a broad repository audit.

## Phase 6 — validation, CI, review, and discussion inspection

Inspect validation and collaboration evidence when applicable:

- relevant test source;
- validation commands and accessible output;
- current CI/check status;
- workflow or job summaries and logs when needed;
- current reviews and approvals;
- unresolved review threads;
- PR comments and discussion; and
- linked test or CI artifacts.

Distinguish check existence, execution, status, logs, scope, and coverage. Passing checks do not replace code review. Local claims do not override contradictory current remote evidence.

## Phase 7 — evidence reconciliation and coverage check

Prepare review state sufficient for the decision rules, including:

- target-state integrity;
- applicable material criteria;
- each material criterion status;
- verified blockers;
- material verification gaps;
- genuine non-blocking notes;
- satisfied criteria;
- `NOT APPLICABLE` criteria;
- evidence conflicts;
- coverage limitations; and
- required escalation state.

Reconcile evidence by target identity, claim relevance, source authority, SHA/ref association, freshness, specificity, and completeness.

This phase does not add an evidence-ledger schema or output template.

## Phase 8 — current-state refresh

Immediately before decision selection, refresh mutable state:

- PR state;
- head SHA and refs;
- changed-file list;
- diff or patch association;
- CI/check status;
- reviews and approvals;
- unresolved threads;
- PR comments and discussion; and
- linked-Issue state when material.

When the head changes during review, invalidate previous-head SHA-specific conclusions, retain them only as history, restart target-state establishment, re-inspect newly changed scope, and do not issue a positive verdict from stale evidence.

Retry budgets and terminal failure behavior remain deferred.

## Phase 9 — decision-rule application

Reuse the existing decision precedence unchanged:

1. target-state integrity failure → `UNABLE TO VERIFY`
2. verified current blocker → `NOT MERGE READY`
3. material verification gap without blocker → `UNABLE TO VERIFY`
4. no blocker/gap, with notes → `MERGE READY WITH NON-BLOCKING NOTES`
5. no blocker/gap/qualification → `MERGE READY`

Do not add verdicts, count findings, score findings, hide limitations, treat `UNABLE TO VERIFY` as a softer blocker verdict, or treat one fixed blocker as proof of full readiness.

Use the exact verdict names defined by the decision rules.

## Phase 10 — verdict-package preparation

Prepare only the logical information needed by the later output contract:

- exact verdict;
- repository and PR;
- reviewed head SHA or equivalent identity;
- concise evidence-grounded summary;
- blockers, when present;
- material verification gaps, when present;
- non-blocking notes, when present;
- validation and CI state;
- coverage and access limitations;
- escalation state; and
- focused correction direction for blockers when practical.

This phase does not define section headings, final formatting, citation syntax, a correction-prompt template, or user-facing presentation order.

## Same-PR re-review workflow

A same-PR re-review must confirm the same repository and PR, refresh head SHA and mutable evidence, compare current and previously reviewed heads, and use previous findings only as a checklist.

The reviewer verifies each prior blocker, inspects newly introduced changes, retains unresolved blockers, identifies new blockers or gaps, and recomputes material criteria and verdict from current evidence.

A reported fix, new commit, passing check, or prior approval does not complete re-review by itself.

## Scope and escalation control

Standard Review preserves normal engineering merge-readiness scope, directly relevant external inspection only, Deep Review recommendation when warranted, and no claim that Deep Review was completed.

It remains separate from implementation, merge, release, deployment, security, privacy, architecture, dependency, and release-certification work. Standard Review is strictly read-only and performs no write action.

## Workflow matrix

| Phase | Required outcome | Typical evidence | Refresh/restart condition | Deferred detail |
| --- | --- | --- | --- | --- |
| 1. request and target intake | One unambiguous Standard Review target | User request, trigger policy, repository and PR identifiers | Multiple targets or mixed requests require clarification or separation | Exact clarification wording |
| 2. target-state establishment | Current target identity and changed state established | PR state, base/head refs, head SHA, changed files, diff or patches | Target, ref, SHA, or path conflict restarts identity establishment | Retry limits and terminal failure behavior |
| 3. governing-requirement discovery | Applicable requirements identified before implementation judgment | Repository instructions, contribution rules, linked Issues, acceptance criteria, docs, required checks or approvals | Material requirement contradiction or newly discovered governing evidence triggers reconciliation | Complete requirement taxonomy |
| 4. change-scope discovery | Complete relevant changed-file and diff scope understood | Changed-file list, per-file patches, binary/truncated markers, public-surface changes | Changed-file list or diff association changes restart scope discovery | Connector-specific pagination or size handling |
| 5. implementation and criterion inspection | Applicable criteria classified by current evidence | Diff, relevant unchanged context, tests, docs, repository conventions | Head change or material new context requires re-inspection | Deep Review procedure and broad audit workflow |
| 6. validation, CI, review, and discussion inspection | Validation and collaboration state distinguished by status, logs, scope, and coverage | Test sources, command output, CI checks, job summaries, reviews, threads, comments | New CI, reviews, comments, or thread changes require refresh before decision | CI-log retrieval strategy and retry budgets |
| 7. evidence reconciliation and coverage check | Decision-ready evidence state assembled | Findings, evidence statuses, conflicts, limitations, escalation requirements | Contradictory or incomplete material evidence triggers reconciliation | Evidence-ledger schema and output template |
| 8. current-state refresh | Mutable state confirmed immediately before decision | PR state, head SHA, refs, changed files, diff association, checks, reviews, threads, comments | Head change restarts target-state establishment and invalidates SHA-specific conclusions | Terminal stale-state handling |
| 9. decision-rule application | Existing verdict precedence applied unchanged | Reconciled criterion statuses, blockers, gaps, notes, limitations | Any refreshed material evidence change requires recomputation | Alternative scoring or new verdicts |
| 10. verdict-package preparation | Logical decision inputs prepared for later presentation | Verdict, target, reviewed head, summary, blockers, gaps, notes, validation/CI, limitations, escalation | Output must match refreshed current evidence | Final format, citation rendering, and presentation order |

## Deferred specification

This document intentionally defers:

- detailed stopping and failure conditions;
- retry counts and time budgets;
- terminal tool-failure behavior;
- exact verdict presentation contract;
- final output format;
- citation rendering;
- correction-prompt contract;
- examples or golden cases beyond the workflow matrix;
- evaluation implementation;
- production package structure;
- Skill frontmatter/final description;
- installation behavior; and
- Deep Review workflow.
