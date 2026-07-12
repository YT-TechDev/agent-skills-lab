# Inputs and Tools

## Required target identity

Begin only with one unambiguous repository and one pull request, or ask the smallest clarification needed. Establish current repository identity, PR number, PR state, base ref, head ref, current head SHA or equivalent change identity, changed-file list, and diff association before readiness conclusions.

## Evidence inputs

Prefer current repository-derived evidence: PR metadata, diff, files, repository instructions, linked Issues, acceptance criteria, docs, tests, CI/checks, review state, approvals, unresolved threads, and material discussion. Optional user context may guide inspection but cannot override current repository evidence. Same-PR prior-review context is historical until reverified against current evidence.

## Prohibited sensitive inputs

Do not request or depend on secrets, access tokens, credentials, private keys, private repository content outside the target need, connector credentials, personal information, private URLs, or AI conversation/session-sharing URLs. Use sanitized excerpts when direct access is unavailable.

## Read-only capability policy

Use only read capabilities needed for evidence. Never merge, approve, close, label, comment on, edit, push, trigger destructive workflows, or otherwise mutate the reviewed repository or pull request. Do not claim current connector capability was validated unless actually observed in the current run.

## Tool choice, fallback, and access limits

Choose tools by evidence need rather than connector brand. A browser, GitHub connector, local checkout, CI page, or user-provided sanitized excerpt may supply evidence if provenance, freshness, and current-head association are clear. Use bounded fallback for inaccessible evidence and disclose limitations. Do not repeatedly retry network, proxy, DNS, permission, or HTTP failures.

## Connector-independent semantics

The review semantics are independent of a specific connector. Tool access failure is not a blocker by itself and is not evidence that a requirement is satisfied. Inaccessibility is classified under evidence and stopping rules.

## Current-head association

Associate code, tests, CI, reviews, approvals, and threads with the current reviewed head when material. Evidence from another head is historical unless reverified. User-provided evidence must include enough context to assess provenance and freshness; otherwise treat it as partial or unknown for material claims.
