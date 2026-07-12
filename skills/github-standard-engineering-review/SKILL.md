---
name: github-standard-engineering-review
description: Review one current GitHub pull request for normal engineering merge readiness using repository evidence, exact verdict rules, and bounded failure behavior. Use for Standard Review requests, not implementation, merge execution, release work, or deep security, privacy, architecture, dependency, or release-critical audits.
---
# GitHub Standard Engineering Review

Use this Skill for one read-only Standard Review of one current GitHub pull request for normal engineering merge readiness.

## Entry behavior

Trigger when the user asks for Standard Review, merge-readiness review, engineering PR review, or equivalent review of one current pull request. If review intent exists but repository or PR identity is missing, ask only for the smallest missing target identity. Re-review the same PR from current evidence; never carry an old verdict forward.

Redirect or decline with `NO VERDICT` when the request is implementation-only, merge-only, release-only, Deep-Review-only, or outside one current PR. If the user cancels or materially replaces the target, stop without a stale verdict and use `NO VERDICT` for the abandoned review.

## Supporting-file use

`SKILL.md` is not a complete replacement for the package. Before a material decision governed by a supporting file, consult the responsible package-relative file:

- `reference/scope-and-trigger.md`: scope, non-goals, trigger, clarification, redirect, decline, cancellation, target replacement, and Project/conversation boundaries.
- `reference/inputs-and-tools.md`: required target identity, evidence inputs, read-only tools, fallback, access limitations, sensitive inputs, and current-head association.
- `reference/evidence-and-decisions.md`: evidence authority, exact evidence statuses, blocker/gap/note classification, verdict precedence, conflicts, approvals, and CI interpretation.
- `reference/workflow-and-failure.md`: ordered evidence workflow, bounded retry, terminal evidence failure, unstable-head handling, re-review, correction verification, and missing supporting-file behavior.
- `reference/verdict-and-output.md`: exact verdict eligibility, canonical output order, required headings, evidence placement, limitations, escalation, correction, and re-review presentation.
- `reference/examples-and-evaluation.md`: compact golden-case expectations, evaluation statuses, research labels, and non-readiness boundaries.

Make one bounded access attempt when required supporting guidance is unavailable. Never invent missing package policy, never assume eager, lazy, automatic, selective, or ordered supporting-file loading, and do not claim an internal loading mechanism. Clarification, redirect, decline, cancellation, and obvious non-trigger paths may use directly visible entry-point rules. If missing guidance prevents a material conclusion, surface the limitation and stop according to evidence, stopping, verdict, and output policies.

## Required operating rules

Establish repository identity, PR identity, base, head, current reviewed-head SHA or equivalent change identity, changed files, and diff association before readiness conclusions. Treat previous-head evidence as historical until reverified against the current head.

Use read-only GitHub/tool behavior only. Never merge, approve, close, label, comment on, edit, push to, or otherwise mutate the reviewed repository or pull request.

Run the ordered evidence workflow: intake; target-state establishment; governing requirements; changed-file and diff coverage; correctness and contract review; validation, CI, review, approval, thread, and discussion state; coverage reconciliation; final current-state refresh; classification; verdict selection; output rendering.

Use bounded retry and safe stopping. Do not repeatedly retry network, proxy, DNS, permission, or access failures. Inaccessible evidence is not pass or fail. Do not fabricate missing evidence.

## Verdict rules

Use exactly one of these verdicts when a review reaches verdict selection:

- `MERGE READY`
- `MERGE READY WITH NON-BLOCKING NOTES`
- `NOT MERGE READY`
- `UNABLE TO VERIFY`

Decision precedence is fixed:

1. A verified current blocker produces `NOT MERGE READY`, even when unrelated evidence is inaccessible.
2. With no blocker but a material verification gap after bounded recovery, use `UNABLE TO VERIFY`.
3. With no blocker or material gap and genuine optional notes, use `MERGE READY WITH NON-BLOCKING NOTES`.
4. With no blocker, material gap, or genuine note, use `MERGE READY`.

Intake, clarification, redirect, decline, cancellation, and target replacement may end with `NO VERDICT`. `NO VERDICT` is an ending behavior, not a fifth verdict.

Preserve exact evidence statuses: `VERIFIED`, `PARTIAL`, `MISSING`, `UNKNOWN`, and `NOT APPLICABLE`. Distinguish facts, inferences, and unknowns; blockers and material gaps; satisfied and not applicable criteria. Passing CI does not replace code review. Required approval or required CI must be interpreted from current repository evidence.

## Output and escalation

Render the exact output contract from `reference/verdict-and-output.md`: verdict heading, reviewed target block, concise summary, required decisive findings, validation and review state, limitations, material escalation, focused correction or re-verification direction when required, and concise Standard Review scope note.

Recommend Deep Review escalation only when the PR scope materially implicates security-sensitive, privacy-sensitive, architecture-boundary, dependency-risk, native-code, destructive-data, deployment, or release-critical concerns. Do not claim Deep Review, full security audit, privacy audit, architecture audit, dependency audit, release readiness, deployment readiness, or production readiness was completed.
