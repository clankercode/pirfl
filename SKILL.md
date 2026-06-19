---
name: pirfl
description: Runs a fallibilist plan-implement-review-fix loop (PIRFL) for complex tasks, coding, writing, research, document work, and multi-task projects. Use when the user wants robust execution, iterative critique, validation, subagent review, error correction, or review-and-fix loops. Do not use for trivial one-step requests.
license: MIT
compatibility: Works in skills-compatible agents. Subagent steps are optional; simulate independent review passes when no subagent tool exists.
metadata:
  version: "1.0.0"
  aliases: "plan-implement-review-fix-loop,error-correcting-workflow,fallible-workflow"
---

# PIRFL: Plan → Implement → Review → Fix → Loop

PIRFL is an error-correction workflow for nontrivial work. Treat plans and outputs as conjectures, actively look for known errors, fix them, and loop until the artifact is fit for the user's goal or remaining limits are explicit.

## Trigger guard

Use PIRFL when the task has multiple steps, multiple files, meaningful ambiguity, costly mistakes, user-visible artifacts, code changes, research synthesis, or the user asks for planning, implementation, critique, validation, iteration, subagents, or review/fix loops.

Skip PIRFL for simple one-shot tasks where a full loop would add noise. For medium tasks, use a lightweight PIRFL pass: brief plan, implement, one self-review, quick fix, final.

## Operating stance

- Goals first: evaluate work against explicit `{idea, goal, context}` triples, not vibes.
- Fallibilism: no plan or review is final proof. “No known error found” is enough to proceed, but not a claim of certainty.
- Criticism over praise: reviews should identify concrete ways an artifact fails a goal in context. Praise is optional and usually low-value.
- Conjecture and criticism are separate modes, but both are creative: brainstorm candidate approaches before judging them; then criticize and eliminate known failures.
- Transparency: never hide known unresolved errors. If a limitation remains, state it plainly in the final answer.
- Proportionality: scale the loop to the task. Avoid ceremony when the user needs a small answer.

For philosophy and methodological details, read [references/cf-principles.md](references/cf-principles.md).

## Workflow

### 1. Intake and task model

Create a compact task model before acting:

- User goal and deliverable.
- Required context, constraints, inputs, deadlines, style, safety, and acceptance criteria.
- Assumptions you can safely make; blockers that truly require a user answer.
- Tests, validators, citations, or review criteria that can reveal errors.
- If the runtime provides a session goal, idle reminder, or similar goal-setting tool, set a concise goal for the whole task early, then clear or complete it when the PIRFL loop exits.

If there are multiple tasks, choose an orchestration strategy before implementation. See [references/multi-task-orchestration.md](references/multi-task-orchestration.md) for details.

### 2. Plan

Write the smallest useful plan that can guide implementation and review:

- Break the task into deliverable slices.
- Identify dependencies and irreversible/destructive steps.
- Choose validation methods before implementing.
- For risky or batch operations, create a plan artifact first and validate it before execution.

Do not over-plan. The plan is a conjecture to improve, not a contract to defend.

### 3. Implement

Implement the next slice or the whole task, depending on size:

- Prefer reversible, checkable changes.
- Keep notes on decisions that reviewers should examine.
- Run obvious mechanical checks immediately: tests, linters, schema validation, link checks, file open/read checks, source verification, or artifact inspection.
- When creating files, verify that the files exist and are usable before finalizing.

### 4. Review

Run at least one review pass for nontrivial tasks. When subagents or child tasks are available, use fresh independent reviewers for complex, high-risk, or multi-domain tasks. If subagents are unavailable, simulate separate reviewer passes and label them internally.

Default reviewer roles:

- Goal-fit critic: checks whether the output satisfies the user’s actual goal and context.
- Correctness critic: checks factual, logical, code, data, or artifact correctness.
- Edge-case critic: searches for failure modes, missing constraints, and brittle assumptions.
- Integration critic: for multi-task work, checks consistency across deliverables.

Ask reviewers for issue records, not general impressions. A useful issue includes: artifact/location, failing goal/context, evidence, severity, proposed fix or verification. See [references/subagent-prompts.md](references/subagent-prompts.md) and [assets/reviewer-report-template.md](assets/reviewer-report-template.md).

### 5. Fix

Aggregate review findings by issue, not by vote count. Duplicate reports make an issue easier to notice but do not make it truer.

For each issue:

- Accept it if it identifies a concrete failure against a goal/context or a failed test.
- Reject it only with a reason tied to the goal/context.
- Defer it only if it is outside scope, low-value, or blocked; mention material deferrals in the final answer.
- Fix accepted blocker and major issues before finalizing unless a user-imposed limit prevents it.

### 6. Loop

After fixes, re-review the changed parts. Run a broader review if the fix changed the plan, architecture, argument, data pipeline, or user-facing structure.

Stop when one of these exit gates is true:

- No accepted blocker or major issue remains against required goals.
- Mechanical validators pass and targeted re-review finds no new accepted blocker/major issues.
- A user/developer/tool limit prevents further work; final output explicitly lists remaining known errors or risks.
- Further work is only preference polish and the user did not ask for that level of refinement.

For a detailed issue-state loop, read [references/loop-protocol.md](references/loop-protocol.md).

### 7. Final response

Give the user the result, not the whole scratchpad. Include only useful process evidence:

- What was delivered.
- What checks/reviews were done.
- Important assumptions or unresolved risks.
- Links/paths to created artifacts when applicable.

Do not claim the result is perfect. Say what is known to have passed and what remains uncertain.

## Multi-task default

When the user gives multiple tasks, first classify them:

- Shared deliverable or shared source of truth: aggregate into one PIRFL workflow with one integrated review.
- Independent deliverables: run separate PIRFL workflows, parallelizing with subagents when available.
- Dependency chain: plan the dependency order, implement upstream tasks first, then review integration.
- Many small homogeneous tasks: batch the implementation, then use shared validators and sampled plus targeted review.

Use [assets/task-portfolio-template.md](assets/task-portfolio-template.md) for large task sets.

## Work log

For complex tasks, keep a private or file-based PIRFL log. Use [assets/pirfl-log-template.md](assets/pirfl-log-template.md), or generate one with:

```bash
python scripts/new_pirfl_log.py "Task title" --out pirfl-log.md
```

Only share the log if the user asks or it is useful as a deliverable.

## Gotchas

- Do not ask for clarification when a safe assumption is enough; proceed and label the assumption.
- Do not let review become endless. Loop only while it is finding material errors or the task’s stakes justify more checking.
- Do not treat a reviewer’s preference as an error unless it affects a stated or inferred goal.
- Do not let reviewers see each other’s reports before their first pass unless the goal is focused verification.
- Do not count “positive reasons” as sufficient validation. Prefer tests, examples, citations, or concrete failure checks.
- Do not bury known errors under a polished final answer.
