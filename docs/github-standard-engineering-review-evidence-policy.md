# GitHub Standard Engineering Review — Evidence Policy

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: evidence hierarchy and evidence-status definition
- production package: not implemented
- production readiness: not established

This document defines evidence categories, claim-relative authority, provenance, freshness, conflict handling, inference limits, and evidence-status meanings for future Standard Review.

It does not establish or claim:

- a production Skill implementation;
- an evidence-ledger implementation;
- a machine-readable evidence schema;
- connector implementation;
- automatic provenance capture;
- automatic evidence refresh;
- verdict-selection logic;
- production installation behavior; or
- production readiness.

## Evidence principles

Standard Review must apply these principles:

- Every important conclusion must be traceable to supporting evidence.
- Evidence authority is evaluated for the specific claim being made.
- Current target-bound evidence is preferred for current PR-state claims.
- Exact source content is preferred over summaries when both are available.
- Evidence should retain repository, PR, ref, SHA, path, check, review, or external-source association when available.
- Mutable evidence must be checked for freshness before being presented as current.
- Partial access remains partial.
- Absence of evidence is not automatically evidence of absence.
- Passing checks prove only what those checks exercised.
- Unsupported certainty is prohibited.
- Reasonable inference must be labeled and bounded.
- Inaccessible or unresolved conflicting evidence remains unknown.

This is not a simplistic universal source ranking. The strongest source depends on the claim. This document does not define the final verdict algorithm.

## Claim-relative evidence categories

### Current target-state evidence

Examples include:

- current PR metadata and state;
- current head SHA and refs;
- changed-file list;
- complete diff or per-file patches;
- current repository files at known refs;
- current CI/check results;
- current review submissions;
- current unresolved review threads;
- current PR discussion/comments; and
- current linked-Issue state.

Use this category for claims about what the target PR currently contains or what GitHub currently reports.

### Governing requirement evidence

Examples include:

- repository instructions;
- contribution rules;
- linked Issue acceptance criteria;
- repository documentation defining expected behavior;
- public API commitments owned by the repository; and
- compatibility commitments owned by the repository.

Use this category for claims about what the change is required to satisfy.

### Validation evidence

Examples include:

- test source;
- current CI/check result;
- workflow/job summary;
- available logs;
- reproducible validation command and output;
- static-analysis result; and
- type-check result.

A passing result supports only the checks actually run. A passing result does not prove general correctness, complete coverage, or absence of regressions.

### Review and discussion evidence

Examples include:

- submitted reviews;
- unresolved review threads;
- maintainer comments;
- author explanations; and
- recorded design rationale.

Discussion can identify requirements, concerns, or intent, but it cannot override contradictory current code or repository evidence.

### Supporting context

Examples include:

- PR description;
- user summary;
- local validation claim without accessible output;
- sanitized excerpt;
- linked official external documentation; and
- explanation of an unusual design choice.

Supporting context may guide inspection but is not automatically verified current-state evidence.

### Historical context

Examples include:

- prior review findings;
- prior verdicts;
- cached tool results;
- stale CI status;
- evidence tied to a previous head SHA; and
- conversation memory.

Historical context may guide re-review but is not proof of current PR state.

## Claim-specific authority rules

### Current PR state

Prefer current structured GitHub and repository evidence associated with the current target and current head SHA over PR prose, user summaries, local-only claims, cached results, or conversation memory.

### Requirements and acceptance criteria

Prefer repository-governing instructions, linked Issue acceptance criteria, and maintained repository documentation over informal summaries. Contradictory governing sources must be surfaced rather than silently resolved. This document does not define the eventual precedence algorithm for every possible repository.

### Test and validation claims

Prefer current check status, test definitions, workflow/job summaries, accessible logs, and output over statements that tests passed. Distinguish check existence, check execution, check status, available logs, test scope, and coverage.

### Review status

Prefer current review submissions and unresolved-thread state over textual claims that review is complete.

### External API or compatibility facts

Prefer directly relevant official documentation or specification for the external fact. Use repository evidence to determine how the target PR interacts with that fact. External documentation does not prove the target PR's implementation state by itself.

### Intended behavior

Use linked requirements, repository documentation, PR description, and author explanation as intent evidence. Verify implementation claims against current code, diff, and validation evidence. This document does not define repository inspection order.

## Exact evidence-status vocabulary

These statuses classify evidence or review criteria only. They are not mapped to final verdicts in this document.

### `VERIFIED`

The claim is directly supported by current, accessible, relevant evidence with sufficient target, ref, SHA, or source association for that claim. Not every claim must be SHA-bound when the evidence is mutable non-code state, but it must have appropriate current-source association.

### `PARTIAL`

Some relevant evidence is available, but one or more of these are incomplete: coverage, freshness, target association, pagination, logs, file visibility, review-thread visibility, or scope.

### `MISSING`

An expected or required evidence artifact is confirmed absent from otherwise sufficiently inspected accessible sources. `MISSING` is a confirmed absence. Inability to inspect is not `MISSING`; it is normally `UNKNOWN` or `PARTIAL`.

### `UNKNOWN`

The claim cannot be determined because evidence is inaccessible, contradictory, ambiguous, stale without refresh, truncated, incompletely paginated, or otherwise insufficient to establish presence or absence.

### `NOT APPLICABLE`

The criterion does not apply to the target PR based on PR scope and relevant repository evidence. Do not use `NOT APPLICABLE` because evidence is inconvenient to obtain, and do not use it as a substitute for `UNKNOWN`.

## Provenance and traceability

Important conclusions must retain enough provenance to identify the supporting source when available, including:

- repository `owner/name`;
- PR number;
- current head SHA or relevant ref;
- file path and line/range when practical;
- Issue number;
- check/workflow/job identity;
- review or thread identity;
- external document identity; and
- observation time when freshness matters.

A source reference must actually support its associated conclusion. Provenance should be specific enough for later verification. Provenance does not make a weak or stale source authoritative. A citation to a summary does not become proof of underlying current state.

This document does not create a JSON schema, YAML schema, typed evidence object, mandatory evidence-ledger format, or output template.

## Freshness and SHA anchoring

- Current head SHA anchors code, diff, changed-file, and SHA-specific validation evidence when available.
- Evidence tied to a previous head SHA becomes historical after the head changes.
- PR state, reviews, threads, comments, linked Issues, and CI remain mutable even when head SHA does not change.
- Stale evidence may remain useful as history but must not be presented as current.
- Timestamps alone do not prove content freshness.
- Cached tool results must not be assumed current.
- Final review conclusions will require refresh behavior later defined by the workflow specification.

This document does not define the complete refresh sequence.

## Completeness and coverage

- Complete claims require complete relevant coverage.
- Partial changed-file coverage cannot support a claim that all changed files were reviewed.
- Incomplete pagination reduces evidence coverage.
- Truncated responses reduce evidence coverage.
- Inaccessible files reduce evidence coverage.
- Binary-only changes may limit semantic verification.
- Oversized-file limitations must be preserved.
- Unavailable logs reduce what can be claimed about execution details.
- Unavailable review-thread data prevents complete thread-state claims.
- Visible CI status without logs supports the status claim, not detailed execution-content or failure-cause claims.
- Public rendered pages may expose less structured data than repository-native sources.
- Missing optional context does not prove requirement satisfaction.

This document does not define final verdict-specific sufficiency thresholds.

## Negative evidence and absence claims

- Do not claim no tests exist unless the relevant accessible scope was inspected sufficiently.
- Do not claim no unresolved threads exist when thread data is unavailable.
- Do not claim no public API impact exists because the PR description omits it.
- Do not claim no documentation change is needed because documentation was not changed.
- Do not claim no compatibility risk exists because no risk was reported.
- Silence in comments or PR prose is not approval.
- Silence is not requirement satisfaction.
- Distinguish `not found after complete relevant inspection` from `not observed in partial evidence`.
- Negative claims require coverage appropriate to the claim.

## Inference policy

Reasonable inference is permitted only when:

- direct evidence is identified;
- the inference follows clearly from that evidence;
- no accessible evidence contradicts it;
- it is labeled as inference rather than verified fact; and
- it remains within Standard Review scope.

Inference must not:

- invent inaccessible code;
- invent acceptance criteria;
- convert user claims into verified results;
- infer remote CI success from local success;
- infer review approval from lack of comments;
- infer full coverage from one passing check; or
- infer security, privacy, architecture, dependency, or release assurance beyond Standard Review scope.

## Conflict handling

Conflicting evidence must be surfaced and evaluated using target identity, claim relevance, source authority for that claim, SHA/ref association, freshness, specificity, and completeness.

Examples include:

- PR description conflicts with current diff;
- user summary conflicts with current GitHub state;
- linked Issue acceptance criteria conflict with repository instructions;
- two read sources report different head SHAs;
- two read sources report different CI/check states;
- current file content conflicts with cached content;
- local test claim conflicts with current remote CI; and
- prior verdict conflicts with current changed state.

Do not silently reconcile material conflicts. Unresolved material conflict is `UNKNOWN` or `PARTIAL` for the affected claim. Conflict in one claim does not automatically invalidate unrelated verified claims. This document does not map conflicts to final verdicts.

## Concise evidence matrix

| Claim or criterion | Strongest typical evidence | Supporting evidence | Common limitation | Prohibited overclaim |
| --- | --- | --- | --- | --- |
| Current PR state | Current structured PR metadata for the target PR | PR page, user-provided PR URL | stale cache or wrong target | Current state is verified from a summary alone |
| Changed files and diff | Changed-file list and complete diff or patches at current head SHA | PR description or author summary | pagination, truncation, binary files | All changed files were reviewed from partial files |
| Acceptance criteria | Linked Issue criteria and repository requirements | PR description or maintainer comment | inaccessible Issue or conflicting requirements | Criteria are satisfied without implementation evidence |
| Repository instructions | Current repository instruction files and contribution docs | user summary of rules | hidden or inaccessible rules | No rules exist without sufficient inspection |
| Implementation correctness | Current code, diff, requirements, and validation evidence | author explanation | limited scope or untested paths | Passing checks prove general correctness |
| Test existence | Test files, workflow definitions, and changed test paths | README command notes | incomplete file visibility | No tests exist from a narrow search |
| Test result | Current check result or reproducible command output | user-reported local run | logs unavailable or stale SHA | Tests passed remotely because local tests passed |
| CI status | Current check suite/status for target PR | badge or PR prose | logs unavailable or delayed checks | Visible status proves execution details |
| Review approval | Current review submissions | comments saying looks good | stale approval or new commits | Silence means approval |
| Unresolved threads | Current review-thread state | discussion excerpts | thread data unavailable | No unresolved threads when threads were inaccessible |
| Documentation impact | Changed docs, relevant docs, and requirements | PR prose | docs not inspected | No docs needed because none changed |
| Public API or compatibility impact | Current diff plus repository API/compat commitments | author explanation | unclear owned commitment | No API impact because none was mentioned |
| User-provided local result | Accessible command output with environment and ref details | user statement | no output or unverified environment | User claim is verified validation |
| External API fact | Official external documentation or specification | blog or summary | outdated external source | External docs prove PR implementation |
| Same-PR re-review finding | Refreshed current evidence and prior finding as checklist | prior verdict | head SHA or thread state changed | Prior verdict still applies automatically |

## Deferred specification

This document does not define:

- repository inspection order;
- review workflow;
- stopping conditions;
- final evidence-sufficiency thresholds;
- decision rules;
- verdict-selection algorithm;
- exact verdict-contract details beyond the existing names;
- output template;
- correction-prompt contract;
- examples or golden cases;
- evaluation implementation;
- production package structure;
- Skill frontmatter or final description;
- production installation behavior; or
- deep-review evidence policy.
