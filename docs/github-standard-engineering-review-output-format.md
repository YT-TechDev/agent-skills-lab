# GitHub Standard Engineering Review — Output Format

## 1. Status and boundary

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: user-facing output format definition
- production package: not implemented
- production readiness: not established

This document defines the future Standard Review user-facing response contract for response order, target and current-head presentation, verdict-specific sections, evidence references, validation and review state, coverage limitations, escalation, correction or re-verification direction, concise and expanded modes, same-PR re-review presentation, and placeholder skeletons.

This document does not implement a Skill, connector-specific renderer, automatic citation generation, decision engine, merge action, implementation action, release action, installation behavior, or Deep Review output. Standard Review reviews one current GitHub PR, remains read-only, and remains separate from Deep Review. Exact verdict names, verdict precedence, evidence statuses, materiality rules, verdict eligibility, prohibited claims, and the logical verdict package already exist in the surrounding specifications and are reused unchanged. Final production packaging remains deferred, and no production Skill package exists.

## 2. Output principles

- The exact verdict is the first substantive content.
- One response contains exactly one Standard Review verdict.
- Repository, PR, refs, and reviewed head identity appear near the top.
- Decisive findings appear before supporting detail.
- Every blocker and material verification gap is evidence-traceable.
- Positive verdicts disclose material validation and coverage state.
- The output never implies that inaccessible or uninspected areas passed.
- Verified fact, reasonable inference, and unknown remain distinguishable.
- No score, grade, confidence percentage, severity total, or finding-count logic determines presentation or verdict.
- Avoid generic praise, marketing prose, and repeated evidence.
- The response remains useful without hidden reasoning.
- The Standard Review scope limitation is concise and explicit.
- Evidence-reference obligations are connector-independent even when citation syntax varies.

## 3. Canonical top-level order

Use this top-level order:

1. verdict heading;
2. reviewed target block;
3. concise review summary;
4. decisive findings section when required;
5. validation, CI, and review state;
6. coverage and access limitations when present;
7. escalation when material or worth surfacing;
8. correction or re-verification direction when required; and
9. concise Standard Review scope note.

The verdict heading is:

```markdown
## Verdict: <EXACT VERDICT>
```

`<EXACT VERDICT>` must be exactly one of:

- `MERGE READY`
- `MERGE READY WITH NON-BLOCKING NOTES`
- `NOT MERGE READY`
- `UNABLE TO VERIFY`

Do not add emoji, aliases, grades, traffic-light labels, confidence percentages, or a second verdict label.

## 4. Reviewed target block

Immediately after the verdict heading, present a compact reviewed target block containing:

- repository: `owner/name`;
- PR number and title when available;
- base ref;
- head ref;
- reviewed head SHA or equivalent current change identity when established; and
- review mode: `initial` or `same-PR re-review`.

For `UNABLE TO VERIFY` when head or change-state identity is not established:

- repository and PR must still be established;
- head or change state is shown as `UNKNOWN` or an equivalent explicit unresolved state; and
- the exact unresolved target-state property is named.

Do not expose connector IDs, API endpoints, raw tool arguments, credentials, authentication data, or hidden metadata.

## 5. Concise review summary

Use one short paragraph or at most three compact bullets. The summary must:

- explain why the verdict was selected;
- identify the decisive evidence category;
- avoid repeating all findings; and
- remain within Standard Review scope.

Positive verdicts summarize sufficient material coverage and state that no blocker or material verification gap was found within Standard Review scope. `NOT MERGE READY` is blocker-led. `UNABLE TO VERIFY` leads with the exact material limitation or target-state failure. Counts may aid navigation, but they never determine the verdict.

## 6. Findings sections and exact headings

Use only these finding headings:

- `### Blocking findings`
- `### Material verification gaps`
- `### Non-blocking notes`

Rules:

- `### Blocking findings` appears only with verified current blockers.
- `### Material verification gaps` appears whenever material gaps must be disclosed, including under `NOT MERGE READY`.
- `### Non-blocking notes` appears only with genuine non-blocking notes.
- Do not render empty headings.
- Blockers are not notes.
- Inability to verify is not a blocker.
- Satisfied and `NOT APPLICABLE` criteria are not findings by default.

Each finding contains, in compact form:

1. short title;
2. criterion or governing requirement;
3. current evidence and source reference;
4. target, ref, or head association when relevant;
5. merge-readiness effect; and
6. correction or re-verification direction when applicable.

Use prose or compact bullets. Do not define or require a machine-readable schema.

## 7. Evidence-reference presentation

Evidence references must be adjacent to supported claims and connector-independent. Require:

- at least one direct evidence reference per blocker;
- the exact inaccessible source or coverage area per material gap;
- current evidence references for important positive-readiness claims;
- current-head association for CI, review, and thread claims when available;
- user-provided evidence labeled as user-provided;
- inference labeled as inference and supported by evidence; and
- previous-head evidence labeled historical.

Allowed source locators include platform-native citations, repository path and line locators, PR, Issue, check, workflow, job, review, thread, or artifact identifiers, and equivalent source locators. This specification does not mandate one citation syntax.

Prohibit:

- raw hidden tool IDs;
- unsupported claims such as “all checks passed”;
- irrelevant citations;
- unexplained citation dumps; and
- citation-only paragraphs with no explained conclusion.

## 8. Validation and review state

Use the exact heading:

```markdown
### Validation and review state
```

Present material applicable state for:

- local or user-reported validation, clearly labeled;
- current remote CI/check status;
- required versus optional interpretation;
- review or approval state;
- unresolved material thread state;
- relevant PR discussion state; and
- head association.

Distinguish check existence, execution, status, scope or coverage, and inspected logs or artifacts. Passing CI does not replace code review. Omit non-applicable categories, or use `NOT APPLICABLE` only with supported scope reasoning and evidence.

## 9. Coverage and access limitations

Use the exact heading:

```markdown
### Coverage and access limitations
```

Render this section only when relevant. Include:

- exact inaccessible or partial area;
- evidence status when useful;
- materiality;
- verdict effect; and
- retry or fallback exhaustion when relevant.

Use exact file, job, thread, artifact, or target-state identifiers when known. Blockers do not suppress unrelated limitations. Immaterial limitations may be disclosed without changing a positive verdict.

## 10. Escalation

Use the exact heading:

```markdown
### Escalation
```

Render this section only when required Deep Review or specialist approval affects the verdict, or when an optional Deep Review recommendation is a genuine note worth surfacing. State the reason, evidence status, and verdict effect. Never claim Deep Review completion, and do not perform Deep Review.

## 11. `MERGE READY`

Required:

- verdict heading;
- reviewed target block;
- concise summary;
- `### Validation and review state`;
- disclosure-worthy immaterial limitations when present; and
- scope note.

Forbidden:

- `### Blocking findings`;
- `### Material verification gaps`;
- `### Non-blocking notes`;
- correction direction;
- meaningful unresolved optional escalation recommendation;
- required pre-merge work; and
- perfection, Deep Review, release, deployment, or risk-free assurance.

State that no blocker or material verification gap was found within Standard Review scope.

## 12. `MERGE READY WITH NON-BLOCKING NOTES`

Required:

- verdict heading;
- reviewed target block;
- positive summary;
- `### Non-blocking notes`;
- `### Validation and review state`;
- relevant limitations;
- `### Escalation` when an optional recommendation is surfaced; and
- scope note.

Each note explains why it is safe to defer. Do not imply a note must be fixed before merge.

## 13. `NOT MERGE READY`

Required:

- verdict heading;
- reviewed target block;
- blocker-led summary;
- `### Blocking findings`;
- `### Validation and review state`;
- `### Material verification gaps` when present;
- `### Coverage and access limitations` when present;
- `### Escalation` when material;
- focused correction direction; and
- scope note.

Use the exact heading:

```markdown
### Focused correction direction
```

Focused correction direction must:

- address only verified current blockers;
- remain scoped to the current PR;
- identify the smallest coherent correction;
- name affected files or criteria when supported;
- include validation or re-check expectations when practical;
- avoid unrelated cleanup or next-task work; and
- avoid claiming implementation.

A code-fenced implementation prompt may be included when the surrounding workflow requests one, but the reusable Skill must not require a specific coding agent, branch, command set, or repository workflow. Do not provide a next-task prompt while blockers remain.

## 14. `UNABLE TO VERIFY`

Required:

- verdict heading;
- reviewed target block;
- limitation-led summary;
- `### Material verification gaps`;
- known `### Validation and review state`;
- `### Coverage and access limitations`;
- `### Escalation` when material;
- re-verification direction; and
- scope note.

Use the exact heading:

```markdown
### Re-verification requirement
```

Identify the smallest evidence, access, target-state, or repository-state change needed for another review when known. Do not phrase unknowns as confirmed blockers, promise indefinite polling, or approve merge.

## 15. Scope note

End every verdict with concise wording equivalent to:

> Standard Review evaluates normal engineering merge readiness for this PR. It is not a complete security, privacy, architecture, dependency, release, or deployment audit.

The wording may be shorter, but it must preserve that boundary.

## 16. Concise and expanded modes

### Concise mode

Use concise mode when findings are few, evidence is straightforward, a quick verdict is requested, and no nuance is lost. All mandatory sections remain. Validation and review state may be compressed. Empty optional sections are omitted. All blockers, material gaps, and required evidence references remain.

### Expanded mode

Use expanded mode when there are multiple blockers or gaps, evidence conflicts, head changes or re-review history, material API, compatibility, or escalation reasoning, or the user requests detail. Keep canonical order, avoid evidence duplication, and preserve fact, inference, and unknown separation. Do not define numeric word limits.

## 17. Same-PR re-review

A same-PR re-review requires:

- re-review mode and current head in the target block;
- previous verdict labeled historical;
- prior blockers summarized as resolved, unresolved, or unverified;
- only current findings in verdict sections;
- newly introduced material findings identified;
- no copied prior finding without re-verification; and
- one recomputed current verdict.

Optional heading when materially useful:

```markdown
### Re-review delta
```

`### Re-review delta` does not replace full current-scope evaluation.

## 18. Evidence-status presentation

- Use `UNKNOWN` only when material or interpretation-relevant.
- Use `PARTIAL` for incomplete but meaningful coverage.
- Use `MISSING` only for confirmed absence.
- Use `NOT APPLICABLE` only with supported scope reasoning.
- Inline labels or compact bullets are allowed.
- Do not render a large status ledger by default.

## 19. Anti-patterns

Prohibit:

- verdict buried after analysis;
- multiple verdicts;
- verdict aliases;
- unsupported “looks good” language;
- blockers without evidence;
- citation dumps;
- empty headings;
- repeated PR description;
- every inspected file listed as a finding;
- unbounded checklists;
- scores or confidence percentages;
- severity labels that alter verdict semantics;
- material gaps hidden in footnotes;
- correction mixed with next-Issue planning;
- claims of merge execution, release readiness, deployment assurance, or Deep Review completion.

## 20. Placeholder-only output skeletons

These skeletons are placeholders, not golden tests.

### `MERGE READY` skeleton

```markdown
## Verdict: MERGE READY

- Repository: <owner/repository>
- PR: <#PR> <title>
- Base ref: <base ref>
- Head ref: <head ref>
- Reviewed head: <head SHA>
- Review mode: <initial>

<Concise summary stating no blocker or material verification gap was found within Standard Review scope, supported by <evidence reference>.>

### Validation and review state

- Validation: <current validation state and head association> — <evidence reference>
- CI/checks: <current required/optional status and scope> — <evidence reference>
- Reviews/threads: <current review and thread state> — <evidence reference>

<Standard Review scope note.>
```

### `MERGE READY WITH NON-BLOCKING NOTES` skeleton

```markdown
## Verdict: MERGE READY WITH NON-BLOCKING NOTES

- Repository: <owner/repository>
- PR: <#PR> <title>
- Base ref: <base ref>
- Head ref: <head ref>
- Reviewed head: <head SHA>
- Review mode: <initial>

<Positive summary stating no blocker or material verification gap was found and that notes are safe to defer, supported by <evidence reference>.>

### Non-blocking notes

- <Note title>: <criterion/context>; <current evidence and source reference>; <why safe to defer>.

### Validation and review state

- Validation: <current validation state and head association> — <evidence reference>
- CI/checks: <current required/optional status and scope> — <evidence reference>
- Reviews/threads: <current review and thread state> — <evidence reference>

<Standard Review scope note.>
```

### `NOT MERGE READY` skeleton

```markdown
## Verdict: NOT MERGE READY

- Repository: <owner/repository>
- PR: <#PR> <title>
- Base ref: <base ref>
- Head ref: <head ref>
- Reviewed head: <head SHA>
- Review mode: <initial or same-PR re-review>

<Blocker-led summary identifying the decisive current blocker evidence category.>

### Blocking findings

- <Blocking title>: <criterion/governing requirement>; current evidence: <evidence reference>; head/ref: <head SHA>; merge-readiness effect: <why this blocks merge>; correction direction: <smallest scoped correction>.

### Validation and review state

- Validation: <known validation state> — <evidence reference>
- CI/checks: <current required/optional status and scope> — <evidence reference>
- Reviews/threads: <current review and thread state> — <evidence reference>

### Focused correction direction

<Smallest coherent correction for verified current blockers only, plus practical validation or re-check expectations.>

<Standard Review scope note.>
```

### `UNABLE TO VERIFY` skeleton

```markdown
## Verdict: UNABLE TO VERIFY

- Repository: <owner/repository>
- PR: <#PR> <title>
- Base ref: <base ref>
- Head ref: <head ref or UNKNOWN>
- Reviewed head: <head SHA or UNKNOWN>
- Review mode: <initial or same-PR re-review>
- Unresolved target-state property: <property name>

<Limitation-led summary identifying the material target-state or evidence limitation.>

### Material verification gaps

- <Gap title>: <criterion/target-state property>; inaccessible or unresolved evidence: <evidence reference or exact missing area>; status: <UNKNOWN/PARTIAL/MISSING>; verdict effect: <why positive readiness cannot be verified>; re-verification need: <smallest needed state change>.

### Validation and review state

- Validation: <known validation state, if any> — <evidence reference>
- CI/checks: <known current state or UNKNOWN with reason> — <evidence reference or exact inaccessible source>

### Coverage and access limitations

- <Exact inaccessible area>: <materiality and retry/fallback state>.

### Re-verification requirement

<Smallest evidence, access, target-state, or repository-state change needed to retry the review when known.>

<Standard Review scope note.>
```

## 21. Quality checks

Before responding, verify:

- exactly one verdict is present;
- target and current-head state are correct;
- finding type matches verdict;
- every blocker and material gap has evidence;
- a positive verdict has sufficient material coverage;
- CI and review claims are current and head-associated when available;
- limitations are disclosed;
- no unsupported or Deep Review completion claims are made;
- no empty sections are rendered;
- no unrelated next task appears under blockers;
- correction or re-verification direction is present when required;
- the scope note is present; and
- the response is concise enough for maintainers.

## 22. Deferred areas

Deferred work remains:

- realistic golden cases and expected-verdict fixtures;
- evaluation implementation;
- production package structure;
- final `SKILL.md` and frontmatter;
- installation behavior;
- connector-specific rendering implementation; and
- Deep Review output format.
