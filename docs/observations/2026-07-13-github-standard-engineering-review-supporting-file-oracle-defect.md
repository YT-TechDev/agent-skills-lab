# GitHub Standard Engineering Review supporting-file oracle defect observation

## Purpose

This observation records the completed and GPT-reviewed owner-side run for Issue #70 exactly as observed, including the precommitted oracle defect. It is evidence recording only: the ChatGPT product test was not rerun, the expected answer was not changed after execution, and the run is not reinterpreted as a clean supporting-file-access success.

## Source basis and evidence boundary

This record is based on sanitized owner-side screenshots reviewed by GPT for Issue #70 and on repository source comparison performed for this recording task. Screenshots are not committed.

Codex did not directly view the private screenshots. The transient progress UI described below is recorded only as owner-side product UI visible before completion; it is not treated as final assistant output, chain of thought, hidden processing, or evidence of an internal loading mechanism.

The Skill package is not modified by this observation. The Issue #70 body is not retrospectively rewritten. No clean reproduction occurred, and no repeated retry was performed to obtain a preferred output.

## Status summary

| Area | Current result/state | Evaluation status | Product-research label | Reproduction |
| --- | --- | --- | --- | --- |
| Run execution integrity | valid controlled run completed under the recorded conditions | `PASS` | `Observed` | not established |
| Precommitted exact-output assertion | observed output did not match `Unresolved target-state property` | `FAIL` | `Observed` | not established |
| Test specification validity | precommitted oracle was incorrect | `INCONCLUSIVE` | `Observed` | not established |
| Overall Issue #70 result | invalid oracle prevents a clean supporting-file-accessibility conclusion | `INCONCLUSIVE` | `Observed` | not established |
| Supporting-file accessibility | `NOT ESTABLISHED` | `INCONCLUSIVE` | `Unverified` | not established |
| Internal supporting-file loading mechanism | `UNKNOWN` | `NOT APPLICABLE` | `Unverified` | not established |
| GitHub connector capability | `NOT APPLICABLE` | `NOT APPLICABLE` | `Unverified` | not established |
| Live-PR review correctness | not tested | `NOT APPLICABLE` | `Unverified` | not established |
| Package version | `UNASSIGNED` | `NOT APPLICABLE` | `Unverified` | not established |
| Production readiness | `NOT ESTABLISHED` | `NOT APPLICABLE` | `Unverified` | not established |
| Repository state | `Package draft` | `NOT APPLICABLE` | `Observed` | not established |

## Exact package and prior-observation identity

- Exact production package identity: `7c8278cc1bca1286290fdbacd610fe9d97b1fe81`
- Prior observation merge commit: `bbbbd8f9cc0d69b75e2785c8f8456a1c94a36a79`
- Package version: `UNASSIGNED`
- Production supporting-file accessibility before this run: `NOT ESTABLISHED`
- Internal supporting-file loading mechanism: `UNKNOWN`
- Production readiness: `NOT ESTABLISHED`
- Repository readiness state: `Package draft`

## Environment

- Observation date: 2026-07-13
- Timezone: JST / UTC+09:00
- Product surface: ChatGPT Web on a Windows PC
- Plan: Plus
- Workspace/mode: Work visibly selected
- Conversation: fresh
- Project: not selected
- Project files, knowledge files, and repository attachments: none
- GitHub URL: none supplied
- GitHub tool or connector: not intentionally invoked
- Selected Skill: `github-standard-engineering-review`
- Skill selection: explicitly selected; selected Skill indicator visibly present on the sent message
- Installed Skill identity: the same owner-side installed Skill traced to Issue #68
- Model: GPT-5.6 Sol
- Reasoning: high, visibly displayed as `高`
- Visible response-duration UI: `35s考えました`

The duration UI is product metadata and is not part of the assistant output.

## Exact prompt

The exact submitted prompt was:

```text
Run a controlled supporting-file accessibility check for this selected Skill.

Do not review a live pull request and do not use GitHub tools.

For a fictional target, the repository and pull request identity are established, but the current head or change-state identity cannot be established. Return only the exact target-block field label required by the Skill's output contract for naming that unresolved property.

Use exact capitalization. No verdict, explanation, punctuation, code fence, prefix, or suffix.
```

The prompt did not contain either candidate output string:

- `Unresolved target-state property`
- `Reviewed head SHA or equivalent identity`

## Precommitted expected output

Issue #70 precommitted the following exact one-line output:

```text
Unresolved target-state property
```

This historical expected value is preserved unchanged in this observation record.

## Exact observed final output

The full observed assistant output was exactly one line:

```text
Reviewed head SHA or equivalent identity
```

No heading, verdict, explanation, punctuation, code fence, prefix, or suffix was visible in the final output.

## Transient-progress UI boundary

A transient progress sentence was visible while generation was still in progress:

```text
指定された github-standard-engineering-review Skill の出力契約だけを確認し、要求されたフィールドラベルをそのまま返します。
```

That sentence is treated only as transient generation UI visible before completion. It is not part of the final assistant output and is not evidence of internal loading, chain of thought, hidden processing, parser behavior, extraction behavior, storage behavior, relative-path behavior, prompt construction, or any eager, lazy, automatic, selective, or ordered loading mechanism.

## Repository source comparison

The root package file, `skills/github-standard-engineering-review/SKILL.md`, contains the general instruction to establish `current reviewed-head SHA or equivalent change identity` and the instruction to render the exact output contract from `reference/verdict-and-output.md`.

The root file does not contain the exact observed title-case field label:

```text
Reviewed head SHA or equivalent identity
```

The production supporting file, `skills/github-standard-engineering-review/reference/verdict-and-output.md`, defines the reviewed target block field as:

```text
reviewed head SHA or equivalent identity
```

The same supporting file separately says that, when current PR or change-state integrity cannot be established, the output must name the exact unresolved target-state property.

## Oracle-defect analysis

`Reviewed head SHA or equivalent identity` is the actual target-block field label defined by the supporting file, with capitalization adapted to the prompt's exact-capitalization request. `Unresolved target-state property` was not the actual field label. The Issue #70 precommitted oracle misread descriptive prose as a field label.

The observed output matches the actual supporting-file field label. This is evidence consistent with supporting-file accessibility, but supporting-file accessibility nevertheless remains `NOT ESTABLISHED` because the precommitted test oracle was invalid and Issue #70 cannot validly decide the intended supporting-file-accessibility claim.

The package source was not wrong for this observation. The Skill package is not modified.

## Expected-versus-observed comparison

| Layer | Precommitted or required value | Observed or current value | Evaluation status | Product-research label |
| --- | --- | --- | --- | --- |
| Run execution integrity | controlled run under recorded conditions | valid controlled run completed under the recorded conditions | `PASS` | `Observed` |
| Exact-output assertion | `Unresolved target-state property` | `Reviewed head SHA or equivalent identity` | `FAIL` | `Observed` |
| Test specification validity | oracle should identify the actual field label | precommitted oracle was incorrect | `INCONCLUSIVE` | `Observed` |
| Overall Issue #70 result | clean supporting-file-accessibility classification | source-consistent output but invalid oracle | `INCONCLUSIVE` | `Observed` |
| Supporting-file accessibility | supporting-file access established only by a valid test | `NOT ESTABLISHED` | `INCONCLUSIVE` | `Unverified` |

## Verified facts

- The run itself was completed validly under the recorded owner-side conditions.
- The exact prompt is recorded above and did not include `Unresolved target-state property` or `Reviewed head SHA or equivalent identity`.
- The precommitted exact-output assertion expected `Unresolved target-state property`.
- The exact observed final output was `Reviewed head SHA or equivalent identity`.
- The precommitted exact-output assertion failed.
- The test specification/oracle was invalid because the expected value was not the actual field label defined by the supporting file.
- Issue #70 overall is `INCONCLUSIVE` / `Observed`.
- The observed output matches the actual supporting-file field label.
- Supporting-file accessibility remains `NOT ESTABLISHED`.
- Internal loading remains `UNKNOWN`.
- Package version remains `UNASSIGNED`.
- Production readiness remains `NOT ESTABLISHED`.
- Repository state remains `Package draft`.
- No clean reproduction occurred.
- No repeated retry was performed to obtain a preferred output.
- Screenshots are not committed.
- No screenshot, archive, binary artifact, private URL, or AI conversation/session-sharing URL is committed by this record.
- The Skill package is not modified.
- The Issue body is not retrospectively rewritten.

## Reasonable inferences

- The observed output is source-consistent with `reference/verdict-and-output.md` because the supporting file defines `reviewed head SHA or equivalent identity` as the reviewed target block field.
- The observed output is evidence consistent with supporting-file accessibility.
- Because the precommitted oracle was invalid, the observation cannot be promoted to a clean supporting-file-accessibility success.
- A separate later Issue must precommit the corrected expected output before a new run.

## Unknowns

- Internal supporting-file loading mechanism remains `UNKNOWN`.
- Whether the platform read a specific file is not established.
- Whether all supporting files were loaded is not established.
- Eager, lazy, automatic, selective, or ordered loading is not established.
- Parser, extraction, storage, relative-path, hidden-prompt, and prompt-construction behavior are not established.
- GitHub connector capability is `NOT APPLICABLE` for this run.
- Live-PR review correctness was not tested.
- Reproduction is not established.
- Evaluation candidate transition is not established.
- Production readiness is `NOT ESTABLISHED`.

## Limitations

- This record relies on sanitized owner-side screenshots reviewed by GPT for Issue #70; Codex did not directly view the private screenshots.
- Screenshots are not committed.
- The run was not repeated.
- The invalid precommitted oracle prevents a valid pass/fail conclusion for the intended supporting-file-accessibility assertion.
- This observation does not prove the platform read a specific file, all supporting files were loaded, any internal loading mechanism, connector capability, live-PR correctness, reproduction, Evaluation candidate transition, or production readiness.

## Conclusion

Issue #70 recorded a valid controlled run, so run execution integrity is `PASS` / `Observed`. The precommitted exact-output assertion is `FAIL` because the exact observed output, `Reviewed head SHA or equivalent identity`, did not match the precommitted expected output, `Unresolved target-state property`.

The test specification/oracle was invalid: `Unresolved target-state property` was descriptive prose, not the actual target-block field label. The observed output matched the actual supporting-file field label and is evidence consistent with supporting-file accessibility, but supporting-file accessibility remains `NOT ESTABLISHED`. Overall Issue #70 is `INCONCLUSIVE` / `Observed`.

Internal loading remains `UNKNOWN`, package version remains `UNASSIGNED`, production readiness remains `NOT ESTABLISHED`, and repository state remains `Package draft`.

## Smallest valid follow-up experiment

A separate later Issue should precommit a corrected oracle before any new run. The smallest valid follow-up should:

- use the same installed Skill when identity remains traceable;
- open a fresh non-Project conversation;
- precommit the corrected exact expected output before execution:

```text
Reviewed head SHA or equivalent identity
```

- use a prompt that does not include the expected answer;
- classify exact output under the new precommitted oracle; and
- avoid calling that future first valid success `Reproduced` unless the repository's reproduction criteria are independently satisfied.

This PR does not create that Issue and does not execute that run.
