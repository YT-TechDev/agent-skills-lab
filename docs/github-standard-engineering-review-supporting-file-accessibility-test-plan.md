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

## Raw-output observability

ChatGPT may render Markdown headings and visually suppress the literal heading markers. Rendered-output evidence alone cannot establish whether the final output contained the exact `###` prefix.

The later owner-side execution must capture both:

1. the rendered final response as shown by ChatGPT; and
2. an unedited raw/plain-text representation of the complete final response.

The raw/plain-text representation should be obtained using the product's response-copy operation when available. Paste the copied response directly, without modification, into a plain-text destination that does not render Markdown, such as a basic text editor. Do not normalize whitespace, add or remove characters, change capitalization, retype the response, or manually reconstruct Markdown markers. Do not paste or resend the copied response into ChatGPT or another model for verification.

Record the capture method and any known transformation risk. Preserve the rendered and plain-text evidence privately for GPT review. Do not commit screenshots, copied response files, clipboard artifacts, exports, or other product-generated evidence to the repository.

Copy/export behavior must not be used to infer model internals, hidden prompts, storage, parser behavior, or supporting-file loading mechanics. This protocol treats the copied text only as a raw/plain-text representation captured through the product copy operation, not as an internal raw model token stream or authoritative hidden source format.

## Classification policy

Evaluation statuses remain separate from product-research labels.

- `PASS`: allowed only when the rendered final response contains no extra visible final-output content; the unedited raw/plain-text evidence contains exactly one line; that line exactly equals `### Re-verification requirement`; exact capitalization is preserved; all three `#` markers are present; no prefix, suffix, code fence, verdict, explanation, extra content line, or additional blank content line is present; and the raw capture method is sufficiently reliable to compare the exact string.
- `PARTIAL`: allowed only when reliable raw/plain-text evidence exists and the expected heading is identifiable, but the exact-output contract is violated, including missing or altered Markdown markers, altered capitalization, extra explanation, prefix or suffix, additional final-output lines, surrounding code fence, or another directly observable formatting deviation. Do not use `PARTIAL` merely because the rendered UI hides Markdown markers.
- `FAIL`: allowed only when the controlled run is otherwise valid, reliable raw/plain-text evidence exists, and the expected heading is absent or incorrect.
- `INCONCLUSIVE`: required when installed identity, explicit selection, prompt integrity, environment integrity, or final output cannot be established reliably; only the rendered heading is available; literal Markdown markers cannot be verified; the product copy/export operation is unavailable; the copied representation may have transformed the output in a way that prevents exact comparison; the plain-text destination rendered or altered Markdown; the copied response was edited, retyped, normalized, or reconstructed; capture integrity is otherwise uncertain; or any existing identity, selection, prompt, environment, access, interruption, or evidence stop condition applies.

Rendered heading evidence alone is not `PASS`. Rendered heading evidence alone is not `PARTIAL`. When marker observability is uncertain, classify `INCONCLUSIVE`. Do not infer failure causes without evidence.

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
- an available product response-copy operation or other pre-authorized capture mechanism capable of preserving the complete final response;
- a plain-text destination that does not render Markdown;
- a plan to capture rendered and plain-text evidence from the same final response;
- no transformation or manual reconstruction of copied output;
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
- [ ] Raw/plain-text capture method is available.
- [ ] Plain-text destination does not render Markdown.
- [ ] Rendered and plain-text evidence will come from the same final response.
- [ ] Copied text will not be edited, normalized, retyped, or reconstructed.
- [ ] Copied response will not be resent to ChatGPT or another model.

## Stop and retry policy

Classify the run as `INCONCLUSIVE` without answer-seeking retries when:

- Skill identity cannot be traced;
- explicit selection cannot be established;
- Project, attachment, URL, or tool is used;
- prompt is altered or leaks the answer;
- product, network, or permission failure blocks a reliable final output;
- final output cannot be captured reliably;
- raw/plain-text capture is unavailable;
- copy/export transformation cannot be ruled out enough for exact comparison;
- the destination renders or modifies Markdown;
- copied evidence was accidentally edited or reconstructed;
- rendered and raw evidence cannot be tied to the same final response.

One clean retry is allowed only for an obvious UI/input/capture setup mistake before a valid assistant response is produced. Never retry because the captured answer did not match the oracle, and never retry to obtain the expected answer.

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
- rendered final-output evidence;
- raw/plain-text final-output evidence;
- exact raw capture method;
- plain-text destination type;
- whether the copied representation was edited or transformed;
- known capture-method limitations;
- exact marker verification result;
- whether rendered and raw evidence were confirmed to originate from the same final response;
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
- internal raw model output representation from any product copy operation;
- hidden prompts, token streams, package storage, parser behavior, or supporting-file loading from copied text;
- behavior in other models, workspaces, Projects, devices, or package versions;
- unselected invocation;
- live PR correctness;
- connector capability;
- full evaluation;
- version assignment;
- Evaluation candidate transition;
- production readiness.

A product copy operation does not prove the model's internal raw output representation. Copied text does not reveal hidden prompts, token streams, package storage, parser behavior, or supporting-file loading. Capture fidelity is only an evidence-quality condition for this exact-output test.

Supporting-file accessibility remains `NOT ESTABLISHED`, internal loading remains `UNKNOWN`, package version remains `UNASSIGNED`, production readiness remains `NOT ESTABLISHED`, and repository state remains `Package draft` regardless of outcome.

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
- [x] Raw-output observability method committed.
- [x] Rendered-only evidence classified as insufficient.
- [x] Exact-marker verification rule committed.
- [x] Capture-integrity stop conditions committed.
- [x] No raw or rendered product evidence was produced during Issue #72.
- [x] No execution occurred.
- [x] No Skill package changes.
- [x] Current unknown/readiness states preserved.
