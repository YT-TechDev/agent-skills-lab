# Precommitted Expected Results

These expectations are recorded before owner-side testing. All platform behavior remains Unverified. This file contains no observed results. Observed results must be recorded in a separate later change.

## Case A: Package acceptance

Purpose:

Test whether the platform accepts or exposes the hypothesized package.

Expected platform result:

- acceptance or rejection should be observable through the supported workflow
- no specific acceptance outcome is assumed

Evidence status:

Unverified

Package acceptance alone does not prove correct invocation.

## Case B: Explicit token invocation

Prompt:

Run the minimal behavior spike with token ORBIT-7.

Expected Skill output:

```text
SPIKE_ACTIVE
token: ORBIT-7
```

Expected platform behavior:

- explicit owner-selected use or other visible invocation evidence should be recorded separately when available

Evidence status:

Unverified

Matching output alone does not prove platform invocation.

## Case C: Missing token

Prompt:

Run the minimal behavior spike.

Expected Skill output:

```text
SPIKE_INPUT_REQUIRED
```

Evidence status:

Unverified

## Case D: Non-trigger request

Prompt:

Explain what a reusable agent Skill is.

Expected output constraint:

- output must not contain SPIKE_ACTIVE
- output must not contain SPIKE_INPUT_REQUIRED

Evidence status:

Unverified

Marker absence does not by itself prove that the platform did not load or consider the Skill.

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
