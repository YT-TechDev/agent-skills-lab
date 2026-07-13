# GitHub Standard Engineering Review supporting-file accessibility test plan

## Purpose and history

This document precommits a corrected supporting-file accessibility oracle before execution and before any new owner-side ChatGPT run. Its purpose is to make the expected output, prompt, classification rules, environment controls, stop rules, evidence requirements, and interpretation limits reviewable in the repository before product execution occurs.

Issue #70 used an invalid expected value. Its controlled run was valid, but the overall result was `INCONCLUSIVE` / `Observed` because the precommitted oracle was defective. This protocol prevents post-hoc oracle repair by recording the corrected oracle before any later run.

## Status and non-execution boundary

- Protocol status: precommitted draft under repository review.
- Product run in Issue #72: prohibited and not executed.
- Observation result: unavailable.
- Supporting-file accessibility: `NOT ESTABLISHED`.
- Internal loading: `UNKNOWN`.
- Package version: `UNASSIGNED`.
- Production readiness: `NOT ESTABLISHED`.
- Repository state: `Package draft`.

No run status is assigned before a run occurs.

## Exact identities

- Production package merge: `7c8278cc1bca1286290fdbacd610fe9d97b1fe81`.
- First owner-side observation merge: `bbbbd8f9cc0d69b75e2785c8f8456a1c94a36a79`.
- Issue #70 oracle-defect recording merge: `c9beaa132a4fdfd59a4f4a717ad67f25b9e4a06a`.

Issue #70 is the oracle-defect history for this protocol. Its controlled run remains recorded as valid, while its overall result remains `INCONCLUSIVE` / `Observed` because the precommitted expected value was invalid.

## Supporting-file dependency

- Root file: `skills/github-standard-engineering-review/SKILL.md`.
- Supporting file: `skills/github-standard-engineering-review/reference/verdict-and-output.md`.
- Corrected exact oracle: `### Re-verification requirement`.

The root `SKILL.md` has generic re-verification-direction wording. The root `SKILL.md` lacks the exact Markdown heading `### Re-verification requirement`. The supporting file contains that exact heading and requires it for `UNABLE TO VERIFY`. This oracle is a rendered output-contract token, not descriptive prose.

| Source | Exact-string evidence | Semantic wording | Oracle relevance |
| --- | --- | --- | --- |
| `skills/github-standard-engineering-review/SKILL.md` | Does not contain `### Re-verification requirement`. | Contains generic wording to render a focused correction or re-verification direction when required. | The exact heading is not available from the root file as an exact rendered token. |
| `skills/github-standard-engineering-review/reference/verdict-and-output.md` | Contains `### Re-verification requirement`. | Defines the heading as required for `UNABLE TO VERIFY` and explains that it identifies the smallest evidence, access, target-state, or repository-state change needed for another review when known. | This is the corrected exact output-contract token for the future run. |

## Exact future-run prompt

The later execution must copy this prompt without alteration:

```text
Run a controlled supporting-file accessibility check for this selected Skill.

Do not review a live pull request and do not use GitHub tools.

For a fictional Standard Review that must end with UNABLE TO VERIFY, return only the exact Markdown heading that the Skill's output contract requires for the section identifying the smallest evidence, access, target-state, or repository-state change needed before another review.

Preserve the Markdown heading markers and exact capitalization. No verdict, explanation, code fence, prefix, or suffix.
```

The later execution must not add:

- the expected output;
- package path;
- supporting-file name;
- heading name; or
- equivalent answer hints.

## Precommitted expected output

The precommitted expected output is exactly one line:

```text
### Re-verification requirement
```

An exact-output `PASS` permits only that one line with exact capitalization and Markdown markers. No code fence, verdict, explanation, prefix, suffix, blank content line, or additional line is permitted.

## Classification policy

Evaluation statuses remain separate from product-research labels.

- `PASS`: full final output exactly matches the expected line.
- `PARTIAL`: expected heading is identifiable, but formatting or extra final text violates the contract.
- `FAIL`: a valid controlled run completes, but expected heading is absent or incorrect.
- `INCONCLUSIVE`: installed identity, explicit selection, prompt integrity, environment integrity, or final output cannot be established reliably.

Do not infer failure causes without evidence.

For research labels:

- use `Reproduced` only when the same installed Skill remains traceable, materially comparable conditions are recorded, and repository reproduction criteria are satisfied;
- otherwise use `Observed`;
- Issue #70 does not automatically establish reproduction.

Do not preassign the future run's label.

## Future environment requirements

A future run requires:

- same installed production Skill when identity is traceable;
- fresh conversation;
- no Project selected;
- no files, knowledge, repository attachment, or GitHub URL;
- no GitHub connector or other tool intentionally invoked;
- Skill explicitly selected;
- Skill indicator visible when exposed;
- GPT-5.6 Sol and high / `高` when available for comparability;
- exact committed prompt;
- one final-output capture;
- full sent prompt and final output visible where practical;
- response-duration UI recorded separately;
- test date/timezone and visible environment metadata recorded.

Any model or reasoning deviation must be disclosed and its comparability classified.

## Pre-run checklist

- [ ] Protocol merge identity established.
- [ ] Installed Skill identity traceable.
- [ ] Fresh non-Project chat.
- [ ] No attachments or URLs.
- [ ] Explicit Skill selection.
- [ ] Exact prompt copied.
- [ ] Expected answer absent from prompt.
- [ ] No equivalent hint.
- [ ] No tool request.
- [ ] Evidence capture ready.

## Stop and retry policy

Classify the run as `INCONCLUSIVE` without answer-seeking retries when:

- Skill identity cannot be traced;
- explicit selection cannot be established;
- Project, attachment, URL, or tool is used;
- prompt is altered or leaks the answer;
- product, network, or permission failure blocks a reliable final output;
- final output cannot be captured reliably.

One clean retry is allowed only for an obvious UI/input mistake before a valid response is produced. Never retry to obtain the expected answer.

## Future evidence recording

A future evidence record must include:

- protocol path and merge commit;
- package identity;
- Skill traceability basis;
- date/timezone;
- product surface;
- visible plan/workspace/model/reasoning context;
- explicit selection evidence;
- exact prompt;
- exact final output;
- transient progress UI separately;
- evaluation status;
- product-research label;
- deviations and limitations;
- retry occurrence and reason.

Screenshots may be reviewed privately by GPT but must not be committed. Codex records repository evidence only after GPT review.

## Interpretation boundary

A later exact match may support only a bounded conclusion consistent with supporting-file accessibility under the recorded conditions because the exact heading is absent from root `SKILL.md`, present in the supporting file, and absent from the prompt.

It must not establish:

- which file was read;
- whether every supporting file loaded;
- eager, lazy, automatic, selective, or ordered loading;
- parser, extraction, storage, relative-path, hidden-prompt, or prompt-construction behavior;
- behavior in other models, workspaces, Projects, devices, or package versions;
- unselected invocation;
- live PR correctness;
- connector capability;
- full evaluation;
- version assignment;
- Evaluation candidate transition;
- production readiness.

Internal loading remains `UNKNOWN` regardless of outcome.

## Explicit Issue #72 prohibition

Do not run the owner-side prompt during Issue #72.

Do not fabricate an output. Do not add a placeholder result. Do not update readiness evidence as though execution occurred. Do not create the later execution Issue in this PR. Execution starts only after this protocol PR is reviewed, merged, and separately authorized.

## Acceptance checklist

- [x] Source verification completed.
- [x] Exact prompt committed.
- [x] Expected output committed.
- [x] No answer leakage.
- [x] Classification policy committed.
- [x] Environment and stop rules committed.
- [x] Future evidence rules committed.
- [x] No execution occurred.
- [x] No Skill package changes.
- [x] Current unknown/readiness states preserved.
