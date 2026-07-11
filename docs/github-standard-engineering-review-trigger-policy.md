# GitHub Standard Engineering Review — Trigger Policy

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: trigger and non-trigger definition
- production package: not implemented
- production readiness: not established

This document specifies intended selection behavior only. It does not establish or claim:

- observed ChatGPT automatic invocation;
- internal routing behavior;
- Skill precedence;
- prompt assembly behavior;
- trigger implementation details; or
- production installation behavior.

Do not treat this specification as platform routing evidence.

## Trigger model

Standard Review selection has two separate concepts.

### Intent eligibility

A request is intent-eligible when the user is asking for normal engineering review or a merge-readiness judgment for one GitHub pull request.

### Execution readiness

A request is execution-ready when one target PR and sufficient repository identity or context are available to begin evidence collection without guessing.

A request may be intent-eligible but not execution-ready. Missing identity requires clarification; it is not permission to infer or fabricate a PR. Evidence accessibility affects later review and verdict behavior, not whether the user's request expresses Standard Review intent. This document does not define the evidence collection workflow.

## Positive trigger cases

The Skill should be selected when the user explicitly asks for a normal merge-readiness review of one identifiable GitHub pull request.

Representative intents include:

- review this PR;
- check whether this PR is ready to merge;
- identify blockers in PR #N;
- review the current PR against its linked Issue;
- give the Standard Review verdict for one specified PR;
- re-review the same PR after its branch was updated; and
- verify whether previously identified blockers were fixed.

Acceptable PR identity sources include:

- PR URL;
- repository plus PR number;
- clearly established current PR context; and
- unambiguous follow-up referring to the same PR already under review.

Explicit selection of `github-standard-engineering-review` is strong user intent, but it does not override the one-PR boundary, missing PR identity, evidence accessibility, Standard Review non-goals, write-action restrictions, or Deep Review separation.

Avoid keyword-only rules. The word “review” by itself is not sufficient.

## Clarification cases

The Skill should ask for the smallest missing detail when Standard Review intent is present but the target or depth is ambiguous.

Clarification is required when:

- no repository or PR identifier is available;
- “review this” has no resolvable PR context;
- “review the latest changes” could refer to a branch, commit, repository, or PR;
- multiple PRs are referenced without one primary target;
- a referenced PR conflicts with the established conversation context;
- the repository is identified but the PR number is not;
- the PR number is provided but the repository is ambiguous; or
- the user requests both Standard Review and a deep audit without separating the requested outputs.

Required behavior:

- request only the smallest missing detail;
- do not silently select a PR;
- do not silently select a repository;
- do not silently downgrade or expand review depth; and
- do not fabricate current context.

## Explicit non-trigger cases

The following requests must not select this Skill as the primary procedure:

- broad repository audit;
- general code explanation;
- isolated code snippet review without a GitHub PR;
- issue triage;
- backlog planning;
- implementation or bug fixing;
- writing or rewriting a PR description;
- creating commits;
- editing files;
- merge execution;
- release execution;
- deployment execution;
- branch-protection changes;
- release-readiness certification;
- security-only deep audit;
- privacy-only deep audit;
- architecture-only deep audit;
- dependency or supply-chain-only audit;
- compliance certification;
- penetration testing;
- multi-PR batch review in one judgment; and
- review of unrelated non-GitHub artifacts.

Evidence attached to the one target PR may still be inspected later during Standard Review. A deep-audit-only request should route to a separate deep-review procedure. Standard Review may later recommend escalation, but must not pretend the deep audit was completed. This document does not design a future deep-review Skill.

## Mixed-intent requests

Mixed-intent requests combine Standard Review with another action, such as:

- “Review this PR and fix it.”
- “Review and merge this PR.”
- “Do a standard review and a full security audit.”
- “Review PRs #10, #11, and #12.”
- “Review the PR and write the release notes.”

Preserve the one-job boundary:

- Standard Review may evaluate only one identified PR per review unit;
- implementation remains a separate task;
- merge, release, deployment, and write operations remain separate tasks;
- deep audit remains a separate procedure;
- multiple PRs require separate review units or explicit selection of one PR;
- the Skill must not silently perform write actions; and
- the Skill may identify the separable Standard Review portion, but must clearly separate it from other requested work.

Use `TRIGGER STANDARD REVIEW ONLY / SEPARATE OTHER TASK` where the one-PR Standard Review portion is identifiable and the other requested work remains separate.

## Follow-up and re-review

Follow-ups remain within the same target context when:

- the user reports that the reviewed PR branch was updated;
- the user asks whether identified blockers were fixed;
- the user asks for a new verdict on the same PR;
- the user asks about one finding from the current review; or
- the user supplies missing evidence for the same PR.

Context must be re-established when:

- a different PR is introduced;
- the repository changes;
- the PR identity is unclear;
- the current PR may no longer be the same target;
- the branch or evidence changed materially; or
- the user refers to an old verdict after new commits or CI results.

Re-review is a new evidence evaluation of the same PR. Stale evidence must not be assumed current, and the prior verdict must not be copied forward without checking current evidence. Detailed evidence-refresh rules remain deferred to the workflow specification.

## Selection principles

- Semantic intent over isolated keywords.
- Explicit intent over inferred intent.
- One review unit equals one PR.
- Current repository evidence over stale conversation memory.
- Missing identity produces clarification, not guessing.
- Explicit Skill selection does not waive scope limits.
- Deep-review language does not broaden Standard Review authority.
- Inaccessible evidence does not erase trigger intent.
- Mixed requests must be decomposed rather than silently expanded.
- Follow-up context is reusable only while PR identity remains unambiguous.

## Case matrix

| Representative request | Disposition | Reason or required next step |
| --- | --- | --- |
| “Is `https://github.com/org/repo/pull/42` ready to merge?” | TRIGGER | One identifiable PR and merge-readiness intent. |
| “Find blockers in `org/repo` PR #42.” | TRIGGER | Repository and PR number identify one PR. |
| “The branch was updated; re-review the same PR.” | TRIGGER | Same-PR re-review intent with established target. |
| “Review this.” | CLARIFY | Ask for the PR or current PR context. |
| “Review the latest changes.” | CLARIFY | Ask whether the target is a PR, branch, commit, or repository. |
| “Review the PR in `org/repo`.” | CLARIFY | Ask for the PR number or URL. |
| “Review PRs #10, #11, and #12.” | CLARIFY | Ask for one primary PR or separate review units. |
| “Audit the whole repository.” | DO NOT TRIGGER | Broad repository audit is outside the one-PR job. |
| “Review this code snippet.” | DO NOT TRIGGER | No GitHub PR target. |
| “Fix the bugs in this PR.” | DO NOT TRIGGER | Implementation is not Standard Review. |
| “Rewrite this PR description.” | DO NOT TRIGGER | PR description writing is a separate task. |
| “Do a full security audit.” | DO NOT TRIGGER | Deep-security-only request belongs to a separate procedure. |
| “Review this PR and fix it.” | TRIGGER STANDARD REVIEW ONLY / SEPARATE OTHER TASK | Review one PR only; implementation is separate. |
| “Review and merge this PR.” | TRIGGER STANDARD REVIEW ONLY / SEPARATE OTHER TASK | Review one PR only; merge execution is separate. |
| “Do a Standard Review and a full security audit of PR #42.” | TRIGGER STANDARD REVIEW ONLY / SEPARATE OTHER TASK | Standard Review can be separated; deep audit remains separate. |
| “Explain the third blocker from the current review.” | TRIGGER | Same-current-PR finding follow-up. |

## False-positive and false-negative controls

False-positive controls:

- do not select based only on the word “review”;
- do not treat repository audit as PR review;
- do not treat implementation requests as review requests;
- do not treat deep-audit language as Standard Review authority; and
- do not treat explicit Skill selection as permission to ignore non-goals.

False-negative controls:

- recognize merge-readiness language even when “review” is absent;
- recognize same-PR follow-ups and re-review requests;
- recognize repository-plus-PR-number references;
- recognize explicit requests for blockers or one of the exact verdicts; and
- preserve intent eligibility even when clarification is required.

## Deferred specification

This document does not define:

- GitHub connector or tool selection;
- required and optional inputs beyond identity-level trigger context;
- evidence source requirements;
- evidence hierarchy;
- repository inspection sequence;
- review workflow;
- stopping conditions;
- verdict-selection algorithm;
- output template;
- correction-prompt contract;
- large example or golden-case suite;
- evaluation implementation;
- package structure;
- Skill frontmatter or final description wording; or
- observed ChatGPT auto-routing behavior.
