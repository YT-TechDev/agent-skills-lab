# First Owner-Side Supporting-File Observation — 2026-07-10

This record documents the first reviewed owner-side evidence for the supporting-file package-handling spike and the first explicitly selected supporting-file run for GitHub Issue #26. It records evidence only; it does not rerun, simulate, reinterpret, or invent ChatGPT product behavior.

Source basis: Issue #26 and its precommitted classification policy, repository files at the tested revision, and the sanitized owner-side evidence reviewed for this closeout. Screenshots are not committed.

## Status summary

| Area | Result status | Platform label |
| --- | --- | --- |
| Case A package handling | VERIFIED | Observed |
| Case A package-handling classification: accepted after visible transformation | VERIFIED | Observed |
| Original `SKILL.md` retained in package detail view | VERIFIED | Observed |
| Original `reference/payload.md` retained and inspectable in package detail view | VERIFIED | Observed |
| Skill selectable after upload | VERIFIED | Observed |
| Case B exact selected-run output | VERIFIED | Observed |
| Internal loading mechanism | UNKNOWN | Unverified |
| Loading indicator such as `スキルの読み込み` | UNKNOWN | Unverified |
| Reproduction | MISSING | Unverified |
| Production readiness | NOT APPLICABLE | Unverified |

`Observed` applies only to the named owner-side evidence from this first run. This record is Observed, not Reproduced. Requirement/result statuses and platform labels are separate classifications.

## Tested artifact identity

- tested repository revision: `433299c4ddb62dc4666d8beab1fcbb5cdac361d3`
- package path: `experiments/chatgpt-skill-supporting-file-spike/package/`
- submitted archive name: `supporting-file-loading-spike.zip`
- ZIP archive SHA-256: not independently supplied or recorded in the reviewed evidence
- observation date: `2026-07-10`
- Skill name shown in detail view: `supporting-file-loading-spike`
- exact frontmatter description shown in detail view: `An explicitly invoked experimental Skill that reads one static supporting file and returns its deterministic payload for behavior-discovery testing.`

Original package tree:

```text
package/
├── SKILL.md
└── reference/
    └── payload.md
```

## Local integrity evidence

- local working tree at the tested revision was clean
- both package source files were tracked at the tested revision
- the package contained exactly two source files
- no package file was modified
- `SKILL.md` SHA-256: `eee352b5036bad5d4de98cbfa79cf8c1290ad5b8cf925ad3e31347522748ef1c`
- `reference/payload.md` SHA-256: `62e198df7ef61fbca8cbd0c2aa2b678e118318ed5b6600f025966d08600d5b6f`

## Environment

- product surface: ChatGPT Web on PC
- workspace: `Work`
- owner-facing package workflow: ChatGPT Skills upload page at the visible `/skills` product surface
- model for Case B: GPT-5.6 Terra
- reasoning for Case B: light, visibly displayed as `軽`
- conversation for Case B: fresh
- Project for Case B: not intentionally selected
- Skill for Case B: `supporting-file-loading-spike`
- selection state for Case B: Skill explicitly selected, with selected Skill pill visibly present before sending

## Case A — Package-handling evidence

Visible upload and package-detail evidence:

- the upload dialog advertised `.zip`, `.skill`, and `SKILL.md`
- `supporting-file-loading-spike.zip` was submitted
- the UI displayed a successful-upload notification
- no rejection or validation error was visible
- the Skill appeared under installed Skills
- the Skill appeared under self-created Skills
- the Skill became selectable
- the detail view displayed the exact Skill name `supporting-file-loading-spike`
- the detail view displayed the exact frontmatter description recorded above
- the detail view exposed the original `SKILL.md`
- the detail view exposed the original `reference/payload.md`
- the supporting-file contents were visibly inspectable in the package detail view
- the visible package file selector also contained platform-added files:
  - `agents/openai.yaml`
  - `assets/icon.svg`
- the installed-list summary appeared different from the exact frontmatter description and began with wording similar to `Fetches specific data from ...`

Classification:

- package-handling classification: `accepted after visible transformation`
- platform label: `Observed`
- original `SKILL.md` retained: yes
- original `reference/payload.md` retained: yes
- Skill selectable: yes

Boundaries:

- visible generated files establish a visible transformation in the owner-facing package view
- this record does not claim the platform modified the submitted ZIP bytes
- this record does not claim a particular storage, extraction, parser, validation, or package-normalization mechanism
- package acceptance alone does not prove runtime supporting-file access
- the visible package detail confirms retention and inspectability in that UI, not the internal runtime loading mechanism
- this record does not claim why the installed-list summary differed from the exact frontmatter description

## Case B — Exact prompt and output

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

Output details:

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
- response-duration UI displayed `19s考えました`
- the duration UI was separate from the Skill output
- a loading indicator such as `スキルの読み込み` was not captured and remains `UNKNOWN`
- a persistent Skill pill was not visible in the composer after the response

Classification:

- requirement/result status: `VERIFIED`
- platform label: `Observed`
- reproduction: not established

Interpretation boundary:

- the exact output is evidence consistent with supporting-file access under the recorded conditions
- it does not prove a particular parser
- it does not prove a particular relative-path resolver
- it does not prove a particular prompt-injection or instruction-loading mechanism
- it does not prove internal storage behavior
- internal loading mechanics remain `UNKNOWN`
- this first successful run is `Observed`, not `Reproduced`
- this record does not generalize to other models, reasoning settings, workspaces, Projects, devices, package shapes, file types, or unselected invocation

## Expected-versus-observed comparison

| Case | Precommitted expectation or policy | Observed evidence | Result status | Platform label |
| --- | --- | --- | --- | --- |
| Case A package handling | Classify acceptance, rejection, transformation, or inaccessible result without treating acceptance as runtime proof. | ZIP submitted and accepted; original files retained and inspectable; platform-added files visible. | VERIFIED | Observed |
| Case A classification | Do not assume package-handling outcome. | `accepted after visible transformation`. | VERIFIED | Observed |
| Case B exact selected run | Expected exact output `SUPPORT_FILE_ACTIVE` and `payload: POLARIS-23`. | Exact two-line output matched with no extra response text. | VERIFIED | Observed |
| Case B reproduction | First result must not be labeled `Reproduced`. | Reproduction remains not established. | MISSING | Unverified |
| Internal loading mechanism | Do not claim parser, path resolver, prompt-injection, storage, or file-loading mechanism. | No internal mechanism was visible or independently verified. | UNKNOWN | Unverified |

## Verified facts

- The tested repository revision was `433299c4ddb62dc4666d8beab1fcbb5cdac361d3`.
- The original package source contained `SKILL.md` and `reference/payload.md`.
- The recorded local SHA-256 values for both source files are listed in this record.
- The ZIP archive SHA-256 was not independently supplied or recorded.
- The uploaded ZIP was visibly accepted after visible transformation in the owner-facing package view.
- The original `SKILL.md` and `reference/payload.md` were retained and visible in the package detail view.
- The original supporting-file contents were visibly inspectable in the package detail view.
- `agents/openai.yaml` and `assets/icon.svg` were visible as platform-added files in the package file selector.
- The Skill was selectable.
- The selected-run prompt exactly matched the precommitted prompt.
- The selected-run prompt did not contain `SUPPORT_FILE_ACTIVE` or `POLARIS-23`.
- The selected-run output exactly matched the precommitted success output.
- The response-duration UI `19s考えました` was separate from the Skill output.
- Screenshots are not committed.

## Reasonable inferences

- The Case A evidence is reasonably classified as `accepted after visible transformation` because the owner-facing package view showed successful upload and additional visible platform-added files.
- The Case B exact output is evidence consistent with runtime supporting-file access under the recorded selected-run conditions because the prompt did not include the marker or payload and the exact expected payload was returned.

These are inferences from visible evidence. They do not identify or prove internal platform mechanisms.

## Unknowns

- internal parser behavior: `UNKNOWN`
- relative-path resolution behavior: `UNKNOWN`
- prompt-injection or instruction-loading mechanism: `UNKNOWN`
- internal storage behavior: `UNKNOWN`
- whether the submitted ZIP bytes were modified: `UNKNOWN`
- reason for the installed-list summary differing from the exact frontmatter description: `UNKNOWN`
- whether a loading indicator such as `スキルの読み込み` appeared: `UNKNOWN`
- whether the result will recur in a later materially comparable run: `UNKNOWN`
- behavior for other models, reasoning settings, workspaces, Projects, devices, package shapes, file types, or unselected invocation: `UNKNOWN`

## Visible discrepancies or transformations

- The owner-facing package detail view showed platform-added files `agents/openai.yaml` and `assets/icon.svg` in addition to the original two package source files.
- The installed-list summary differed from the exact frontmatter description and began with wording similar to `Fetches specific data from ...`.
- A persistent Skill pill was not visible in the composer after the response.

These observations are recorded only as visible UI evidence. They do not establish why the differences appeared or how the platform represented, stored, extracted, or transformed the package internally.

## Limitations

- This record uses only the source basis stated above.
- Issue #26 product behavior was not rerun or reproduced for this repository change.
- No screenshots, archives, generated platform files, or private URLs are committed.
- The ZIP archive SHA-256 was not independently recorded.
- Package acceptance is not conflated with runtime supporting-file access.
- Visible package retention is distinguished from runtime behavior.
- Internal loading mechanics remain `UNKNOWN`.
- Production readiness is `NOT APPLICABLE`.

## Conclusion

For GitHub Issue #26, the first owner-side package-handling evidence is classified as `accepted after visible transformation` with platform label `Observed`. The original `SKILL.md` and `reference/payload.md` were retained and inspectable in the owner-facing package view, while `agents/openai.yaml` and `assets/icon.svg` were visible as platform-added files.

The first explicitly selected supporting-file run returned the exact precommitted success output and is classified as `VERIFIED` with platform label `Observed`. This is Observed, not Reproduced. The result is evidence consistent with supporting-file access under the recorded selected-run conditions, but no internal loading mechanism is claimed.
