# GitHub Standard Engineering Review — Tool Policy

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: GitHub tool and connector policy definition
- production package: not implemented
- production readiness: not established

This document defines intended read capabilities, read/write boundaries, fallback principles, and access-failure behavior only for future Standard Review evidence collection.

It does not establish or claim:

- a specific connector implementation;
- a GitHub API implementation;
- permission scopes;
- automatic tool invocation;
- hidden routing or prompt assembly behavior;
- production installation behavior; or
- production readiness.

## Tool-policy principles

Standard Review tool use must follow these principles:

- Prefer repository-native current evidence over stale conversation memory.
- Prefer structured GitHub data over rendered-page inference when both are available.
- Collect evidence read-only by default.
- Use the least capability necessary for the Standard Review job.
- Treat one target PR as one review unit.
- Report explicit unknowns instead of fabricating evidence.
- Use the current head SHA as the review-state anchor when available.
- Keep the specification connector-independent.
- Do not collect credentials.
- Do not perform silent write actions.

These principles guide tool authority and source choice; they do not define a complete evidence hierarchy.

## Required read capability classes

Standard Review may require these read capability classes when accessible:

- repository and PR identity;
- PR metadata and current state;
- base/head refs and current head SHA;
- changed filenames;
- complete diff or per-file patches;
- linked Issue or Issues and acceptance criteria;
- repository instructions and contribution rules;
- relevant repository files and documentation;
- relevant commit metadata;
- CI/check status and workflow/job summaries;
- review submissions;
- unresolved review threads;
- PR discussion and comments; and
- public API or compatibility context relevant to changed files.

This list defines capabilities, not:

- a mandatory fetch order;
- a workflow;
- a connector inventory;
- an API endpoint inventory; or
- a complete evidence hierarchy.

## Preferred source behavior

When selecting among available read sources, Standard Review should prefer:

- authorized GitHub repository access for private repositories;
- repository-native structured PR, Issue, commit, review, and check data;
- exact file contents and diffs at known refs;
- current remote state over local-only claims; and
- exact identifiers such as `owner/name`, PR number, SHA, ref, and path.

PR descriptions, user summaries, local command reports, and conversation memory are context until verified against current accessible repository evidence. This section does not complete evidence ranking beyond what is required for tool selection.

## Strict read-only boundary

Standard Review itself must not:

- merge or close a PR;
- enable auto-merge;
- push commits;
- create, update, or delete branches or tags;
- create, edit, or delete repository files;
- create commits;
- change PR title or body;
- post comments or reviews;
- resolve or unresolve review threads;
- add or remove labels, assignees, or reviewers;
- rerun or cancel CI;
- change repository or branch-protection settings;
- create releases or deployments; or
- expose or modify secrets.

These actions can only be separate, explicit user-directed tasks outside the Standard Review procedure and subject to their own safeguards. Explicit Skill selection does not authorize write actions.

## Current-state and re-review refresh

Each review or re-review must refresh changeable current data, including:

- PR state;
- head SHA;
- base/head refs;
- changed-file list;
- diff or patches;
- CI/check status;
- review submissions;
- unresolved threads;
- PR comments/discussion; and
- linked-Issue state when relevant.

Cached results and prior evidence must not be assumed current after:

- branch updates;
- new commits;
- force-pushes;
- new reviews;
- new comments;
- new CI runs; or
- linked-Issue changes.

Exact inspection order is deferred to the workflow specification.

## Fallback classes

Use this ordered fallback model:

1. repository-native structured access;
2. direct read-only access to public GitHub pages or raw repository content when reliable;
3. user-supplied sanitized excerpts or exported evidence; and
4. explicit unknown or access limitation.

Fallback must follow these requirements:

- never silently change the repository or PR target;
- do not represent rendered-page inference as structured data;
- label partial evidence as partial;
- do not treat conversation memory as a substitute for current repository evidence;
- identify user-provided excerpts as user-supplied context;
- do not request credentials for inaccessible private evidence; and
- do not convert missing evidence into a positive claim.

This policy does not add browser-scraping implementation instructions.

## Access and tool failure behavior

When read access or tool results are limited, Standard Review must preserve the limitation, retry only when reasonable, safe, and non-destructive, avoid fabricating missing fields, avoid reporting unavailable evidence as verified, distinguish partial access from full access, and surface cross-source conflicts.

Apply that behavior to conditions including:

- repository or PR not found;
- connector unavailable;
- authorization denied;
- private repository inaccessible;
- rate limit;
- transient tool error;
- incomplete pagination;
- truncated response;
- file too large;
- binary-only change;
- CI status visible but logs unavailable;
- review-thread data unavailable; and
- conflicting results from two read sources.

This document does not define full stopping conditions or exact `UNABLE TO VERIFY` rules.

## Cross-source consistency

- Current head SHA anchors review-state evidence when available.
- Results for different SHAs must not be silently combined.
- Repository, PR, SHA, ref, and path identifiers should be retained with tool output.
- Conflicting PR state, diff, checks, or review-thread results must be surfaced.
- Stale results should be refreshed before a final verdict.
- A branch update invalidates evidence that was specific to the previous head SHA.

This section does not define an evidence ledger schema or output template.

## External linked references

Standard Review may inspect external references read-only only when directly relevant to the target PR, such as:

- linked official documentation;
- linked specifications;
- linked compatibility references; and
- linked test or CI artifacts.

Broad external research, dependency audit, security audit, privacy audit, or architecture audit is not silently added to Standard Review.

## Sensitive data policy

The Skill must not ask for, require, expose, or commit:

- access tokens;
- API keys;
- passwords;
- private keys;
- SSH private keys;
- session cookies;
- connector credentials;
- OAuth secrets;
- secret environment values;
- service-account credentials;
- private AI conversation URLs;
- AI task URLs; or
- AI session-sharing URLs.

When access is unavailable, prefer sanitized evidence or an explicit unknown.

## Concise capability matrix

| Evidence need | Preferred capability/source | Acceptable fallback | When unavailable | Write allowed |
| --- | --- | --- | --- | --- |
| PR identity and metadata | Repository-native structured PR metadata | Reliable public page or user-supplied sanitized identifier | Report unknown or access limitation | No |
| Head SHA and refs | Structured PR refs and current head SHA | Raw repository refs or sanitized exported evidence | Do not anchor SHA-specific conclusions | No |
| Changed files | Structured changed-file list | Reliable public diff view or exported file list | Label file coverage partial or unknown | No |
| Diff or patches | Complete diff or per-file patches at known SHA | Reliable public patch/diff or sanitized excerpt | Do not verify changed behavior from missing diff | No |
| Linked Issue and acceptance criteria | Repository-native linked Issue data | Reliable public Issue page or sanitized excerpt | Treat criteria as unavailable context | No |
| Repository instructions/files | Exact repository file contents at known ref | Raw file content or sanitized excerpt | Do not invent repository rules | No |
| CI/check status | Structured check and workflow/job summaries | Public status view or sanitized CI export | Do not claim CI passed or failed as verified | No |
| CI logs | Read-only job log or artifact access | Sanitized log excerpt | Report logs unavailable while preserving visible status | No |
| Review submissions | Structured review submissions | Public review view or sanitized export | Do not claim approval/blocking review state beyond accessible data | No |
| Unresolved threads | Structured review-thread state | Public discussion view or sanitized export | Label thread state unavailable | No |
| PR comments | Structured PR discussion/comments | Public page or sanitized excerpt | Do not claim discussion was fully reviewed | No |
| External linked documentation | Direct read-only linked official or compatibility reference | User-supplied sanitized excerpt | Mark external context unavailable | No |
| Private repository evidence | Authorized repository-native access | User-supplied sanitized excerpts or exports | Use explicit unknown; do not request credentials | No |
| Merge or repository mutation | Outside Standard Review, not an evidence source | Separate explicit user-directed task with safeguards | Do not perform inside Standard Review | No |

## Deferred specification

This document does not define:

- complete evidence hierarchy;
- evidence sufficiency rules;
- repository inspection order;
- review workflow;
- stopping conditions;
- decision rules;
- verdict-selection algorithm;
- exact verdict-contract details beyond the existing names;
- output template;
- correction-prompt contract;
- examples or golden cases;
- evaluation implementation;
- production package structure;
- Skill frontmatter or final description;
- production installation behavior; or
- deep-review tool policy.
