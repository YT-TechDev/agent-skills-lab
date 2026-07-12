# GitHub Standard Engineering Review — Package Structure

## 1. Status and boundary

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: package-structure definition
- production package: not implemented
- package installation: not validated
- supporting-file access: not established for this production package
- production readiness: not established

This document defines the proposed future package root and tree, `SKILL.md` entry-point responsibilities, supporting-file responsibilities and boundaries, mapping from repository specifications to package files, source-of-truth and synchronization rules, repository-specific Project-context boundaries, package validation expectations, loading-independent failure behavior, packaging prerequisites, and change control.

This document does not create the package, define final `SKILL.md` prose or frontmatter, validate installation, invocation, or supporting-file retrieval, reveal internal loading behavior, implement connectors, scripts, or automation, declare production readiness, or define the Deep Review package.

## 2. Design principles

- Use one package for one clear job: normal one-PR GitHub Standard Review.
- Use one top-level `SKILL.md` as the explicit package entry point.
- Use one `reference/` directory for supporting files.
- Keep supporting files minimal, cohesive, and bounded by responsibility.
- Do not create nested packages or nested `SKILL.md` files.
- Do not embed repository-specific rules in reusable package files.
- Exact verdict names, evidence statuses, and decision precedence cannot drift from the reviewed specifications.
- `SKILL.md` remains the explicit entry point; supporting files refine it and do not silently replace it.
- The package structure assumes no eager, lazy, automatic, or selective supporting-file loading behavior.
- A standalone `SKILL.md` cannot silently substitute for the exact multi-file package.
- Package acceptance and supporting-file access are evaluated separately.
- The internal loading mechanism remains `UNKNOWN` unless separately observed and reproduced.
- Avoid one huge monolithic prompt.
- Avoid fragmentation into one file per minor rule.

## 3. Proposed future package tree

The proposed future package tree is:

```text
skills/github-standard-engineering-review/
├── SKILL.md
└── reference/
    ├── scope-and-trigger.md
    ├── inputs-and-tools.md
    ├── evidence-and-decisions.md
    ├── workflow-and-failure.md
    ├── verdict-and-output.md
    └── examples-and-evaluation.md
```

These names are proposed stable package paths. The tree is an implementation target, not an existing artifact. Scripts, schemas, binaries, archives, nested packages, or unrelated assets require a separately justified Issue. No extra root README, changelog, or manifest should be added unless later justified by verified platform or release requirements. Final frontmatter fields and package metadata remain deferred.

## 4. `SKILL.md` responsibilities

`SKILL.md` is the package entry point. It must eventually contain enough directly visible instruction to:

- identify the Skill and its one-PR Standard Review job;
- distinguish trigger, clarification, redirect, and non-trigger cases;
- enforce read-only GitHub behavior;
- identify required target inputs;
- establish the repository, PR, and current-head workflow;
- list the exact four verdict names: `MERGE READY`, `MERGE READY WITH NON-BLOCKING NOTES`, `NOT MERGE READY`, and `UNABLE TO VERIFY`;
- preserve blocker-versus-material-gap precedence;
- summarize ordered review phases;
- summarize bounded stopping and unstable-head behavior;
- summarize canonical output order and correction/re-verification behavior;
- identify each supporting file and when it is needed;
- fail safely when a required supporting file cannot be accessed; and
- record version and status when implemented.

`SKILL.md` must not:

- contain every detailed rubric and golden case;
- embed repository-specific policy;
- duplicate supporting-file detail word-for-word;
- claim supporting files were loaded without evidence;
- claim installation or production readiness; or
- silently continue a material review when required package guidance is inaccessible.

Loading-independent fallback rules:

- make one bounded access attempt for materially required guidance;
- stop or emit the appropriate evidence limitation if access remains unavailable;
- never invent missing package policy;
- never silently act as a standalone replacement package; and
- allow clarification, redirect, or decline responses to use entry-point rules directly present in `SKILL.md`.

## 5. Supporting-file responsibilities

### `reference/scope-and-trigger.md`

Contains job and scope boundary, Standard Review versus Deep Review boundary, trigger, clarification, non-trigger, redirect, decline, cancellation, target-replacement behavior, and Project-context boundary.

Does not contain detailed tool mechanics, evidence hierarchy, or verdict rendering examples.

### `reference/inputs-and-tools.md`

Contains required and optional inputs, prohibited sensitive inputs, target identity, repository-derived evidence inputs, read-only GitHub capability policy, tool selection, fallback, capability limitations, and connector-independent semantics.

Does not contain verdict precedence, detailed finding classification, or final output structure.

### `reference/evidence-and-decisions.md`

Contains evidence authority, provenance, freshness, current-head association, exact evidence statuses, requirement applicability, blocker, gap, note, satisfied, and `NOT APPLICABLE` classification, exact decision precedence, and unsupported-claim constraints.

Does not contain ordered tool workflow, complete output skeletons, or packaging runtime behavior.

### `reference/workflow-and-failure.md`

Contains ordered review workflow, target-state establishment and refresh, evidence collection phases, bounded retries and fallback, stopping conditions, unstable-head behavior, same-PR re-review, graceful failure, and re-verification conditions.

Does not create new decision semantics, verdict names, or detailed outputs.

### `reference/verdict-and-output.md`

Contains exact verdict contract, eligibility and prohibited claims, canonical output order, exact headings, verdict-specific required and omitted sections, evidence reference placement, focused correction direction, re-verification requirement, concise and expanded mode, and same-PR presentation.

Does not contain coding-agent-specific prompts, repository-specific PR workflow, or Deep Review output.

### `reference/examples-and-evaluation.md`

Contains compact representative examples, normative golden-case references or distilled cases, traceability expectations, evaluation layers and statuses, human procedure, regression summary, and promotion-gate summary.

Does not contain executable tests, connector mocks, a scoring engine, undated platform observations, or full duplicated repository docs.

## 6. Specification-to-package mapping

| Specification area | Authoritative repository document | Primary package destination | Required `SKILL.md` summary | Packaging notes |
| --- | --- | --- | --- | --- |
| job and scope | `docs/github-standard-engineering-review-scope.md` | `reference/scope-and-trigger.md` | One-PR job, Standard Review boundary, Deep Review separation, reviewer-not-implementer boundary | Keep repository-specific context out of package defaults. |
| trigger policy | `docs/github-standard-engineering-review-trigger-policy.md` | `reference/scope-and-trigger.md` | Trigger, clarify, non-trigger, redirect, decline, cancellation, and target-replacement summary | Must not create silent activation outside the one-PR job. |
| input contract | `docs/github-standard-engineering-review-input-contract.md` | `reference/inputs-and-tools.md` | Required target inputs, optional context, prohibited sensitive inputs | Conversation context may supplement but not override authoritative repository evidence. |
| tool policy | `docs/github-standard-engineering-review-tool-policy.md` | `reference/inputs-and-tools.md` | Read-only GitHub behavior, fallback, and capability limits | No write-capable connector behavior in Standard Review. |
| evidence policy | `docs/github-standard-engineering-review-evidence-policy.md` | `reference/evidence-and-decisions.md` | Evidence authority, freshness, current-head association, exact evidence statuses, and unsupported-claim rule | Exact tokens must remain synchronized with the specification. |
| decision rules | `docs/github-standard-engineering-review-decision-rules.md` | `reference/evidence-and-decisions.md` | Four verdict names, blocker/material-gap/note precedence, and positive-verdict constraints | Do not duplicate competing decision tables elsewhere. |
| workflow | `docs/github-standard-engineering-review-workflow.md` | `reference/workflow-and-failure.md` | Ordered review phases and evidence refresh before verdict | Workflow does not change verdict semantics. |
| stopping and failure | `docs/github-standard-engineering-review-stopping-and-failure-policy.md` | `reference/workflow-and-failure.md` | Bounded retries, terminal evidence failure, unstable head, material versus immaterial failure | Loading-independent package failure is surfaced rather than hidden. |
| verdict contract | `docs/github-standard-engineering-review-verdict-contract.md` | `reference/verdict-and-output.md` | Exact verdict eligibility, prohibited claims, and re-review disclosures | Verdict labels cannot drift. |
| output format | `docs/github-standard-engineering-review-output-format.md` | `reference/verdict-and-output.md` | Canonical output order, headings, evidence placement, correction and re-verification direction | Output examples cannot redefine policy. |
| examples and golden cases | `docs/github-standard-engineering-review-examples-and-golden-cases.md` | `reference/examples-and-evaluation.md` | Representative case coverage and traceability purpose | Keep examples compact; avoid duplicating every repository doc. |
| evaluation plan | `docs/github-standard-engineering-review-evaluation-plan.md` | `reference/examples-and-evaluation.md` | Evaluation layers, statuses, regression summary, and promotion-gate reminder | Evaluation may test policy but cannot introduce new verdict semantics. |

A repository document may contribute a short entry-point summary plus one primary supporting file. It must not create competing canonical copies of the same detailed rule.

## 7. Source-of-truth policy

Before package implementation, `docs/` is authoritative. After a package draft exists, reviewed specifications remain the normative design source and the package is an implementation artifact. Conflicts make the package non-conforming; the package does not override the docs.

Specification changes occur in docs first or in the same coherent PR with explicit traceability. Package changes identify the source specification and reviewed commit used for derivation. Observed product behavior does not silently rewrite normative rules. Platform constraints are recorded separately with date and status. Repository-specific Project instructions remain outside reusable specs and package files.

## 8. Duplication and drift controls

- Each detailed rule has one primary package file.
- `SKILL.md` contains operational summaries and navigation.
- Cross-file repetition is limited to non-negotiable invariants.
- Allowed repeated invariants are: one PR, read-only behavior, four verdicts, blocker precedence, Deep Review separation, current-head association, and no unsupported claims.
- Repeated invariants remain semantically identical everywhere they appear.
- Exact verdict and evidence tokens are checked against the specifications.
- References use relative package paths.
- No circular dependency is needed to understand the entry point.
- Golden cases cannot redefine policy.
- Evaluation cannot introduce new verdict semantics.

## 9. Project and conversation boundary

- Project context: repository-specific requirements, branch and merge workflow, required checks, approvals, and owner preferences.
- Skill package: reusable procedure.
- Current conversation: immediate target, temporary constraints, and optional user evidence.

Project instructions may constrain a current review but are evidence inputs, not package defaults. The package must not copy this repository's `AGENTS.md`, milestones, issue numbers, branches, or owner workflow. Conversation context cannot override repository-owned requirements without authority.

## 10. Supporting-file loading uncertainty

- Package acceptance and supporting-file accessibility are different claims.
- One successful access is `Observed`, not automatically `Reproduced`.
- Content use does not reveal eager, lazy, or internal loading.
- The internal loading mechanism remains `UNKNOWN`.
- The structure must not assume loading order.
- Missing file access is surfaced, not hidden.
- Exact-package tests cannot omit a supporting file.
- Standalone `SKILL.md` cannot silently substitute for a multi-file package.
- Future tests record exact tree, date, product surface, acceptance, invocation, and supporting-file evidence separately.
- Do not claim current ChatGPT behavior guarantees access.

## 11. Package validation expectations

Future static checks should verify:

- exact expected tree;
- one root `SKILL.md`;
- no nested `SKILL.md`;
- all required supporting files present;
- no binaries, archives, screenshots, secrets, credentials, private URLs, or AI sharing URLs;
- UTF-8 and text hygiene;
- relative references resolve;
- frontmatter validation only after a verified schema exists;
- exact verdict and evidence tokens match specs;
- no repository-specific identifiers;
- no prohibited write actions;
- no Deep Review completion claims;
- no unresolved placeholders in a promoted package;
- package docs pass repository validation; and
- static shape does not prove runtime behavior.

These checks are expectations only and are not implemented by this document.

## 12. Packaging prerequisites

### Before initial package implementation

Before creating the first package draft:

- complete the specification conformance review;
- execute the required pre-package cases or explicitly justify any case that cannot yet be executed;
- have no unresolved critical `FAIL` in trigger precision, verdict selection, blocker detection, false-blocker avoidance, unsupported claims, scope boundary, or output-contract compliance;
- document every material `PARTIAL` or `INCONCLUSIVE` result and its next experiment;
- record dated observations where product behavior matters;
- document connector limitations separately from Skill logic; and
- record the initial regression baseline.

These prerequisites do not require exact-package acceptance or supporting-file-access testing before the package draft exists.

### After the package draft exists, before promotion or readiness

Before promoting the package or declaring readiness:

- test exact package acceptance;
- test supporting-file access as a separate claim;
- run the full minimum promotion suite defined by the evaluation plan against the exact package;
- record package-specific failures, limitations, and unknowns;
- confirm that static package validation is not treated as runtime evidence; and
- confirm that documentation alone is not treated as production-readiness evidence.

This Issue does not declare either stage satisfied.

## 13. Version and change control

Version and status live in `SKILL.md` or verified package metadata. The initial version is assigned only when implementation begins. Behavior changes require specification and evaluation traceability. Editorial changes are distinguished from behavior changes. Supporting-file changes participate in package versioning. Tree changes require explicit review. Final version and readiness remain scope item 13. This document does not publish, tag, or release anything.

## 14. Implementation sequence

1. Satisfy or explicitly resolve the pre-implementation prerequisites.
2. Implement the exact proposed tree in a separate Issue and PR.
3. Derive package content from reviewed specifications.
4. Run static package validation.
5. Test exact package acceptance.
6. Test supporting-file access separately.
7. Run a selected golden-case subset only as an early smoke test.
8. Record and correct package-specific failures and unknowns.
9. Run the full minimum promotion suite required by the evaluation plan.
10. Record dated observations and regression results.
11. Decide version and production readiness in a separate Issue.

The selected subset in step 7 does not replace the full minimum suite in step 9. This sequence is a plan only.

## 15. Anti-patterns

Prohibited anti-patterns include:

- creating the package in this Issue;
- one enormous `SKILL.md`;
- one supporting file per minor rule;
- conflicting duplicate decision tables;
- repository-specific package instructions;
- hidden dependency on supporting-file access;
- silent standalone fallback;
- assumptions about internal loading;
- treating package acceptance as behavioral validation;
- treating file access as installation success;
- selecting a final version before evaluation;
- unjustified frameworks or scripts;
- merging Deep Review into Standard Review; and
- private content or AI sharing URLs.

## 16. Quality checklist

This package-structure specification confirms:

- the exact tree is shown;
- each file has one clear responsibility;
- all completed specs are mapped;
- entry-point fallback is safe;
- source-of-truth policy is explicit;
- Project and context boundary is explicit;
- no loading-mechanism claim is made;
- acceptance and file access are separate;
- validation expectations are static only;
- promotion prerequisites are not declared satisfied;
- version and readiness are deferred; and
- no package files are created.

## 17. Deferred work

Deferred work remains:

- actual package implementation;
- final `SKILL.md` content;
- verified frontmatter schema;
- package installation;
- exact runtime tests;
- production-package supporting-file observations;
- automated packaging;
- publication;
- final version and readiness status; and
- Deep Review package.
