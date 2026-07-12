# agent-skills-lab

`agent-skills-lab` is a public MIT-licensed repository for designing, testing, evaluating, versioning, and packaging reusable AI agent Skills and engineering workflows.

## Current phase

This repository is currently in the foundation and behavior-discovery phase. The goal at this stage is to keep the repository small, establish a clear structure, and separate reusable Skill procedures from repository-specific Project instructions.

The initial production target is `github-standard-engineering-review`. The production Skill has not been implemented yet.

## Skill development lifecycle

Skill development proceeds incrementally through:

1. design
2. behavior discovery
3. specification
4. implementation
5. evaluation
6. packaging
7. review and installation

Early work may validate behavior in temporary experiments before any production-target Skill package is created. See the [Skill development lifecycle](docs/skill-lifecycle.md) for evidence gates, revision loops, packaging boundaries, and installation rules.

## Agent responsibilities

This repository is intended to support coordinated work across multiple AI coding and review agents:

- GPT helps shape intent, requirements, reasoning, and reusable Skill behavior.
- Codex implements repository changes, validates diffs, and prepares controlled pull requests.
- Claude Code may provide independent implementation, review, and behavior-comparison feedback.

Repository-specific Project instructions must remain separate from reusable Skill procedures so Skills can be packaged and reused outside this repository. Repository-wide agent operating rules are defined in `AGENTS.md`.

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       └── repository-validation.yml
├── .gitignore
├── AGENTS.md
├── LICENSE
├── README.md
├── docs/
│   ├── design-principles.md
│   ├── evaluation-strategy.md
│   ├── github-standard-engineering-review-decision-rules.md
│   ├── github-standard-engineering-review-examples-and-golden-cases.md
│   ├── github-standard-engineering-review-evidence-policy.md
│   ├── github-standard-engineering-review-evaluation-plan.md
│   ├── github-standard-engineering-review-input-contract.md
│   ├── github-standard-engineering-review-output-format.md
│   ├── github-standard-engineering-review-package-structure.md
│   ├── github-standard-engineering-review-scope.md
│   ├── github-standard-engineering-review-stopping-and-failure-policy.md
│   ├── github-standard-engineering-review-verdict-contract.md
│   ├── github-standard-engineering-review-version-and-readiness.md
│   ├── github-standard-engineering-review-tool-policy.md
│   ├── github-standard-engineering-review-trigger-policy.md
│   ├── github-standard-engineering-review-workflow.md
│   └── skill-lifecycle.md
├── experiments/
│   ├── chatgpt-skill-minimal-spike/
│   ├── chatgpt-skill-supporting-file-spike/
│   └── chatgpt-skill-project-context-spike/
├── scripts/
│   └── validate_repository.py
└── skills/
    └── .gitkeep
```

- `docs/` contains repository documentation that is not itself a packaged Skill, including the [Skill design principles](docs/design-principles.md), [initial Skill evaluation strategy](docs/evaluation-strategy.md), [Standard Review decision rules](docs/github-standard-engineering-review-decision-rules.md), [Standard Review evidence policy](docs/github-standard-engineering-review-evidence-policy.md), [Standard Review evaluation plan](docs/github-standard-engineering-review-evaluation-plan.md), [Standard Review examples and golden cases](docs/github-standard-engineering-review-examples-and-golden-cases.md), [Standard Review job and scope](docs/github-standard-engineering-review-scope.md), [Standard Review package structure](docs/github-standard-engineering-review-package-structure.md), [Standard Review stopping and failure policy](docs/github-standard-engineering-review-stopping-and-failure-policy.md), [Standard Review verdict contract](docs/github-standard-engineering-review-verdict-contract.md), [Standard Review version and readiness](docs/github-standard-engineering-review-version-and-readiness.md), [Standard Review input contract](docs/github-standard-engineering-review-input-contract.md), [Standard Review output format](docs/github-standard-engineering-review-output-format.md), [Standard Review trigger policy](docs/github-standard-engineering-review-trigger-policy.md), [Standard Review tool policy](docs/github-standard-engineering-review-tool-policy.md), [Standard Review workflow](docs/github-standard-engineering-review-workflow.md), and [Skill development lifecycle](docs/skill-lifecycle.md). The Standard Review decision rules define blocker versus verification-gap classification, non-blocking notes, positive-verdict conditions, and verdict precedence. The Standard Review evidence policy defines claim-relative evidence authority, evidence statuses, provenance and freshness, partial/unknown handling, and inference and conflict limits. The Standard Review evaluation plan defines evaluation layers, dimensions and acceptance metrics, golden-case traceability, human execution and observation recording, regression comparison, and promotion evidence before package work. The Standard Review examples and golden cases provide repository-neutral examples, normative human-readable golden cases, trigger, verdict, failure, unstable-head, and re-review edge cases, a compact traceability matrix, and short illustrative outputs for all four verdicts. The Standard Review package structure defines the proposed package tree, `SKILL.md` and supporting-file responsibilities, specification mapping, source-of-truth and drift controls, Project-context boundary, loading uncertainty, and validation and promotion prerequisites without claiming package existence, installation testing, supporting-file accessibility, observed package behavior, or readiness. The Standard Review version and readiness document defines the milestone/package-version boundary, current readiness snapshot, readiness progression and transition evidence, version-impact policy, observation/reproduction rules, and current conclusions that the package version is `UNASSIGNED`, production readiness is `NOT ESTABLISHED`, and all 13 specification areas are documented without claiming package implementation, `SKILL.md`, installation, package acceptance, supporting-file accessibility, exact-package evaluation, publication, version assignment, or production readiness. The Standard Review input contract distinguishes target identity, repository-derived evidence, optional user context, and prohibited sensitive inputs before production implementation. The Standard Review trigger policy defines when one-PR Standard Review should trigger, clarify, or decline before production implementation. The Standard Review tool policy defines read-only GitHub evidence capabilities, fallback behavior, and the no-write boundary before production implementation. The Standard Review workflow defines the ordered repository-inspection phases, evidence refresh before verdict selection, coverage reconciliation, and same-PR re-review before production implementation. The Standard Review verdict contract defines semantic eligibility for all four verdicts, required and prohibited claims, blocker/gap/note consistency, and coverage, CI/review, escalation, and re-review disclosures. The Standard Review output format defines exact response order, verdict-specific sections, evidence-reference placement, validation/review/coverage/escalation presentation, correction/re-verification direction, and concise/expanded modes before production implementation. The Standard Review stopping and failure policy defines bounded retries and read-only fallbacks, terminal evidence failures, unstable-head stopping, material versus immaterial failure, and decision effects under existing verdict rules before production implementation.
- `experiments/` contains behavior spikes and temporary investigations, including the [minimal ChatGPT Skill behavior spike](experiments/chatgpt-skill-minimal-spike/README.md), [minimal ChatGPT Skill supporting-file spike](experiments/chatgpt-skill-supporting-file-spike/README.md), and [ChatGPT Skill Project-context interaction spike](experiments/chatgpt-skill-project-context-spike/README.md).
- `.github/workflows/repository-validation.yml` runs the minimal static repository validator in CI.
- `scripts/validate_repository.py` provides local static validation for repository hygiene, links, package shape, and artifact boundaries.
- `skills/` contains production-target or validated Skill packages.

## Experiments vs. production-target Skills

`experiments/` is for temporary behavior discovery, comparison notes, and small spikes that help determine how a Skill should work.

`skills/` is reserved for production-target or validated Skill packages. Experimental findings should only move into `skills/` after they have been specified, implemented, evaluated, and prepared for packaging.

## Validation

Run the same minimal static validator used by CI:

```bash
python3 scripts/validate_repository.py
```

The validator checks static repository text hygiene, repository-relative Markdown links, Skill package shape, and artifact boundaries. It does not test ChatGPT runtime behavior and does not establish production readiness.

## Public repository hygiene

Do not commit secrets, credentials, private repository content, personal information, private URLs, or AI session-sharing URLs. Keep public examples sanitized and ensure any reusable procedures avoid depending on private context.

## Implementation status

The repository foundation exists, but no production Skill package is implemented yet. In particular, `github-standard-engineering-review` is only the initial production target and is not present as an implemented Skill.
