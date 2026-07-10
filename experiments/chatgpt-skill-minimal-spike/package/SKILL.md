---
name: minimal-behavior-spike
description: An explicitly invoked experimental Skill that returns a deterministic marker for behavior-discovery testing.
---
# Minimal Behavior Spike

Use this experimental behavior only when the user explicitly asks to run the minimal behavior spike.

When the user provides a token, output exactly:

```text
SPIKE_ACTIVE
token: <exact token>
```

Preserve the token exactly as provided.

When the user explicitly asks to run the spike but provides no token, output exactly:

```text
SPIKE_INPUT_REQUIRED
```

For unrelated requests, do not output `SPIKE_ACTIVE` or `SPIKE_INPUT_REQUIRED`.

Do not use tools, connectors, external files, network access, or repository-specific knowledge.
