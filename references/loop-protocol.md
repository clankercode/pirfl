# Error-correction loop protocol

## Contents

- Review packet
- Reviewer independence
- Issue states
- Severity rubric
- Fix rules
- Re-review rules
- Exit gates

## Review packet

Before review, prepare a compact packet:

```markdown
Task: [one sentence]
User goal: [goal]
Context/constraints: [facts, files, audience, risk]
Artifact(s): [paths or sections]
Acceptance checks: [tests, citations, visual inspection, rubric]
Known assumptions: [assumptions already made]
Reviewer request: Find concrete errors against the goal/context. Use issue records.
```

Do not overload reviewers with irrelevant history. Give enough context to find errors.

## Reviewer independence

For complex tasks, use independent first-pass reviewers:

1. Send the same review packet to each reviewer.
2. Do not include other reviewers’ findings in the first pass.
3. Ask each reviewer to output issue records only.
4. Aggregate after all first-pass reviews return.
5. Run targeted follow-up review on accepted fixes.

If the environment has no subagents, simulate this by making separate passes with different reviewer hats and not reusing conclusions until aggregation.

## Issue states

Track every material issue with one state:

- `open`: reported but not triaged.
- `accepted`: shows a real failure against goal/context.
- `rejected`: does not show a failure; reason recorded.
- `duplicate`: same underlying issue as another record.
- `deferred`: real or plausible issue, but outside current scope or blocked.
- `resolved`: accepted issue fixed and checked.
- `unknown`: insufficient evidence; needs a check if material.

## Severity rubric

- **Blocker**: violates a must-have requirement, produces invalid/unusable output, creates serious safety/security/legal/data-loss risk, or makes the main answer wrong.
- **Major**: substantially harms usefulness, correctness, maintainability, user trust, or integration; should normally be fixed before delivery.
- **Minor**: polish, small clarity issue, non-critical edge case, or optional improvement.

Severity depends on the user’s goal and context. A typo in a legal filing may be major; a typo in private scratch notes is minor.

## Fix rules

- Fix accepted blockers and majors before finalizing unless a hard limit prevents it.
- Fix minors when cheap and unlikely to introduce new risk.
- For each rejected issue, record the reason in terms of goal/context.
- For each deferred issue, record why it is deferred and whether the user should know.
- After any nontrivial fix, run a targeted check to avoid regression.

## Re-review rules

Use targeted re-review when fixes are local. Use broad re-review when the fix changes architecture, argument structure, data model, citation basis, public-facing wording, security posture, or cross-task integration.

A simple loop can be:

```text
review → aggregate → triage → fix blockers/majors → targeted re-review → finalize
```

A robust loop can be:

```text
review → aggregate → triage → fix → targeted re-review → broad adversarial review → fix → final verification
```

## Exit gates

Exit the loop when:

1. Required validators pass.
2. No accepted blocker/major issue remains.
3. Targeted re-review of fixes finds no new blocker/major issue.
4. Remaining issues are minor, out-of-scope, or explicitly disclosed.

If a hard limit prevents clean exit, deliver the best current artifact and disclose the unresolved accepted issues or unknowns.
