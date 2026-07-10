# Controlled Supporting-File Reproduction — 2026-07-10

This record documents the reviewed owner-side controlled repetition of the explicitly selected `supporting-file-loading-spike` behavior for GitHub Issue #28. It records evidence documentation only; it does not rerun, simulate, reinterpret, or invent ChatGPT product behavior.

Source basis: GitHub Issue #28 and its precommitted classification policy, the existing first observation and repository package files, and the sanitized owner-side evidence reviewed for this closeout. Screenshots are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Pre-send explicit Skill selection and visible pill | VERIFIED | Observed |
| Exact prompt supplied | VERIFIED | Observed |
| Exact deterministic two-line selected output | VERIFIED | Reproduced |
| Absence of heading, explanation, code fence, prefix, suffix, warning, fallback, or visible error | VERIFIED | Reproduced |
| Owner confirmation of no reupload, reinstall, edit, rename, or replacement | VERIFIED | Unverified |
| Package acceptance | NOT APPLICABLE | Unverified |
| Package-detail supporting-file retention | NOT APPLICABLE | Unverified |
| Internal parser behavior | UNKNOWN | Unverified |
| Relative-path resolution implementation | UNKNOWN | Unverified |
| Internal storage behavior | UNKNOWN | Unverified |
| Prompt construction or prompt injection | UNKNOWN | Unverified |
| File-loading implementation | UNKNOWN | Unverified |
| Runtime package extraction | UNKNOWN | Unverified |
| Loading indicator such as `スキルの読み込み` | UNKNOWN | Unverified |
| Response-duration UI | UNKNOWN | Unverified |
| Production readiness | NOT APPLICABLE | Unverified |

`Reproduced` applies only to the exact deterministic selected output and the absence of additional response text, warning, fallback, or visible error under the recorded materially comparable conditions. Setup and comparability facts are classified as `Observed`, not `Reproduced`. Requirement/result statuses and platform labels are separate classifications.

## Tested artifact and first-observation identity

- repository baseline before this observation: `5f77aeea2de4cbfd90d44283265210e2cd228734`
- tested package source revision: `433299c4ddb62dc4666d8beab1fcbb5cdac361d3`
- experiment path: `experiments/chatgpt-skill-supporting-file-spike/`
- package path: `experiments/chatgpt-skill-supporting-file-spike/package/`
- first observation: `experiments/chatgpt-skill-supporting-file-spike/observations/2026-07-10-first-owner-run.md`
- installed Skill: `supporting-file-loading-spike`
- controlled reproduction observation date: `2026-07-10`

The first observation recorded the same selected prompt returning exactly:

```text
SUPPORT_FILE_ACTIVE
payload: POLARIS-23
```

That first selected-run result was classified as requirement/result status `VERIFIED`, platform label `Observed`, and reproduction not established.

## Owner-confirmed artifact continuity

The owner confirmed that after the first run the Skill was not:

- reuploaded
- reinstalled
- edited
- renamed
- replaced

This record treats that statement as owner-confirmed artifact continuity for this controlled repetition. It is not a cryptographic verification, independent installed-artifact hash, independent runtime integrity verification, or proof of exact internal platform storage identity.

## Controlled environment

- product surface: ChatGPT Web on PC
- workspace: `Work`
- model: GPT-5.6 Terra
- reasoning: light, visibly displayed as `軽`
- conversation: fresh
- Project: not intentionally selected
- Skill: `supporting-file-loading-spike`
- Skill selection: explicitly selected
- pre-send state: selected Skill pill visibly present before sending

No package upload, reinstall, edit, rename, replacement, or package-detail retest is recorded for this controlled reproduction.

## Exact prompt and output

Exact prompt:

```text
Run the supporting-file loading spike.
```

The prompt did not contain:

- `SUPPORT_FILE_ACTIVE`
- `POLARIS-23`

Exact observed output:

```text
SUPPORT_FILE_ACTIVE
payload: POLARIS-23
```

Output evidence:

- exact two-line match
- no heading
- no explanation
- no code fence
- no prefix
- no suffix
- no warning
- no fallback
- no visible error
- the submitted user message visibly showed the named Skill
- a persistent Skill pill was not visible in the composer after the response
- a loading indicator such as `スキルの読み込み` was not captured and remains `UNKNOWN`
- response-duration UI was not captured and remains `UNKNOWN`

## First-versus-repeated comparison

| Compared item | First owner-side observation | Controlled repetition | Result status | Platform label |
| --- | --- | --- | --- | --- |
| Installed Skill name | `supporting-file-loading-spike` | `supporting-file-loading-spike` | VERIFIED | Observed |
| Pre-send explicit Skill selection and visible pill | Selected Skill pill visibly present before sending | Selected Skill pill visibly present before sending | VERIFIED | Observed |
| Prompt | `Run the supporting-file loading spike.` | `Run the supporting-file loading spike.` | VERIFIED | Observed |
| Prompt excludes success marker and payload | Excluded `SUPPORT_FILE_ACTIVE` and `POLARIS-23` | Excluded `SUPPORT_FILE_ACTIVE` and `POLARIS-23` | VERIFIED | Observed |
| Exact output | `SUPPORT_FILE_ACTIVE`<br>`payload: POLARIS-23` | `SUPPORT_FILE_ACTIVE`<br>`payload: POLARIS-23` | VERIFIED | Reproduced |
| Extra response text | None recorded | None recorded | VERIFIED | Reproduced |
| Loading indicator such as `スキルの読み込み` | Not captured; `UNKNOWN` | Not captured; `UNKNOWN` | UNKNOWN | Unverified |
| Response-duration UI | Captured separately as `19s考えました` | Not captured; `UNKNOWN` | UNKNOWN | Unverified |
| Persistent Skill pill after response | Not visible in composer | Not visible in composer | VERIFIED | Observed |
| Package acceptance | Observed in first run | Not retested | NOT APPLICABLE | Unverified |
| Package-detail supporting-file retention | Observed in first run | Not retested | NOT APPLICABLE | Unverified |

## Reproduced visible behaviors

The following visible selected-output behaviors are classified as `VERIFIED` with platform label `Reproduced`:

- exact deterministic two-line output
- absence of extra response text, warning, fallback, or visible error

The materially comparable setup conditions remain documented as evidence supporting the reproduction decision, but they are classified as `Observed`, not `Reproduced`. The repeated output remains evidence consistent with supporting-file access. Internal loading mechanics remain `UNKNOWN`.

## Verified facts

- The repository baseline before this observation was recorded as `5f77aeea2de4cbfd90d44283265210e2cd228734`.
- The tested package source revision remained recorded as `433299c4ddb62dc4666d8beab1fcbb5cdac361d3`.
- The first observation file is `experiments/chatgpt-skill-supporting-file-spike/observations/2026-07-10-first-owner-run.md`.
- The owner confirmed the Skill was not reuploaded, reinstalled, edited, renamed, or replaced after the first run.
- The repeated run used ChatGPT Web on PC, workspace `Work`, GPT-5.6 Terra, light reasoning displayed as `軽`, a fresh conversation, no intentionally selected Project, and explicitly selected `supporting-file-loading-spike` with the selected Skill pill visibly present before sending.
- The repeated prompt exactly matched `Run the supporting-file loading spike.`.
- The repeated prompt did not contain `SUPPORT_FILE_ACTIVE` or `POLARIS-23`.
- The repeated output exactly matched the two-line success output.
- The repeated output had no heading, explanation, code fence, prefix, suffix, warning, fallback, or visible error.
- The submitted user message visibly showed the named Skill.
- A persistent Skill pill was not visible in the composer after the response.
- Screenshots are not committed.

## Reasonable inferences

- The selected-output behavior is reasonably classified as reproduced because the same installed Skill, same exact prompt, fresh conversation, same product surface, workspace, model, reasoning setting, Project-selection constraint, explicit Skill selection, visible pre-send Skill pill, and exact two-line output were recorded.
- The repeated exact output is evidence consistent with supporting-file access because the prompt did not include the marker or payload and the output matched the deterministic payload recorded in the package supporting file.

These are inferences from the bounded evidence. They do not identify or prove internal platform mechanisms.

## Unknowns

- internal parser behavior: `UNKNOWN`
- relative-path resolution implementation: `UNKNOWN`
- internal storage behavior: `UNKNOWN`
- prompt construction or prompt injection: `UNKNOWN`
- file-loading implementation: `UNKNOWN`
- runtime package extraction: `UNKNOWN`
- exact installed artifact hash or internal platform identity: `UNKNOWN`
- whether a loading indicator such as `スキルの読み込み` appeared: `UNKNOWN`
- response-duration UI for the repeated run: `UNKNOWN`
- behavior in other models, reasoning settings, workspaces, Projects, devices, product surfaces, package shapes, file types, or unselected invocation: `UNKNOWN`

## Limitations

- This record uses only the stated source basis and sanitized owner-side evidence.
- Package acceptance was not retested and is not relabeled as reproduced.
- Package-detail supporting-file retention was not retested and is not relabeled as reproduced.
- Owner-confirmed artifact continuity is not independent runtime integrity verification.
- The repeated output is evidence consistent with supporting-file access but does not prove how supporting-file access occurred.
- Internal supporting-file mechanics remain `UNKNOWN`.
- The result does not generalize to unselected invocation or other environments.
- No production Skill claim is made.
- Production readiness is `NOT APPLICABLE`.
- No screenshots, ChatGPT conversation URLs, session URLs, task URLs, private URLs, personal information, ZIP files, binaries, generated platform files, or local artifacts are committed.

## Conclusion

For GitHub Issue #28, the exact deterministic two-line selected output and absence of additional response text, warning, fallback, or visible error repeated under the recorded materially comparable conditions. Those selected-output behaviors are classified as requirement/result status `VERIFIED` and platform label `Reproduced`. Setup and comparability facts, including explicit Skill selection, visible pre-send Skill pill, installed Skill name, exact prompt supplied, and prompt exclusion of marker and payload, are classified as `VERIFIED` / `Observed`.

This conclusion is limited to the explicitly selected run and exact two-line output. Package acceptance and package-detail file retention remain scoped to the earlier first owner-side observation. The repeated output remains evidence consistent with supporting-file access, while internal parser behavior, relative-path resolution, storage, prompt construction, file-loading implementation, and runtime package extraction remain `UNKNOWN`.
