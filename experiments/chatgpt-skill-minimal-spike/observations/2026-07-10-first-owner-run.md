# First Owner-Side Observation — 2026-07-10

This record documents the first owner-side observation of the minimal ChatGPT Skill behavior spike. It records evidence only; it does not modify the experimental package or the precommitted expectations.

Source basis: GitHub Issue #13 owner-provided observation evidence and repository files at the tested revision. Product-side observations were not rerun, simulated, inferred, or invented for this repository change.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Direct `SKILL.md` upload | VERIFIED | Observed |
| Installed Skill listing | VERIFIED | Observed |
| Explicit token output | VERIFIED | Observed |
| Missing-token output | VERIFIED | Observed |
| Marker suppression for the selected non-trigger case | VERIFIED | Observed |
| Automatic non-trigger routing | UNKNOWN | Unverified |
| Reproduction | MISSING | Not established |

`Reproduced` is not assigned because this is the first recorded run. Requirement/result statuses and platform observation labels are separate classifications. `Not established` is explanatory text, not a platform observation label.

## Tested artifact identity

- tested repository revision: `1a6f91f8fd894b5df628d7e9098191c9254a6948`
- package path: `experiments/chatgpt-skill-minimal-spike/package/SKILL.md`
- Skill name: `minimal-behavior-spike`
- synthetic token: `ORBIT-7`
- observation date: `2026-07-10`

The repository package was not edited during the owner-side run. `expected-results.md` was not edited before or during the run. The uploaded artifact was a direct `SKILL.md` file.

No local uploaded file hash was independently recorded. Binary identity beyond the tested repository revision and owner-provided evidence is not claimed.

## Environment context

- product surface: ChatGPT Web
- Skills entry point: `/skills`
- visible workspace surface during the conversation: `Work`
- browser and operating-system UI were visible, but exact browser and OS version information was not recorded
- Project membership or Project instructions: `UNKNOWN`
- plan or account tier: `UNKNOWN`
- tools and connectors relevant to Skill behavior: not evaluated
- overall model/runtime context: `PARTIAL`

The supplied screenshots showed different visible model selections during the overall flow:

- a setup screen showed GPT-5.6 Sol with a very-high reasoning setting
- later execution screenshots showed GPT-5.6 Terra with a light reasoning setting

Therefore, this record does not report one stable model for the entire run. The core Case B, exact Case C, and Case D execution screenshots visibly showed GPT-5.6 Terra / light where available. Invisible model routing is not inferred. This record does not claim that every observed output used the same model and does not claim that the model changed automatically.

## Case A — Package workflow

The expected behavior was precommitted in `experiments/chatgpt-skill-minimal-spike/expected-results.md`.

Directly observed UI behavior:

- `/skills` existed on ChatGPT Web
- the Skill creation menu displayed:
  - chat creation
  - editor creation
  - upload from computer
- the upload dialog advertised:
  - `.zip`
  - `.skill`
  - direct `SKILL.md`
- the upload dialog displayed a third-party Skill safety warning
- direct `SKILL.md` upload was accepted
- the UI displayed a successful-upload message
- `minimal-behavior-spike` appeared under installed Skills
- the frontmatter name appeared as the displayed Skill name
- a description appeared in the Skill list

Requirement/result status: `VERIFIED`.
Platform observation label: `Observed`.

Boundaries:

- package acceptance does not prove invocation
- this run does not prove that `name` is universally required
- this run does not prove that `description` is universally required
- this run does not prove that every advertised format is accepted
- `.zip` acceptance was not tested
- `.skill` acceptance was not tested
- internal parsing behavior remains unknown
- validation behavior remains unknown
- storage behavior remains unknown
- transformation behavior remains unknown

No account-specific UI data or screenshot files are included.

## Case B — Explicit token invocation

Prompt:

```text
Run the minimal behavior spike with token ORBIT-7.
```

Precommitted expected output:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Observed output:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Directly observed evidence:

- the `minimal-behavior-spike` Skill pill was visibly attached to the request
- the output exactly matched the precommitted expected output
- `ORBIT-7` was preserved exactly
- no relevant extra text appeared in the output

Output status: `VERIFIED`.
Platform observation label: `Observed`.

Interpretation boundaries:

- the visible Skill pill plus deterministic matching output is strong invocation evidence for this run
- the platform's internal instruction-loading mechanism was not directly visible
- matching output alone would not have been sufficient proof without the UI evidence
- one run is not reproduction
- this result applies only to the recorded date, package revision, product surface, and observed context

Exact prompt-injection mechanics and internal system-prompt structure are not claimed.

## Case C — Missing token

Exact precommitted prompt:

```text
Run the minimal behavior spike.
```

Precommitted expected output:

```text
SPIKE_INPUT_REQUIRED
```

Observed output:

```text
SPIKE_INPUT_REQUIRED
```

Directly observed evidence:

- the exact precommitted Case C prompt was used
- the output exactly matched the precommitted expected output
- no clarification question appeared
- no fallback text appeared
- no warning appeared in the relevant output
- no unrelated relevant text appeared

Output status: `VERIFIED`.
Platform observation label: `Observed`.

Interpretation boundaries:

- this confirms missing-token behavior for this dated run and recorded context
- the platform's internal instruction-loading mechanism remains unknown
- one run is not reproduction

### Supplemental missing-token observation

Before the exact Case C prompt was run, ChatGPT supplied an automatic exploratory prompt after Skill installation:

```text
I just added the “minimal-behavior-spike” skill. Let's explore what it does with an example. Make up a realistic user prompt and then use the full Skill end to end.
```

That different prompt produced:

```text
SPIKE_INPUT_REQUIRED
```

This automatic exploratory prompt is supplemental evidence. It is not the primary Case C result and must not replace the exact precommitted prompt in the expected-versus-observed comparison. The exact prompt is the primary evidence for Case C.

## Case D — Selected non-trigger request

Prompt:

```text
Explain what a reusable agent Skill is.
```

Directly observed constraints:

- `SPIKE_ACTIVE` did not appear
- `SPIKE_INPUT_REQUIRED` did not appear
- the response answered the general question
- the `minimal-behavior-spike` Skill pill was visibly attached
- the response explicitly mentioned `minimal-behavior-spike`
- the response summarized the experimental behavior of the selected Skill

Marker-suppression status: `VERIFIED`.
Platform observation label: `Observed`.

Critical interpretation:

- the precommitted marker-suppression constraint passed
- automatic non-trigger routing was not tested because the Skill was explicitly selected and attached
- the selected Skill still influenced the response enough to be mentioned
- avoiding all Skill influence on unrelated answers was not part of the current package contract
- automatic trigger precision remains `UNKNOWN`
- automatic non-trigger routing remains `UNKNOWN`

This case is not described as a failure and is not proof of automatic routing precision. This record does not claim that the platform automatically chose not to invoke the Skill.

## Expected-versus-observed comparison

| Case | Expected behavior | Observed behavior | Result status | Platform label | Meaningful discrepancy or limitation |
| --- | --- | --- | --- | --- | --- |
| Case A — Package workflow | Package handling result should be observable; no specific acceptance result was assumed. | Direct `SKILL.md` upload was advertised and accepted; installed Skill listing appeared. | VERIFIED | Observed | `.zip` and `.skill` were advertised but not tested; internal parsing, validation, storage, and transformation behavior remain unknown. |
| Case B — Explicit token invocation | `SPIKE_ACTIVE`<br>`token: ORBIT-7` | `SPIKE_ACTIVE`<br>`token: ORBIT-7` | VERIFIED; exact match | Observed | One run is not reproduction; internal instruction-loading mechanism was not visible. |
| Case C — Missing token | `SPIKE_INPUT_REQUIRED` | `SPIKE_INPUT_REQUIRED` | VERIFIED; exact match | Observed | One run is not reproduction; supplemental automatic exploratory prompt is not the primary Case C comparison. |
| Case D — Selected non-trigger request | Constraint: no `SPIKE_ACTIVE`; no `SPIKE_INPUT_REQUIRED`. | Neither marker appeared; the general question was answered; the selected Skill was still referenced. | VERIFIED; marker constraint passed | Observed | Automatic routing remains `UNKNOWN` because the Skill was explicitly selected and attached. |

## Verified facts

- ChatGPT Web exposed a Skills page on `2026-07-10`.
- The Skills page exposed chat creation, editor creation, and upload-from-computer options.
- The upload dialog advertised `.zip`, `.skill`, and direct `SKILL.md`.
- Direct `SKILL.md` upload was accepted in this run.
- Uploaded frontmatter values were reflected in the installed Skill listing.
- The uploaded Skill appeared under installed Skills.
- A selected Skill appeared as a visible Skill pill in conversation.
- Explicit token behavior matched expectations.
- The token was preserved exactly.
- Missing-token behavior matched expectations.
- The selected Case D marker-suppression constraint passed.
- The upload dialog displayed a third-party Skill safety warning.

## Inferred

- The uploaded Skill instructions likely affected model behavior because the selected Skill pill and deterministic outputs aligned with the package contract.
- The frontmatter was parsed sufficiently to populate displayed Skill metadata.

These are inferences rather than directly visible internal facts. This record does not infer exact internal prompt injection, exact instruction-loading architecture, storage architecture, validation implementation, universal metadata requirements, automatic invocation behavior, behavior when the Skill is not selected, behavior across all ChatGPT plans, behavior across all models, or behavior across all product surfaces.

## Unknowns

- whether `name` is universally required: `UNKNOWN`
- whether `description` is universally required: `UNKNOWN`
- `.zip` acceptance: `UNKNOWN`
- `.skill` acceptance: `UNKNOWN`
- archive layout requirements: `UNKNOWN`
- supporting-file behavior: `UNKNOWN`
- automatic invocation: `UNKNOWN` / Unverified
- automatic trigger selection: `UNKNOWN` / Unverified
- automatic non-trigger routing: `UNKNOWN` / Unverified
- behavior when the Skill is installed but not explicitly attached: `UNKNOWN`
- behavior inside a Project: `UNKNOWN`
- interaction with Project instructions: `UNKNOWN`
- tool behavior: `UNKNOWN`
- connector behavior: `UNKNOWN`
- behavior across other models: `UNKNOWN`
- behavior across other reasoning settings: `UNKNOWN`
- behavior across other ChatGPT product surfaces: `UNKNOWN`
- persistence across new sessions: `UNKNOWN`
- persistence across devices: `UNKNOWN`
- internal parsing mechanism: `UNKNOWN`
- internal validation mechanism: `UNKNOWN`
- internal storage mechanism: `UNKNOWN`
- internal instruction-loading mechanism: `UNKNOWN`
- reproduction under materially comparable conditions: `UNKNOWN` / Unverified

## Discrepancies

- Cases B and C matched their expected output exactly.
- Case D passed its marker constraint, but the response still referenced the selected experimental Skill.
- Model/runtime context was not held constant across the entire setup and execution flow.
- Automatic non-trigger routing was not exercised.
- The first missing-token response came from an automatic exploratory prompt rather than the precommitted prompt, but the exact prompt was subsequently run successfully.
- `.zip` and `.skill` were advertised but not tested.

These discrepancies do not classify Case D as a failed test and do not identify model inconsistency as the cause of any observed behavior.

## Limitations

- This was the first dated run.
- No result qualifies as `Reproduced`.
- Screenshots were owner-provided and are not committed.
- No independent UI event log exists.
- No stable single model was preserved across the entire flow.
- Project context was not established.
- Plan or account tier was not recorded.
- No automatic invocation case was run.
- No installed-but-unattached case was run.
- No Project compatibility case was run.
- No `.zip` package was tested.
- No `.skill` package was tested.
- No supporting files were tested.
- No tools were tested.
- No connectors were tested.
- No persistence or cross-device behavior was tested.

## Decision

- The first behavior spike produced sufficient evidence to confirm direct `SKILL.md` acceptance under the recorded conditions.
- The first behavior spike produced sufficient evidence to confirm selected deterministic explicit-token behavior under the recorded conditions.
- The first behavior spike produced sufficient evidence to confirm selected deterministic missing-token behavior under the recorded conditions.
- The selected Case D marker-suppression constraint passed.
- Automatic invocation and automatic routing remain unverified.
- The package must remain experimental.
- The result is not `Reproduced`.
- No production Skill should be created from this single run.
- No final packaging standard should be inferred from this run.

## Smallest justified next experiment

Repeat Cases B, C, and D in a fresh conversation while:

- using the same reviewed package revision
- explicitly attaching the Skill
- fixing one model
- fixing one reasoning setting
- recording the model and reasoning setting before execution
- recording comparable environment context
- using the same exact prompts
- keeping the Skill package unchanged

Purpose:

- determine whether the observed deterministic selected-Skill behavior can be labeled `Reproduced`

Automatic invocation must remain a separate later experiment. Automatic invocation tests a different question. Supporting-file behavior must remain a separate later experiment. Project compatibility must remain a separate later experiment.
