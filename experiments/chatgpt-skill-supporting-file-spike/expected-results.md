# Precommitted Expected Results

These expectations are recorded before owner-side product testing. All platform behavior remains Unverified. This file contains no observed results. Observed results must be recorded in a separate later change.

## Case A: Package handling

Purpose:

Determine whether the owner-facing workflow accepts, rejects, transforms, or cannot access the two-file package.

Prompt or input:

The exact reviewed package from the identified commit.

Precommitted outcome policy:

- no package-handling outcome is assumed
- acceptance does not prove supporting-file access
- rejection does not automatically prove that `SKILL.md` is invalid
- standalone `SKILL.md` acceptance without the supporting file does not satisfy the experiment

Evidence needed:

- exact tested commit
- package tree or hash where practical
- product surface
- date
- owner-facing workflow
- acceptance, rejection, transformation, or inaccessible result
- safe visible evidence where available

What cannot be concluded:

- package acceptance does not prove invocation
- package acceptance does not prove supporting-file access
- rejection does not identify a specific invalid instruction
- repository presence does not prove platform availability

Current evidence classification:

```text
Unverified
```

## Case B: Explicit selected supporting-file run

Purpose:

Test whether the explicitly selected Skill can obtain the deterministic payload from the static supporting file.

Exact prompt:

```text
Run the supporting-file loading spike.
```

Fixed environment:

- ChatGPT Web on PC
- workspace `Work`
- GPT-5.6 Terra
- reasoning light / `軽`
- fresh conversation
- no Project intentionally selected
- Skill explicitly selected and visible as a pill

The prompt must not contain the success marker or payload.

### Success-output result

Expected exact output:

```text
SUPPORT_FILE_ACTIVE
payload: POLARIS-23
```

Classification policy:

- requirement status: `VERIFIED` when exact
- first platform label: `Observed`
- not `Reproduced`
- the result is evidence consistent with supporting-file access under the recorded conditions
- do not claim a specific parser, path-resolution implementation, prompt injection, or file-loading mechanism

### Explicit fallback result

Expected exact fallback:

```text
SUPPORT_FILE_UNAVAILABLE
```

Classification policy:

- record that the required supporting payload was not obtained under the recorded conditions
- platform label: `Observed`
- do not infer whether the cause was packaging, transformation, path resolution, file access, instruction interpretation, or another factor
- do not call it a permanent platform limitation

### Other result

Classification policy:

- preserve the exact output
- use `PARTIAL`, `MISSING`, or `UNKNOWN` as supported
- record visible Skill and package evidence
- do not force the result into success or fallback
- do not infer hidden mechanisms

Evidence needed:

- exact tested commit
- exact package contents or hash where practical
- package-handling result
- exact prompt
- exact output
- date and fixed environment
- visible selected Skill pill
- visible loading or file indicators where available
- warnings, fallback text, or transformations
- safe screenshots or written notes where useful

What cannot be concluded from output alone:

- package acceptance does not prove file loading
- success output does not prove a particular internal implementation
- fallback output does not identify the failure cause
- marker absence does not prove the supporting file was never considered
- one run does not establish reproduction
- behavior cannot be generalized to other models, devices, Projects, tools, connectors, or package shapes

Current evidence classification:

```text
Unverified
```

## Expected discrepancy categories

- package rejected
- workflow inaccessible
- package transformed
- supporting file omitted
- Skill unavailable
- Skill not selectable
- no visible invocation evidence
- exact success payload returned
- explicit unavailable fallback returned
- partial payload returned
- payload altered
- additional output added
- wrong file content returned
- ambiguous result
- inaccessible evidence
- inconsistent later repetition

No discrepancy category is assigned in this preparation change.
