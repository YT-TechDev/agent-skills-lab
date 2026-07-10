# Skill Development Lifecycle

This lifecycle keeps Skill development incremental, requires evidence before progression, makes behavior discovery a first-class stage, allows controlled iteration back to earlier stages, and does not allow direct progression from an idea to a stable package. It does not claim any untested ChatGPT Skills behavior. Lifecycle stages are evidence gates, not merely a checklist: a Skill may return to an earlier stage when evidence changes, but it must not skip required evidence gates.

## Terminology

- **Stage:** A bounded development step with a purpose, required evidence, expected artifacts, and exit condition.
- **Exit condition:** The minimum evidence required before work may progress to the next stage.
- **Blocker:** A missing, contradictory, failed, unsafe, or inaccessible requirement that prevents progression.
- **Revision loop:** A controlled return to an earlier stage when experiments, reviews, or evaluations invalidate assumptions.
- **Packaging gate:** The final evidence and review boundary before installation or publication.

These terms are operational guidance, not a permanent machine-readable lifecycle schema.

## Lifecycle overview

| Stage | Stage name | Primary purpose | Primary artifact or evidence | Exit condition |
| --- | --- | --- | --- | --- |
| 1 | Define the job to be done | Identify one clear user or agent job | Job statement, outcome, assumptions, unknowns | Job is specific, bounded, and unresolved ambiguity is recorded |
| 2 | Define scope and explicit non-goals | Establish responsibility boundaries | In-scope and out-of-scope responsibilities | Scope is reviewable and unrelated responsibilities are removed or split |
| 3 | Define trigger and non-trigger cases | Specify when the Skill should and should not apply | Positive and negative invocation cases | Mandatory inputs and stop behavior are identified |
| 4 | Define inputs, tools, connectors, and evidence requirements | Define required information and access | Input, tool, connector, and evidence requirements | Required evidence and unavailable-tool behavior are clear |
| 5 | Define workflow, stopping conditions, and failure behavior | Describe safe operational sequence | Workflow, stopping conditions, and failure states | The Skill can stop safely without fabricating conclusions |
| 6 | Define decision rules and output contract | Make conclusions consistent and inspectable | Decision categories and output sections | Facts, inferences, and unknowns are distinguishable |
| 7 | Add examples and golden cases | Convert rules into representative scenarios | High-level example outcomes | Success, failure, non-trigger, and inaccessible cases are covered |
| 8 | Run controlled behavior experiments | Investigate real platform and Skill behavior | Dated focused experiment records | Focused questions are answered or limitations are recorded |
| 9 | Classify and record observations | Prevent ambiguous behavior from becoming unsupported fact | Classified observation records | Material conclusions have appropriate classification and dates |
| 10 | Refine and review the specification | Revise design based on evidence | Updated specification and rationale | Failures and contradictions are addressed or retained as unknowns |
| 11 | Implement the first production-target package | Implement reviewed specification without broadening scope | Focused package and implementation notes | Implementation matches the reviewed specification |
| 12 | Evaluate and harden | Test representative success and failure behavior | Evaluation results and revision decisions | Blocking failures are fixed or prevent packaging |
| 13 | Prepare and review a validated package | Package only evidence-supported contents | Reviewed package, limitations, and verdict | Package matches evaluated version and no blockers remain |
| 14 | Install or publish only after review | Prevent unreviewed packages from becoming stable | Approved package and installation record | Installed artifact matches reviewed package and owner approval |

## Detailed lifecycle stages

### Stage 1: Define the job to be done

**Purpose:** Identify one clear user or agent job, state the intended outcome, and identify the problem being solved.

**Expected evidence or artifacts:**

- Job statement.
- Intended user or caller.
- Success description.
- Initial assumptions and unknowns.

**Exit condition:** The job is specific enough to distinguish it from adjacent responsibilities, the Skill is not a broad universal agent, and unresolved foundational ambiguity is recorded. This stage does not define the complete production Skill.

### Stage 2: Define scope and explicit non-goals

**Purpose:** Establish responsibility boundaries and prevent uncontrolled expansion.

**Expected evidence or artifacts:**

- In-scope responsibilities.
- Out-of-scope responsibilities.
- Escalation boundaries.
- Safety or authority boundaries.

**Exit condition:** Scope and non-goals are concrete enough to review, unrelated responsibilities have been removed or split, and Standard Review and Deep Review boundaries remain separate where applicable.

### Stage 3: Define trigger and non-trigger cases

**Purpose:** Specify when the Skill should and should not apply.

**Expected evidence or artifacts:**

- Trigger cases.
- Non-trigger cases.
- False-trigger risks.
- Missed-trigger risks.
- Missing-input behavior.

**Exit condition:** Representative positive and negative invocation cases exist, mandatory inputs and stop behavior are identified, and no undocumented platform behavior is presented as fact.

### Stage 4: Define inputs, tools, connectors, and evidence requirements

**Purpose:** Define what information and access the Skill requires.

**Expected evidence or artifacts:**

- Required inputs.
- Optional inputs.
- Required tools or connectors.
- Optional tools or connectors.
- Read/write boundaries.
- Evidence requirements.
- Fallback behavior when access is denied or unavailable.

**Exit condition:** Required evidence is distinguishable from optional evidence, unavailable-tool behavior is defined, destructive or write-capable behavior has explicit intent and safeguards, and repository-specific Project context is not embedded in the reusable procedure.

### Stage 5: Define workflow, stopping conditions, and failure behavior

**Purpose:** Describe the operational sequence without hiding uncertainty.

**Expected evidence or artifacts:**

- Ordered workflow.
- Stopping conditions.
- Failure states.
- Missing-input behavior.
- Contradictory-evidence behavior.
- Escalation points.

**Exit condition:** The Skill can stop safely, evidence gaps do not become fabricated conclusions, unsafe continuation paths have been removed, and required failure behavior is reviewable.

### Stage 6: Define decision rules and output contract

**Purpose:** Make conclusions consistent and inspectable.

**Expected evidence or artifacts:**

- Decision categories.
- Minimum evidence for each decision.
- Unsupported-claim rules.
- Output sections.
- Uncertainty representation.

**Exit condition:** Identical evidence should lead to materially consistent conclusions, facts, inferences, and unknowns are distinguishable, and outputs do not claim more than the available evidence supports. This stage does not define the final `github-standard-engineering-review` verdict rubric or complete schema.

### Stage 7: Add examples and golden cases

**Purpose:** Convert abstract rules into reviewable representative scenarios.

**Expected evidence or artifacts:**

- Clear success example.
- Blocked example.
- Ambiguous example.
- Inaccessible-evidence example.
- Missing-input example.
- Non-trigger example.
- Escalation example.
- Expected high-level outcome for each case.

**Exit condition:** Examples cover both successful and failure behavior, examples include non-trigger and inaccessible cases, examples do not contain private content or secrets, and expected outcomes are consistent with the specification. Actual golden fixtures are not created in this stage description.

### Stage 8: Run controlled behavior experiments

**Purpose:** Investigate real platform and Skill behavior before production implementation.

**Expected evidence or artifacts:**

- Focused experiment question.
- Expected behavior.
- Test setup.
- Observed behavior.
- Test date.
- Environment or configuration context where relevant.
- Unresolved questions.

**Location guidance:** Behavior spikes and temporary investigations belong under `experiments/`; experiments must not be presented as production packages; and the smallest focused experiment should be preferred.

**Exit condition:** The experiment answered its focused question or clearly documented why it could not, observations are separated from interpretation, and limitations and unresolved questions are recorded. This lifecycle document does not implement an experiment.

### Stage 9: Classify and record observations

**Purpose:** Prevent temporary or ambiguous platform behavior from becoming unsupported repository fact.

Observation records must use these classifications:

- **Observed:** Behavior directly seen in a dated test. A single observation does not automatically establish stability.
- **Reproduced:** Previously observed behavior repeated under recorded, materially comparable conditions. State what was repeated and when.
- **Inferred:** A reasonable interpretation supported by evidence but not directly observed. The supporting evidence and inference must be distinguishable.
- **Unverified:** A claim, expectation, or behavior that has not been adequately confirmed. It must not be used as established fact.
- **Changed since previous test:** A dated observation that materially differs from a prior dated record. Both the previous and current test context should be identifiable.

Observation records must include an ISO-formatted date: `YYYY-MM-DD`.

Where relevant, also record:

- Product or platform surface.
- Model or runtime.
- Skill version or commit.
- Tool or connector availability.
- Project instructions.
- Relevant configuration.
- Expected behavior.
- Observed behavior.
- Interpretation.
- Limitations.
- Unresolved questions.

**Expected evidence or artifacts:** Dated observation records that classify each material finding and separate expected behavior, observed behavior, interpretation, limitations, and unresolved questions.

**Exit condition:** Every material platform conclusion has an appropriate classification, changeable behavior has a test date, and observations are not silently generalized beyond the tested conditions. This document does not record actual ChatGPT Skills findings.

### Stage 10: Refine and review the specification

**Purpose:** Revise assumptions and design based on experimental evidence.

**Expected evidence or artifacts:**

- Updated job, scope, triggers, inputs, workflow, decisions, or outputs.
- Resolved contradictions.
- Retained unknowns.
- Rationale for material design changes.

**Exit condition:** Observed failures and contradictions are addressed, unsupported assumptions are removed or labeled, the specification is coherent enough for production-target implementation, and reviewers can identify remaining unknowns.

### Stage 11: Implement the first production-target package

**Purpose:** Implement the reviewed specification without broadening scope.

**Expected evidence or artifacts:**

- Focused `SKILL.md`.
- Supporting files when justified.
- Version or maturity status.
- Implementation notes.
- Traceability to the reviewed specification.

**Location guidance:** Production-target packages belong under `skills/`; experimental files must not simply be renamed as production packages; and detailed rubrics, policies, examples, schemas, and templates may use supporting files when this improves clarity.

**Exit condition:** Implementation matches the reviewed specification, no unrelated responsibilities were added, package status does not imply validation that has not occurred, and required files are source-readable and reviewable. This Issue does not add files under `skills/`.

### Stage 12: Evaluate and harden

**Purpose:** Test the implemented Skill against representative success and failure conditions.

**Expected evidence or artifacts:**

- Evaluation cases.
- Observed outputs.
- Requirement-status assessment.
- Missed blockers.
- False blockers.
- Unsupported claims.
- Trigger failures.
- Tool or connector failure behavior.
- Revision decisions.

Representative scenarios should include a clearly successful case, blocked case, ambiguous case, inaccessible evidence, missing inputs, non-trigger case, false-trigger risk, conflicting instructions, Project-instruction interaction, connector or tool failure, and Deep Review escalation case.

**Exit condition:** Blocking failures are fixed or explicitly prevent packaging, representative cases have been evaluated, unsupported-claim and graceful-failure behavior is acceptable for the intended maturity level, and remaining limitations are documented. This stage remains high-level and does not duplicate the detailed evaluation strategy reserved for a later Issue.

### Stage 13: Prepare and review a validated package

**Purpose:** Package only the version supported by actual evidence.

**Expected evidence or artifacts:**

- Reviewed package contents.
- Version or maturity status.
- Evaluation summary.
- Known limitations.
- Installation or publication notes.
- Review verdict.

**Exit condition:** Package contents match the evaluated version, package status accurately reflects validation evidence, no blocking review findings remain, relative links and supporting files are valid, and no secrets, private content, or session-sharing URLs are present. A written Skill is not automatically a validated Skill.

### Stage 14: Install or publish only after review

**Purpose:** Prevent unreviewed or mismatched packages from becoming the stable installed version.

**Expected evidence or artifacts:**

- Reviewed package.
- Approved version or commit.
- Installation or publication record.
- Documented limitations.
- Rollback or replacement path where relevant.

**Exit condition:** The installed or published artifact matches the reviewed package, the owner has explicitly approved installation or publication, no newer unreviewed changes are silently included, and the lifecycle record identifies what version was installed or published. Installation or publication is not evidence that the Skill is correct; validation must precede it.

## Revision, stopping, and no-package conditions

Work must stop, return to an earlier stage, or avoid packaging when:

- The job remains ambiguous.
- Scope and non-goals conflict.
- Mandatory inputs are unavailable.
- Required tools or connectors are inaccessible.
- Evidence is contradictory.
- Observed behavior differs from the specification.
- A representative failure case exposes a blocker.
- Unsafe write or destructive boundaries are unresolved.
- Project-specific rules have leaked into reusable procedure.
- Platform behavior is only assumed or unverified.
- Package status would overstate validation.
- The evaluated files differ from the package being prepared.
- Review identifies unresolved blockers.

The next step should be the smallest focused experiment or repository inspection that can resolve the uncertainty. Unavailable or contradictory evidence must not be converted into a positive or negative completion assumption. A revision loop may revisit job definition, scope, triggers, inputs, workflow, decision rules, examples, experiments, or implementation until the blocking evidence is resolved or the work is explicitly deferred.

## Expected artifacts by lifecycle phase

| Phase | Likely artifacts |
| --- | --- |
| Idea and job definition | Job statement, intended user or caller, success description, assumptions, unknowns |
| Design and specification | Scope, non-goals, triggers, inputs, evidence requirements, workflow, stopping behavior, decision rules, output contract |
| Behavior discovery | Focused experiment notes, temporary prototypes, platform comparisons, experiment limitations |
| Observation records | Dated records with classification, expected behavior, observed behavior, interpretation, limitations, and unresolved questions |
| Production-target implementation | Focused `SKILL.md`, justified supporting files, maturity status, implementation notes, specification traceability |
| Evaluation and hardening | Representative cases, observed outputs, blocker analysis, unsupported-claim checks, revision decisions |
| Packaging and installation | Reviewed package, evaluation summary, known limitations, approved version or commit, installation or publication record |

Formats should remain portable and Markdown-first. This lifecycle does not mandate one permanent file schema or directory layout for every future Skill type.

## `experiments/` and `skills/`

Use `experiments/` for behavior spikes, temporary investigations, platform comparisons, uncertain assumptions, observation records tied to an experiment, and minimal prototypes used to answer focused questions. Experiment artifacts may be incomplete, may fail, may be discarded, must not be labeled stable, and must not be treated as installed production packages.

Use `skills/` for production-target packages based on reviewed specifications, evaluated or validated package versions, supporting files required by the package, and explicit maturity and version status. A package should not move into `skills/` merely because an experiment produced a promising result.

## Maturity and version progression

A Skill may progress conceptually through:

1. Idea.
2. Experimental behavior spike.
3. Specified production target.
4. First functional package.
5. Evaluated candidate.
6. Hardened or validated package.
7. Stable reviewed installation or publication.

These are maturity concepts, not a mandatory permanent version-number schema. Version numbers must not imply validation that did not occur. Package status must be evidence-based. Behavior changes may require re-entry into earlier lifecycle stages, and a new version must be evaluated when its behavior or evidence boundary materially changes. This lifecycle does not define a universal Semantic Versioning policy.

## Issue and PR boundaries

Use the repository workflow: Issue → short-lived branch from `main` → implementation → validation → pull request → GPT review → correction when blocked → merge.

`main` is the default integration branch. Each Issue should advance one lifecycle artifact or one coherent development question. Each PR should remain small, coherent, reviewable, reversible, and issue-scoped. Behavior discovery, specification, implementation, and evaluation should normally be separate Issues or PRs. Blocked PRs must be corrected before moving to the next Issue. Unrelated lifecycle stages must not be bundled merely to move faster. Future stages may be planned, but must not be presented as completed.

## Validation expectations before merge

Implementation agents and reviewers should confirm before merge that:

- Changed files match the active Issue.
- Required acceptance criteria are satisfied.
- Repository documentation is consistent.
- Relative links work.
- Claimed validation was actually run.
- Observed results are reported.
- Unknowns and limitations remain visible.
- No unverified platform behavior is presented as fact.
- No secrets, private content, personal information, private URLs, or AI session-sharing URLs are committed.
- No unnecessary dependencies, automation, directories, or abstractions were introduced.
- Future artifacts are not presented as already implemented.

The depth of validation should match the scope and risk of the change. Documentation-only work does not require new CI tooling solely for appearance.
