# Research notes behind this skill

Date: 2026-06-12

## Skill-format decisions

- A skill is packaged as a folder with required `SKILL.md` and optional scripts, references, and assets.
- `SKILL.md` frontmatter includes `name` and `description`; the folder name should match the skill name for broad compatibility.
- The main file should stay concise and use progressive disclosure: detailed philosophy, prompts, templates, and evals live in separate files.
- Description quality matters for activation. This pack keeps the opaque user-preferred name `pirfl`, but makes the description explicit about plan/implement/review/fix loops, subagent review, validation, and complex tasks.
- Workflows benefit from checklists and validation loops. PIRFL makes review/fix a first-class loop rather than an afterthought.

## Critical fallibilist decisions

- The workflow evaluates outputs in `{idea, goal, context}` form, following the IGC framing in the user-provided gist and CF material.
- Reviews ask for concrete error reports rather than praise or weighted scores.
- “No known error” is treated as a practical exit state, not a proof of correctness.
- The loop stops when no accepted blocker/major issues remain, or when a hard limit forces disclosure of remaining errors.

## Sources consulted

### Agent skill format and authoring

- OpenAI Codex Agent Skills docs: https://developers.openai.com/codex/skills
- OpenAI cookbook example for skills in the API: https://developers.openai.com/cookbook/examples/skills_in_api
- Agent Skills open specification: https://agentskills.io/specification
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
- Agent Skills optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- Agent Skills evaluating skills: https://agentskills.io/skill-creation/evaluating-skills
- Anthropic Agent Skills overview: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic Skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices

### Critical Fallibilism and fallibilism

- User-provided IGC skill gist: https://gist.githubusercontent.com/XertroV/29cc4765829892872c645cadaf84a1ca/raw/d9e10f214eb47d13b9ad0095ccbbda7f53050355/igc-skill.md
- Critical Fallibilism home: https://criticalfallibilism.com/
- Introduction to Critical Fallibilism: https://criticalfallibilism.com/introduction-to-critical-fallibilism/
- Critical Fallibilism terminology and partial truth: https://criticalfallibilism.com/critical-fallibilism-terminology-and-partial-truth/
- Question-based CF epistemology outline: https://criticalfallibilism.com/question-based-critical-fallibilism-epistemology-outline/
- Practice thinking in terms of error correction: https://criticalfallibilism.com/practice-thinking-in-terms-of-error-correction/
- Fallibilism, Internet Encyclopedia of Philosophy: https://iep.utm.edu/fallibil/
