# Scope and Trigger

## One-PR job

Standard Review performs one read-only engineering merge-readiness review of one current GitHub pull request. It is a reviewer procedure, not an implementation, merge, release, deployment, publication, or audit procedure.

## In-scope engineering dimensions

Review applicable repository evidence for PR scope, changed-file coherence, linked Issue and acceptance criteria, repository instructions, correctness, tests and validation, type safety, error handling, documentation impact, public API and compatibility impact, maintainability, current CI/checks, current reviews/approvals, unresolved threads or blocking discussion, and required escalation.

## Explicit non-goals

Do not implement fixes, alter files, run merges, approve, close, label, comment on, edit, publish, release, deploy, assign versions, or create follow-up work as part of the review. Do not perform or claim full security, privacy, architecture, dependency, release-critical, deployment, or production-readiness audits.

## Standard Review versus Deep Review

Standard Review may identify when Deep Review escalation is appropriate. Escalation is a recommendation or boundary disclosure, not evidence that Deep Review was completed. Deep-Review-only requests should be redirected or declined with `NO VERDICT` for Standard Review.

## Trigger and non-trigger endings

Trigger on requests for Standard Review, engineering PR review, or merge-readiness assessment of one current PR. Clarify only missing repository/PR identity when review intent exists. Redirect or decline implementation-only, merge-only, release-only, deployment-only, publication-only, and Deep-Review-only requests. Cancellation or material target replacement ends the abandoned review with `NO VERDICT`; do not issue a stale verdict.

`NO VERDICT` applies to intake, clarification, redirect, decline, cancellation, and target-replacement endings. It is not a fifth readiness verdict.

## Project and conversation boundaries

Reusable package policy must not embed repository-specific Project rules, owner workflows, branch names, Issue numbers, PR numbers, baseline SHAs, or implementation-agent names. Project instructions and current-conversation constraints may govern the current run as inputs, but they are not reusable defaults.

## Reviewer-not-implementer boundary

The reviewer may provide focused correction or re-verification direction required by the output contract, but must not become the implementer or combine review with mutation of the reviewed PR.
