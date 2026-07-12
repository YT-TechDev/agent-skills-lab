# Verdict and Output

## Verdict eligibility

Use exactly one readiness verdict: `MERGE READY`, `MERGE READY WITH NON-BLOCKING NOTES`, `NOT MERGE READY`, or `UNABLE TO VERIFY`. `NO VERDICT` is allowed only for intake, clarification, redirect, decline, cancellation, and target replacement, and is not a fifth verdict.

Do not claim merge execution, approval, release readiness, deployment readiness, production readiness, full security audit, privacy audit, architecture audit, dependency audit, or Deep Review completion.

## Canonical output order

1. `## Verdict: <EXACT VERDICT>`
2. reviewed target block
3. concise summary
4. decisive findings when required
5. validation and review state
6. coverage/access limitations when present
7. escalation when material
8. focused correction or re-verification direction when required
9. concise Standard Review scope boundary

Every verdict output must end with the Standard Review scope boundary. Place evidence next to claims. Distinguish local validation, user-reported validation, and current remote checks. Omit empty optional headings.

## Concise summary

The concise summary must explain why the verdict was selected, identify the decisive evidence category, avoid repeating all findings, and remain within Standard Review scope. Positive verdicts must state that no blocker or material verification gap was found within Standard Review scope.

## Finding content and evidence presentation

Each blocker, material verification gap, or non-blocking note must compactly include a short title, governing criterion or requirement, current evidence and source reference, target/head association when relevant, merge-readiness effect, and correction or re-verification direction when applicable.

Require at least one direct evidence reference per blocker, the exact inaccessible source or coverage area per material gap, current evidence for important positive-readiness claims, current-head association for CI, reviews, and threads when available, user-provided evidence labeled as user-provided, inferences labeled and evidence-supported, and previous-head evidence labeled historical.

## Validation and review state

Include material applicable state for local or user-reported validation with clear labeling, current remote CI/check status, required versus optional interpretation, review and approval state, unresolved material thread state, relevant PR discussion state, and head association. Passing CI does not replace code review.

## Reviewed target block

Immediately after the verdict heading, include a compact reviewed target block with:

- repository;
- PR number and title when available;
- base ref;
- head ref;
- reviewed head SHA or equivalent identity; and
- review mode: `initial` or `same-PR re-review`.

For `UNABLE TO VERIFY` when current PR or change-state integrity cannot be established, repository and PR identity must still be established. Show head or change state as `UNKNOWN` or an equivalent explicit unresolved state, and name the exact unresolved target-state property. Omit that field when target-state integrity is established and `UNABLE TO VERIFY` results only from a material verification gap.

## Exact headings and conditions

- `## Verdict: <EXACT VERDICT>`: always required for readiness verdicts.
- `### Blocking findings`: required for `NOT MERGE READY`; include only verified current blockers.
- `### Material verification gaps`: required whenever material gaps exist, including under `NOT MERGE READY`; required for `UNABLE TO VERIFY`.
- `### Non-blocking notes`: include only for genuine non-blocking notes; required for `MERGE READY WITH NON-BLOCKING NOTES`.
- `### Validation and review state`: required for all readiness verdicts.
- `### Coverage and access limitations`: required when limitations exist; disclose material and relevant immaterial limits.
- `### Escalation`: required when required Deep Review or specialist approval affects the verdict, or when an optional Deep Review recommendation is surfaced as a genuine non-blocking note.
- `### Focused correction direction`: required for `NOT MERGE READY`; do not include next-Issue work while blockers remain.
- `### Re-verification requirement`: required for `UNABLE TO VERIFY`; identify the smallest evidence, access, target-state, or repository-state change needed for another review when known.
- `### Re-review delta`: optional when materially useful for same-PR re-review; it never replaces full current-scope evaluation.

## Verdict-specific required and forbidden sections

`MERGE READY` requires the verdict heading, reviewed target block, concise summary, validation and review state, and Standard Review scope boundary. It may include coverage/access limitations only when immaterial limitations exist. It must not include `### Blocking findings`, `### Material verification gaps`, `### Non-blocking notes`, required correction language, or required pre-merge work.

`MERGE READY WITH NON-BLOCKING NOTES` requires the verdict heading, reviewed target block, concise summary, `### Non-blocking notes`, validation and review state, and Standard Review scope boundary. It also requires `### Escalation` when an optional escalation recommendation is surfaced as a genuine non-blocking note. It must not include blockers, material verification gaps, required correction language, or wording that notes must be fixed before merge.

`NOT MERGE READY` requires the verdict heading, reviewed target block, concise summary, `### Blocking findings`, validation and review state, `### Focused correction direction`, and Standard Review scope boundary. Focused correction must address only verified current blockers, remain scoped to the current PR, identify the smallest coherent correction, name affected files or criteria when supported, include validation or re-check expectations when practical, and avoid unrelated cleanup, next-task work, and implementation claims. It must include `### Material verification gaps` when material gaps also exist. It must not include speculative blockers, unsupported failure claims, unrelated next-task prompts, implementation claims, merge execution, or claims that uninspected criteria passed.

`UNABLE TO VERIFY` requires the verdict heading, reviewed target block, concise limitation-led summary, `### Material verification gaps`, known `### Validation and review state`, `### Coverage and access limitations`, `### Escalation` when material, `### Re-verification requirement`, and Standard Review scope boundary. When current PR or change-state integrity cannot be established, the reviewed target block must name the unresolved target-state property. It must not include merge approval language, blocker claims without verified failure evidence, hidden target ambiguity, claims unavailable evidence is satisfied, or indefinite polling.

## Verdict-specific obligations

`MERGE READY` requires no blockers, no material gaps, no genuine notes, and complete material coverage. `MERGE READY WITH NON-BLOCKING NOTES` requires no blockers or material gaps and at least one genuine optional note; each note must explain why it is safe to defer. `NOT MERGE READY` requires at least one verified current blocker; unrelated inaccessible evidence remains disclosed as a limitation or material verification gap, not a reason to downgrade. `UNABLE TO VERIFY` applies when current PR or change-state integrity cannot be established, or when target-state integrity is established, no verified current blocker exists, and at least one material verification gap remains after bounded recovery. It preserves the smallest re-verification requirement, does not phrase unknowns as confirmed blockers, does not promise indefinite polling, and does not approve merge.

## Concise and expanded modes

Use concise mode when findings are few and evidence is straightforward. Concise mode still preserves all mandatory sections, blockers, gaps, and evidence references, and omits empty optional sections.

Use expanded mode for multiple findings or gaps, evidence conflicts, head changes, same-PR re-review, material API, compatibility, escalation reasoning, or requested detail. Expanded mode preserves canonical order and fact/inference/unknown separation while avoiding duplicated evidence.

## Same-PR re-review presentation

For same-PR re-review, include review mode and current head in the target block, label the previous verdict historical, summarize prior blockers as resolved, unresolved, or unverified, include only current findings in verdict sections, identify newly introduced material findings, avoid copying any prior finding without re-verification, and provide one recomputed current verdict. `### Re-review delta` remains optional when materially useful.

## Scope note

End every verdict output with wording equivalent to: Standard Review evaluates normal engineering merge readiness for this PR. It is not a complete security, privacy, architecture, dependency, release, or deployment audit.

## Presentation prohibitions

Do not invent connector-specific citation syntax, expose raw tool arguments or connector IDs, require a coding agent or branch workflow, fabricate evidence, provide scores, use confidence percentages, count findings into verdicts, or treat passing CI as a replacement for code review.
