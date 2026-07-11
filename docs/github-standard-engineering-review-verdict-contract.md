# GitHub Standard Engineering Review — Verdict Contract

## 1. Status and contract boundary

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: exact verdict contract definition
- production package: not implemented
- production readiness: not established

This document defines the semantic contract for the exact verdict emitted by the future reusable Standard Review Skill. It defines:

- exact verdict semantics;
- eligibility conditions;
- required logical claims and disclosures;
- prohibited claims;
- blocker, material verification gap, and non-blocking note consistency;
- coverage and current-state disclosure obligations;
- same-PR re-review verdict behavior; and
- correction or re-verification direction at a logical level.

This document does not define:

- final section headings;
- final ordering;
- final response formatting;
- citation rendering syntax;
- prose style or response length;
- a correction-prompt template;
- connector behavior;
- automatic verdict generation; or
- production installation behavior.

Standard Review handles one current GitHub pull request, remains read-only, and remains separate from Deep Review. Existing evidence statuses, blocker meanings, verification-gap meanings, non-blocking-note meanings, exact verdict names, selection precedence, ten-phase workflow, and bounded stopping and failure behavior are reused unchanged. Final output format remains deferred, and no production Skill package exists.

## 2. Universal verdict contract

Whenever a Standard Review merge-readiness verdict is emitted, the logical verdict package must include exactly one of the established verdict names:

- `MERGE READY`
- `MERGE READY WITH NON-BLOCKING NOTES`
- `NOT MERGE READY`
- `UNABLE TO VERIFY`

Every emitted verdict requires:

- one repository and one PR target;
- the reviewed current head SHA or equivalent change identity;
- target-state integrity state;
- current evidence association;
- evidence provenance and status for material conclusions;
- material validation, CI, review, and discussion state;
- material coverage and access limitations;
- required escalation state;
- separation of verified fact, reasonable inference, and unknown;
- the Standard Review scope limitation; and
- no write action.

Every emitted verdict prohibits:

- numeric scoring or confidence percentages;
- extra verdict aliases;
- unsupported readiness claims;
- claims of perfect, risk-free, repository-wide, deeply audited, release-certified, deployed, or guaranteed-safe status;
- claims that Deep Review was completed;
- claims about uninspected areas; and
- merge execution, implementation, release, or deployment actions.

No Standard Review merge-readiness verdict is emitted for:

- non-trigger requests;
- unresolved target ambiguity before target-state establishment;
- decline or redirect endings;
- user cancellation; or
- target replacement before the current review unit completes.

## 3. Verdict-selection integrity

The existing selection precedence is reused unchanged:

1. target-state integrity not established → `UNABLE TO VERIFY`
2. verified current blocker exists → `NOT MERGE READY`
3. no blocker, but unresolved material verification gap exists → `UNABLE TO VERIFY`
4. no blocker or material gap, with genuine non-blocking notes → `MERGE READY WITH NON-BLOCKING NOTES`
5. no blocker, material gap, or qualification → `MERGE READY`

This contract validates the selected verdict. It does not create a second decision algorithm. One review emits one verdict. Blocker, gap, and note classification remains evidence-relative and requirement-relative.

## 4. `MERGE READY` contract

Eligibility requires all of the following:

- target-state integrity established;
- sufficient inspection of the complete relevant change scope;
- governing requirements known for material applicable criteria;
- all material criteria are `VERIFIED` satisfied or evidence-supported `NOT APPLICABLE`;
- no verified blocker;
- no unresolved material verification gap;
- no genuine merge-related qualification worth surfacing;
- required validation and CI state sufficient;
- required review, approval, and thread state sufficient; and
- required escalation or specialist-review state satisfied or `NOT APPLICABLE`.

Required logical content:

- repository and PR;
- reviewed head SHA or equivalent identity;
- concise evidence-grounded readiness rationale;
- statement that no blocker or material verification gap was found within Standard Review scope;
- material validation, CI, and review state;
- any immaterial limitation whose disclosure remains necessary; and
- Standard Review scope limitation.

Forbidden content:

- non-blocking notes presented as qualifications;
- hidden material caveats;
- unresolved optional escalation recommendation worth surfacing;
- language that optional future work is required before merge;
- claims of perfection, Deep Review, release certification, or guaranteed safety; and
- claims that uninspected areas are satisfactory.

A meaningful note or optional escalation recommendation requires `MERGE READY WITH NON-BLOCKING NOTES`.

## 5. `MERGE READY WITH NON-BLOCKING NOTES` contract

Eligibility requires:

- every positive-verdict minimum condition;
- no blocker;
- no material verification gap; and
- at least one genuine evidence-supported non-blocking note.

Each note must:

- be non-required by governing evidence;
- be safe to defer;
- have an evidence basis;
- explain practical relevance;
- not conceal correctness, validation, type-safety, error-handling, public API, compatibility, maintainability, review-state, or escalation risk; and
- not be called non-blocking merely because its fix is small.

Required logical content:

- repository and PR;
- reviewed head SHA or equivalent identity;
- positive readiness rationale;
- statement that no blocker or material verification gap was found;
- material validation, CI, and review state;
- each genuine non-blocking note;
- optional Deep Review recommendation when worth surfacing, without claiming it was completed; and
- Standard Review scope limitation.

Forbidden content:

- material unknowns;
- failed or pending required conditions;
- required correction language;
- disguised blockers; and
- wording that notes must be fixed before merge.

## 6. `NOT MERGE READY` contract

Eligibility requires:

- at least one verified current blocker; and
- blocker association with the reviewed current head or current repository state.

For every blocker, require:

- affected criterion or governing requirement;
- current evidence;
- target, ref, or SHA association when relevant;
- why the condition blocks merge readiness; and
- smallest focused correction direction when practical.

Required logical content:

- repository and PR;
- reviewed current head SHA or equivalent identity;
- one or more verified current blockers;
- material validation, CI, and review state relevant to blockers;
- unrelated material coverage limitations or verification gaps;
- required escalation state;
- focused correction direction for the current PR when practical; and
- Standard Review scope limitation.

A single blocker is sufficient for this verdict. Unrelated evidence failure does not erase a verified blocker, and unrelated gaps remain disclosed. A previous-head blocker cannot support the current verdict without re-verification. Fixing one blocker does not prove full readiness. `UNABLE TO VERIFY` is not emitted as a second verdict when a verified current blocker exists.

Forbidden content:

- speculative blockers;
- preference-based blockers;
- unsupported failure claims;
- unrelated next-task prompts;
- implementation or merge execution; and
- claims that uninspected criteria passed.

## 7. `UNABLE TO VERIFY` contract

Eligibility requires either:

- target-state integrity cannot be established; or
- no verified current blocker exists, but at least one unresolved material verification gap remains after bounded recovery.

For every material gap, require:

- affected criterion or target-state property;
- missing, inaccessible, partial, stale, contradictory, or unstable evidence;
- bounded retry, fallback, or clarification state when applicable;
- why the gap prevents a trustworthy readiness judgment; and
- smallest evidence or state change needed for re-evaluation when known.

Required logical content:

- repository or PR identity that could be established;
- target identity that could not be established, when applicable;
- current head identity when established;
- material verification gaps;
- logical recovery attempts or access limitations;
- known validation, CI, and review state;
- re-verification requirement when known; and
- Standard Review scope limitation.

`UNABLE TO VERIFY` is not a softer `NOT MERGE READY`. Inaccessible CI is not failed CI. Unavailable thread state is not resolved thread state. Tool failure alone does not prove `MISSING`. A verified current blocker changes the verdict to `NOT MERGE READY`, with the gap disclosed there.

Forbidden content:

- merge approval language;
- blocker claims without verified failure evidence;
- hidden target ambiguity;
- claims that unavailable evidence is satisfied; and
- indefinite polling or unbounded retry promises.

## 8. Finding and qualification consistency

- `MERGE READY` has no blocker, material gap, or meaningful qualification.
- `MERGE READY WITH NON-BLOCKING NOTES` has no blocker or material gap and has at least one genuine note.
- `NOT MERGE READY` has at least one verified current blocker.
- `UNABLE TO VERIFY` has target-integrity failure or a material gap and no verified current blocker.
- The same claim at the same evidence state cannot simultaneously be a blocker, material gap, and note.
- Satisfied or `NOT APPLICABLE` criteria are not unresolved findings.
- Immaterial unavailable evidence may be disclosed without promotion into a material gap.
- Every qualification must be compatible with the selected verdict.
- A small fix can still be blocking.
- A large optional improvement can still be non-blocking.

## 9. Coverage and disclosure contract

Positive verdicts require sufficient material coverage. Blockers do not permit silent omission of unrelated coverage limitations. Coverage disclosures identify the affected area without claiming satisfaction.

Material binary, oversized, truncated, inaccessible, conflicting, or incomplete evidence prevents positive verdicts unless a verified blocker already determines `NOT MERGE READY`. Immaterial limitations do not automatically downgrade a verdict. Scope wording never implies repository-wide or Deep Review assurance. Reviewed head association is explicit for SHA-specific findings.

## 10. Validation, CI, review, and thread contract

Verdict handling and disclosure follow the existing decision rules unchanged:

- failed required CI is a blocker;
- pending required CI is handled under existing blocker rules when completion is a confirmed merge requirement;
- skipped or cancelled required CI is a blocker when repository policy requires successful completion, and unclear required status or meaning is a material verification gap;
- inaccessible required CI state is a material verification gap;
- optional checks are evaluated against governing evidence and materiality, not automatically treated as blocking or ignorable;
- current required approval supports readiness only when current and applicable;
- absent required approval is a blocker;
- stale approval must not be assumed current after material branch changes;
- inaccessible required approval state is a material verification gap;
- unresolved material blocking thread is a blocker;
- unavailable required thread state is a material verification gap; and
- lack of comments is not approval.

Passing CI does not replace code review. Lack of comments is not approval. A local validation claim does not override contradictory current remote evidence. Current head association matters for CI and review evidence.

## 11. Escalation contract

Repository-required Deep Review or specialist approval confirmed absent is a blocker. Required escalation state that is inaccessible is a material verification gap. Optional Deep Review recommendation is a non-blocking note when worth surfacing.

Standard Review never claims Deep Review completion. `MERGE READY` does not carry a meaningful unresolved optional escalation qualification. Use `MERGE READY WITH NON-BLOCKING NOTES` when an optional escalation recommendation should be surfaced.

## 12. Correction and re-verification direction

`NOT MERGE READY` provides focused correction direction for verified blockers when practical. Correction direction stays scoped to the current PR. No unrelated next task is included. No implementation is claimed. When safe correction cannot be specified, explain the evidence limitation instead of inventing steps.

Positive verdicts do not require correction direction. `UNABLE TO VERIFY` identifies the smallest evidence or state change needed for re-evaluation when known. A re-verification requirement is not phrased as a confirmed blocker fix.

## 13. Same-PR re-review verdict contract

Same-PR re-review requires:

- same repository and PR reconfirmed;
- current head SHA and mutable state refreshed;
- previous verdict treated as historical context;
- previous blockers re-verified;
- blockers removed only when current evidence verifies resolution;
- new blockers, gaps, and notes incorporated;
- complete verdict recomputed from current evidence; and
- current reviewed head included in the logical verdict package.

A reported fix does not determine the new verdict. A new commit does not determine the new verdict. A passing check alone does not determine the new verdict. Prior approval alone does not determine the new verdict.

## 14. Logical verdict package

Later output-format work must have at least the following logical information available:

- exact verdict;
- repository and PR;
- reviewed head SHA or equivalent identity;
- target-state integrity state;
- concise verdict rationale;
- verified blockers;
- material verification gaps;
- genuine non-blocking notes;
- material validation, CI, and review state;
- coverage and access limitations;
- escalation state;
- correction direction or re-verification requirement when applicable; and
- Standard Review scope limitation.

This is not:

- a final schema;
- a heading set;
- an ordering rule;
- citation syntax;
- a response template; or
- a correction-prompt template.

## 15. Compact verdict-contract matrix

| Verdict | Eligibility | Required logical content | Forbidden content | Re-review implication |
| --- | --- | --- | --- | --- |
| `MERGE READY` | Target-state integrity established; sufficient material coverage; all material criteria `VERIFIED` satisfied or `NOT APPLICABLE`; no blocker, material gap, or meaningful qualification. | Repository, PR, reviewed head, evidence-grounded readiness rationale, no-blocker/no-gap statement, material validation/CI/review state, necessary immaterial limitations, Standard Review scope limitation. | Hidden material caveats, meaningful notes or optional escalation qualifications, required future work, perfection/Deep Review/release-safety claims, uninspected-area satisfaction claims. | Recompute from refreshed current evidence; prior readiness is historical only. |
| `MERGE READY WITH NON-BLOCKING NOTES` | Every positive-verdict minimum condition; no blocker; no material gap; at least one genuine evidence-supported non-blocking note. | Repository, PR, reviewed head, positive rationale, no-blocker/no-gap statement, material validation/CI/review state, each note, optional Deep Review recommendation when worth surfacing, scope limitation. | Material unknowns, failed or pending required conditions, required correction language, disguised blockers, wording that notes must be fixed before merge. | Reconfirm target and head, verify notes remain non-blocking, incorporate new blockers/gaps/notes, and recompute. |
| `NOT MERGE READY` | At least one verified current blocker associated with the reviewed head or current repository state. | Repository, PR, reviewed current head, verified blockers with evidence and blocking reason, blocker-relevant validation/CI/review state, unrelated limitations or gaps, escalation state, focused correction direction when practical, scope limitation. | Speculative or preference-based blockers, unsupported failure claims, unrelated next-task prompts, implementation/merge execution, claims uninspected criteria passed. | Previous blockers must be re-verified; resolved blockers are removed only with current evidence; one current blocker remains decisive. |
| `UNABLE TO VERIFY` | Target-state integrity cannot be established, or no verified current blocker exists and at least one material verification gap remains after bounded recovery. | Established repository/PR identity if any, target identity that could not be established when applicable, current head when established, material gaps, recovery/access state, known validation/CI/review state, re-verification need when known, scope limitation. | Merge approval language, blocker claims without verified failure evidence, hidden target ambiguity, claims unavailable evidence is satisfied, indefinite polling. | Refresh target/head and missing evidence; prior gaps remain historical until current evidence resolves or replaces them. |

## 16. Deferred specification

The following remain deferred:

- final output headings and order;
- final response formatting;
- citation rendering format;
- correction-prompt template;
- examples and golden cases beyond the compact matrix;
- evaluation implementation;
- production package structure;
- Skill frontmatter and final description;
- installation behavior; and
- Deep Review verdict contract.
