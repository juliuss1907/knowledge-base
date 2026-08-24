# Quick-scan false positives — taxonomy & fixes

Session evidence for the SKILL.md rule "verify mechanically before reporting". Both heuristics below live in `scripts/quick-scan.sh` and have mis-fired on 2026-06-19, 2026-08-22, and 2026-08-24.

## FP-1: "Empty Key ideas" counts only dash bullets

**Script section:** `# ─── 6. Empty sections ───` — counts `grep -c '^- '` inside the `## Key ideas` range.

**Wrong when a concept uses numbered lists or tables.** Files flagged as "empty" in 08-24 all had full content:

| File | Actual content |
|---|---|
| ai-coach-prompting.md | numbered list `1. **Phase 1...**` |
| ai-first-business-model.md | numbered list |
| content-generation-workflow.md | numbered list |
| digital-product-flywheel.md | numbered list |
| expert-knowledge-extraction.md | numbered list |
| google-project-oxygen.md | bold intro + ranked list (1.–8.) |
| multi-agent-taxonomy.md | numbered list |
| personal-branding-ai.md | numbered list |
| six-stage-research-pipeline.md | markdown table |

Python cross-check that returned **0 truly empty** (run via terminal heredoc; execute_code is blocked for cron profiles):

```python
import os, re
kb = "/home/julius/knowledge-base/wiki/concepts"
for fn in sorted(os.listdir(kb)):
    if not fn.endswith(".md"): continue
    text = open(os.path.join(kb, fn), encoding="utf-8").read()
    m = re.search(r'^## Key ideas\s*\n(.*?)(?=^## )', text, re.M | re.S)
    body = (m.group(1) if m else "").strip()
    content = re.sub(r'^[-*\d.]+\s*', '', body).strip()
    if not content:
        print(fn)   # only REAL empties print
```

**Script fix suggestion:** section 6 change `grep -c '^- '` → `grep -cE '^- |^[0-9]+\. '`.

## FP-2: "1-sentence definitions" counts lines-with-periods, not sentences

**Script section:** `# ─── 3. 1-sentence definitions ───`

```bash
sentences=$(sed -n '/^## Definition$/,/^## /p' "$f" \
    | sed '1d;/^## /,$d' | grep -v '^$' | grep -c '\.')
```

Counts *lines containing a period*. A definition written as one paragraph of 3–4 sentences on a single line scores 1 → the whole KB reads as "1-sentence definitions: 527/527 concepts" while every new file actually has 2–4 sentence definitions. Useless as a quality signal; ignore the aggregate number entirely and read today's new files' Definitions directly.

**Fix options:** count sentence enders on text (`grep -o '[.!?]' | wc -l`) instead of matching lines — or remove section 3 from the script (recommended; it has never produced an accurate signal).

## Reporting rule

When these counters disagree with reality:
- Do NOT file N per-file completeness issues.
- File ONE tooling WARNING describing the heuristic defect + suggested patch.
- Note the false positive in `.hermes/MEMORY.md` entry ("False positive ghi nhận") so recurrence is visible across runs.
