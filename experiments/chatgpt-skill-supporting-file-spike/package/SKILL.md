---
name: supporting-file-loading-spike
description: An explicitly invoked experimental Skill that reads one static supporting file and returns its deterministic payload for behavior-discovery testing.
---

# Supporting File Loading Spike

Use this experimental behavior only when the user explicitly asks to run the supporting-file loading spike.

For an explicit run:

1. Read the package-relative file `reference/payload.md`.
2. Locate the only fenced `text` block under `## Required output`.
3. Confirm that the block contains exactly two non-empty lines.
4. Output those two lines exactly without the Markdown fence.
5. Add no explanation, heading, prefix, suffix, or other text.

If the supporting file cannot be accessed, the required section or fenced block cannot be found, or the block does not contain exactly two non-empty lines, output exactly:

```text
SUPPORT_FILE_UNAVAILABLE
```

Do not add diagnostic details and do not guess the supporting payload.

For unrelated requests, do not output `SUPPORT_FILE_UNAVAILABLE`, do not output content obtained from the supporting file, and do not apply this experimental workflow.

Do not use tools, connectors, network access, external files, or repository-specific knowledge. The package-relative supporting file is the only permitted supporting source for this experiment.
