---
name: error-correction-loop
description: Reviews and fixes an existing artifact through a fallibilist error-correction loop using independent critic subagents when available. Use when the user asks for iterative critique, validation, QA, reviewer subagents, or a review/fix loop on a draft, patch, plan, report, or file.
license: Unlicense OR CC0-1.0
compatibility: Works in skills-compatible agents. Subagent steps are optional; simulate independent review passes when unavailable.
metadata:
  version: "1.0.0-template"
---

# Error-Correction Loop

This is an optional standalone companion skill template extracted from PIRFL. To use it as its own skill, copy this file to `error-correction-loop/SKILL.md` in your skills directory. It is intentionally not named `review-and-fix`.

## Workflow

1. Build a review packet: goal, context, artifact, acceptance criteria, known assumptions.
2. Run independent reviewers when available: goal-fit, correctness, edge-case, integration.
3. Require issue records with location, failing goal/context, evidence, severity, and proposed fix/check.
4. Aggregate by issue, not vote count.
5. Triage states: accepted, rejected, duplicate, deferred, resolved, unknown.
6. Fix accepted blocker and major issues.
7. Re-review changed parts.
8. Stop when no accepted blocker/major remains or disclose remaining known errors.

## Final response

Report the improved artifact, checks performed, and any material remaining risks. Do not claim certainty or perfection.
