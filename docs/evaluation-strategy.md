# Initial Skill Evaluation Strategy

Skills require representative evaluation, not one successful example. Expected and observed results must remain separate, important conclusions must be traceable to evidence, and trigger behavior and output quality are separate evaluation concerns. Platform behavior may change, so platform observations must be dated. This document defines an initial Markdown-first evaluation strategy, not an automated framework, and it does not claim that any ChatGPT Skills behavior is already validated.

## Evaluation goals

Initial Skill evaluation is intended to expose failure modes, not merely confirm expected success. Evaluation should:

1. Verify that the Skill activates in appropriate cases.
2. Verify that it does not activate in inappropriate cases.
3. Assess whether instructions are followed.
4. Assess whether conclusions are supported by evidence.
5. Detect unsupported claims.
6. Detect missed and false blockers.
7. Assess consistency across materially comparable cases.
8. Assess graceful failure when inputs, tools, or evidence are unavailable.
9. Verify compatibility with Project instructions.
10. Determine whether the evaluated version has sufficient evidence for its stated maturity.

## Evaluation unit

A single evaluation run is a recorded combination of:

- Named case.
- Exact Skill version, package version, commit, or working revision.
- Platform or product surface.
- Model or runtime where relevant.
- Project instructions or environment context.
- Tool and connector availability.
- Execution date.
- Expected result.
- Observed result.

Results from one version or environment must not be silently generalized to another. This strategy does not require a permanent machine-readable schema.

## Evaluation layers

### Platform behavior evaluation

Platform behavior evaluation covers behavior controlled partly by the host platform, such as:

- Whether the Skill is discoverable or available.
- Whether it is invoked.
- Whether it fails to invoke.
- Whether Project instructions interact with it as expected.
- Whether supporting files are available.
- Whether tools or connectors are accessible.
- Whether behavior changes across platform versions or dates.

Platform observations must use dated evidence classifications. A platform observation should not be treated as permanent fact merely because it was seen once.

### Skill output-quality evaluation

Skill output-quality evaluation covers behavior produced by the Skill after it runs, such as:

- Instruction compliance.
- Scope fidelity.
- Evidence use.
- Unsupported claims.
- Blocker detection.
- Verdict consistency.
- Escalation behavior.
- Graceful failure.
- Output clarity and usefulness.

Good output quality cannot compensate for broken trigger behavior, and correct invocation cannot compensate for unsupported output.

## Mandatory scenario classes

Each future evaluation set should include multiple scenario classes. At minimum, it must include the following classes.

### 1. Successful case

A case with:

- Appropriate invocation.
- Accessible required evidence.
- A clearly supportable outcome.
- No intentional blocker.

Purpose:

- Verify normal operation.
- Verify evidence-backed output.
- Verify useful and correctly scoped conclusions.

### 2. Blocked case

A case containing a real blocking condition.

Purpose:

- Verify that the blocker is found.
- Verify that it is supported by concrete evidence.
- Verify that non-blocking notes are not confused with blockers.
- Verify that the Skill does not proceed as if the work were complete.

### 3. Ambiguous case

A case where evidence supports more than one reasonable interpretation or where requirements are incomplete.

Purpose:

- Verify that uncertainty is visible.
- Verify that inference is separated from fact.
- Verify that the Skill does not fabricate certainty.
- Verify that the smallest missing input or experiment is identified.

### 4. Inaccessible-evidence case

A case where required repository data, tools, connectors, checks, or files cannot be accessed.

Purpose:

- Verify graceful failure.
- Verify that inaccessible evidence is reported.
- Verify that missing evidence is not treated as success or failure.
- Verify that the conclusion is appropriately limited.

### 5. Non-trigger case

A request or context that is outside the Skill's defined job.

Purpose:

- Verify that the Skill does not activate.
- Verify that adjacent tasks remain separate.
- Detect false invocation.

Recommended future scenario classes include:

- Missing-input case.
- False-trigger-risk case.
- Conflicting-instructions case.
- Project-instruction compatibility case.
- Tool or connector failure case.
- Repeated-run consistency case.
- Standard Review to Deep Review escalation case.

Actual case files and fixtures belong to later Issues.

## Representative case design

Future cases should be intentionally selected rather than copied only from convenient successful examples. A representative case should record:

- Case identifier.
- Scenario class.
- Purpose.
- Relevant requirement or risk.
- Inputs.
- Available evidence.
- Intentionally unavailable evidence.
- Expected trigger behavior.
- Expected high-level result.
- Expected failure or escalation behavior.
- Relevant Project instructions.
- Tool and connector assumptions.
- Version and date context.

Cases should vary material conditions such as:

- Complete versus incomplete requirements.
- Accessible versus inaccessible evidence.
- Real blocker versus no blocker.
- Standard-review scope versus deep-review scope.
- Consistent versus contradictory evidence.
- Correct trigger versus non-trigger request.

This strategy does not define a fixed universal fixture schema.

## Golden-case purpose and limitations

Golden cases are reviewed reference cases with expected outcomes. They are useful for:

- Regression comparison.
- Instruction-change review.
- Output-contract review.
- Verdict consistency checks.
- Identifying behavior changes.

Golden cases are not:

- Proof of general correctness.
- A replacement for exploratory evaluation.
- Permanent truth when platform behavior changes.
- Sufficient when only happy paths are covered.
- Valid for a new Skill version without review.

Golden cases must identify:

- What behavior they protect.
- Why the expected result is justified.
- Which evidence supports the expectation.
- Version and date context.
- Known limitations.

Detailed golden cases and fixtures belong to later Issues.

## Expected and observed results

Expected results must be recorded before interpreting the observed run.

### Expected-result record

An expected-result record should include:

- Expected trigger or non-trigger behavior.
- Expected evidence to be inspected.
- Expected decision or high-level outcome.
- Expected blockers or absence of blockers.
- Expected uncertainty.
- Expected escalation.
- Expected tool-failure behavior.
- Rationale and supporting source.

### Observed-result record

An observed-result record should include:

- Actual trigger behavior.
- Evidence actually accessed.
- Tools or connectors actually used.
- Unavailable evidence.
- Actual output or verdict.
- Actual blockers and notes.
- Uncertainty handling.
- Escalation behavior.
- Result statuses.
- Run date and environment.
- Limitations.

Observed results must not be edited to match expectations.

## Result statuses

These statuses describe individual requirements or evaluation dimensions:

- **VERIFIED:** Available evidence directly supports the expected condition.
- **PARTIAL:** Some required behavior or evidence is present, but the condition is not fully satisfied or verified.
- **MISSING:** A required input, behavior, output element, or evidence item is absent.
- **UNKNOWN:** The condition cannot be determined from available evidence. Use this when evidence is inaccessible, contradictory, or insufficient to decide.
- **NOT APPLICABLE:** The condition is outside the scope of the case.

These are evidence-status labels, not automatically the final Skill verdict. MISSING and UNKNOWN are different: MISSING means the needed item is absent, while UNKNOWN means the available evidence does not allow a determination. NOT APPLICABLE must not be used to hide an untested requirement.

## Evaluation dimensions

The following dimensions guide review. Metric names below are dimension names, not measured results; no rates have been measured yet.

| Dimension | Operational definition | Typical evidence | Common failure signal |
| --- | --- | --- | --- |
| Trigger precision | Whether the Skill activates only for requests inside its defined job. | Trigger and non-trigger case records, platform observations, request text. | Skill activates for adjacent work or fails to stop when outside scope. |
| False invocation rate | The proportion or count of non-trigger cases where the Skill activates incorrectly; no rate has been measured yet. | Non-trigger case runs and dated invocation observations. | Any non-trigger case incorrectly invokes the Skill. |
| Missed invocation rate | The proportion or count of valid trigger cases where the Skill does not activate; no rate has been measured yet. | Successful, blocked, ambiguous, and inaccessible-evidence case runs. | A valid trigger case does not invoke the Skill. |
| Instruction compliance | Whether the Skill follows its reusable procedure, Project instructions, immediate user constraints, and safety boundaries. | Skill output, Project instructions, user prompt, package instructions. | Ignores explicit constraints, leaks Project rules into reusable procedure, or violates safety boundaries. |
| Evidence completeness | Whether required and materially relevant evidence was inspected, or its absence was explicitly reported. | File citations, diff review notes, tool outputs, unavailable-evidence records. | Required evidence is skipped without disclosure. |
| Unsupported-claim rate | The proportion or count of consequential claims that lack traceable supporting evidence; no rate has been measured yet. | Output claims compared with cited files, diffs, tool results, or issue evidence. | Claims tests passed, behavior works, or requirements are satisfied without inspected evidence. |
| Missed-blocker rate | The proportion or count of expected real blockers that were not identified; no rate has been measured yet. | Blocked case expectations and observed blocker findings. | A known blocker is absent from the output or verdict. |
| False-blocker rate | The proportion or count of reported blockers that are not supported by requirements or evidence; no rate has been measured yet. | Reported blockers compared with requirements and inspected evidence. | Notes or preferences are elevated to blockers without support. |
| Verdict consistency | Whether materially comparable evidence produces materially consistent decisions. | Repeated or paired cases with comparable evidence. | Similar facts produce conflicting conclusions without explanation. |
| Output usefulness | Whether the output is clear, prioritized, actionable, scoped, and useful to the intended user. | Final report, review comments, user task, acceptance criteria. | Output is vague, unprioritized, overbroad, or not actionable. |
| Tool and connector evidence coverage | Whether required accessible tools and connectors were used appropriately and unavailable sources were disclosed. | Tool logs, connector records, inaccessible-evidence notes. | Available required tools are skipped, or unavailable tools are silently treated as checked. |
| Project instruction compatibility | Whether repository-specific instructions are applied correctly without being embedded permanently into the reusable Skill. | Project instructions, Skill package content, output rationale. | Project-specific rules are ignored during evaluation or hard-coded into reusable Skill instructions. |
| Graceful failure behavior | Whether the Skill stops safely, reports limitations, avoids fabrication, and identifies the smallest useful next step when required evidence is unavailable. | Inaccessible-evidence cases, missing-input cases, tool-failure records. | The Skill fabricates results, proceeds as complete, or fails to identify the limiting gap. |
| Scope fidelity | Whether the Skill stays within the defined job and explicit non-goals. | Scope statement, prompt, output, changed files where relevant. | The Skill expands into unrelated review, implementation, release, or audit responsibilities. |
| Escalation correctness | Whether escalation occurs only when the defined boundary or risk requires it. | Escalation cases, Standard Review and Deep Review boundaries, output rationale. | Required escalation is missed, or routine work is escalated unnecessarily. |
| Output-contract compliance | Whether required sections, labels, and evidence references are present without inventing a final verdict algorithm. | Output contract draft, evaluation output, status labels. | Required output elements are missing or extra unsupported verdict semantics are added. |

## Comparison and discrepancy analysis

Evaluation must compare expected and observed results explicitly. Useful discrepancy classes include:

- False invocation.
- Missed invocation.
- Instruction violation.
- Scope expansion.
- Evidence omission.
- Unsupported claim.
- Missed blocker.
- False blocker.
- Incorrect verdict.
- Inconsistent verdict.
- Failed escalation.
- Unnecessary escalation.
- Tool or connector misuse.
- Failure to disclose inaccessible evidence.
- Output-contract deviation.
- Low-usefulness output.
- Platform behavior change.

For each material discrepancy, record:

- Expected behavior.
- Observed behavior.
- Supporting evidence.
- Impact.
- Whether it blocks validation.
- Proposed revision or next experiment.
- Retest requirement.

Discrepancies should drive revision rather than be hidden by averaging them into one score.

## Repeated testing for changeable behavior

Repeated testing is required when:

- Platform behavior is load-bearing.
- Trigger behavior may be nondeterministic.
- Model or runtime versions change.
- Project instructions change.
- Tools or connectors change.
- Supporting-file behavior changes.
- A previous observation produced contradictory results.
- A Skill version materially changes.

Repeated-test records must include:

- Date in YYYY-MM-DD.
- Materially relevant environment.
- Version or commit.
- Repeated case identifier.
- Whether conditions were comparable.
- Expected behavior.
- Observed behavior.
- Differences from the previous run.

One observation is not automatically reproducible evidence.

## Platform-observation labels

Use these labels for platform findings:

- **Observed:** Behavior directly seen in a dated test.
- **Reproduced:** Previously observed behavior repeated under materially comparable recorded conditions.
- **Inferred:** A reasonable interpretation supported by evidence but not directly observed.
- **Unverified:** A claim or expectation that has not been adequately confirmed.
- **Changed since previous test:** A dated observation that materially differs from a previous dated test.

These labels describe the evidence status of platform findings and are separate from VERIFIED, PARTIAL, MISSING, UNKNOWN, and NOT APPLICABLE. This document does not claim that any current ChatGPT Skills behavior has already received one of these labels through actual testing.

## Minimum evidence before declaring a version validated

A Skill version must not be called validated merely because:

- It was written.
- It installed successfully.
- One case succeeded.
- One reviewer liked the output.
- The expected keywords appeared.
- The package has a version number.

At minimum, validation requires:

- The exact evaluated Skill version, package version, commit, or revision is identified.
- Required scenario classes are represented.
- Expected results were recorded.
- Observed results were recorded separately.
- Trigger behavior and output quality were both assessed.
- Key evaluation dimensions were reviewed.
- Inaccessible evidence and unsupported claims were tracked.
- Material discrepancies were analyzed.
- Blocking discrepancies were resolved or explicitly prevented validation.
- Load-bearing platform assumptions have suitable dated evidence.
- Repeated testing was performed where changeable behavior materially affects the result.
- Known limitations remain visible.
- The package under consideration matches the evaluated contents.
- Review confirms that the evidence supports the stated maturity.

This strategy does not define a permanent numerical pass threshold. Validation is version-specific and may be invalidated by material behavior, package, platform, tool, connector, or instruction changes.

## Evaluation summary expectations

A future evaluation summary should report at least:

- Evaluated version or commit.
- Evaluation date.
- Platform and environment context.
- Scenario classes covered.
- Cases executed.
- Expected versus observed discrepancies.
- Dimension-level statuses.
- Blocker-class failures.
- Platform-observation labels.
- Known limitations.
- Unresolved questions.
- Revision or retest decision.
- Validation recommendation.

This strategy does not define the final output contract for `github-standard-engineering-review`.

## Current limitations

This initial strategy does not yet include:

- Actual cases.
- Actual golden fixtures.
- Automated scoring.
- Measured rates.
- Statistical confidence.
- Final quality thresholds.
- CI integration.
- Behavior-spike results.
- Production Skill results.

Those items belong to later Issues and evidence-producing work.
