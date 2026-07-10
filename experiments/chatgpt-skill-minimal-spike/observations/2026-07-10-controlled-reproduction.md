# Controlled Reproduction — 2026-07-10

This record documents the completed owner-side controlled reproduction of the minimal ChatGPT Skill behavior spike for GitHub Issue #16. It records dated repository evidence from the owner-reported product-side runs and reviewed screenshots; it does not rerun, simulate, infer, or invent ChatGPT product behavior.

Source basis: GitHub Issue #16, the owner-provided Issue #16 evidence, and the repository files listed below. Screenshots were reviewed for evidence but are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Case B selected explicit-token output | VERIFIED | Reproduced |
| Case C selected missing-token output | VERIFIED | Reproduced |
| Case D selected marker suppression | VERIFIED | Reproduced |
| Exact unrelated-answer wording | PARTIAL | Observed difference |
| Consistent selected-Skill influence on unrelated content | UNKNOWN | Unverified |
| Automatic invocation | UNKNOWN | Unverified |
| Automatic trigger selection | UNKNOWN | Unverified |
| Automatic non-trigger routing | UNKNOWN | Unverified |
| Language-adaptation mechanism | UNKNOWN | Unverified |

`Reproduced` applies only to the named selected-Skill behaviors. It does not apply to the entire Skill, all output wording, all platform behavior, or production readiness. Requirement/result statuses and platform observation labels are separate classifications.

## Repository artifact identity

- original package source revision: `1a6f91f8fd894b5df628d7e9098191c9254a6948`
- current repository baseline: `333ec32668c312da5b6b8d808a7f8df457702b44`
- package path: `experiments/chatgpt-skill-minimal-spike/package/SKILL.md`
- Skill name: `minimal-behavior-spike`
- synthetic token: `ORBIT-7`
- reproduction date: `2026-07-10`

Artifact-identity boundaries:

- the already installed Skill was reused
- the Skill was not reuploaded for this reproduction run
- the repository package and precommitted expectations were not edited
- no independent installed-artifact hash was recorded
- exact installed binary or stored-platform identity was not independently revalidated
- the result is tied to the owner-reported unchanged installed Skill and the recorded repository package source

This record does not overclaim installed artifact identity beyond those boundaries.

## Owner-reported controlled environment setup

- product surface: ChatGPT Web
- workspace surface: `Work`
- model: GPT-5.6 Terra
- reasoning setting: light, visibly displayed as `軽`
- Skill: `minimal-behavior-spike`
- Skill state: explicitly selected and visible as a pill
- conversation isolation: separate fresh conversation for each formal case
- Project use: no Project was intentionally selected
- token: `ORBIT-7`
- screenshots: owner-provided for review and not committed

Visible model, reasoning setting, prompt, Skill pill, and output were reviewed for each formal case. Exact Project-instruction state was not independently inspected and remains limited to the owner-reported setup. Tools and connectors were not evaluated.

## Excluded Case B2 attempt

An earlier Case B2 attempt used conditions that did not match the controlled setup. The owner reran Case B2 using the required visible settings. Only the corrected controlled run is used in the formal reproduction comparison.

The excluded attempt is not classified as a failed Skill result. Its exact differing condition was not preserved as part of the formal comparison, and it is not used to weaken or strengthen the controlled result.

## Case B2 — Repeated selected explicit-token invocation

Exact prompt:

```text
Run the minimal behavior spike with token ORBIT-7.
```

First observed result:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Repeated observed result:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Directly observed UI evidence and observed Skill output:

- exact prompt visible
- selected Skill pill visible
- GPT-5.6 Terra visible
- light reasoning visible
- output exactly matched the first recorded result
- `ORBIT-7` was preserved exactly
- no relevant extra output appeared

Result status: `VERIFIED`.
Platform label for deterministic selected-Skill output: `Reproduced`.

Boundaries:

- this reproduces the selected explicit-token output under the recorded conditions
- it does not prove automatic invocation
- it does not reveal the internal instruction-loading mechanism
- it does not establish behavior across other models or settings

## Case C2 — Repeated selected missing-token invocation

Exact prompt:

```text
Run the minimal behavior spike.
```

First observed result:

```text
SPIKE_INPUT_REQUIRED
```

Repeated observed result:

```text
SPIKE_INPUT_REQUIRED
```

Directly observed UI evidence and observed Skill output:

- exact prompt visible
- selected Skill pill visible
- GPT-5.6 Terra visible
- light reasoning visible
- output exactly matched the first recorded result
- no clarification appeared
- no fallback text appeared
- no warning appeared in the relevant Skill output
- no relevant extra response text appeared

Observed UI detail:

```text
13s考えました
```

That text was a platform reasoning-duration indicator. It was not part of the Skill output and does not change the exact-output comparison.

Result status: `VERIFIED`.
Platform label for deterministic selected-Skill output: `Reproduced`.

## Case D2 — Repeated selected non-trigger request

Exact prompt:

```text
Explain what a reusable agent Skill is.
```

Repeated observed output:

```text
Reusable agent Skill は、特定の作業手順・判断基準・ツール利用ルールをまとめて、必要なときにエージェントへ再利用できる形にしたものです。

たとえば「PRレビュー」「PDF作成」「Supabase設計」のような作業ごとに Skill を用意すると、毎回長い指示を書かなくても、同じ品質・安全基準・手順で実行できます。
要するに、AIエージェント向けの再利用可能な作業マニュアル兼ワークフローです。
```

Directly observed UI evidence and observed output:

- exact prompt visible
- selected Skill pill visible
- GPT-5.6 Terra visible
- light reasoning visible
- `SPIKE_ACTIVE` did not appear
- `SPIKE_INPUT_REQUIRED` did not appear
- the general question was answered
- the answer was in Japanese
- the answer did not mention `minimal-behavior-spike`

Marker-suppression result status: `VERIFIED`.
Platform label for selected marker suppression: `Reproduced`.

The entire response is not labeled as exactly reproduced.

## Case D comparison

First Case D:

- both experiment markers were suppressed
- the response answered the general question
- the response explicitly mentioned `minimal-behavior-spike`
- the response summarized the experimental Skill behavior

Repeated Case D2:

- both experiment markers were suppressed
- the response answered the general question
- the response did not mention `minimal-behavior-spike`
- the answer was in Japanese

Conclusions:

- selected marker suppression was repeated and qualifies as `Reproduced`
- exact answer wording was not reproduced
- explicit mention of the selected Skill was not reproduced
- the degree of selected-Skill influence on unrelated answer content was inconsistent
- this content difference is directly `Observed`
- its cause remains `UNKNOWN`

Case D2 is not classified as a failure. The wording difference is recorded as `Observed`, not as `Changed since previous test`, because this record does not treat nondeterministic free-form answer wording as a load-bearing platform behavior change.

## Response-language observation

- the Case D2 request was written in English
- the response was in Japanese
- the response language difference was directly observed

The following remain `UNKNOWN`:

- whether the experimental Skill influenced language selection
- whether ChatGPT automatically adapted to user language
- whether account, workspace, conversation, model, or other context affected language
- whether the behavior is consistent
- whether a reusable Skill should encode or delegate language adaptation

This single observation is not a language-design validation. Language matching is not claimed as reproduced.

## Expected-versus-observed comparison

| Case | First result | Repeated result | Condition comparability | Result status | Platform label | Limitation or discrepancy |
| --- | --- | --- | --- | --- | --- | --- |
| Case B2 | `SPIKE_ACTIVE`<br>`token: ORBIT-7` | `SPIKE_ACTIVE`<br>`token: ORBIT-7` | Materially comparable controlled selected-Skill conditions after excluding the earlier non-comparable attempt. | VERIFIED | Reproduced | Exact output match; automatic invocation remains unverified. |
| Case C2 | `SPIKE_INPUT_REQUIRED` | `SPIKE_INPUT_REQUIRED` | Materially comparable controlled selected-Skill conditions. | VERIFIED | Reproduced | Exact output match; UI reasoning-duration indicator was not part of the output. |
| Case D2 | Both markers suppressed; general answer mentioned `minimal-behavior-spike` and summarized the selected experimental Skill. | Both markers suppressed; general answer did not mention `minimal-behavior-spike`; answer was in Japanese. | Materially comparable for selected marker suppression only. | Marker constraint: VERIFIED | Selected marker suppression: Reproduced | Exact wording and selected-Skill influence were not reproduced consistently; answer-content difference was observed and cause remains UNKNOWN. |

## Verified facts

- Cases B2, C2, and D2 were run in separate fresh ChatGPT Web conversations.
- GPT-5.6 Terra and light reasoning were visibly selected.
- `minimal-behavior-spike` was visibly attached for every formal case.
- Case B2 exactly repeated the first explicit-token output.
- Case C2 exactly repeated the first missing-token output.
- Case D2 suppressed both experiment markers.
- The first and repeated Case D differed in whether the response mentioned the selected Skill.
- The Case D2 response was in Japanese.
- Screenshots were reviewed but are not committed.

## Inferences

Inferred:

- the selected installed Skill likely influenced Cases B2 and C2 because the Skill pill was visible and the deterministic outputs aligned exactly with the package contract

This record does not infer exact internal prompt injection, internal instruction-loading implementation, automatic invocation, automatic routing, language-adaptation implementation, why Case D answer content differed, or exact installed artifact storage identity.

## Unknowns

- exact installed artifact identity: `UNKNOWN`
- internal parsing mechanism: `UNKNOWN`
- internal instruction-loading mechanism: `UNKNOWN`
- automatic invocation: `UNKNOWN`
- automatic trigger selection: `UNKNOWN`
- automatic non-trigger routing: `UNKNOWN`
- behavior when the Skill is installed but not attached: `UNKNOWN`
- exact Project-instruction state: `UNKNOWN`
- tool behavior: `UNKNOWN`
- connector behavior: `UNKNOWN`
- behavior across other models: `UNKNOWN`
- behavior across other reasoning settings: `UNKNOWN`
- consistent degree of selected-Skill influence on unrelated content: `UNKNOWN`
- reason for the Case D content difference: `UNKNOWN`
- reason for the Japanese Case D2 response: `UNKNOWN`
- stability of response-language adaptation: `UNKNOWN`
- persistence across devices or sessions: `UNKNOWN`

## Discrepancies

- an initial B2 attempt used non-comparable conditions and was excluded
- Case D marker suppression matched, but answer content differed
- the first Case D mentioned the selected Skill; Case D2 did not
- Case D2 answered in Japanese despite an English prompt
- exact installed artifact identity was not independently rehashed or revalidated

None of these discrepancies invalidate the reproduced marker and deterministic-output conclusions. They limit broader generalization.

## Limitations

- same-day first observation and repetition
- one owner
- one account context
- one product surface
- one visible model
- one reasoning setting
- selected Skill only
- no automatic invocation test
- no installed-but-unattached test
- no Project compatibility test
- no tools or connectors
- no supporting files
- no cross-device test
- no independent event log
- screenshots are not committed
- exact installed artifact identity was not independently recorded

This record does not claim statistical reliability.

## Reproduction decision

The following qualify as `Reproduced` under the recorded controlled conditions:

- selected explicit-token deterministic output
- selected missing-token deterministic output
- selected non-trigger marker suppression

The following do not qualify as reproduced findings:

- automatic invocation
- automatic trigger selection
- automatic non-trigger routing
- exact unrelated-answer wording
- consistent degree of selected-Skill influence
- language-adaptation behavior
- behavior across other models, settings, surfaces, Projects, devices, tools, or connectors

The package remains experimental. Reproduction does not make the package production-ready. No production Skill should be created from this result alone.

## Next experiment boundary

The smallest justified later experiment is to test installed-but-unattached behavior in fresh conversations to distinguish:

- selected Skill behavior
- installed-but-not-selected behavior
- automatic invocation or non-invocation evidence

Do not perform that experiment in this Issue. Language-policy design should be documented separately from platform-language behavior testing.
