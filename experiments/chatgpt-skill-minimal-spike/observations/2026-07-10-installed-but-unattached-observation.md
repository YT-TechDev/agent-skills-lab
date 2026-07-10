# Installed-but-Unattached Observation — 2026-07-10

This record documents the completed owner-side installed-but-unattached observation for GitHub Issue #20. It records only owner-reported product-side evidence from Issue #20 and Issue #20 comments. The product-side runs were not rerun, simulated, inferred, or invented for this repository change.

Source basis: GitHub Issue #20 raw owner comments as provided for this Issue, the repository package source, and the earlier selected-Skill observation records. Owner-provided pre-send and post-response screenshots were reviewed for evidence but are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Case E1 pre-send installed-but-unattached state | VERIFIED | Observed |
| Case E1 visible automatic Skill execution/loading | VERIFIED | Observed |
| Case E1 deterministic marker output | VERIFIED | Observed |
| Case E1 token preservation | VERIFIED | Observed |
| Case F1 pre-send installed-but-unattached state | VERIFIED | Observed |
| Case F1 absence of visible automatic Skill execution/loading | VERIFIED | Observed |
| Case F1 experiment-marker suppression | VERIFIED | Observed |
| Internal trigger-selection mechanism | UNKNOWN | Unverified |
| Internal non-trigger routing mechanism | UNKNOWN | Unverified |
| Installed-but-unattached reproduction | UNKNOWN | Unverified |
| Response-language mechanism | UNKNOWN | Unverified |

`Observed` applies only to the named visible behavior in these runs. Nothing in this installed-but-unattached experiment qualifies as `Reproduced`. Requirement/result statuses and platform labels are separate classifications. Visible execution evidence does not reveal internal routing implementation.

## Artifact identity

- package source revision: `1a6f91f8fd894b5df628d7e9098191c9254a6948`
- repository baseline: `e2d2a84de99a5d0ec75688ee14cfdc87d0be1afa`
- package path: `experiments/chatgpt-skill-minimal-spike/package/SKILL.md`
- Skill: `minimal-behavior-spike`
- token: `NOVA-11`
- observation date: `2026-07-10`

The already installed Skill was reused. It was not edited, renamed, reuploaded, reinstalled, or manually attached before either formal request. No independent installed-artifact hash was recorded. Exact stored-platform artifact identity remains `UNKNOWN`. This record is tied to the owner-reported unchanged installed Skill and the repository package source above.

## Controlled environment

- product surface: ChatGPT Web
- workspace surface: `Work`
- model: GPT-5.6 Terra
- reasoning: light, displayed as `軽`
- conversation isolation: separate fresh conversation for each case
- Project selection: no Project intentionally selected
- Skill state: installed
- manual Skill selection: no Skill manually selected
- pre-send Skill pill: no `minimal-behavior-spike` pill visible before either request
- evidence reviewed: owner-provided pre-send and post-response screenshots
- screenshot handling: screenshots are not committed

Exact Project-instruction state was not independently inspected. Tools and connectors were not evaluated.

## Case E1 — Installed but unattached explicit trigger

### Prompt

```text
Run the minimal behavior spike with token NOVA-11.
```

### Pre-send unattached evidence

The reviewed pre-send evidence showed:

- fresh conversation
- GPT-5.6 Terra visible
- light reasoning visible
- no Project selected
- no `minimal-behavior-spike` pill visible
- no Skill manually selected
- exact prompt visible before sending

Pre-send installed-but-unattached state: `VERIFIED` / `Observed`.

### Visible post-send UI

The visible post-send execution UI was:

```text
minimal-behavior-spike スキルを実行します。指定トークン NOVA-11 をそのまま入力として扱います。
```

The visible loading indicator was:

```text
スキルの読み込み
```

Visible automatic Skill execution/loading after sending: `VERIFIED` / `Observed`.

The platform-duration UI was recorded separately:

```text
18s考えました
```

The duration indicator was platform UI, not Skill output.

### Observed output

The final output was exactly:

```text
SPIKE_ACTIVE
token: NOVA-11
```

Exact deterministic output: `VERIFIED` / `Observed`.
Exact token preservation: `VERIFIED` / `Observed`.
Automatic Skill execution for this specific run: `Observed`.
Reproduction: not assigned.

### Interpretation boundaries

The evidence proves visible execution and loading indicators for this run. It does not establish that a persistent Skill pill appeared after execution.

The following remain `UNKNOWN`:

- internal trigger matching
- internal routing algorithm
- internal prompt injection
- instruction-loading implementation
- whether the same result will recur
- whether description, name, prompt wording, account context, or another signal caused selection

## Case F1 — Installed but unattached unrelated request

### Prompt

```text
Explain what a reusable agent Skill is.
```

### Pre-send unattached evidence

The reviewed pre-send evidence showed:

- fresh conversation
- GPT-5.6 Terra visible
- light reasoning visible
- no Project selected
- no `minimal-behavior-spike` pill visible
- no Skill manually selected
- exact prompt visible before sending

Pre-send installed-but-unattached state: `VERIFIED` / `Observed`.

### Observed response excerpt

The exact supported response excerpt was:

```text
再利用可能な Agent Skill は、特定の仕事を安定してこなすための「AI向け作業手順パッケージ」です。
```

The remaining response is recorded only at the level supported by the Issue #20 comment:

- it answered the general Agent Skill question
- it discussed examples
- it discussed `SKILL.md`
- it discussed possible supporting content
- it mentioned explicit `@skill-name` invocation
- it discussed reusable workflow principles
- it included a general statement that Codex/ChatGPT can judge relevance and automatically use a Skill

The general automatic-use statement was answer content, not visible execution evidence for this run.

### Visible execution and marker observations

Directly recorded observations:

- no visible automatic Skill attachment appeared
- no visible `minimal-behavior-spike` execution message appeared
- no visible `スキルの読み込み` indicator appeared
- `SPIKE_ACTIVE` did not appear
- `SPIKE_INPUT_REQUIRED` did not appear
- `minimal-behavior-spike` was not explicitly mentioned
- the response was in Japanese despite the English prompt

The platform-duration UI was recorded separately:

```text
23s考えました
```

Absence of visible automatic Skill execution/loading: `VERIFIED` / `Observed`.
Both marker constraints: `VERIFIED` / `Observed`.
Unrelated request answered normally: `VERIFIED` / `Observed`.
Internal Skill consideration/loading: `UNKNOWN` / Unverified.
Internal automatic non-trigger routing: `UNKNOWN` / Unverified.
Cause of Japanese response: `UNKNOWN` / Unverified.
Reproduction: not assigned.

Marker absence and lack of visible execution UI do not prove that the platform did not internally consider the Skill.

## Comparison with selected-Skill behavior

### Explicit trigger

Selected Case B2:

- Skill manually selected
- Skill pill visible before sending
- deterministic output reproduced

Installed-but-unattached Case E1:

- no Skill manually selected
- no Skill pill visible before sending
- visible automatic execution/loading appeared after sending
- deterministic output matched the package contract
- first installed-but-unattached observation only

Conclusion:

- selected deterministic output was already reproduced separately
- installed-but-unattached visible automatic execution was observed here for the first time
- do not label the unattached behavior `Reproduced`

### Unrelated request

Selected Case D2:

- Skill manually selected
- marker suppression reproduced
- general answer returned

Installed-but-unattached Case F1:

- no Skill manually selected
- no visible execution/loading appeared
- both markers were suppressed
- general answer returned

Conclusion:

- no visible automatic execution was observed for the unrelated request
- internal routing remains `UNKNOWN`
- do not call non-trigger routing reproduced or verified

## Response-language observation

- Case F1 used an English prompt
- the response was in Japanese
- this was directly observed
- the cause remains `UNKNOWN`

The following could have affected language selection but were not isolated:

- account context
- workspace context
- product surface
- model behavior
- previous user-language history
- host-platform behavior
- other hidden context

This is not proof that `minimal-behavior-spike` performed language adaptation. This is not validation of Principle 18. Repository language policy and platform-observed behavior remain separate.

## Verified facts

- the Skill remained installed
- it was not manually selected before either formal request
- no Skill pill was visible before either prompt
- both cases used separate fresh ChatGPT Web conversations
- GPT-5.6 Terra and light reasoning were visible
- Case E1 displayed a named Skill execution message
- Case E1 displayed a Skill-loading indicator
- Case E1 returned the exact deterministic output
- Case E1 preserved `NOVA-11`
- Case F1 displayed no visible Skill execution/loading indicator
- Case F1 suppressed both experiment markers
- Case F1 answered the general question in Japanese
- screenshots were reviewed but are not committed

## Inferences

Inferred:

- because no Skill was manually selected before Case E1 and the UI explicitly named and loaded `minimal-behavior-spike`, the platform automatically selected or invoked that installed Skill for this specific request

The invisible selection mechanics are `Inferred`; the visible execution/loading itself is directly `Observed`.

This record does not infer:

- the routing algorithm
- exact trigger matching implementation
- whether the frontmatter name or description was decisive
- prompt injection details
- persistent attachment state
- cross-session stability
- why Case F1 did not visibly execute the Skill
- why Case F1 answered in Japanese

## Unknowns

- exact installed artifact identity: `UNKNOWN`
- persistent post-response Skill attachment state: `UNKNOWN`
- internal trigger matching: `UNKNOWN`
- internal automatic-selection implementation: `UNKNOWN`
- internal instruction loading: `UNKNOWN`
- internal non-trigger consideration: `UNKNOWN`
- automatic non-trigger routing mechanism: `UNKNOWN`
- behavior reproducibility: `UNKNOWN`
- behavior across other prompts: `UNKNOWN`
- behavior across other models: `UNKNOWN`
- behavior across reasoning settings: `UNKNOWN`
- behavior in Projects: `UNKNOWN`
- behavior on other devices or surfaces: `UNKNOWN`
- response-language cause: `UNKNOWN`
- tool behavior: `UNKNOWN`
- connector behavior: `UNKNOWN`

## Discrepancies

- Case E1 visibly executed the Skill, while Case F1 did not.
- Case E1 had visible execution/loading UI; a persistent post-response Skill pill was not established.
- Case F1 returned Japanese prose from an English prompt.

## Limitations

- exact installed artifact identity was not independently rehashed
- screenshots are not committed
- only one explicit-trigger and one unrelated-request case were run
- both runs occurred on the same date
- one owner and one account context
- one product surface
- one workspace surface
- one model
- one reasoning setting
- no Project test
- no supporting files
- no tools or connectors
- no repetition of the installed-but-unattached cases

These limitations prevent reproduction claims or broad platform generalization.

## Observation decision

The following were `Observed` under the recorded conditions:

- an installed but manually unattached explicit request produced visible automatic Skill execution/loading
- the explicit request returned the exact deterministic package output
- the synthetic token was preserved exactly
- an installed but manually unattached unrelated request produced no visible Skill execution/loading
- the unrelated request suppressed both experiment markers and returned a general answer

The following were not established:

- reproduction of installed-but-unattached behavior
- permanent automatic invocation behavior
- internal routing implementation
- reliable automatic non-trigger behavior
- behavior across other prompts or environments
- language-adaptation behavior
- production readiness

The package remains experimental. No production Skill should be created from this observation alone.

## Next experiment boundary

The smallest justified later experiment is to repeat Cases E1 and F1 under the same controlled conditions with fresh conversations and the same exact prompts.

Purpose:

- determine whether the installed-but-unattached visible execution behavior can qualify as `Reproduced`
- determine whether absence of visible execution for the unrelated request repeats

Do not perform that experiment in this Issue. Do not expand to other models, Projects, tools, connectors, or supporting files yet.
