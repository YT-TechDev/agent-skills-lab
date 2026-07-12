# Examples and Evaluation

Golden cases guide evaluation but do not override policy. This draft has not executed or passed golden cases, smoke cases, or a full suite. Do not make fictional execution claims.

## Compact golden-case index

| Case | Scenario purpose | Expected ending/verdict | Policy category | Prohibited false claim |
| --- | --- | --- | --- | --- |
| `TRG-01` | Complete Standard Review request | `NO VERDICT` until evidence workflow reaches verdict | Trigger/intake | Do not claim runtime trigger success. |
| `TRG-02` | Repository or PR identity unresolved | `NO VERDICT` | Clarification | Do not guess target identity. |
| `TRG-03` | Implementation-only or merge-only request | `NO VERDICT` | Redirect/decline | Do not review, implement, or merge anyway. |
| `TRG-04` | Deep-Review-only request | `NO VERDICT` | Deep Review boundary | Do not claim Deep Review completed. |
| `TRG-05` | Cancellation or material target replacement | `NO VERDICT` | Cancellation/target replacement | Do not issue stale verdict. |
| `POS-01` | Clean current-head review | `MERGE READY` | Positive verdict | Do not claim perfection or release readiness. |
| `POS-02` | Genuine optional improvement | `MERGE READY WITH NON-BLOCKING NOTES` | Optional notes | Do not convert optional work into blocker. |
| `POS-03` | Optional Deep Review recommendation | `MERGE READY WITH NON-BLOCKING NOTES` | Escalation | Do not claim Deep Review was done. |
| `BLK-01` | Verified correctness defect on current head | `NOT MERGE READY` | Blocker | Do not hide verified defect behind notes. |
| `BLK-02` | Failed required CI on current head | `NOT MERGE READY` | Required CI | Do not call failed required CI inaccessible or passing. |
| `BLK-03` | Required CI pending after final refresh | `NOT MERGE READY` | Required CI | Do not treat pending required CI as passed. |
| `BLK-04` | Missing required approval or specialist review | `NOT MERGE READY` | Required approval | Do not ignore required review state. |
| `BLK-05` | Verified blocker plus unrelated inaccessible evidence | `NOT MERGE READY` | Precedence | Do not downgrade verified blocker to gap. |
| `GAP-01` | Current head identity unavailable | `UNABLE TO VERIFY` | Target integrity | Do not infer head identity. |
| `GAP-02` | Material diff coverage inaccessible | `UNABLE TO VERIFY` | Coverage gap | Do not claim inspected files. |
| `GAP-03` | Required CI state inaccessible | `UNABLE TO VERIFY` | CI gap | Do not treat inaccessible CI as pass/fail. |
| `GAP-04` | Required review/thread state inaccessible | `UNABLE TO VERIFY` | Review gap | Do not claim approvals or resolved threads. |
| `GAP-05` | Contradictory material requirements | `UNABLE TO VERIFY` | Conflict | Do not silently reconcile conflict. |
| `GAP-06` | Head changes twice in one invocation | `UNABLE TO VERIFY` | Unstable head | Do not combine different heads. |
| `RRV-01` | Prior blocker fixed and full current review passes | `MERGE READY` | Re-review | Do not carry old blocker forward. |
| `RRV-02` | Fix reported but not verifiable | `UNABLE TO VERIFY` | Re-verification | Do not accept unverified fix. |
| `RRV-03` | One prior blocker fixed, another remains | `NOT MERGE READY` | Re-review blocker | Do not claim all blockers fixed. |

## Evaluation layers and statuses

Keep separate: specification conformance, observed Skill behavior, tool/connector capability, and repository static validation. Evaluation statuses are `PASS`, `FAIL`, `PARTIAL`, `INCONCLUSIVE`, and `NOT APPLICABLE`; they are not verdicts.

Critical dimensions include trigger precision, target/head integrity, evidence coverage, blocker detection, false-blocker avoidance, material-gap handling, verdict selection, output-contract compliance, re-review behavior, unsupported-claim avoidance, Standard/Deep boundary, and graceful failure.

Selected smoke tests do not replace the full minimum suite. Regression expectations require comparing observed outputs against the same case IDs, exact package identity, dated product surface, available tools, and known limitations. Unsupported-claim auditing must check that absent or inaccessible evidence is not presented as verified.

Use research labels `Observed`, `Reproduced`, `Inferred`, `Unverified`, and `Changed since previous test`. First success is `Observed`, not automatically `Reproduced`. Package acceptance and supporting-file access are separate observations. Internal loading remains `UNKNOWN` unless separately established. Exact package acceptance, supporting-file accessibility, selected smoke cases, full suite, runtime regression baseline, publication, package version, and production readiness are not established by this draft.
