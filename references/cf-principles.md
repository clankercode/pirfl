# Critical fallibilist principles for PIRFL

## Contents

- Practical interpretation
- Idea-goal-context triples
- Error and criticism
- Review norms
- Applying CF without overdoing philosophy
- Source trail

## Practical interpretation

PIRFL is inspired by Critical Fallibilism (CF), Critical Rationalism, and related error-correction ideas. It uses them as practical workflow heuristics, not as a demand that every task become a philosophy debate.

Use these principles to make work more correctable:

1. Treat outputs as conjectures.
2. Make goals and context explicit.
3. Search for errors that matter for those goals.
4. Fix known errors.
5. Repeat while the loop is still finding material failures.

## Idea-goal-context triples

Evaluate an artifact as an `{idea, goal, context}` triple:

- **Idea**: the plan, patch, draft, answer, calculation, artifact, or subclaim.
- **Goal**: what it is supposed to accomplish.
- **Context**: constraints, user situation, available tools, input facts, audience, risk level, and environment.

The same idea can succeed for one goal/context and fail for another. Reviewers should avoid saying “this is bad” without saying what goal/context it fails.

Use an IGC matrix when comparing options:

| Idea | All | Goal 1 | Goal 2 | Goal 3 |
|---|---:|---:|---:|---:|
| Option A | ? | ✔ | ? | ✔ |
| Option B | ✘ | ✔ | ✘ | ✔ |

`All` is ✘ if any required goal is ✘; otherwise ? if any required goal is ?; otherwise ✔.

## Error and criticism

An **error** is a reason an idea fails at a goal in context. A **criticism** explains such an error.

A good PIRFL criticism is concrete:

```markdown
Issue: [short name]
Artifact/location: [file, section, claim, output]
Idea: [what is being criticized]
Goal: [goal it is supposed to meet]
Context: [relevant constraints/facts]
Evidence: [test failure, contradiction, missing requirement, source mismatch]
Why it matters: [how this blocks or degrades the goal]
Suggested fix/check: [specific next step]
Severity: blocker | major | minor
```

Prefer decisive criticisms over vague concerns. “This may be bad” is weak unless it identifies a plausible failure mode and a check or fix.

## Review norms

- Separate generation from criticism: first brainstorm or implement, then review.
- Do not seek praise; seek useful error reports.
- Do not use reviewer vote counts as truth. Aggregate by issue and evidence.
- “No known error” is not certainty. It is a practical state for proceeding.
- A criticism can itself be criticized. Reject a review issue only by explaining why it does not show failure for the goal/context.
- Prefer binary issue states for required goals: accepted, rejected, duplicate, deferred, resolved, unknown.

## Applying CF without overdoing philosophy

Use the minimum philosophical machinery that improves the task. For a tiny task, this may be one sentence: “I’ll check the result against the goal before finalizing.” For a high-stakes task, use explicit IGC triples, independent reviewers, and a tracked issue log.

PIRFL should improve outcomes, not become a ritual. If the loop is no longer finding material errors, stop and deliver.

## Source trail

- Critical Fallibilism overview: https://criticalfallibilism.com/
- Introduction to Critical Fallibilism: https://criticalfallibilism.com/introduction-to-critical-fallibilism/
- CF terminology and partial truth / IGC framing: https://criticalfallibilism.com/critical-fallibilism-terminology-and-partial-truth/
- Question-based CF outline: https://criticalfallibilism.com/question-based-critical-fallibilism-epistemology-outline/
- Practice thinking in terms of error correction: https://criticalfallibilism.com/practice-thinking-in-terms-of-error-correction/
- IGC skill gist supplied by the user: https://gist.githubusercontent.com/XertroV/29cc4765829892872c645cadaf84a1ca/raw/d9e10f214eb47d13b9ad0095ccbbda7f53050355/igc-skill.md
- General fallibilism reference: https://iep.utm.edu/fallibil/
