# PIRFL task log format

Use a PIRFL log for complex tasks, long-running work, multi-file edits, or anything where review/fix traceability helps.

The log can be private scratch material. Share it only when the user asks or when it is itself a useful deliverable.

## Minimal log

```markdown
# PIRFL Log: [task]

## Task model
- Goal:
- Context:
- Deliverable:
- Acceptance checks:
- Assumptions:

## Plan
1.
2.
3.

## Implement notes
- [timestamp/step] Change made:
- Check run:

## Review issues
| ID | State | Severity | Location | Issue | Evidence | Fix/check |
|---|---|---|---|---|---|---|

## Fix log
| Issue ID | Fix | Verification |
|---|---|---|

## Exit gates
- [ ] Required validators pass
- [ ] No accepted blocker/major remains
- [ ] Targeted re-review completed after fixes
- [ ] Known remaining risks listed

## Final summary
- Delivered:
- Checked:
- Remaining risks:
```

## Final response extraction

Do not paste the whole log into the final answer unless requested. Extract:

- delivered artifact/result,
- checks performed,
- important assumptions,
- remaining material risks,
- links or paths.
