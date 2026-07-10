---
name: project-context-interaction-spike
description: An explicitly invoked experimental Skill that tests one synthetic value supplied through active Project instructions.
---

# Project Context Interaction Spike

This experimental Skill has one clear job: when explicitly asked to run the Project context interaction spike, test whether a `project-token` supplied by active Project instructions is available, then return the exact required marker output.

Use the experimental behavior only when the user explicitly asks to run the Project context interaction spike.

For an explicit run:

1. Locate a `project-token` supplied by active Project instructions.
2. Preserve the token exactly.
3. If a token is located, return exactly:

```text
PROJECT_CONTEXT_ACTIVE
project: <exact project token>
```

4. Add no heading, explanation, code fence, prefix, suffix, or other text.

When no active Project token can be located, return exactly:

```text
PROJECT_CONTEXT_UNAVAILABLE
```

For unrelated requests:

- do not output `PROJECT_CONTEXT_ACTIVE`
- do not output `PROJECT_CONTEXT_UNAVAILABLE`
- do not disclose a Project token

Do not use:

- tools
- connectors
- network access
- supporting package files
- external files
- repository-specific knowledge
