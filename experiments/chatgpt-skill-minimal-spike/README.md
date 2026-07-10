# Minimal ChatGPT Skill Behavior Spike

## Status

- maturity: experimental
- first owner-side observation: recorded
- selected deterministic behavior reproduction: established under the recorded controlled conditions
- automatic invocation: unverified
- production readiness: not applicable

## Recorded observations

- [First owner-side run — 2026-07-10](observations/2026-07-10-first-owner-run.md)
- [Controlled reproduction — 2026-07-10](observations/2026-07-10-controlled-reproduction.md)
- direct `SKILL.md` upload was observed
- selected deterministic token behavior was observed and selected explicit-token behavior was reproduced under recorded controlled conditions
- selected deterministic missing-token behavior was observed and reproduced under recorded controlled conditions
- selected marker suppression was observed and reproduced under recorded controlled conditions
- automatic invocation remains unverified
- the package remains experimental

## Experiment question

Can a minimal hypothesized Skill package be accepted by the platform and provide deterministic behavior during an explicit owner-run invocation?

## Why this experiment exists

This experiment is the smallest first behavior-discovery slice after repository foundation work. It prepares an isolated package and manual protocol so later owner-side testing can record evidence without mixing expectations with observations.

This is not the production `github-standard-engineering-review` Skill.

## Package under test

```text
package/
└── SKILL.md
```

The package deliberately contains no supporting files.

## Package hypothesis

- The package directory and `SKILL.md` format are test inputs.
- Any metadata or frontmatter is a hypothesis.
- Repository presence does not prove platform acceptance.
- Successful upload or installation would not by itself prove correct invocation.
- Deterministic output would not by itself prove host-platform invocation.

## Scope

- package or installation acceptance
- explicit owner-selected invocation
- deterministic token response
- missing-token behavior
- non-trigger marker suppression

## Non-goals

- supporting-file loading
- automatic broad invocation
- Project instruction interaction
- tools and connectors
- GitHub integration
- Standard Review
- Deep Review
- production packaging
- automated evaluation
- installation scripts

## Manual test prerequisites

The owner-run test should use:

- a supported ChatGPT interface capable of installing or using Skills
- the exact package contents from the reviewed commit
- a recorded test date
- relevant product, model, Project, and configuration context
- sanitized screenshots or notes only when safe and useful

Do not include private session links.

## Safety and privacy constraints

Owner-side testing must:

- not include secrets or credentials
- not include personal information
- not use private repository content
- not store private URLs
- not store AI conversation or session-sharing URLs
- use only a synthetic token such as `ORBIT-7`
- sanitize screenshots and notes
- capture only the minimum UI evidence necessary
- avoid copying unrelated conversation content
- stop if evidence cannot be recorded safely

## Manual test procedure

These steps describe a later owner-run test. They were not run in this repository change.

1. Identify the exact commit being tested.
2. Inspect and archive the exact package contents.
3. Attempt package installation or availability through the supported owner-facing workflow.
4. Record whether the platform accepts, rejects, or transforms the package.
5. Record visible platform evidence of Skill availability or invocation where available.
6. Run the explicit-token case.
7. Run the missing-token case.
8. Run the non-trigger case.
9. Record expected and observed results separately.
10. Classify platform findings using repository terminology.
11. Record limitations and unresolved questions.
12. Do not call the behavior reproduced until it is repeated under comparable conditions.

## Evidence to record later

- date in `YYYY-MM-DD`
- tested commit
- exact package hash or contents when practical
- product surface
- model or runtime
- Project instructions
- tool and connector availability
- installation result
- invocation evidence
- prompts
- outputs
- expected versus observed differences
- limitations
- unresolved questions

## Interpretation guardrails

- package acceptance does not prove invocation
- output compliance does not prove platform invocation
- one successful run is not reproduction
- failure may reflect the package, platform, workflow, configuration, or unsupported assumption
- inaccessible evidence must remain UNKNOWN
- no result should be generalized beyond the tested conditions

## Stopping conditions

Stop and record limitations when:

- the platform workflow is unavailable
- package installation is inaccessible
- platform evidence cannot distinguish invocation from normal prompt following
- the package is transformed unexpectedly
- tested contents differ from the reviewed commit
- required context cannot be recorded safely
- results are contradictory

## Next experiment boundary

Later Issues may separately test:

- owner-run installation and invocation observations
- supporting-file availability
- Project instruction interaction
- explicit versus automatic invocation
- tool and connector behavior
- packaging changes

Do not implement those experiments now.
