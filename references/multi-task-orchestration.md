# Multi-task orchestration

## Contents

- Task portfolio
- Strategy selection
- Subagent distribution
- Integration review
- Avoiding loop explosion

## Task portfolio

For multiple tasks, create a portfolio before implementation:

| Task | Goal | Context | Inputs | Dependencies | Validation | Status | Known errors |
|---|---|---|---|---|---|---|---|
| T1 |  |  |  | none |  | planned |  |

Use [../assets/task-portfolio-template.md](../assets/task-portfolio-template.md) for larger projects.

## Strategy selection

Choose one of these patterns:

### Aggregate workflow

Use when tasks contribute to one deliverable or share one source of truth. Plan once, implement slices, then run an integrated review.

Examples: create a report with sections, update a codebase feature spanning files, prepare a launch checklist.

### Separate PIRFL workflows

Use when tasks are independent deliverables. Each task gets its own plan, implementation, review, fix, and exit gate.

Examples: summarize three unrelated documents, create separate scripts, answer unrelated research questions.

### Dependency pipeline

Use when one task feeds another. Run PIRFL on upstream tasks first, then review downstream integration.

Examples: clean data → analyze data → write report; design API → implement client → update docs.

### Parallel subagent workflows

Use when tasks are independent enough for separate workers. Give each subagent:

- a task-specific goal/context,
- expected output format,
- shared constraints,
- validation criteria,
- instruction to report known errors.

Then use an integration critic to check consistency across outputs.

### Batch workflow

Use for many small homogeneous tasks. Plan the batch, implement all or a safe chunk, run shared validators, sample-review typical outputs, and targeted-review anomalies.

## Subagent distribution

A useful distribution for complex multi-task work:

1. Planner/integrator: builds portfolio and dependencies.
2. Worker agents: implement independent tasks.
3. Reviewer agents: review outputs independently.
4. Fixer or original worker: fixes accepted issues.
5. Final integrator: checks consistency and user-facing packaging.

Do not let worker agents mark their own work as final without independent review when stakes are meaningful.

## Integration review

After per-task review, check:

- consistent terminology, style, filenames, APIs, and assumptions,
- no duplicate or contradictory outputs,
- dependencies were satisfied in the right order,
- shared constraints were applied to every task,
- final packaging is complete and navigable.

## Avoiding loop explosion

Do not run unlimited full loops on every subtask by default. Scale review depth by risk:

- Full PIRFL: high-risk, user-visible, destructive, or central tasks.
- Lightweight PIRFL: routine subtasks.
- Shared validation: homogeneous batches.
- Escalation: if sampled review finds a systemic error, widen review to the whole batch.
