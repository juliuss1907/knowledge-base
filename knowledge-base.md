# Knowledge Base V2

> Personal knowledge management system powered by AI agents
> Last manual update: 2026-05-09

---

## System Status

> **Note:** Metrics below update automatically when you open this file in Obsidian (requires Dataview plugin)

### Raw Layer

```dataview
TABLE WITHOUT ID
  "Unprocessed files" AS Metric,
  length(filter(rows, (r) => contains(string(r.file.frontmatter.status), "unprocessed"))) AS Count
FROM "raw"
WHERE file.name != "README"
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  "Total raw files" AS Metric,
  length(rows) AS Count
FROM "raw"
WHERE file.name != "README"
GROUP BY true
```

### Wiki Layer — Concepts

```dataview
TABLE WITHOUT ID
  file.frontmatter.status AS Status,
  length(rows) AS Count
FROM "wiki/concepts"
WHERE file.name != "README"
GROUP BY file.frontmatter.status
SORT Status ASC
```

### Wiki Layer — Sources

```dataview
TABLE WITHOUT ID
  "Total source files" AS Metric,
  length(rows) AS Count
FROM "wiki/sources"
WHERE file.name != "README"
GROUP BY true
```

### Wiki Layer — Indexes

```dataview
TABLE WITHOUT ID
  "Tag indexes" AS Type,
  length(rows) AS Count
FROM "wiki/tag"
WHERE file.name != "README"
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  "Topic indexes" AS Type,
  length(rows) AS Count
FROM "wiki/topic"
WHERE file.name != "README"
GROUP BY true
```

### Pending Reviews

```dataview
TABLE WITHOUT ID
  "Pending review entries" AS Metric,
  length(file.tasks.text) AS Count
FROM "wiki/reviews"
WHERE file.name = "_action-required"
GROUP BY true
```

---

## Quick Navigation

### Core Documentation
- [[AGENTS.md]] — Global system rules
- [[TAGS.md]] — Tag taxonomy (2 pools)
- [[README.md]] — How to use this KB

### Ground Truth Files
- [[wiki/meta/format-spec.md]] — Format Validator ground truth
- [[wiki/meta/folder-structure.md]] — Hygiene Inspector ground truth

### Agent Homes
- [[.openclaw/IDENTITY.md]] — OpenClaw identity
- [[.openclaw/SOUL.md]] — OpenClaw personality
- [[.hermes/IDENTITY.md]] — Hermes identity
- [[.hermes/SOUL.md]] — Hermes personality

### Action Required
- [[wiki/reviews/_action-required.md]] — Pending reviews and fixes

---

## Agent Status

### OpenClaw (Kara, AX400)

**Role:** Automation engine (Ingest → Compile → Index)

**Skills:**
- [[.openclaw/skills/ingest-agent/SKILL.md]] — Save external content to raw/
- [[.openclaw/skills/compile-agent/SKILL.md]] — Transform raw → wiki
- [[.openclaw/skills/index-agent/SKILL.md]] — Maintain tag/topic indexes
- [[.openclaw/skills/fix-agent/SKILL.md]] — Apply approved Hermes reports

**Schedule:**
- Heartbeat: Every 30 minutes
- Readwise sync: Daily 07:00
- Compile: Daily 08:00
- Index update: Daily 21:00

**Last activity:** Check `.openclaw/MEMORY.md`

---

### Hermes (Connor, RK800)

**Role:** Validation agent (Quality → Format → Structure)

**Skills:**
- [[.hermes/skills/output-validator/SKILL.md]] — Content quality validation
- [[.hermes/skills/format-validator/SKILL.md]] — Structure validation
- [[.hermes/skills/hygiene-inspector/SKILL.md]] — Folder structure validation

**Schedule:**
- Output validation: Daily 22:00
- Format validation: Daily 22:30
- Hygiene inspection: Daily 23:00

**Last activity:** Check `.hermes/MEMORY.md`

---

## Recent Activity (Last 7 Days)

### Files Ingested

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_ingested AS "Date Ingested",
  file.frontmatter.source_type AS Type
FROM "raw"
WHERE file.frontmatter.date_ingested >= date(today) - dur(7 days)
SORT file.frontmatter.date_ingested DESC
LIMIT 10
```

### Files Compiled

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_compiled AS "Date Compiled",
  file.frontmatter.topic AS Topic
FROM "wiki/sources"
WHERE file.frontmatter.date_compiled >= date(today) - dur(7 days)
SORT file.frontmatter.date_compiled DESC
LIMIT 10
```

### Concepts Updated

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.last_updated AS "Last Updated",
  file.frontmatter.status AS Status
FROM "wiki/concepts"
WHERE file.frontmatter.last_updated >= date(today) - dur(7 days)
SORT file.frontmatter.last_updated DESC
LIMIT 10
```

---

## Quick Actions

### Ingest Content

**Via Telegram:**
- Send link → OpenClaw auto-ingests to `raw/`
- Send file → OpenClaw saves with frontmatter

**Manual:**
```bash
openclaw ingest [url]
```

---

### Compile Files

**Automatic:**
- Daily 08:00 — all unprocessed files in `raw/`

**Manual:**
```bash
openclaw compile all new      # Compile all unprocessed
openclaw compile [filename]   # Compile specific file
```

---

### Review Pending Actions

**Check pending:**
- Open [[wiki/reviews/_action-required.md]]
- Review individual reports in `wiki/reviews/`

**Approve via Telegram:**
```
approve output      # Approve Output Validator report
approve format      # Approve Format Validator report
approve hygiene     # Approve Hygiene Inspector report
```

**View details:**
```
show output         # View full Output Validator report
show format         # View full Format Validator report
show hygiene        # View full Hygiene Inspector report
```

**Reject:**
```
reject output       # Reject Output Validator report
reject format       # Reject Format Validator report
reject hygiene      # Reject Hygiene Inspector report
```

---

### Update Indexes

**Automatic:**
- Daily 21:00 — all tag and topic indexes

**Manual:**
```bash
openclaw index update
```

---

### Check System Health

**Heartbeat:**
```bash
openclaw heartbeat
```

Returns:
- `HEARTBEAT_OK` — all systems normal
- Brief report — issues detected (max 3 bullets)

---

## Tag Taxonomy

### Pool A — Main Tags (7)

```dataview
TABLE WITHOUT ID
  file.link AS Tag,
  length(rows) AS "Files Using This Tag"
FROM "wiki/tag"
WHERE file.name != "README"
GROUP BY file.link
SORT length(rows) DESC
```

### Pool B — Sub Tags (12)

See [[TAGS.md]] for complete taxonomy and tagging rules.

---

## System Health Indicators

### Raw Backlog Alert

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_ingested AS "Ingested",
  date(today) - file.frontmatter.date_ingested AS "Days Waiting"
FROM "raw"
WHERE file.frontmatter.status = "unprocessed"
  AND date(today) - file.frontmatter.date_ingested > dur(1 day)
SORT file.frontmatter.date_ingested ASC
```

> **Action:** If files appear above, run `openclaw compile all new`

---

### Concepts Awaiting Review

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.last_updated AS "Last Updated",
  date(today) - file.frontmatter.last_updated AS "Days Waiting"
FROM "wiki/concepts"
WHERE file.frontmatter.status = "draft"
SORT file.frontmatter.last_updated ASC
```

> **Action:** Hermes validates daily at 22:00. Check [[wiki/reviews/_action-required.md]] after validation.

---

## Maintenance

### Weekly Tasks
- [ ] Review [[wiki/reviews/_action-required.md]]
- [ ] Archive old reports (>30 days) to `wiki/reviews/archive/`
- [ ] Check for orphaned files via Hygiene Inspector

### Monthly Tasks
- [ ] Review tag taxonomy — consolidate or add tags
- [ ] Check concept link coverage
- [ ] Update agent skills if needed
- [ ] Review `.openclaw/MEMORY.md` and `.hermes/MEMORY.md` for patterns

---

## Troubleshooting

### Raw Backlog Building Up

**Symptoms:** Many files in "Raw Backlog Alert" section above

**Solutions:**
1. Check OpenClaw heartbeat status
2. Manual trigger: `openclaw compile all new`
3. Check `.openclaw/MEMORY.md` for compile errors

---

### Hermes Reports Not Appearing

**Symptoms:** No new entries in [[wiki/reviews/_action-required.md]]

**Solutions:**
1. Check Hermes last validation timestamp in `.hermes/MEMORY.md`
2. Verify files have correct status (`draft` or `ready_review`)
3. Check if files are in correct folders (`wiki/concepts/` or `wiki/sources/`)

---

### Tags Not in Taxonomy

**Symptoms:** OpenClaw proposes new tag via notification

**Solutions:**
1. Review tag proposal in Telegram
2. Approve or reject via Telegram
3. If approved, OpenClaw adds to [[TAGS.md]]
4. Index Agent creates `wiki/tag/[tag].md` at next run (21:00)

---

## Contact

**System Owner:** Julius

**Agent Communication:**
- OpenClaw (Kara): Telegram bot
- Hermes (Connor): Reports via `wiki/reviews/`

---

*Knowledge Base V2 — Powered by OpenClaw & Hermes*  
*Dashboard auto-updates via Obsidian Dataview plugin*
