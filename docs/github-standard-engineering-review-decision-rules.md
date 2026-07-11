# GitHub Standard Engineering Review — Decision Rules

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: decision rules and merge-readiness criteria definition
- production package: not implemented
- production readiness: not established

This document defines applicable criteria, blocker classification, material verification gaps, non-blocking notes, verdict-selection precedence, and same-PR re-review behavior for future Standard Review.

It does not claim an automated decision engine, complete workflow, output template, installation behavior, production package, or production readiness.

## Exact verdict names

Standard Review uses exactly these verdict names:

- `MERGE READY`
- `MERGE READY WITH NON-BLOCKING NOTES`
- `NOT MERGE READY`
- `UNABLE TO VERIFY`

Do not add aliases, grades, extra verdicts, numeric scores, confidence percentages, severity totals, or finding-count thresholds.

## Decision principles

- One current target PR is one review unit.
- Target identity and current change-state integrity are established before readiness conclusions.
- Every blocker and readiness conclusion is backed by accessible evidence.
- A confirmed failure differs from an inability to inspect or determine.
- Material unknowns prevent a positive verdict.
- One verified current blocker is sufficient for `NOT MERGE READY`.
- Unrelated partial coverage does not erase a verified blocker.
- Passing checks prove only what they exercised.
- Findings are not counted, weighted, scored, or summed to calculate a verdict.
- Non-blocking notes cannot conceal material risk.
- Standard Review cannot claim Deep Review assurance.

## Target-state integrity gate

Before selecting a readiness verdict, Standard Review must establish:

- one unambiguous repository and PR;
- accessible current PR state;
- current head SHA or equivalent change identity when available;
- current changed-file and diff association; and
- resolved target/head conflicts.

If current target identity or current change state cannot be established, select `UNABLE TO VERIFY`.

A blocker tied only to a previous head must not be used as proof against the current head. After target-state integrity is established, a verified current blocker may support `NOT MERGE READY` even if unrelated areas remain partially inspected. The coverage limitation must still be preserved and disclosed later.

## Applicable merge-readiness criteria

Apply criteria only when relevant to the PR scope and governing repository evidence. Not every PR requires every artifact.

Standard Review may evaluate:

- PR scope and changed-file coherence;
- linked Issue and acceptance criteria;
- repository instructions and conventions;
- implementation correctness;
- tests and validation appropriate to the change;
- type safety where applicable;
- error handling where applicable;
- documentation impact;
- public API impact;
- compatibility impact;
- maintainability;
- unnecessary complexity;
- current CI/check status;
- current reviews and approvals;
- unresolved review threads or blocking discussion; and
- repository-required escalation or specialist approval.

A criterion can be excluded only when scope and repository evidence support `NOT APPLICABLE`.

## Blocking finding

A blocker is a current evidence-supported condition where merging would materially violate a governing requirement or leave a known readiness failure.

Representative blockers include:

- verified unmet acceptance criterion;
- material correctness defect;
- required repository instruction violation;
- failed required validation or CI;
- pending required CI when completion is a confirmed merge requirement;
- absent required approval;
- unresolved material blocking review thread;
- required tests confirmed absent or materially inadequate;
- material type-safety or error-handling defect;
- missing required documentation;
- verified API or compatibility break contrary to contract;
- unrelated scope that materially violates the Issue/PR contract; and
- repository-required Deep Review or specialist approval confirmed absent.

Each blocker must identify the criterion, current evidence, blocking reason, and the smallest focused correction direction when practical. Speculation, preference, optional polish, and unsupported concern are not blockers.

## Material verification gap

A material verification gap is an evidence limitation that prevents a trustworthy positive judgment but does not prove failure.

Material verification gaps include:

- incomplete current diff or changed-file inspection;
- conflicting current head identity;
- inaccessible or ambiguous material acceptance criteria;
- required test result cannot be determined;
- required CI state is inaccessible or contradictory;
- required thread state is unavailable;
- material binary or oversized change cannot be evaluated;
- essential compatibility fact remains unresolved; and
- required repository instructions are inaccessible.

Confirmed failure or confirmed required absence is a blocker. Inability to inspect or determine is a verification gap. Use `UNABLE TO VERIFY` for unresolved material gaps only when target-state integrity is established and no verified blocker already establishes `NOT MERGE READY`.

## Non-blocking note

A non-blocking note is an evidence-supported observation that is not required by governing evidence, does not materially threaten correctness, validation, type safety, error handling, API, compatibility, or maintainability, and can be deferred safely.

Examples include:

- optional naming or readability improvement;
- optional refactor;
- extra tests beyond sufficient current coverage;
- optional documentation clarification;
- follow-up cleanup outside scope; and
- optional Deep Review recommendation without claiming completion.

A finding is not non-blocking merely because its fix is small.

## Evidence-status interpretation

Use existing evidence-status meanings unchanged:

- `VERIFIED` satisfied supports readiness.
- `VERIFIED` failed is a blocker.
- `MISSING` required artifact is a blocker.
- `MISSING` optional artifact is a note or `NOT APPLICABLE`.
- `PARTIAL` material criterion is a verification gap unless a blocker decides.
- `UNKNOWN` material criterion is a verification gap unless a blocker decides.
- `NOT APPLICABLE` excludes a criterion only when supported by scope and repository evidence.

Status labels do not replace reasoning about materiality or requirement status.

## Verdict-selection precedence

Select the verdict using exactly this precedence:

1. Target-state integrity not established → `UNABLE TO VERIFY`.
2. At least one verified current blocker → `NOT MERGE READY`.
3. No blocker, but unresolved material verification gap → `UNABLE TO VERIFY`.
4. No blocker or material gap, with genuine non-blocking notes → `MERGE READY WITH NON-BLOCKING NOTES`.
5. No blocker, material gap, or qualification → `MERGE READY`.

Coverage limitations remain disclosed even when a blocker is decisive. `UNABLE TO VERIFY` is not a softer `NOT MERGE READY`; it means material evidence could not be determined. `NOT MERGE READY` requires a known blocker. Positive verdicts require sufficient coverage of all material criteria. `MERGE READY` does not mean perfect, risk-free, deeply audited, or release-certified.

## Criterion-specific rules

### Scope and acceptance criteria

An unmet requirement is a blocker. An inaccessible material requirement is a verification gap. No linked Issue is not automatically a blocker; evaluate repository rules, PR context, and available acceptance evidence. Unrelated scope that materially violates the Issue or PR contract is a blocker.

### Correctness

A material correctness defect supported by current code, diff, behavior evidence, or validation output is a blocker. Inability to inspect code or behavior necessary for a correctness judgment is a verification gap.

### Tests and validation

A failed required test or validation command is a blocker. Required tests confirmed absent or materially inadequate are blockers. A required result that is inaccessible, ambiguous, stale, or not associated with the current change state is a verification gap. Extra tests beyond sufficient current coverage are optional notes, not blockers.

### CI/checks

Failed required CI is a blocker. Pending required CI is a blocker when completion is a confirmed merge requirement. Required CI state that is inaccessible or contradictory is a verification gap. Optional check failure is evaluated against repository rules and materiality rather than treated as automatically blocking or automatically ignorable.

### Reviews and unresolved threads

An absent required approval is a blocker. An unresolved material blocking thread is a blocker. Required thread or review state that is inaccessible is a verification gap. Lack of comments is not approval.

### Documentation

A verified required documentation omission is a blocker. Optional documentation clarification is a non-blocking note. When material documentation requirements are inaccessible or ambiguous, treat the issue as a verification gap rather than assuming satisfaction.

### Public API and compatibility

A verified required public API or compatibility break contrary to governing contract is a blocker. Unclear material compatibility impact is a verification gap. Public API or compatibility criteria may be `NOT APPLICABLE` only when supported by scope and repository evidence.

### Maintainability and unnecessary complexity

Material unnecessary complexity that threatens correctness, reviewability, future maintenance, or repository conventions can be a blocker when tied to governing evidence. Taste, preference, or optional simplification is not a blocker.

### Deep Review escalation

Repository-required Deep Review or specialist approval confirmed absent is a blocker. Optional escalation recommendation is a non-blocking or escalation note. Standard Review never claims Deep Review completion.

## Positive-verdict minimum conditions

Both positive verdicts require:

- established target-state integrity;
- sufficient inspection of the complete relevant change scope;
- known governing requirements for material criteria;
- no verified blockers;
- no unresolved material verification gaps;
- sufficient current CI/review state;
- all material criteria supported as satisfied or `NOT APPLICABLE`.

`MERGE READY WITH NON-BLOCKING NOTES` requires at least one genuine note. `MERGE READY` requires no merge-related qualification worth surfacing.

## Same-PR re-review

A same-PR re-review must refresh current head SHA and mutable evidence, re-evaluate each prior blocker, verify resolutions, preserve unresolved blockers, treat prior verdicts as historical context, inspect newly introduced changes, and recompute the verdict from the full precedence.

Fixing one prior blocker does not automatically produce a positive verdict.

## Decision matrix

| Condition | Evidence interpretation | Decision effect | Resulting verdict when decisive | Prohibited shortcut |
| --- | --- | --- | --- | --- |
| Unresolved target/head identity | Target-state integrity not established | Stop positive and negative readiness judgment | `UNABLE TO VERIFY` | Review from memory or stale SHA |
| Unmet acceptance criterion | Verified current requirement failure | Block merge | `NOT MERGE READY` | Downgrade to note because other criteria pass |
| Failed required CI | Verified required validation failure | Block merge | `NOT MERGE READY` | Treat local success as overriding remote failure |
| Pending required CI | Confirmed merge requirement not complete | Block until complete | `NOT MERGE READY` | Call it ready because checks have not failed yet |
| Inaccessible required CI state | Material evidence cannot be determined | Prevent positive verdict | `UNABLE TO VERIFY` | Assume pass or failure |
| Material correctness defect | Verified readiness failure | Block merge | `NOT MERGE READY` | Count against unrelated passing findings |
| Inaccessible material changed file | Material change not inspectable | Prevent positive verdict | `UNABLE TO VERIFY` | Claim complete diff coverage |
| Required tests confirmed absent | Required artifact missing | Block merge | `NOT MERGE READY` | Treat absence as optional without evidence |
| Required test result unknown | Required validation cannot be determined | Prevent positive verdict | `UNABLE TO VERIFY` | Report tests passed from assertion alone |
| Unresolved blocking thread | Current review state blocks readiness | Block merge | `NOT MERGE READY` | Treat lack of new comments as resolution |
| Required thread state unavailable | Material review state cannot be determined | Prevent positive verdict | `UNABLE TO VERIFY` | Infer no unresolved threads |
| Optional cleanup only | Evidence-supported deferrable note | Qualify if worth surfacing | `MERGE READY WITH NON-BLOCKING NOTES` | Inflate into blocker |
| No blockers/gaps | Material criteria satisfied or not applicable | Permit positive verdict | `MERGE READY` | Claim risk-free or Deep Review assurance |
| No blockers/gaps with notes | Material criteria satisfied with deferrable observations | Permit qualified positive verdict | `MERGE READY WITH NON-BLOCKING NOTES` | Hide notes inside unqualified readiness |
| Known blocker plus unrelated partial coverage | Verified blocker decides; partial coverage remains disclosed | Block merge and report limitation | `NOT MERGE READY` | Use partial coverage to avoid blocker decision |
| Prior blocker fixed but new changes exist | Historical blocker may be resolved; current state must be reviewed | Recompute full verdict | Depends on current precedence | Automatically mark ready |

## Deferred specification

This document intentionally defers:

- repository inspection order;
- complete review workflow;
- detailed stopping and retry procedure;
- final output template;
- correction-prompt format;
- exact verdict presentation contract beyond names and selection logic;
- large examples or golden cases;
- evaluation implementation;
- production package structure;
- Skill frontmatter/final description;
- installation behavior; and
- Deep Review decision rules.
