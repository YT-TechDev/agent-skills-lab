# ChatGPT Skill Project-Context Interaction Spike

## Status

- maturity: experimental
- current evidence: unverified
- repository package preparation: complete after this change
- owner-side product experiment: not run by this change
- production readiness: not applicable

## Experiment question

Can an explicitly selected experimental Skill return one exact synthetic value supplied only through active Project instructions, while returning a deterministic fallback outside a Project?

## Scope

- one minimal ChatGPT Skill package
- one synthetic Project-instruction fixture outside the package
- explicit owner-selected invocation only
- outside-Project control case
- active-Project interaction case
- exact-output behavior classification

## Package boundary

```text
package/
└── SKILL.md
```

The package contains exactly one file. The package must not contain the Project-instruction fixture or the synthetic token.

## Project-instruction fixture boundary

`project-instructions.md` is a repository experiment fixture for a later temporary Project. It remains outside `package/` and is not part of the installed Skill package.

## Runtime token-separation rule

The synthetic token may appear in repository experiment documentation and the Project-instruction fixture to precommit expected results. It must not appear in `package/SKILL.md`, in the installed package, or in the later manual user prompt.

## Skill behavior contract

When the user explicitly asks to run the Project context interaction spike, the selected Skill should:

- locate a `project-token` supplied by active Project instructions
- preserve the token exactly
- return exactly the active marker and token when available
- return exactly the unavailable marker when no active Project token can be located
- add no heading, explanation, code fence, prefix, suffix, or other text

For unrelated requests, it must not output either experiment marker and must not disclose a Project token.

## Fixed owner-side environment

Use the same fixed environment for both cases:

- ChatGPT Web on PC
- workspace `Work`
- GPT-5.6 Terra
- reasoning `軽`
- separate fresh conversation for each case
- `project-context-interaction-spike` explicitly selected
- selected Skill pill visible before sending
- no tools or connectors intentionally used

Exact prompt for both cases:

```text
Run the project context interaction spike.
```

The prompt must contain none of:

- `PROJECT_CONTEXT_ACTIVE`
- `PROJECT_CONTEXT_UNAVAILABLE`
- `LYRA-42`

## Case A outside-Project control

Run the exact prompt in a fresh conversation with no Project intentionally selected. The expected exact output is the unavailable marker recorded in `expected-results.md`.

## Case B active-Project interaction

Create or use a temporary Project whose Project instructions field contains exactly the contents of `project-instructions.md`. Do not upload `project-instructions.md` as a Project file or knowledge attachment. Run the exact prompt in a fresh conversation inside that Project with the Skill explicitly selected. The expected exact output is the active marker and synthetic token recorded in `expected-results.md`.

## Evidence to capture

- exact tested commit
- exact package tree or hash where practical
- exact Project instructions field contents used for Case B
- confirmation that no Project files or knowledge attachments were used
- product surface, workspace, model, and reasoning setting
- separate fresh conversation per case
- visible selected Skill pill before sending
- exact prompt
- exact output
- whether tools or connectors were intentionally used
- sanitized textual evidence for the repository record
- owner-side screenshots may be reviewed privately or in the working conversation when useful, but must never be committed

## Status and platform-label separation

Keep requirement/result statuses such as `VERIFIED`, `PARTIAL`, `MISSING`, and `UNKNOWN` separate from platform labels such as `Observed` or `Reproduced`. The first owner-side run, if performed later, is `Observed`, not `Reproduced`.

## Interpretation boundaries

A matching active-Project output is evidence consistent with interaction between active Project instructions and the selected Skill. It does not prove precedence, parsing, prompt composition, context assembly, Project storage, Skill-loading implementation, or behavior in other environments.

A fallback output outside a Project shows only that the Project token was not obtained under the recorded outside-Project conditions. It does not prove how Project context is omitted, assembled, or represented internally.

## Stopping conditions

Stop and record the limitation when:

- the Skill cannot be selected
- the selected Skill pill is not visible before sending
- the temporary Project instructions field cannot be configured with exactly the fixture contents
- the fixture is uploaded as a Project file or knowledge attachment
- the fixed model, reasoning, workspace, or product surface is unavailable
- the prompt accidentally includes a marker or token
- tools or connectors are used unintentionally
- evidence cannot be recorded safely
- results are contradictory or ambiguous

## Safety and privacy constraints

- use only the synthetic token in the fixture
- do not include secrets, credentials, personal information, private URLs, or private repository content
- do not commit AI conversation, task, or session-sharing URLs
- use sanitized textual evidence as the repository record
- owner-side screenshots may be reviewed privately or in the working conversation
- do not commit screenshots in this preparation PR or any later observation PR
- do not add generated platform files or archives
- capture only the minimum evidence needed later

## Next experiment boundary

A later separate change may record owner-side observations for these two cases. Do not add an observation file, production Skill, automation, tools, connectors, or broader Project-instruction tests in this preparation change.

## Non-goals

- owner-side Project run in this change
- observed-result claim in this change
- instruction-precedence test
- internal prompt or context assembly test
- tools or connectors
- Project file or knowledge-attachment testing
- supporting package files
- screenshots or archives
- production Skill work
- CI, scripts, dependencies, or automation
