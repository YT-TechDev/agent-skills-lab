# Minimal ChatGPT Skill Supporting-File Spike

## Status

- maturity: experimental
- repository package preparation: complete after this change
- package acceptance: observed — ZIP accepted after visible transformation in the first owner-side run
- supporting-file availability: observed — original supporting file retained and inspectable in the package detail view during the first owner-side run
- selected supporting-file behavior: reproduced — exact output repeated under materially comparable selected-run conditions
- internal loading mechanism: unknown
- production readiness: not applicable

## Observation

- first owner-side observation: [`observations/2026-07-10-first-owner-run.md`](observations/2026-07-10-first-owner-run.md)
- controlled reproduction: [`observations/2026-07-10-controlled-reproduction.md`](observations/2026-07-10-controlled-reproduction.md)

These observations record owner-side evidence only. The controlled reproduction record classifies only the exact explicitly selected output behavior as reproduced under the recorded materially comparable conditions. Package acceptance and package-detail file retention remain scoped to the first owner-side observation. The records do not establish production readiness, broad ChatGPT Skill support, unselected invocation behavior, behavior in other environments, or any internal loading mechanism.

## Experiment question

Can a minimal installed ChatGPT Skill access one static Markdown supporting file and return an exact two-line payload that is absent from both `SKILL.md` and the user prompt?

## Why this experiment exists

The previous minimal Skill spike deliberately contained no supporting files. This experiment isolates the next behavior-discovery question in a separate package so earlier artifacts and evidence remain immutable. Only one static Markdown supporting file is tested, and this is not production packaging.

## Package under test

```text
package/
├── SKILL.md
└── reference/
    └── payload.md
```

- the package contains exactly one supporting file
- the success payload exists only in that supporting file within the package
- `SKILL.md` contains the relative path and extraction workflow but not the success payload
- the later user prompt does not contain the success payload

## Package hypothesis

- the directory layout is a test input
- the relative path is a test input
- the supporting-file access procedure is a hypothesis
- repository presence does not prove platform support
- successful package acceptance does not prove supporting-file access
- exact success output would be evidence consistent with supporting-file access
- exact success output would not reveal the internal loading implementation
- one successful owner-side run would be `Observed`, not `Reproduced`

## Scope

- package-shape preparation
- one static supporting Markdown file
- explicit owner-selected invocation
- deterministic success payload
- deterministic unavailable fallback
- evidence classification

## Non-goals

- multiple supporting files
- non-Markdown supporting files
- scripts or executable assets
- automatic invocation
- Project instructions
- tools or connectors
- network access
- mobile
- other models or reasoning settings
- multilingual behavior
- production packaging
- Standard Review
- Deep Review
- implementing `github-standard-engineering-review`

## Manual test prerequisites

Document a later owner-side run using:

```text
Product surface: ChatGPT Web on PC
Workspace surface: Work
Model: GPT-5.6 Terra
Reasoning: light, displayed as 軽
Conversation: fresh
Project: not intentionally selected
Skill: supporting-file-loading-spike explicitly selected and visible as a pill
```

Also require:

- exact tested commit
- exact package contents or hash where practical
- recorded owner-facing package-installation or availability workflow
- safe screenshots or written notes only
- no private URLs
- no conversation-sharing, task, or session-sharing URLs

Do not claim that a particular upload or installation workflow is officially supported.

## Manual test procedure

1. Identify the exact reviewed commit.
2. Inspect the exact package contents.
3. Attempt package installation or availability through the owner-facing workflow.
4. Record acceptance, rejection, transformation, or an inaccessible workflow.
5. Confirm whether the new Skill is available.
6. Open a fresh conversation using the fixed environment.
7. Explicitly select `supporting-file-loading-spike`.
8. Confirm the selected Skill is visible as a pill.
9. Send the exact prompt.
10. Record the exact output.
11. Record visible Skill, loading, file, warning, or fallback indicators where available.
12. Classify the result using `expected-results.md`.
13. Record observations in a later dated observation file.
14. Do not label the first product result `Reproduced`.

Exact prompt:

```text
Run the supporting-file loading spike.
```

The prompt must not contain:

- `SUPPORT_FILE_ACTIVE`
- `POLARIS-23`

## Evidence boundaries

- package acceptance alone does not prove supporting-file loading
- exact success output is evidence consistent with file access but does not reveal the internal parser or loading mechanism
- fallback output does not identify why the supporting file was unavailable
- an unexpected output may reflect package shape, upload transformation, path handling, platform behavior, or instruction interpretation
- inaccessible evidence remains `UNKNOWN`
- a first result is `Observed`, not `Reproduced`
- no result may be generalized beyond recorded conditions

## Safety and privacy

- synthetic payload only
- no secrets or credentials
- no personal information
- no private repositories or private URLs
- no AI conversation, task, or session-sharing URLs
- no screenshots committed
- no unrelated conversation content

## Stopping conditions

Stop and record the limitation when:

- the package cannot be submitted with the supporting file
- the platform accepts only a standalone `SKILL.md`
- the package is transformed unexpectedly
- the Skill cannot be selected
- the supporting-file state cannot be distinguished safely
- GPT-5.6 Terra or light reasoning is unavailable
- the test accidentally runs inside a Project
- evidence cannot be recorded safely
- results are contradictory or ambiguous

Stopping is a valid experiment result.

## Observation boundary

- this repository change contains no platform observations
- future observations require a separate dated file and PR
- after testing begins, changing the package requires a new artifact identity
- reproduction requires another materially comparable later run
