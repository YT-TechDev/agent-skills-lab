# Repository Agent Instructions

These instructions apply repository-wide. Keep repository operating rules here separate from reusable Skill procedures in `skills/`.

## Source of truth

- Use this repository as the source of truth for Skill development work.
- Support important claims with current repository evidence before acting on them.
- Do not let conversation context, memory, or assumptions override accessible repository evidence.
- Keep repository-specific Project rules separate from reusable Skill procedures so Skills remain portable.

## Current development phase

- Treat the repository as being in the foundation and behavior-discovery phase.
- Keep work incremental, evidence-driven, and limited to the active Issue.
- Do not prematurely implement the complete production Skill.
- Do not present future structures, workflows, packages, or Skills as already implemented.

## Repository structure boundaries

- Use `docs/` for repository documentation that is not itself a packaged Skill.
- Use `experiments/` for behavior spikes, temporary investigations, and comparison notes.
- Use `skills/` for production-target or validated Skill packages.
- Create `fixtures/` only when representative test data is needed for scoped work.
- Create `scripts/` only when executable automation has a demonstrated purpose.
- Do not add new directories, frameworks, schemas, dependencies, or abstractions merely to make the repository appear mature.
- Do not add nested `AGENTS.md` files without a concrete need for narrower instructions.

## Responsibility model

### GPT

GPT is responsible for planning, Skill architecture, specification, Issue decomposition, acceptance criteria, evaluation design, Codex task prompts, PR review, merge-readiness judgment, correction planning, and milestone or release-readiness coordination.

### Codex

Codex is the default implementation agent for normal scoped repository work, including repository setup, documentation implementation, templates, justified fixtures, justified small validation scripts, focused Skill implementation, and Issue-scoped changes.

### Claude Code

Reserve Claude Code for unusually difficult work, such as architecture-heavy implementation, difficult multi-file changes, advanced validation automation, or work that has exceeded a properly scoped Codex task. Claude Code is not the default implementation agent.

## Git and GitHub workflow

- Use the default workflow: Issue -> short-lived branch from `main` -> implementation -> validation -> pull request -> GPT review -> correction when blocked -> merge.
- Treat `main` as the default integration branch.
- Do not introduce a permanent `develop` branch without demonstrated need.
- Keep each Issue and PR small, coherent, reviewable, reversible, and limited to one responsibility.
- Do not proceed to the next Issue while the current PR has unresolved blockers.
- Inspect the active Issue, acceptance criteria, relevant files, and current repository state before implementation.

## Evidence and unsupported-claim policy

- Distinguish verified facts, reasonable inferences, and unknowns.
- Do not claim that tests passed, validation succeeded, files exist, behavior works, requirements are complete, a package is valid, a PR is safe, or a Skill triggered correctly unless supporting evidence was actually inspected.
- Trace important conclusions to evidence such as source files, diffs, Issue criteria, PR discussions, validation output, CI results, connector or tool results, or directly observed platform behavior.
- When evidence is missing or inaccessible, report the limitation instead of converting it into a positive or negative assumption.

## Standard Review and Deep Review boundary

- Treat `github-standard-engineering-review` as intended support for normal GitHub PR merge-readiness review.
- Standard Review may consider Issue scope, acceptance criteria, changed files and diff, correctness, tests, type safety, error handling, documentation, compatibility, maintainability, repository conventions, and CI status.
- Standard Review must not claim to have completed a full security audit, privacy audit, architecture audit, dependency audit, or release-critical audit.
- Recommend escalation when changes involve security-sensitive behavior, privacy boundaries, architecture boundaries, native code, destructive data operations, dependency risk, or release-critical behavior.
- Do not define the complete Standard Review workflow, rubric, output contract, or decision algorithm in this repository instruction file.

## Scope-control rules

- Keep changes limited to the active Issue.
- Avoid unrelated rewrites, premature abstractions, speculative compatibility layers, and enormous prompt files.
- Avoid combining review, implementation, release, merge, and deep audit responsibilities into one universal Skill.
- Avoid creating scripts before an executable need exists.
- Prefer small, reviewable, reversible changes.
- Stop and report uncertainty when required evidence is inaccessible or contradictory.

## Public repository hygiene

- Do not commit API keys, access tokens, credentials, secrets, private repository content, confidential information, personal information, private URLs, connector credentials, sensitive local machine configuration, ChatGPT session-sharing URLs, Codex session-sharing URLs, Claude session-sharing URLs, or other AI conversation-sharing URLs.
- Use placeholders and sanitized examples for public documentation and tests.
- Require explicit owner intent and appropriate safeguards before implementing destructive or write-capable workflows.

## Validation expectations

- Inspect the final diff before reporting completion.
- Verify that changes remain Issue-scoped.
- Run relevant validation available in the environment.
- Do not add validation tooling solely for appearance.
- Report commands actually run and observed results.
- Report assumptions, known limitations, and anything not completed.
- Do not claim success for commands that were not run.

## Final implementation report

Implementation agents must report at least:

- branch name
- files changed
- implementation summary
- validation commands run
- validation results
- assumptions
- known limitations
- anything not completed
- commit status
- push status
- pull request status or URL when available
