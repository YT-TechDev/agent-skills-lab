# Verdict and Output

## Verdict eligibility

Use exactly one readiness verdict: `MERGE READY`, `MERGE READY WITH NON-BLOCKING NOTES`, `NOT MERGE READY`, or `UNABLE TO VERIFY`. `NO VERDICT` is allowed only for intake, clarification, redirect, decline, cancellation, and target replacement, and is not a fifth verdict.

Do not claim merge execution, approval, release readiness, deployment readiness, production readiness, full security audit, privacy audit, architecture audit, dependency audit, or Deep Review completion.

## Canonical output order

1. `## Verdict: <EXACT VERDICT>`
2. reviewed target block with repository, PR, base, head, current reviewed head SHA or equivalent identity, and review timestamp/status when available
3. concise summary
4. decisive findings when required
5. validation and review state
6. coverage/access limitations when present
7. escalation when material
8. focused correction or re-verification direction when required
9. concise Standard Review scope note

Place evidence next to claims. Distinguish local validation, user-reported validation, and current remote checks. Omit empty optional headings.

## Exact headings and conditions

- `## Verdict: <EXACT VERDICT>`: always required for readiness verdicts.
- `### Blocking findings`: required for `NOT MERGE READY`; include only verified current blockers.
- `### Material verification gaps`: required for `UNABLE TO VERIFY`; include material gaps after bounded recovery.
- `### Non-blocking notes`: required only when genuine optional notes support `MERGE READY WITH NON-BLOCKING NOTES`; optional for other verdicts only when useful and non-confusing.
- `### Validation and review state`: required for all readiness verdicts.
- `### Coverage and access limitations`: required when limitations exist; disclose material and relevant immaterial limits.
- `### Escalation`: required when Standard Review identifies material need for Deep Review or specialist review.
- `### Focused correction direction`: required for `NOT MERGE READY`; do not include next-Issue work while blockers remain.
- `### Re-verification requirement`: required when fixes or changed evidence must be checked before readiness can be claimed.
- `### Re-review delta`: required for same-PR re-review when prior review context materially influenced inspection.

## Verdict-specific obligations

`MERGE READY` requires no blockers, no material gaps, no genuine notes, and complete material coverage. `MERGE READY WITH NON-BLOCKING NOTES` requires no blockers or material gaps and at least one genuine optional note. `NOT MERGE READY` requires at least one verified current blocker; unrelated inaccessible evidence remains a limitation, not a reason to downgrade. `UNABLE TO VERIFY` requires no verified current blocker and at least one material verification gap.

## Presentation prohibitions

Do not invent connector-specific citation syntax, expose raw tool arguments or connector IDs, require a coding agent or branch workflow, fabricate evidence, provide scores, use confidence percentages, count findings into verdicts, or treat passing CI as a replacement for code review.
