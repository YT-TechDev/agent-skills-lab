# Workflow and Failure

## Ordered workflow

1. Decide trigger, non-trigger, clarification, redirect, decline, cancellation, or target replacement.
2. Establish target state: repository, PR, state, base, head, current head SHA or equivalent identity, changed files, and diff.
3. Discover governing requirements, including instructions, linked Issues, acceptance criteria, docs, APIs, compatibility, and required approvals.
4. Inspect complete changed-file and diff coverage relevant to the PR.
5. Review correctness, contracts, error handling, type safety, documentation, compatibility, maintainability, and unnecessary complexity when applicable.
6. Inspect validation, CI, review, approval, thread, and discussion state.
7. Reconcile coverage, evidence statuses, conflicts, blockers, material gaps, notes, satisfied criteria, and `NOT APPLICABLE` criteria.
8. Refresh mutable current state before verdict selection.
9. Apply the canonical decision table.
10. Render the required output contract.

## Bounded retries and fallbacks

Make bounded attempts proportionate to materiality. Use alternate read-only sources when available. Do not repeatedly retry network, proxy, DNS, permission, HTTP 403, or connector failures. Record the retry bound when unstable head or access recovery matters.

## Terminal evidence failure

If required target identity or current change state cannot be established, stop with `UNABLE TO VERIFY` once a review has reached verdict selection. If a material evidence source remains inaccessible after bounded recovery and no verified blocker decides, use `UNABLE TO VERIFY`. Immaterial access failures may be disclosed without preventing a positive verdict.

## Unstable head behavior

If the head changes during review, refresh once and reassociate evidence. If it changes again or cannot be stabilized within the documented bounded retry, use `UNABLE TO VERIFY`. Do not combine evidence from different heads silently.

## Same-PR re-review

A re-review is a new current-evidence review. Prior findings guide inspection but do not decide the new verdict. Reverify reported fixes, prior blockers, validation, CI, approvals, and thread state against the current head.

## Cancellation, target replacement, correction, and re-verification

Cancellation or material target replacement ends the abandoned review with `NO VERDICT`. For `NOT MERGE READY`, include focused correction direction only for current verified blockers. For claimed fixes, require current evidence before changing the finding; otherwise preserve the appropriate gap or blocker.

## Missing supporting-file behavior

If a required supporting file is unavailable, make one bounded access attempt. If still unavailable, do not invent the missing package policy or silently rely on `SKILL.md` as complete. For material conclusions governed by the missing guidance, surface the limitation and stop under evidence, decision, and output rules. Obvious non-trigger, clarification, redirect, decline, cancellation, and target-replacement paths may use visible entry rules.
