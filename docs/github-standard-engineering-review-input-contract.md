# GitHub Standard Engineering Review — Input Contract

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: required and optional input definition
- production package: not implemented
- production readiness: not established

This document defines logical inputs, input categories, and input authority only.
It does not establish or claim:

- a specific GitHub connector or API implementation;
- permission scopes;
- automatic context injection;
- automatic repository discovery;
- observed ChatGPT routing behavior;
- observed Skill installation behavior; or
- production readiness.

## Input model

These categories are logical inputs, not a machine-readable form or prompt schema.
Not every input is something the user must type manually.

### Target identity inputs

Information needed to identify exactly one GitHub repository and exactly one pull request.

### User constraints

Temporary instructions that affect the requested Standard Review, such as a specific emphasis, access limitation, or explicit request not to perform another action.

### Repository-derived inputs

Current information expected to be retrieved from accessible GitHub and repository evidence rather than manually supplied by the user.

### User-supplied supporting context

Relevant information supplied when it is not linked, cannot be retrieved, or requires clarification.

### Prior-review context

Earlier findings or verdicts used to guide re-review, but never treated as proof of the current PR state.

## Minimum required inputs to begin

The minimum logical inputs for beginning Standard Review are:

1. one unambiguous GitHub repository identity;
2. one unambiguous pull request identity within that repository; and
3. Standard Review intent already established under the trigger policy.

Acceptable identity forms may include:

- a PR URL;
- repository `owner/name` plus PR number;
- clearly established current PR context; or
- an unambiguous same-PR re-review reference.

Repository and PR identities may be resolved from accessible current context, but identities must not be guessed. One invocation targets one PR. Multiple possible targets require clarification. Unavailable or contradictory target identity blocks review start.

The user must not be required to manually supply the diff, changed files, current head SHA, CI status, linked Issue, acceptance criteria, repository instructions, or review comments when those inputs are accessible from the target repository and PR.

This preserves the trigger policy distinction between intent eligibility and execution readiness: Standard Review intent can exist before the request is ready to execute, and missing target identity requires clarification rather than guessing.

## Required user-supplied information

The user must supply only information that cannot be safely or unambiguously resolved.
Examples include:

- missing repository identity;
- missing PR identity;
- selecting one primary PR when several are referenced;
- clarifying review depth when Standard Review and Deep Review are combined;
- temporary constraints that materially affect the requested review; and
- inaccessible acceptance criteria or private context the user explicitly wants considered.

The Skill should request the smallest missing detail rather than presenting a large intake questionnaire.

Required behavior:

- do not ask for information already accessible from the repository;
- do not ask the user to repeat a PR URL already established unambiguously;
- do not force optional context to become mandatory;
- do not infer private acceptance criteria; and
- do not fabricate repository identity from weak hints.

This section does not define a full conversational clarification script.

## Repository-derived inputs

Candidate input types expected to be retrieved when accessible include:

- PR metadata and current state;
- repository identity;
- PR number and URL;
- base branch or base reference;
- head branch or head reference;
- current head SHA;
- changed filenames;
- current diff or per-file patches;
- linked Issue or Issues;
- acceptance criteria;
- repository instructions;
- contribution rules;
- relevant repository files;
- repository conventions;
- tests and validation evidence;
- CI/check status;
- review submissions;
- unresolved review threads;
- PR discussion and comments;
- documentation context relevant to the change; and
- public API and compatibility context relevant to the change.

This list defines input types. It does not define a mandatory fetch order, which tool or connector obtains each input, or the complete evidence hierarchy. Not every input is applicable to every PR, and accessibility is not guaranteed. Do not imply that all repositories expose all inputs.

## Optional user-supplied context

Optional information may improve review quality. Examples include:

- intended behavior;
- problem statement;
- known risks;
- compatibility expectations;
- public API expectations;
- local validation commands;
- local validation results;
- areas to emphasize within Standard Review scope;
- explicit non-goals;
- time or access constraints;
- links or sanitized excerpts for relevant inaccessible evidence;
- previous blocker list for a same-PR re-review; and
- explanation of intentionally unusual design choices.

Optional context should reduce ambiguity, not replace repository evidence. User-provided local results remain claims until supported by accessible output or other evidence. Optional context must not override contradictory current repository evidence. Absence of optional context must not be converted into a positive claim.

## Input authority and contradiction handling

Concise authority rules:

- current accessible repository and PR evidence is authoritative for current repository state;
- current repository evidence is stronger than stale conversation memory;
- user summaries are supporting context until verified;
- prior review findings are historical context;
- previous verdicts are not evidence that the current PR remains unchanged;
- contradictory input must be surfaced rather than silently reconciled;
- repository identity conflicts require clarification;
- missing optional context does not prove a requirement is satisfied;
- inaccessible information must remain unknown; and
- current head SHA should be used to distinguish materially changed review state when accessible.

This section does not define the complete evidence hierarchy, final evidence sufficiency rules, or complete conditions for `UNABLE TO VERIFY`.

## Same-PR re-review inputs

A same-PR re-review should use:

- the same confirmed repository identity;
- the same confirmed PR identity;
- refreshed current repository-derived inputs;
- previous findings as a re-evaluation checklist only; and
- newly supplied evidence and constraints when relevant.

The following must not be assumed current:

- prior diff;
- prior changed-file list;
- prior head SHA;
- prior CI/check result;
- prior review-thread status;
- prior comments;
- prior linked-Issue state; or
- prior verdict.

Re-review is a new evidence evaluation of the same PR. The full evidence refresh sequence is deferred to the workflow specification.

## Sensitive and prohibited inputs

The Skill must not ask for or require:

- GitHub access tokens;
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
- AI task URLs;
- AI session-sharing URLs; or
- unrelated confidential repository content.

Never ask a user to paste credentials to make review possible. Do not commit credentials or private URLs into repository documentation. When relevant evidence is inaccessible, prefer a sanitized excerpt or an explicit unknown. Access setup and authentication procedures are outside this Issue.

This document does not design credential storage or permission setup.

## Missing, inaccessible, and contradictory input behavior

| Condition | Behavior |
| --- | --- |
| Ambiguous target identity | Clarify before review. |
| Contradictory repository or PR identity | Stop and ask the smallest clarifying question. |
| Missing optional context | Continue when current evidence is otherwise sufficient. |
| Inaccessible supporting evidence | Record the limitation and continue only where a trustworthy conclusion remains possible. |
| Inaccessible evidence required for a trustworthy judgment | Preserve the unknown for later verdict-selection logic. |
| Unavailable repository or PR | Do not fabricate content, infer a diff, or review from memory. |
| Multiple PRs | Require one primary PR or separate review units. |

This document does not fully define stopping conditions or the `UNABLE TO VERIFY` decision algorithm.

## Concise input matrix

| Input | Category | Typical source | Required to begin | Handling when missing |
| --- | --- | --- | --- | --- |
| Repository identity | Target identity | PR URL, `owner/name`, current context | Yes | Clarify; do not guess. |
| PR identity | Target identity | PR URL, PR number, current context | Yes | Clarify; do not guess. |
| Standard Review intent | User intent | User request or explicit Skill selection | Yes | Do not start Standard Review. |
| Primary PR selection when multiple PRs are referenced | Target identity | User clarification | Yes, when multiple PRs exist | Ask for one primary PR or separate reviews. |
| User constraints | User constraints | User request | No | Continue unless constraints are material and ambiguous. |
| Current PR metadata | Repository-derived | GitHub/repository evidence | No | Record limitation when inaccessible. |
| Current diff and head SHA | Repository-derived | GitHub/repository evidence | No | Preserve unknown if inaccessible. |
| Linked Issue and acceptance criteria | Repository-derived or supporting context | GitHub links, repository docs, user excerpts | No | Retrieve when accessible; otherwise record unknown or request needed private context. |
| Repository instructions | Repository-derived | Repository files or Project context | No | Do not invent; record unknown if inaccessible. |
| Relevant tests and validation evidence | Repository-derived or supporting context | CI, logs, repository commands, user excerpts | No | Treat user claims as unverified until supported. |
| CI/check status | Repository-derived | GitHub checks | No | Do not claim pass/fail without current evidence. |
| Review comments and unresolved threads | Repository-derived | GitHub review data | No | Record limitation when inaccessible. |
| Optional risk or compatibility context | User-supplied supporting context | User notes or linked docs | No | Absence is not proof of no risk. |
| Prior review findings | Prior-review context | Earlier same-PR review | No | Use as checklist only; refresh current evidence. |
| Inaccessible private context | User-supplied supporting context | Sanitized excerpt or user summary | No | Keep unknown unless the user supplies safe context. |
| Credentials or secrets | Prohibited | None | Prohibited | Never request or require. |

## Deferred specification

This document does not define:

- GitHub connector or tool selection;
- permission scopes;
- authentication setup;
- tool fallback behavior;
- complete evidence hierarchy;
- evidence sufficiency rules;
- repository inspection order;
- review workflow;
- stopping conditions;
- verdict-selection algorithm;
- exact output template;
- correction-prompt contract;
- examples or golden cases;
- evaluation implementation;
- package structure;
- Skill frontmatter or final description wording; or
- production installation behavior.
