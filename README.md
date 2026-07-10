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

Early work may validate behavior in temporary experiments before any production-target Skill package is created.

## Agent responsibilities

This repository is intended to support coordinated work across multiple AI coding and review agents:

- GPT helps shape intent, requirements, reasoning, and reusable Skill behavior.
- Codex implements repository changes, validates diffs, and prepares controlled pull requests.
- Claude Code may provide independent implementation, review, and behavior-comparison feedback.

Repository-specific Project instructions must remain separate from reusable Skill procedures so Skills can be packaged and reused outside this repository.

## Repository structure

```text
.
├── .gitignore
├── LICENSE
├── README.md
├── docs/
│   └── .gitkeep
├── experiments/
│   └── .gitkeep
└── skills/
    └── .gitkeep
```

- `docs/` contains repository documentation that is not itself a packaged Skill.
- `experiments/` contains behavior spikes and temporary investigations.
- `skills/` contains production-target or validated Skill packages.

## Experiments vs. production-target Skills

`experiments/` is for temporary behavior discovery, comparison notes, and small spikes that help determine how a Skill should work.

`skills/` is reserved for production-target or validated Skill packages. Experimental findings should only move into `skills/` after they have been specified, implemented, evaluated, and prepared for packaging.

## Public repository hygiene

Do not commit secrets, credentials, private repository content, personal information, private URLs, or AI session-sharing URLs. Keep public examples sanitized and ensure any reusable procedures avoid depending on private context.

## Implementation status

The repository foundation exists, but no production Skill package is implemented yet. In particular, `github-standard-engineering-review` is only the initial production target and is not present as an implemented Skill.
