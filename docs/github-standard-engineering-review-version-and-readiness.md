# GitHub Standard Engineering Review — Version and Readiness

## Status and boundary

- canonical name: `github-standard-engineering-review`
- repository milestone: `v0.3.0`
- repository milestone meaning: specification-foundation planning milestone
- Skill package version: `UNASSIGNED`
- specification status: foundation specified through package structure
- production package: not implemented
- installation and invocation: not validated
- production readiness: `NOT ESTABLISHED`

This document defines milestone/package version boundaries, version assignment, version impact, current readiness, readiness progression, transition evidence, owner decision requirements, observation/reproduction rules, and completion of the current specification sequence.

This document does not create a package, select a version, validate runtime behavior, execute evaluations, publish, release, close the milestone, or declare readiness.

## Core distinctions

- Repository milestones organize repository work.
- Package versions identify actual packaged artifacts.
- Repository milestone `v0.3.0` must not be presented as the `github-standard-engineering-review` package version.
- Future package versions trace to exact package commits, source specification commits, and evaluation records.
- Documentation completion is not package implementation.
- Static validation is not runtime validation.
- Package acceptance is not supporting-file access.
- Supporting-file access does not reveal the internal loading mechanism.
- Test completion does not replace the final owner readiness decision.
- Milestones, Git tags, GitHub Releases, archives, publication, distribution, and package versions remain distinct unless a later owner decision explicitly connects them for a specific release action.

## Current readiness snapshot

| Dimension | Current state | Evidence basis | What remains |
| --- | --- | --- | --- |
| Specification coverage | Specification areas 1–12 are reviewed and linked; this document defines item 13. | `docs/github-standard-engineering-review-scope.md` links items 1–12 and identifies item 13 as version/readiness work before this change. | Merge this document and scope update to complete the documented foundation sequence. |
| Package-structure specification | Proposed future package tree is documented only. | `docs/github-standard-engineering-review-package-structure.md` defines the proposed tree and states it is an implementation target, not an existing artifact. | Separate package implementation planning and PR. |
| Package implementation | Not implemented. | Current tree has no `skills/github-standard-engineering-review/` directory. | Create the exact package tree in a separate authorized implementation PR. |
| `SKILL.md` | Not implemented for the production package. | Current tree has no production `skills/github-standard-engineering-review/SKILL.md`; existing `SKILL.md` files are experiment packages only. | Add one root production `SKILL.md` only in separate package work. |
| Supporting files | Not implemented for the production package. | Current tree has no production `reference/` files under `skills/github-standard-engineering-review/`. | Add the six expected supporting files only in separate package work. |
| Package version | `UNASSIGNED`. | No production package exists, and this document forbids assigning a version here. | Select a first package version in package implementation or later readiness work. |
| Static package validation | Not tested against an exact production package. | Repository validator can check package shape, but no production package exists. | Run static validation after the exact package tree exists. |
| Installation | Not validated. | No production package exists to install. | Test installation separately against the exact package. |
| Invocation | Not validated. | No production package exists to invoke. | Test invocation separately against the exact package and recorded product surface. |
| Exact package acceptance | Not tested. | No exact production package artifact exists. | Test package acceptance separately from supporting-file access. |
| Supporting-file accessibility | Not established for the production package. | Supporting-file spike observations concern an experimental package, not `github-standard-engineering-review`. | Evaluate supporting-file access against the exact production package as a separate claim. |
| Internal loading mechanism | `UNKNOWN`. | Existing spikes preserve internal loading mechanics as unknown, and this Issue adds no runtime observation. | Keep mechanism unknown unless separately observed and reproduced with adequate evidence. |
| Selected smoke cases against exact package | Not executed. | No exact production package exists. | Run selected smoke cases after package acceptance and file-access checks. |
| Full minimum suite against exact package | Not executed. | Evaluation plan exists, but no exact production package exists and no full suite has run against one. | Run the full minimum suite against the exact package. |
| Regression baseline against exact package | Not recorded. | No exact production package exists. | Record baseline after full-suite evaluation against a known package identity. |
| Connector limitations | Separate from Skill logic. | Evaluation plan requires connector limitations to remain distinct from Skill failures. | Record connector limitations in evaluation records without converting them into Skill success or failure. |
| Publication/distribution | Not performed. | No package, archive, tag, release, installation, publication, or distribution artifact exists from this Issue. | Decide and perform publication/distribution only in later explicit work. |
| Production readiness | `NOT ESTABLISHED`. | Required package, version, validation, evaluation, limitation, and owner-decision evidence is absent. | Complete readiness rule evidence and owner approval. |
| Owner readiness decision | Not occurred. | No owner approval for production readiness is recorded in the repository. | Owner must explicitly approve readiness after reviewing exact package and evidence. |

Absent package evidence must be reported as not implemented, not tested, not validated, not established, or unknown. It must not be reported as failed runtime behavior.

## Readiness progression

| State | Purpose | Entry evidence | Exit evidence | Prohibited claims | Next decision owner |
| --- | --- | --- | --- | --- | --- |
| 1. Specification baseline | Establish reviewed documentation before package work. | Complete reviewed specification sequence, linked scope items, package structure policy, version/readiness policy, and repository validation passing. | Owner authorizes a separate package draft based on the reviewed specifications. | Do not claim package existence, installation, invocation, package acceptance, supporting-file access, package version, or production readiness. | Repository owner or delegated specification owner. |
| 2. Package draft | Create the first exact package implementation for testing. | Exact proposed tree implemented in a separate PR; one root `SKILL.md`; six expected supporting files; traceability to specifications; static package validation. | Exact package is accepted for testing and package-specific unknowns/failures are recorded. | Do not claim production readiness, full evaluation completion, or owner readiness approval. Package draft permits package tests and smoke cases only. | Package implementation owner and reviewer. |
| 3. Evaluation candidate | Exercise the exact package in controlled runtime and smoke evaluation. | Exact package acceptance tested; supporting-file access tested separately; selected smoke cases completed; package failures/unknowns recorded; dated product observations recorded. | Owner authorizes full minimum suite execution after smoke results and limitations are reviewed. | Do not treat smoke cases as the full suite, do not infer loading mechanics, and do not claim readiness. | Evaluation owner. |
| 4. Readiness candidate | Collect complete evidence for owner readiness review. | Full minimum suite completed; regression baseline recorded; no unresolved critical evaluation failure; material `PARTIAL`/`INCONCLUSIVE` results disclosed; connector limitations separated; version candidate selected separately. | Owner explicitly approves or rejects production readiness for one exact package identity/version. | Do not self-declare production ready, hide limitations, or carry forward old readiness to changed content. | Repository owner. |
| 5. Production ready | Identify one exact package/version as ready under disclosed limits. | Explicit owner approval; exact package identity/version; reviewed evaluation evidence; known limitations/unknowns disclosed; applicable install/publication state recorded; no unresolved readiness blocker. | Later changed package content requires renewed impact review and may require renewed evaluation. | Do not imply readiness for other package trees, future changes, Deep Review, or undisclosed environments. | Repository owner for continued readiness and regression decisions. |

The current repository has not reached Production ready. The current work permits package planning only after the baseline is merged and reviewed.

## Transition evidence matrix

| Transition | Required evidence | Blocking unknowns | Decision |
| --- | --- | --- | --- |
| Specification baseline → package draft | Complete linked specification sequence, package-structure specification, this version/readiness policy, inspected current tree showing no existing production package, and repository validation passing. | Contradictory specifications, missing scope links, validation failures, or unresolved package-boundary questions. | This Issue documents the baseline and does not execute package implementation. |
| Package draft → evaluation candidate | Exact implemented package tree, one root `SKILL.md`, six expected supporting files, static validation, traceability to source specification commits, and recorded package artifact identity. | Missing package files, unresolved static validation failures, missing traceability, or unclear exact artifact identity. | Later implementation/evaluation owner decision. |
| Evaluation candidate → readiness candidate | Exact package acceptance tested, supporting-file access tested separately, selected smoke cases completed, package failures/unknowns recorded, and dated product observations captured. | Untested package acceptance, untested supporting-file access, unexplained smoke failures, missing product surface/date/timezone, or unresolved exact-package identity. | Later evaluation owner decision to run the full minimum suite. |
| Readiness candidate → production ready | Full minimum suite completed, regression baseline recorded, no unresolved critical evaluation failure, material `PARTIAL`/`INCONCLUSIVE` outcomes disclosed, connector limitations separated, version candidate selected, known limitations documented, and explicit owner approval. | Missing owner approval, unresolved critical failure, hidden material unknowns, no package version, no exact package identity, missing install/publication state, or Deep Review boundary ambiguity. | Final owner decision only. |

No transition may be inferred from repository validation alone. Owner approval is required for the final transition. This Issue documents the baseline and does not execute later transitions.

## Version assignment policy

- No package version is assigned before an actual package draft exists.
- The first package version is selected in package implementation or later readiness work.
- Do not choose `0.1.0`, `v0.3.0`, or another package version in this document.
- Version syntax and metadata follow verified platform requirements when known.
- Until verified package-version work occurs, the package version remains `UNASSIGNED`.
- One package version identifies one exact tree/content state.
- Every package version maps to a package SHA, source specification commits, evaluation records, known limitations, and readiness state.
- Repository milestones, Git tags, GitHub Releases, and package versions remain distinct.

## Version-impact policy

Version-impact review is required for changes to:

- trigger/non-trigger behavior;
- inputs or tool policy;
- evidence authority/status semantics;
- blocker/gap/note classification;
- verdict names or precedence;
- workflow/stopping/retry/unstable-head behavior;
- output contract/headings;
- same-PR re-review;
- supporting-file responsibilities;
- package tree/paths;
- package metadata; and
- platform-dependent fallback.

Editorial fixes, links, formatting, and semantics-preserving examples do not automatically require a package version change. Supporting-file changes participate in package versioning. Package tree changes always require explicit review. Do not add automatic versioning.

## Observation and reproduction

Use these observation labels for product behavior and evaluation records:

- `Observed`
- `Reproduced`
- `Inferred`
- `Unverified`
- `Changed since previous test`

Product observations record date, timezone, product surface, exact tree, invocation, and result. First success is `Observed`, not `Reproduced`. Reproduction requires another recorded run under materially comparable conditions. Package acceptance and supporting-file access are separate observations. File use does not identify loading mechanics. Internal loading remains `UNKNOWN` unless separately established by adequate evidence. Platform changes do not silently rewrite specifications. Connector limitations remain separate from Skill logic. This Issue adds no runtime observations.

## Production-readiness rule

Production readiness requires all of the following:

- exact package exists;
- version assigned;
- static validation passes;
- package acceptance established;
- supporting-file access separately evaluated;
- full minimum suite completed;
- regression baseline recorded;
- no unresolved critical failure;
- material partial/inconclusive outcomes disclosed;
- unsupported-claim audit passed;
- Standard Review/Deep Review boundary preserved;
- applicable installation/publication state recorded;
- known limitations/unknowns documented; and
- explicit owner approval.

No single check is sufficient. Documentation and repository CI are necessary but insufficient. The current conclusion is `NOT ESTABLISHED`.

## Current conclusion

- Specification foundation: complete after this document is merged
- Package version: `UNASSIGNED`
- Production package: not implemented
- Evaluation against exact package: not executed
- Production readiness: `NOT ESTABLISHED`
- Internal supporting-file loading mechanism: `UNKNOWN`
- Next authorized work: separate package-implementation planning after pre-implementation prerequisites are reviewed

## Milestone interpretation

- Merging this document may complete the documented `v0.3.0` specification sequence.
- Milestone closure remains an explicit owner action.
- Milestone completion does not assign a package version.
- Milestone completion does not declare readiness.
- Later package implementation is separate work.

## Traceability and regression

Future readiness/version changes must record prior state, new state, package SHA, specification commits, evaluation records, changed behavior, limitations, owner decision, date, and product surface.

Readiness may regress. Changed package content does not inherit old readiness automatically. Critical behavior changes require renewed full-suite evaluation.

## Anti-patterns

Do not:

- treat `v0.3.0` as the package version;
- assign a version before package creation;
- infer readiness from documentation or CI alone;
- conflate package acceptance and file access;
- claim loading mechanics from file use;
- call first success reproduced;
- treat smoke cases as the full suite;
- hide `PARTIAL`, `INCONCLUSIVE`, or unknown outcomes;
- automatically carry readiness forward to changed package content;
- create a package, publish, tag, or release in this Issue; or
- mix Deep Review readiness into Standard Review readiness.

## Quality checklist

This document confirms:

- package version remains `UNASSIGNED`;
- production readiness remains `NOT ESTABLISHED`;
- internal supporting-file loading mechanism remains `UNKNOWN`;
- owner approval is required for production readiness;
- five readiness states are defined;
- transition evidence matrix is defined;
- no package/runtime work is performed;
- no milestone closure is performed;
- package acceptance and supporting-file access remain separate claims;
- supporting-file changes participate in package versioning; and
- Deep Review readiness is not defined here.

## Deferred work

Deferred work includes package implementation, first version selection, metadata, install/run tests, package acceptance, supporting-file tests, smoke/full-suite evaluations, regression baseline, publication, tag/release, readiness decision, milestone closure, and Deep Review readiness.
