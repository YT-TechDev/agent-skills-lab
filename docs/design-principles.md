# Skill Design Principles

This document defines durable design principles for reusable AI agent Skills developed in this repository. The principles guide design and review decisions; they are not the complete workflow for any specific Skill, and they do not claim undocumented or untested platform behavior.

## Principles

### 1. One clear job per Skill

**Rule:** Each Skill should perform one clearly defined job.

**Why it matters:** A clear job makes the Skill easier to specify, invoke, review, validate, and maintain.

**Practical consequence:** Define the job before implementation, reject unrelated responsibilities, split broad workflows into composable Skills, and avoid universal agents that review, implement, release, merge, and audit at once.

### 2. Prefer small composable Skills

**Rule:** Prefer small Skills with explicit boundaries over broad multi-purpose agents.

**Why it matters:** Composition improves testability, trigger precision, maintainability, independent versioning, and failure isolation.

**Practical consequence:** Design Skills that can cooperate without defining a permanent composition framework before evidence shows one is needed.

### 3. Define scope and explicit non-goals

**Rule:** Every production-target Skill specification should define what the Skill does, what it may inspect, what it does not do, and what requires escalation.

**Why it matters:** Explicit non-goals prevent unsupported completion claims and uncontrolled scope expansion.

**Practical consequence:** Review new Skill work for boundaries before implementation begins, and treat unclear non-goals as a specification gap.

### 4. Design precise trigger and non-trigger behavior

**Rule:** Define both trigger cases and non-trigger cases.

**Why it matters:** A Skill should not be judged only by whether it succeeds after invocation; it must also avoid false invocation, missed invocation, activation on requests outside its job, and continuation when mandatory inputs are missing.

**Practical consequence:** Include examples or criteria for when the Skill should run, when it should not run, and when it should stop for missing inputs without claiming any currently observed ChatGPT Skills trigger behavior.

### 5. Separate Project context, Skill procedure, and conversation constraints

**Rule:** Keep Project context, reusable Skill procedure, and current conversation constraints distinct.

**Why it matters:** Project context contains repository-specific goals, rules, architecture, and conventions; a Skill contains the reusable procedure; the current conversation contains temporary task constraints and immediate user intent.

**Practical consequence:** Do not embed repository-specific details in reusable Skill packages unless those details are provided as inputs.

### 6. Base important conclusions on evidence

**Rule:** Important conclusions must be traceable to evidence.

**Why it matters:** Confidence or fluent wording is not a substitute for inspected evidence.

**Practical consequence:** Support consequential claims with source code, diffs, repository documentation, Issue acceptance criteria, PR discussions, tests, CI results, connector or tool results, or directly observed platform behavior.

### 7. Distinguish fact, inference, and unknown

**Rule:** Outputs and internal decisions should distinguish verified facts, reasonable inferences, and unknowns.

**Why it matters:** Missing evidence must not be converted into an assumption of success or failure.

**Practical consequence:** Use requirement-status labels when helpful, such as VERIFIED, PARTIAL, MISSING, UNKNOWN, and NOT APPLICABLE, without defining a final output schema for `github-standard-engineering-review`.

### 8. Avoid unsupported claims

**Rule:** A Skill must not claim that tests passed, behavior works, evidence was reviewed, a package is valid, a PR is safe, a requirement is complete, or a trigger worked correctly unless supporting evidence was available and inspected.

**Why it matters:** Graceful uncertainty is preferable to fabricated certainty.

**Practical consequence:** State what was checked, what was not checked, and what conclusion remains unsupported.

### 9. Fail gracefully when evidence or tools are unavailable

**Rule:** Skills should define stopping and failure behavior for inaccessible evidence, missing inputs, and unavailable tools.

**Why it matters:** Continuing without required evidence can produce unsafe or unsupported decisions.

**Practical consequence:** Report unavailable evidence, explain which conclusion cannot be verified, avoid inventing results, avoid unsupported decisions, and identify the smallest missing input or experiment needed to continue.

### 10. Control tool and connector usage

**Rule:** Use tools and connectors only when they materially support the Skill's job.

**Why it matters:** Unbounded tool use can create privacy, safety, reliability, and write-scope risks.

**Practical consequence:** Define required tools, optional tools, fallback behavior, behavior when access is denied, and read versus write boundaries. Write-capable or destructive behavior requires explicit user intent and safeguards.

### 11. Prefer safe and reversible behavior

**Rule:** Skills should default to read-only inspection, scoped changes, reversible actions, explicit confirmation before destructive actions, and preservation of user control.

**Why it matters:** Safe defaults reduce the cost of mistakes and keep authority with the user.

**Practical consequence:** Keep review and recommendation separate from automatic mutation unless the Skill's job explicitly requires writes.

### 12. Use the smallest experiment needed to resolve an unknown

**Rule:** Unknown platform or Skill behavior should be investigated through the smallest focused experiment that can answer the question.

**Why it matters:** Small experiments reduce noise, cost, and accidental overgeneralization.

**Practical consequence:** Record the question, expected behavior, observed behavior, interpretation, unresolved questions, and observation date when behavior may change, without recording actual platform findings in this design document.

### 13. Treat platform behavior as version-sensitive evidence

**Rule:** Do not present platform behavior as permanent fact merely because it was seen once.

**Why it matters:** Platform behavior can change, and production design should depend only on evidence appropriate to the required confidence level.

**Practical consequence:** Classify platform research as Observed, Reproduced, Inferred, Unverified, or Changed since previous test. Do not claim that any ChatGPT Skills behavior has already been observed or reproduced unless separate evidence records support that claim.

### 14. Keep SKILL.md focused

**Rule:** `SKILL.md` should contain the main operational workflow.

**Why it matters:** One enormous prompt file is harder to review, test, version, and maintain.

**Practical consequence:** Move detailed content into supporting files when that improves clarity, including rubrics, policies, examples, schemas, templates, and detailed decision tables, without defining the final package layout for all future Skills.

### 15. Validate before packaging

**Rule:** A Skill should not be treated as stable merely because it has been written.

**Why it matters:** Representative validation is needed before relying on the Skill for packaging or installation decisions.

**Practical consequence:** Validate high-level representative cases before packaging, such as successful, blocked, ambiguous, inaccessible-evidence, missing-input, non-trigger, and escalation cases, without duplicating a full evaluation strategy.

### 16. Keep packaging and version status explicit

**Rule:** Skill packages should state their maturity and validation status.

**Why it matters:** Version numbers and packaging labels can create false confidence if they imply validation that has not occurred.

**Practical consequence:** Use concepts such as experimental, production-target, validated, or stable only when the status matches actual evidence, without defining a permanent repository-wide versioning schema here.

### 17. Separate Standard Review from Deep Review

**Rule:** `github-standard-engineering-review` has a bounded merge-readiness job.

**Why it matters:** Standard Review must not imply completion of a full security audit, privacy audit, architecture audit, dependency audit, or release-critical audit.

**Practical consequence:** Standard Review may recommend escalation when changes involve security-sensitive behavior, privacy boundaries, architecture boundaries, native code, destructive data operations, dependency risk, or release-critical behavior, without defining the complete Standard Review workflow or rubric.

## Common failure patterns

- **Premature abstraction:** Adds frameworks or layers before evidence shows they are needed, making small Issues harder to review.
- **Broad universal prompts:** Combines unrelated responsibilities and weakens trigger precision.
- **Mixing review and implementation:** Blurs whether the Skill should evaluate work or change it.
- **Combining review, merge, release, and deep audit:** Creates unsafe authority boundaries and unsupported completion claims.
- **Claiming unobserved platform behavior:** Treats assumptions as facts and misleads future design work.
- **Treating one successful example as sufficient validation:** Hides failure modes that representative cases would expose.
- **Adding scripts, frameworks, schemas, or dependencies for appearance:** Increases maintenance cost without demonstrated need.
- **Leaking repository-specific rules into reusable packages:** Makes a Skill less portable and harder to reuse in other contexts.
- **Presenting future structures as already implemented:** Confuses roadmap intent with current repository evidence.
- **Hiding unknowns behind confident language:** Prevents reviewers from seeing what still needs evidence.
- **Creating one enormous `SKILL.md`:** Makes review, testing, versioning, and maintenance harder.
- **Packaging an unvalidated Skill as stable:** Implies reliability that the repository has not demonstrated.

## Decision checklist

- Does the Skill have one clear job?
- Are scope and non-goals explicit?
- Are trigger and non-trigger cases defined?
- Are important conclusions evidence-backed?
- Are unavailable evidence and tool failures handled?
- Is Project context separated from reusable procedure?
- Is escalation defined?
- Has representative validation occurred?
- Does packaging status match the evidence?
