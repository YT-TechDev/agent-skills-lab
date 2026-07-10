# Precommitted Expected Results

These expectations are recorded before owner-side testing. All platform behavior remains Unverified. This file contains no observed results. Observed results must be recorded in a separate later change.

## Case A: Package acceptance

Purpose:

Test whether the platform accepts, rejects, exposes, or transforms the hypothesized package.

Prompt or test input:

The exact reviewed package from the identified commit.

Expected platform behavior:

- an acceptance, rejection, transformation, or inaccessible-workflow result should be recordable
- no particular acceptance outcome is assumed

Expected Skill output:

NOT APPLICABLE. This case evaluates package handling rather than Skill response output.

Evidence needed:

- exact tested commit
- exact package contents or hash where practical
- product surface
- dated owner-facing acceptance, rejection, transformation, or inaccessible-workflow evidence
- sanitized screenshot or written observation where safe

What cannot be concluded from output alone:

- acceptance does not prove invocation
- rejection does not automatically prove the Skill instructions are invalid
- repository presence does not prove platform availability

Current evidence classification:

Unverified

## Case B: Explicit token invocation

Purpose:

Test deterministic token-preserving behavior during an explicit owner-run invocation.

Prompt or test input:

Run the minimal behavior spike with token ORBIT-7.

Expected platform behavior:

- the owner explicitly selects or invokes the experiment through the tested workflow
- visible invocation evidence should be recorded where the platform provides it

Expected Skill output:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Evidence needed:

- exact prompt
- exact output
- tested commit and package contents
- date and environment
- visible Skill selection or invocation evidence where available

What cannot be concluded from output alone:

- matching text alone does not prove host-platform Skill invocation
- one successful run does not establish reproduction

Current evidence classification:

Unverified

## Case C: Missing token

Purpose:

Test deterministic missing-input behavior during an explicit owner-run invocation without a token.

Prompt or test input:

Run the minimal behavior spike.

Expected platform behavior:

- the same explicit owner-selected experiment workflow is used without supplying a token
- visible invocation evidence should be recorded where available

Expected Skill output:

```text
SPIKE_INPUT_REQUIRED
```

Evidence needed:

- exact prompt
- exact output
- tested commit
- date and environment
- invocation evidence where available

What cannot be concluded from output alone:

- matching output alone does not prove platform invocation
- failure to return the marker does not by itself identify whether the package, workflow, platform, or instruction interpretation failed

Current evidence classification:

Unverified

## Case D: Non-trigger request

Purpose:

Test marker suppression for an unrelated request.

Prompt or test input:

Explain what a reusable agent Skill is.

Expected platform behavior:

- no experiment-specific marker should appear for this unrelated request
- do not assume the platform did or did not load, inspect, or consider the Skill

Expected Skill output or output constraint:

- must not contain SPIKE_ACTIVE
- must not contain SPIKE_INPUT_REQUIRED

Evidence needed:

- exact prompt
- full relevant output
- tested commit
- date and environment
- any available platform evidence concerning Skill selection or invocation

What cannot be concluded from output alone:

- marker absence does not prove that the Skill was not loaded or considered
- a normal answer does not by itself prove correct non-trigger routing

Current evidence classification:

Unverified

## Expected discrepancy categories

- package rejected
- package transformed
- Skill unavailable
- no visible invocation evidence
- marker missing
- token altered
- incorrect missing-input behavior
- experiment marker emitted for non-trigger case
- inconsistent behavior across repeated runs
- inaccessible platform evidence

No results are assigned to any discrepancy category in this precommitted expected-results document.
