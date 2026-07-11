# GitHub Standard Engineering Review — Job and Scope

## Status

- canonical name: `github-standard-engineering-review`
- status: specification draft
- lifecycle stage: job and scope definition
- production package: not implemented
- production readiness: not established

This document defines the reusable review boundary only. It does not claim that the Skill is implemented, installed, tested, packaged, or production-ready.

## One clear job

Review one GitHub pull request against accessible repository evidence and return a consistent merge-readiness judgment for normal engineering review.

The intended outcome is that:

- the user receives a traceable merge-readiness judgment;
- blockers and evidence gaps are visible;
- unsupported confidence is avoided; and
- escalation is recommended when Standard Review is insufficient.

The review unit is one pull request, including:

- its current diff and changed files;
- its linked Issue and acceptance criteria when accessible;
- repository instructions and relevant repository evidence; and
- current checks, reviews, and discussions when accessible.

The reusable Skill must not embed repository-specific rules. Repository-specific rules are supplied by the repository, Project, or current conversation when available.

## In-scope Standard Review coverage

Standard Review may inspect, when relevant and accessible:

- PR purpose and scope;
- changed files and diff;
- linked Issue;
- acceptance criteria;
- repository instructions;
- repository conventions;
- correctness risks visible from the change;
- tests and validation evidence;
- type safety;
- error handling;
- documentation impact;
- public API impact;
- compatibility impact;
- maintainability;
- unnecessary complexity;
- CI status;
- review comments;
- unresolved threads; and
- missing or contradictory evidence.

Not every category applies to every PR. Absence of applicable evidence must not be converted into a positive claim. A category may be marked not applicable only with a clear reason. The Skill may identify missing evidence and may recommend escalation, but this section is not a scoring system or weighted checklist.

## Explicit Standard Review non-goals

The following are outside Standard Review:

- full security audit;
- full privacy audit;
- deep architecture audit;
- dependency audit;
- software supply-chain audit;
- release-critical certification;
- compliance certification;
- penetration testing;
- exhaustive performance analysis;
- broad repository audit unrelated to the current PR;
- implementation of corrections;
- automatic code modification;
- merge execution;
- release execution;
- deployment execution; and
- branch-protection changes.

A future separate Skill may handle deep review, for example `github-deep-architecture-security-review`.

Standard Review may recommend escalation but must not state or imply that a deep security, privacy, architecture, dependency, or release-critical review was completed. This document does not design the deep-review Skill.

## Evidence and authority boundary

The Skill may judge only from accessible evidence. It must:

- distinguish verified facts, reasonable inferences, and unknowns;
- trace important conclusions to source evidence;
- avoid claiming tests passed unless test evidence was inspected;
- avoid claiming CI passed unless current check evidence was inspected;
- avoid claiming acceptance criteria were satisfied unless the criteria and implementation evidence were inspected;
- avoid claiming files or behavior exist when inaccessible;
- report contradictory evidence;
- avoid inventing repository instructions;
- prefer current repository evidence over stale conversation context; and
- use `UNABLE TO VERIFY` when required evidence cannot be accessed or reconciled.

A later specification will define the selection rules for this exact verdict set:

- MERGE READY
- MERGE READY WITH NON-BLOCKING NOTES
- NOT MERGE READY
- UNABLE TO VERIFY

This document does not define the complete verdict-selection algorithm.

## Reviewer responsibility boundary

The Skill is a reviewer, not an implementation agent.

It may:

- explain concrete blockers;
- identify evidence gaps;
- identify non-blocking notes;
- suggest focused corrections;
- recommend escalation; and
- state what remains unknown.

It must not by default:

- rewrite the PR;
- modify files;
- create unrelated follow-up work;
- merge the PR;
- approve the PR through GitHub;
- release or deploy;
- claim ownership of implementation; or
- combine normal review and deep audit into one judgment.

Correction prompts may be produced later as a review output, but implementation remains a separate action and requires explicit user intent.

## Repository-specific context boundary

Project or repository context includes:

- repository-specific instructions;
- contribution rules;
- commands;
- architecture conventions;
- release policy;
- local acceptance criteria; and
- private or organization-specific rules.

Reusable Skill behavior includes:

- the general procedure for reviewing a PR;
- evidence discipline;
- scope boundaries;
- failure behavior; and
- merge-readiness judgment procedure.

Current conversation context includes:

- the immediate PR;
- temporary user constraints;
- current requested depth; and
- short-lived clarifications.

Repository-specific knowledge must not be embedded as permanent general Skill behavior.

## Escalation boundary

Standard Review may recommend deeper review when the PR involves areas such as:

- authentication or authorization changes;
- secret or credential handling;
- privacy-sensitive data flows;
- major architecture boundaries;
- destructive data operations;
- native code or unsafe memory handling;
- dependency or supply-chain risk;
- cryptography;
- release-critical migrations; or
- ambiguous high-impact behavior.

This is an escalation recommendation boundary only. Standard Review does not define or perform the deep review procedure.

## Later specification work

Later separate specification areas are:

1. [trigger and non-trigger cases](github-standard-engineering-review-trigger-policy.md);
2. [required and optional inputs](github-standard-engineering-review-input-contract.md);
3. [GitHub tool and connector policy](github-standard-engineering-review-tool-policy.md);
4. [evidence hierarchy](github-standard-engineering-review-evidence-policy.md);
5. [decision rules](github-standard-engineering-review-decision-rules.md);
6. [review workflow](github-standard-engineering-review-workflow.md);
7. [stopping and failure conditions](github-standard-engineering-review-stopping-and-failure-policy.md);
8. [exact verdict contract](github-standard-engineering-review-verdict-contract.md);
9. output format;
10. examples and golden cases;
11. evaluation plan;
12. package structure; and
13. version and production-readiness status.

These areas intentionally remain incomplete after this Issue.

## Quality check

This scope definition:

- describes one clear job;
- remains reusable across repositories;
- separates Standard Review from Deep Review;
- separates review from implementation;
- requires evidence-backed claims;
- preserves unknowns;
- does not claim production readiness;
- does not embed repository-specific rules; and
- does not prematurely define the complete Skill.
