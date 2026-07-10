# Installed-but-Unattached Controlled Reproduction — 2026-07-10

This record documents the completed owner-side repetition of the installed-but-unattached `minimal-behavior-spike` experiment for GitHub Issue #22. It records repository evidence from Issue #22 and every Issue #22 comment as the primary raw evidence. The ChatGPT product-side runs were already complete; this repository change does not rerun, simulate, infer, or invent product behavior.

Source basis: GitHub Issue #22, every Issue #22 owner comment, the repository package source, and the earlier observation records. Screenshots were reviewed as evidence and are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Case E2 pre-send installed-but-unattached state | VERIFIED | Observed |
| Case E2 exact deterministic output | VERIFIED | Reproduced |
| Case E2 exact `NOVA-11` preservation | VERIFIED | Reproduced |
| Case E2 visible named Skill execution/loading | MISSING for comparison | Not observed |
| Case E1 visible execution/loading behavior | PARTIAL | Not reproduced by E2 |
| Case E2 persistent post-response Skill pill | NOT APPLICABLE | Not observed |
| Case F2 pre-send installed-but-unattached state | VERIFIED | Observed |
| Case F2 absence of visible named Skill execution/loading | VERIFIED | Reproduced |
| Case F2 `SPIKE_ACTIVE` suppression | VERIFIED | Reproduced |
| Case F2 `SPIKE_INPUT_REQUIRED` suppression | VERIFIED | Reproduced |
| Case F2 general question answered | VERIFIED | Reproduced |
| Case F2 exact free-form wording | PARTIAL | Observed difference |
| Automatic invocation mechanism | UNKNOWN | Unverified |
| Internal non-trigger routing | UNKNOWN | Unverified |
| Persistent automatic Skill attachment | UNKNOWN | Unverified |
| Response-language mechanism | UNKNOWN | Unverified |
| Production readiness | NOT APPLICABLE | Unverified |

`Reproduced` applies only to the named observable behaviors. Installed-but-unattached deterministic output was reproduced. Visible named execution/loading UI was not reproduced. F1/F2 visible non-trigger behavior was reproduced. Internal mechanisms were not reproduced or verified. Requirement statuses and platform labels remain separate classifications. The package remains experimental.

## Artifact identity

- package source revision: `1a6f91f8fd894b5df628d7e9098191c9254a6948`
- repository baseline: `522fa9200ccc8b4b4ef67ba6860d01bf714d6c8d`
- package path: `experiments/chatgpt-skill-minimal-spike/package/SKILL.md`
- Skill: `minimal-behavior-spike`
- token: `NOVA-11`
- date: `2026-07-10`

Artifact-identity boundaries:

- the already installed Skill was reused
- the Skill was not edited, renamed, reuploaded, reinstalled, removed, or manually attached
- no independent installed-artifact hash was recorded
- exact stored-platform artifact identity remains `UNKNOWN`
- the results are tied to the owner-reported unchanged installed Skill and the recorded repository source

This record does not overclaim artifact identity.

## Controlled environment

For the formal E2 and F2 cases, Issue #22 evidence records:

- product surface: ChatGPT Web on PC
- workspace surface: `Work`
- model: GPT-5.6 Terra
- reasoning setting: light, displayed as `軽`
- conversation isolation: separate fresh conversation for each formal case
- Project selection: no Project intentionally selected
- Skill installation state: Skill remained installed
- manual Skill selection: no Skill manually selected
- pre-send Skill pill: no `minimal-behavior-spike` pill visible before sending
- screenshots reviewed but not committed

Environment boundaries:

- exact Project-instruction state was not independently inspected
- tools and connectors were not evaluated
- no supporting files were evaluated
- no cross-device or cross-model result is included in the formal comparison

## Excluded non-comparable setup

Before the formal E2 run:

- the owner prepared the E2 prompt on a smartphone surface
- the visible model was GPT-5.6 Sol
- light reasoning was selected
- this differed from the fixed Issue #22 PC ChatGPT Web / GPT-5.6 Terra setup
- the prompt was not sent as a formal case
- no Skill behavior result was collected
- the owner returned to PC ChatGPT Web and used GPT-5.6 Terra for formal E2

Classification:

- excluded setup: `NOT APPLICABLE` to reproduction comparison
- no success or failure result
- no mobile or Sol behavior conclusion
- no cross-device evidence

This is not treated as a failed E2 case.

## Case E2 — Repeated installed-but-unattached explicit trigger

Exact prompt:

```text
Run the minimal behavior spike with token NOVA-11.
```

Formal pre-send evidence:

- fresh PC ChatGPT Web conversation
- `Work`
- GPT-5.6 Terra visible
- `軽` visible
- no Project selected
- no Skill manually selected
- no Skill pill visible
- exact prompt visible before sending

Exact final output:

```text
SPIKE_ACTIVE
token: NOVA-11
```

Platform-duration UI, recorded separately:

```text
14s考えました
```

The duration indicator was not Skill output.

Owner's explicit report:

- the output appeared after the reasoning state
- no named `minimal-behavior-spike` execution message was seen
- `スキルの読み込み` was not seen
- no other visible named Skill-loading indicator was seen
- no persistent post-response Skill pill was visible

Classifications:

- pre-send state: `VERIFIED` / `Observed`
- exact deterministic output: `VERIFIED` / `Reproduced`
- exact token preservation: `VERIFIED` / `Reproduced`
- visible named Skill execution/loading: `MISSING for E2 comparison` / Not observed
- E1 visible execution/loading behavior: `PARTIAL` / Not reproduced by E2
- persistent post-response pill: `NOT APPLICABLE` / Not observed
- automatic invocation mechanism: `UNKNOWN` / Unverified
- internal routing and instruction loading: `UNKNOWN` / Unverified

Case E2 reproduces the installed-but-unattached deterministic output under materially comparable pre-send conditions. Case E2 does not reproduce the visible named execution/loading UI observed in Case E1. The entire E1 behavior is not labeled reproduced. Deterministic output alone does not prove the internal invocation mechanism.

## Additional same-conversation observation

After the formal E2 result, the same prompt was later submitted a second time in the same conversation. The same exact deterministic output appeared again:

```text
SPIKE_ACTIVE
token: NOVA-11
```

This was not a fresh-conversation formal case. It is excluded from the formal E2 reproduction comparison and is recorded only as an additional same-conversation observation. It is not counted as an independent reproduction run and is not used to upgrade visible execution/loading behavior.

## Case F2 — Repeated installed-but-unattached unrelated request

Exact prompt:

```text
Explain what a reusable agent Skill is.
```

Formal pre-send evidence:

- fresh PC ChatGPT Web conversation
- `Work`
- GPT-5.6 Terra visible
- `軽` visible
- no Project selected
- no Skill manually selected
- no Skill pill visible
- exact prompt visible before sending

Observed answer-generation text:

```text
Skill の仕組みに沿って、再利用できるものとしての意味と実務での使い方を整理します。
```

This was visible answer-generation content. It was not a named `minimal-behavior-spike` execution message, was not `スキルの読み込み`, and was not evidence of named Skill execution.

Exact final response excerpt:

```text
再利用可能な Agent Skill は、AIに特定の仕事を毎回ぶれずに行わせるための「専門作業パッケージ」です。
```

The remainder is recorded only at the level supported by Issue #22 evidence:

- general examples
- `SKILL.md`
- supporting scripts and references
- explicit `@skill-name` invocation
- possible automatic selection in suitable cases
- reusable workflow value

Observed visible behavior and marker evidence:

- no visible named `minimal-behavior-spike` execution message
- no visible `スキルの読み込み`
- no other visible named Skill-loading indicator
- `SPIKE_ACTIVE` did not appear
- `SPIKE_INPUT_REQUIRED` did not appear
- `minimal-behavior-spike` was not explicitly mentioned
- no persistent Skill pill was visible
- the general question was answered
- the response was in Japanese

Duration UI:

```text
15s考えました
```

The duration UI was not part of the response contract.

Classifications:

- pre-send state: `VERIFIED` / `Observed`
- absence of visible named execution/loading: `VERIFIED` / `Reproduced`
- `SPIKE_ACTIVE` suppression: `VERIFIED` / `Reproduced`
- `SPIKE_INPUT_REQUIRED` suppression: `VERIFIED` / `Reproduced`
- general question answered: `VERIFIED` / `Reproduced`
- persistent post-response pill: `NOT APPLICABLE` / Not observed
- exact answer wording: `PARTIAL` / Observed difference
- internal Skill consideration/loading: `UNKNOWN` / Unverified
- automatic non-trigger routing mechanism: `UNKNOWN` / Unverified
- response-language mechanism: `UNKNOWN` / Unverified

## E1 versus E2 comparison

| Evidence | E1 | E2 | Decision |
| --- | --- | --- | --- |
| Skill manually selected before sending | No | No | Comparable |
| Pre-send Skill pill | Not visible | Not visible | Comparable |
| Exact prompt/token | Same | Same | Comparable |
| Exact deterministic output | Yes | Yes | Reproduced |
| Named Skill execution message | Visible | Not observed | Not reproduced |
| Named loading indicator | Visible | Not observed | Not reproduced |
| Persistent post-response pill | Not established | Not observed | UNKNOWN / not established |

Deterministic installed-but-unattached output repeated. Visible invocation UI did not repeat. UI presentation may be transient or variable, but the cause is `UNKNOWN`. The visible difference is recorded as an observed difference and as not reproduced by E2.

## F1 versus F2 comparison

| Evidence | F1 | F2 | Decision |
| --- | --- | --- | --- |
| Skill manually selected before sending | No | No | Comparable |
| Pre-send Skill pill | Not visible | Not visible | Comparable |
| Visible named Skill execution/loading | Not observed | Not observed | Reproduced visible behavior |
| `SPIKE_ACTIVE` | Suppressed | Suppressed | Reproduced |
| `SPIKE_INPUT_REQUIRED` | Suppressed | Suppressed | Reproduced |
| General question answered | Yes | Yes | Reproduced |
| Exact free-form wording | Different | Different | Not required / PARTIAL |
| Response language | Japanese | Japanese | Observed twice, mechanism UNKNOWN |

The visible non-trigger behavior materially repeated. This does not prove that the Skill was not internally considered and does not verify an internal non-trigger routing algorithm. Exact free-form wording is not reproduced. Response language remains outside the reproduction claim.

## Response-language observation

- F1 and F2 both used an English prompt.
- F1 and F2 both returned Japanese prose.
- This repetition was directly observed.

The following remain `UNKNOWN`:

- why Japanese was selected
- whether the Skill affected language choice
- whether account, workspace, prior history, model behavior, or hidden context affected it
- whether the behavior is stable
- whether the repository language policy had any effect

Language behavior is not labeled `Reproduced` in this experiment. Language validation was outside Issue #22 scope. Repository design policy and platform behavior remain separate.

## Verified facts

- E2 and F2 used separate fresh formal conversations.
- The fixed model and reasoning settings were visible.
- No Skill was manually selected.
- No Skill pill was visible before either formal prompt.
- E2 returned the exact deterministic output.
- E2 preserved `NOVA-11`.
- E2 did not visibly show named execution/loading UI.
- F2 did not visibly show named execution/loading UI.
- F2 suppressed both markers.
- F2 answered the general question.
- No persistent Skill pill was visible after either formal result.
- Screenshots were reviewed but not committed.
- The additional E2 same-conversation repeat was excluded from the formal comparison.
- The mobile/Sol preparation was excluded before formal execution.

## Inferences

- `Inferred`: because the installed Skill was not manually attached and E2 returned the exact package-contract output, the installed Skill may have influenced the result.

No inference is made about exact automatic-selection implementation, routing algorithm, frontmatter matching behavior, prompt injection, instruction-loading mechanism, persistent attachment, why visible UI differed between E1 and E2, why F2 did not visibly invoke the Skill, or why Japanese was selected.

## Unknowns

- exact stored installed-artifact identity: `UNKNOWN`
- internal trigger matching: `UNKNOWN`
- internal automatic-selection mechanism: `UNKNOWN`
- internal prompt or instruction loading: `UNKNOWN`
- whether E2 used the installed Skill internally: `UNKNOWN`
- reason visible execution/loading appeared in E1 but not E2: `UNKNOWN`
- persistent automatic attachment: `UNKNOWN`
- internal non-trigger consideration: `UNKNOWN`
- internal non-trigger routing: `UNKNOWN`
- response-language mechanism: `UNKNOWN`
- cross-model behavior: `UNKNOWN`
- mobile behavior: `UNKNOWN`
- cross-device behavior: `UNKNOWN`
- Project behavior: `UNKNOWN`
- supporting-file behavior: `UNKNOWN`
- tool behavior: `UNKNOWN`
- connector behavior: `UNKNOWN`
- production readiness: `NOT APPLICABLE`

## Discrepancies

- E1 showed visible named execution/loading UI; E2 did not.
- E1 and E2 nevertheless returned the same exact deterministic output.
- F1 and F2 returned different free-form wording.
- F1 and F2 both returned Japanese from an English prompt.
- No persistent Skill pill was observed.
- The formal E2 evidence includes one later same-conversation repeat that is excluded.
- A smartphone/Sol preparation was excluded before execution.

These discrepancies do not invalidate deterministic-output reproduction. They do prevent claiming visible invocation UI reproduction and limit broader automatic-routing conclusions.

## Limitations

- same-day observation and repetition
- one owner
- one account context
- one workspace
- one model
- one reasoning setting
- one PC Web surface
- exact installed artifact not independently hashed
- screenshots not committed
- only one formal fresh E2 and one formal fresh F2
- additional E2 repeat was not fresh
- no mobile result
- no other model
- no Project
- no supporting files
- no tools or connectors
- no independent platform logs
- no access to internal routing or loading state

No statistical reliability is claimed.

## Reproduction decisions

The following qualify as `Reproduced` under the recorded conditions:

- installed-but-unattached exact deterministic explicit-token output
- exact preservation of `NOVA-11`
- absence of visible named Skill execution/loading for the unrelated request
- suppression of `SPIKE_ACTIVE` for the unrelated request
- suppression of `SPIKE_INPUT_REQUIRED` for the unrelated request
- normal handling of the unrelated general question

The following do not qualify as reproduced:

- visible named automatic Skill execution/loading for the explicit trigger
- persistent Skill attachment
- internal automatic selection
- internal routing
- instruction loading
- exact unrelated-answer wording
- response-language behavior
- cross-device, mobile, Sol, Project, tool, connector, or supporting-file behavior
- production readiness

The package remains experimental. Partial reproduction does not make it production-ready. No production Skill should be created from this result alone.

## Next experiment boundary

The smallest separate later experiment is to create a new minimal supporting-file loading spike that tests whether an installed Skill can reliably access one static supporting file.

That future experiment should be separately scoped and must not modify the existing tested package or existing observation records. This Issue does not implement that experiment and does not create the next Issue.
