# Evidence and Decisions

## Authority, provenance, freshness, and applicability

Important conclusions require evidence next to the claim. Evidence authority is claim-relative: current PR state comes from current PR/repository evidence; requirements from repository docs, instructions, linked Issues, and acceptance criteria; validation from logs/checks or exact user-reported commands; review status from current review and thread state. Prefer fresh, current-head evidence. Use `NOT APPLICABLE` only when PR scope and repository evidence support exclusion.

## Exact evidence statuses

- `VERIFIED`: adequate authoritative evidence supports the claim.
- `PARTIAL`: some relevant evidence exists but coverage is incomplete.
- `MISSING`: an expected or required artifact is confirmed absent from accessible sources.
- `UNKNOWN`: required evidence is unavailable, stale, ambiguous, or contradictory.
- `NOT APPLICABLE`: the criterion does not apply based on scope and repository evidence.

Distinguish facts, reasonable inferences, and unknowns. Do not turn inaccessible evidence into pass or fail.

## Classification

A blocker is a verified current-head failure of a material requirement or confirmed missing required artifact. A material verification gap is missing, partial, unknown, inaccessible, stale, or contradictory evidence needed for a readiness conclusion when no verified blocker already decides. A non-blocking note is an optional, evidence-supported improvement that does not affect merge readiness. Satisfied criteria are verified or evidence-supported `NOT APPLICABLE`.

## Canonical decision table

| State after bounded recovery | Verdict or ending |
| --- | --- |
| Intake, clarification, redirect, decline, cancellation, or target replacement before readiness selection | `NO VERDICT` |
| Any verified current blocker | `NOT MERGE READY` |
| No verified current blocker, but any material verification gap | `UNABLE TO VERIFY` |
| No blocker or material gap, with genuine optional notes | `MERGE READY WITH NON-BLOCKING NOTES` |
| No blocker, material gap, or genuine note | `MERGE READY` |

This is the only decision table. Do not use scores, percentages, severity totals, or finding-count verdict logic.

## Positive-verdict eligibility

A positive verdict requires target-state integrity, complete material coverage, all material criteria `VERIFIED` satisfied or evidence-supported `NOT APPLICABLE`, current validation/CI/review state interpreted from evidence, no current blocker, and no material verification gap.

## Unsupported-claim restrictions and conflicts

Do not claim tests passed, CI passed, approvals exist, files were inspected, behavior works, requirements are complete, a PR is safe, a release/deployment is ready, or an audit was completed without inspected evidence. Do not silently resolve material conflicts; classify the affected claim as `UNKNOWN` or `PARTIAL` unless a separate verified blocker already decides.

## Historical evidence, approvals, and CI

Previous-head evidence is historical. Prior blockers must be reverified against the current head. Passing CI supports only what it exercised and does not replace code review. Failed required CI, pending required CI after final refresh, or confirmed missing required approval/specialist review is a blocker when tied to the current PR requirements.
