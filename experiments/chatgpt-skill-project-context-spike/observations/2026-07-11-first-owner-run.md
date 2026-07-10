# First Owner-Side Project-Context Observation — 2026-07-11

This record documents the first reviewed owner-side observation for the Project-instruction interaction spike for GitHub Issue #33. It records evidence only; it does not rerun, simulate, reinterpret, or invent ChatGPT product behavior.

Source basis: Issue #33 owner-provided observation evidence, repository files at the tested baseline, and the sanitized owner-side evidence reviewed for this closeout. Screenshots, archives, private URLs, generated platform files, browser metadata, local absolute paths, and conversation or Project identifiers are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Package upload accepted | VERIFIED | Observed |
| Package-handling classification: `accepted` | VERIFIED | Observed |
| Case A exact outside-Project fallback | VERIFIED | Observed |
| Case B exact active-Project output | VERIFIED | Observed |
| Project-instruction interaction | PARTIAL | Observed |
| Owner-confirmed runtime constraints | VERIFIED | Unverified |
| Reproduction | MISSING | Unverified |
| Internal mechanisms | UNKNOWN | Unverified |
| Production readiness | NOT APPLICABLE | Unverified |

`Observed` applies only to visible owner-side platform evidence from this first controlled run. This record is not `Reproduced`. Requirement/result statuses and platform observation labels are separate classifications.

## Maturity and production-readiness status

- maturity: experimental behavior-discovery evidence
- production readiness: `NOT APPLICABLE`
- production Skill claim: none
- reproduction status: not established
- internal mechanism status: `UNKNOWN`

## Tested baseline and artifact identities

- tested repository baseline: `9ef7475493fdd7d4d1ded40bbe8c399c78cfbbfc`
- package path: `experiments/chatgpt-skill-project-context-spike/package/`
- package tree:

```text
package/
└── SKILL.md
```

- Skill name: `project-context-interaction-spike`
- expected and owner-observed `SKILL.md` blob/hash: `c4b1bcd9255331039acd37ef20590ae7f82f80ef`
- fixture path: `experiments/chatgpt-skill-project-context-spike/project-instructions.md`
- fixture blob SHA: `0c61cd1b2baa3fc9f1ea35ae4024c892e77f3303`

Owner-confirmed local packaging facts:

- the owner updated local `main` before packaging
- the owner verified the package contained exactly one root-level `SKILL.md`
- the owner verified the source hash matched the committed artifact

These local packaging facts are recorded as owner confirmation, not as independently rerun validation of the owner environment in this repository change.

## Package-handling result

Visible package-handling evidence:

- ZIP upload was visibly accepted
- ChatGPT displayed that the Skill was uploaded
- package-handling classification: `accepted`

Classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`

Boundaries:

- no visible package transformation was inspected or confirmed
- internal package-loading behavior remains `UNKNOWN`
- upload acceptance does not prove the internal package representation
- upload acceptance does not prove the internal Skill-loading mechanism
- package acceptance alone is not treated as proof of runtime Project-instruction interaction

## Environment

Fixed tested environment for both cases:

- test date: `2026-07-11`
- product surface: ChatGPT Web on PC
- workspace: `Work`
- model: GPT-5.6 Terra
- reasoning: light, displayed as `軽`
- Skill: `project-context-interaction-spike`
- Skill selection: explicitly selected before each send
- Skill pill: visibly present before each send
- conversation state: separate fresh conversation for each case
- prompt handling: exact prompt preserved

## Exact prompt

Exact prompt in both cases:

```text
Run the project context interaction spike.
```

The prompt contained none of:

- `PROJECT_CONTEXT_ACTIVE`
- `PROJECT_CONTEXT_UNAVAILABLE`
- `LYRA-42`

## Case A — Outside-Project control

Observed pre-send conditions:

- fresh conversation
- workspace `Work`
- GPT-5.6 Terra
- reasoning `軽`
- no Project selected
- explicit Skill pill visible
- exact prompt visible

Exact observed output:

```text
PROJECT_CONTEXT_UNAVAILABLE
```

Classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`

Interpretation:

- the required Project token was not obtained under the recorded outside-Project conditions
- this result does not identify how Project context was omitted, assembled, or represented internally

## Case B — Active Project instructions

Observed pre-send conditions:

- fresh conversation inside temporary isolated Project `skills-test`
- Project instructions field visibly contained the committed fixture text
- no Project files or knowledge attachments were visible
- workspace `Work`
- GPT-5.6 Terra
- reasoning `軽`
- explicit Skill pill visible
- exact prompt visible

Exact observed output:

```text
PROJECT_CONTEXT_ACTIVE
project: LYRA-42
```

Classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`

Interpretation:

- the result is evidence consistent with interaction between active Project instructions and the explicitly selected Skill under the recorded conditions
- this is the first observed active-Project result
- this first run is not labeled `Reproduced`
- this result does not identify the exact internal route by which the token reached the response

## Expected-versus-observed comparison

| Case | Expected behavior | Observed behavior | Result status | Platform label | Boundary |
| --- | --- | --- | --- | --- | --- |
| Package handling | Record acceptance, rejection, transformation, or inaccessible result without treating acceptance as runtime proof. | ZIP upload was visibly accepted and ChatGPT displayed that the Skill was uploaded. | VERIFIED | Observed | No visible package transformation was inspected or confirmed; internal package loading remains `UNKNOWN`. |
| Case A — Outside-Project control | `PROJECT_CONTEXT_UNAVAILABLE` | `PROJECT_CONTEXT_UNAVAILABLE` | VERIFIED; exact match | Observed | Shows only that the Project token was not obtained under recorded outside-Project conditions. |
| Case B — Active Project instructions | `PROJECT_CONTEXT_ACTIVE`<br>`project: LYRA-42` | `PROJECT_CONTEXT_ACTIVE`<br>`project: LYRA-42` | VERIFIED; exact match | Observed | Evidence consistent with Project-instruction interaction; not internal proof and not reproduction. |
| Reproduction | A later materially comparable run would be needed. | No second active-Project run is recorded. | MISSING | Unverified | First run only; do not label either runtime result `Reproduced`. |
| Internal mechanisms | Do not claim precedence, prompt construction, parsing, context assembly, storage, loading, or route. | No internal mechanism was directly visible or independently verified. | UNKNOWN | Unverified | Supported conclusion remains limited to evidence consistent with interaction. |

## Directly observed facts

- ZIP upload was visibly accepted.
- ChatGPT displayed that the Skill was uploaded.
- ChatGPT Web on PC was used.
- Workspace `Work` was visible.
- GPT-5.6 Terra was visible.
- Reasoning was displayed as `軽`.
- The Skill `project-context-interaction-spike` was explicitly selected before each send.
- The Skill pill was visibly present before each send.
- A separate fresh conversation was used for each case.
- The exact prompt was visible and preserved in each case.
- Case A had no Project selected.
- Case A returned exactly `PROJECT_CONTEXT_UNAVAILABLE`.
- Case B was inside temporary isolated Project `skills-test`.
- Case B Project instructions field visibly contained the committed fixture text.
- Case B had no visible Project files or knowledge attachments.
- Case B returned exactly:

```text
PROJECT_CONTEXT_ACTIVE
project: LYRA-42
```

- Visible Project settings showed memory: `Default`.
- Visible Project settings showed library access: `Enabled`.

## Owner-confirmed facts

These facts are recorded separately from directly visible platform facts.

| Fact | Requirement/result status | Platform label | Evidence basis |
| --- | --- | --- | --- |
| Tools and connectors were not intentionally used. | VERIFIED | Unverified | Owner confirmation |
| Case B was the first response with no prompt edit or resend. | VERIFIED | Unverified | Owner confirmation |
| No Project files or knowledge attachments were added. | VERIFIED | Unverified | Owner confirmation |
| Local `main` was updated before packaging. | VERIFIED | Unverified | Owner confirmation |
| The package contained exactly one root-level `SKILL.md`. | VERIFIED | Unverified | Owner confirmation |
| The source hash matched the committed artifact. | VERIFIED | Unverified | Owner confirmation |

These owner-confirmed facts are not described as independently verified runtime integrity evidence.

## Reasonable inference

The Case B output is evidence consistent with interaction between active Project instructions and the explicitly selected Skill under the recorded conditions because:

- the prompt did not contain `PROJECT_CONTEXT_ACTIVE`, `PROJECT_CONTEXT_UNAVAILABLE`, or `LYRA-42`
- the Project instructions field visibly contained the committed fixture text
- the selected Skill pill was visibly present before sending
- the exact active marker and synthetic token were returned
- the outside-Project control returned the exact unavailable marker under the recorded control conditions

This inference does not prove internal prompt construction, instruction precedence, parsing behavior, context assembly, hidden context representation, Project storage mechanism, Skill loading implementation, or the exact internal route by which the token reached the response.

## Unknowns

- instruction precedence: `UNKNOWN`
- internal prompt construction: `UNKNOWN`
- parsing behavior: `UNKNOWN`
- context assembly: `UNKNOWN`
- hidden context representation: `UNKNOWN`
- Project storage mechanism: `UNKNOWN`
- Skill loading implementation: `UNKNOWN`
- exact internal route by which the token reached the response: `UNKNOWN`
- whether memory, library access, tools, or connectors contributed to the output: `UNKNOWN`
- whether enabled library access was actually used: `UNKNOWN`
- whether the result will recur in a later materially comparable run: `UNKNOWN`
- behavior in other products, workspaces, models, reasoning settings, Projects, package shapes, or unselected invocation: `UNKNOWN`

## Limitations

- Visible Project settings showed memory `Default` and library access `Enabled`.
- The Project instructions field is not claimed to be the only possible internal context source.
- Complete context isolation is not claimed.
- Enabled library access is not claimed to have been used.
- Memory, library, tools, or connectors are not claimed to have contributed to the output.
- Tools and connectors not being intentionally used is owner-confirmed, not independently verified runtime integrity evidence.
- No visible package transformation was inspected or confirmed.
- Package acceptance is not treated as proof of internal package representation or loading behavior.
- No second active-Project run was performed or recorded.
- This first run is not reproduction.
- Production readiness is `NOT APPLICABLE`.

## Privacy and evidence handling

This repository record uses sanitized text only. It does not include screenshots, ZIP or `.skill` archives, private URLs, ChatGPT conversation/session/task-sharing URLs, Project URLs, personal information, generated platform files, browser metadata, local absolute paths, or private conversation identifiers.

## Next experiment boundary

A later separate change may record a second materially comparable active-Project run or a narrower isolation test. This observation does not add production Skill work, automation, tools, connectors, CI, dependencies, Project file tests, knowledge-attachment tests, or internal mechanism claims.
