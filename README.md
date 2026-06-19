# pirfl

`pirfl` is a skill for a fallibilist **Plan → Implement → Review → Fix → Loop** workflow.

The package keeps the user-requested name `pirfl` for easy explicit invocation, but the skill’s description also exposes clearer trigger terms: plan-implement-review-fix, error-correcting workflow, validation loop, subagent review, iterative critique, and multi-task orchestration.

## Contents

```text
pirfl/
├── SKILL.md
├── references/
│   ├── cf-principles.md
│   ├── loop-protocol.md
│   ├── multi-task-orchestration.md
│   ├── research-notes.md
│   ├── subagent-prompts.md
│   └── task-log-format.md
├── assets/
│   ├── pirfl-log-template.md
│   ├── reviewer-report-template.md
│   ├── standalone-error-correction-loop-skill.template.md
│   └── task-portfolio-template.md
├── scripts/
│   ├── new_pirfl_log.py
│   └── validate_skill.py
└── evals/
    ├── quality-evals.json
    └── trigger-evals.json
```

## Install

Place the `pirfl/` folder wherever your skills-compatible agent loads skills, such as a user-level or repo-level skills directory. The folder name and `name:` field both use `pirfl` for compatibility.

## Validate

```bash
python pirfl/scripts/validate_skill.py pirfl
```

## Create a work log

```bash
python pirfl/scripts/new_pirfl_log.py "Refactor payment flow" --out pirfl-log.md
```

## Optional companion skill

`assets/standalone-error-correction-loop-skill.template.md` is a template for a narrower standalone loop skill named `error-correction-loop`. It is intentionally not named `review-and-fix` and is not stored as `SKILL.md` inside this package so the main ZIP remains a single-skill bundle.

## License

Dual licensed under the Unlicense and CC0 1.0 Universal. See `LICENSE`.
