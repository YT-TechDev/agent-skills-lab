# Precommitted Expected Results

These expectations are recorded before owner-side product testing. They precommit the outside-Project control and active-Project interaction cases separately. This file contains no observed results, and no owner-side product experiment has been run by this repository change.

Keep requirement/result statuses separate from platform labels.

## Case A — Outside-Project control

Purpose:

Test the selected Skill fallback when no Project is intentionally selected.

Exact prompt:

```text
Run the project context interaction spike.
```

Environment:

- fresh conversation
- no Project intentionally selected
- Skill explicitly selected
- Skill pill visible
- fixed model and reasoning settings

Exact expected output:

```text
PROJECT_CONTEXT_UNAVAILABLE
```

Exact-result classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`

Boundary:

- the Project token was not obtained under the recorded outside-Project conditions
- do not infer how Project context is omitted, assembled, or represented internally

## Case B — Active Project interaction

Purpose:

Test whether the explicitly selected Skill can use one synthetic value supplied through active Project instructions.

Exact prompt:

```text
Run the project context interaction spike.
```

Environment:

- fresh conversation inside a temporary Project
- the active Project instructions field contains exactly the contents of `project-instructions.md`
- no Project files or knowledge attachments are used
- Skill explicitly selected
- Skill pill visible
- fixed model and reasoning settings

Exact expected output:

```text
PROJECT_CONTEXT_ACTIVE
project: LYRA-42
```

Exact-result classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`

Boundary:

- the result is evidence consistent with interaction between the active Project instructions and the selected Skill
- it does not prove precedence, parsing, prompt composition, context assembly, Project storage, or Skill-loading implementation
- the first run is `Observed`, not `Reproduced`

## Any other output

- preserve the exact output
- classify with `PARTIAL`, `MISSING`, or `UNKNOWN` as supported
- do not force ambiguous output into success or fallback
- keep requirement/result statuses separate from platform labels

## Prompt separation

The exact prompt for both cases is:

```text
Run the project context interaction spike.
```

The prompt must contain none of:

- `PROJECT_CONTEXT_ACTIVE`
- `PROJECT_CONTEXT_UNAVAILABLE`
- `LYRA-42`
