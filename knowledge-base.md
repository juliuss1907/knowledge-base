# Knowledge Base V2

> Dashboard cho AI-powered knowledge management system
> Last manual update: 2026-05-17

---

## 🗺️ Navigation

### Layer Indexes (Level 1)

3 entry points chính cho toàn bộ KB:

- 📥 [[raw]] — Ingested source material (articles, posts, videos, papers, repos, websites)
- 📚 [[wiki]] — Compiled knowledge (concepts, sources, tags, topics)
- 👤 [[context]] — User profile và environment context

### Master Indexes (Level 2)

- 🏷️ [[tag]] — Master tag index (Pool A + Pool B)

### Action Center

- ⚠️ [[wiki/reviews/_action-required]] — Pending reviews & fixes
- 📋 [[AGENTS]] — Global rules cho tất cả agents
- 🏷️ [[TAGS]] — Tag taxonomy spec

### Ground Truth Specs

- 📐 [[wiki/meta/format-spec]] — File format rules (concept + source)
- 📁 [[wiki/meta/folder-structure]] — Folder hierarchy rules
- 🗂️ [[wiki/meta/index-spec]] — Index file format rules

---

## 📊 System Status

> Metrics auto-update khi mở file (yêu cầu Obsidian Dataview plugin)

### Raw Layer

```dataview
TABLE WITHOUT ID
  "Total raw files" AS Metric,
  length(rows) AS Count
FROM "raw"
WHERE file.name != "raw" AND !contains(file.name, "articles") 
  AND !contains(file.name, "posts") AND !contains(file.name, "videos")
  AND !contains(file.name, "papers") AND !contains(file.name, "repos")
  AND !contains(file.name, "websites")
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  "Unprocessed files" AS Metric,
  length(filter(rows, (r) => contains(string(r.file.frontmatter.status), "unprocessed"))) AS Count
FROM "raw"
WHERE file.frontmatter.type != "index"
GROUP BY true
```

### Wiki Layer

```dataview
TABLE WITHOUT ID
  file.frontmatter.type AS Type,
  length(rows) AS Count
FROM "wiki/concepts" OR "wiki/sources"
WHERE file.frontmatter.type
GROUP BY file.frontmatter.type
```

```dataview
TABLE WITHOUT ID
  "Tag indexes" AS Type,
  length(rows) AS Count
FROM "wiki/tag"
WHERE file.name != "tag" AND file.frontmatter.type = "index"
GROUP BY true
```

```dataview
TABLE WITHOUT ID
  "Topic indexes" AS Type,
  length(rows) AS Count
FROM "wiki/topic"
GROUP BY true
```

---

## 🤖 Agents

### OpenClaw (Kara — AX400)

**Role:** Automation engine — Ingest → Compile → Index → Fix

| Skill | Trigger | Schedule |
|---|---|---|
| [[.openclaw/skills/ingest-agent/SKILL\|Ingest]] | On-demand | Manual (Telegram link share) |
| [[.openclaw/skills/compile-agent/SKILL\|Compile]] | Cron | Daily 08:00 |
| [[.openclaw/skills/index-agent/SKILL\|Index]] | Cron | Daily 21:00 |
| [[.openclaw/skills/fix-agent/SKILL\|Fix]] | On-demand | Manual (after Julius approves) |

**Identity:** [[.openclaw/IDENTITY|Kara]] · [[.openclaw/SOUL|Personality]] · [[.openclaw/MEMORY|Logs]] · [[.openclaw/HEARTBEAT|Status]]

---

### Hermes (Connor — RK800)

**Role:** Validation agent — Quality → Format → Structure (read-only, report-only)

| Skill | Validates | Schedule |
|---|---|---|
| [[.hermes/skills/output-validator/SKILL\|Output]] | Content quality | Daily 23:00 |
| [[.hermes/skills/format-validator/SKILL\|Format]] | File format | Daily 23:15 |
| [[.hermes/skills/hygiene-inspector/SKILL\|Hygiene]] | Folder structure | Daily 23:30 |

**Identity:** [[.hermes/IDENTITY|Connor]] · [[.hermes/SOUL|Personality]] · [[.hermes/MEMORY|Logs]] · [[.hermes/HEARTBEAT|Status]]

---

## 📅 Daily Pipeline (UTC+7)

```
08:00 → Kara compiles raw/ → wiki/sources/ + wiki/concepts/
21:00 → Kara regenerates wiki/tag/ + wiki/topic/
23:00 → Connor validates content quality
23:15 → Connor validates format compliance
23:30 → Connor validates folder structure
        ↓
        Reports → wiki/reviews/_action-required.md
        ↓
        Telegram notification → Julius
```

---

## ⚡ Quick Actions

### Ingest Content

```
# Via Telegram (recommended)
Send link/file to OpenClaw bot

# Via CLI
openclaw ingest [url]
```

### Process Files Manually

```
openclaw compile all new      # All unprocessed
openclaw compile [filename]   # Specific file
openclaw index update         # Regenerate indexes
```

### Review Hermes Reports

| Action | Telegram Command |
|---|---|
| View pending | Open [[wiki/reviews/_action-required]] |
| Approve | `approve output` / `approve format` / `approve hygiene` |
| Reject | `reject output` / `reject format` / `reject hygiene` |
| Show details | `show output` / `show format` / `show hygiene` |

### Apply Fixes

After approval:
```
openclaw apply fixes
```

---

## 📈 Recent Activity (Last 7 Days)

### Files Ingested

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_ingested AS "Ingested",
  file.frontmatter.type AS Type
FROM "raw"
WHERE file.frontmatter.date_ingested >= date(today) - dur(7 days)
  AND file.frontmatter.type != "index"
SORT file.frontmatter.date_ingested DESC
LIMIT 10
```

### Files Compiled

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_compiled AS "Compiled",
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
  file.frontmatter.last_updated AS "Updated",
  file.frontmatter.status AS Status
FROM "wiki/concepts"
WHERE file.frontmatter.last_updated >= date(today) - dur(7 days)
SORT file.frontmatter.last_updated DESC
LIMIT 10
```

---

## 🚨 Health Indicators

### Raw Backlog (>1 day unprocessed)

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.date_ingested AS "Ingested",
  (date(today) - file.frontmatter.date_ingested).days AS "Days Waiting"
FROM "raw"
WHERE file.frontmatter.status = "unprocessed"
  AND (date(today) - file.frontmatter.date_ingested).days > 1
SORT file.frontmatter.date_ingested ASC
```

> **Action:** Run `openclaw compile all new` if files appear above.

### Concepts in Draft Status

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.last_updated AS "Updated",
  (date(today) - file.frontmatter.last_updated).days AS "Days as Draft"
FROM "wiki/concepts"
WHERE file.frontmatter.status = "draft"
SORT file.frontmatter.last_updated ASC
LIMIT 10
```

> **Action:** Hermes validates daily at 23:00. Review reports trong [[wiki/reviews/_action-required]].

### Stale Index Files (>2 days)

```dataview
TABLE WITHOUT ID
  file.link AS File,
  file.frontmatter.last_updated AS "Last Updated",
  (date(today) - file.frontmatter.last_updated).days AS "Days Stale"
FROM "wiki/tag" OR "raw"
WHERE file.frontmatter.type = "index"
  AND (date(today) - file.frontmatter.last_updated).days > 2
SORT file.frontmatter.last_updated ASC
```

> **Action:** Trigger Index Agent (21:00) hoặc Ingest Agent để refresh stats.

---

## 🔧 Maintenance

### Weekly Checklist

- [ ] Review [[wiki/reviews/_action-required]]
- [ ] Approve/reject pending Hermes reports
- [ ] Check OpenClaw [[.openclaw/MEMORY|MEMORY]] for recurring errors
- [ ] Check Hermes [[.hermes/MEMORY|MEMORY]] for systematic issues

### Monthly Checklist

- [ ] Archive reports >30 days to `wiki/reviews/archive/YYYY-MM/`
- [ ] Review tag taxonomy — consolidate hoặc add tags qua [[TAGS]]
- [ ] Check concept link coverage (orphan concepts)
- [ ] Update agent skills nếu workflow thay đổi

---

## 🆘 Troubleshooting

### Raw backlog building up

1. Check Kara heartbeat: `cat .openclaw/HEARTBEAT.md`
2. Manual trigger: `openclaw compile all new`
3. Inspect errors: `cat .openclaw/MEMORY.md | tail -50`

### Hermes reports không xuất hiện

1. Check cron status: `hermes cron list`
2. Check last run: `cat .hermes/MEMORY.md | tail -20`
3. Verify files có `type: concept|source` trong frontmatter

### Tag mới cần thêm

1. Agent gửi proposal qua Telegram
2. Approve/reject qua Telegram
3. Nếu approve → OpenClaw thêm vào [[TAGS]]
4. Index Agent tạo `wiki/tag/[tag].md` ở 21:00

### Index file outdated

1. Check `last_updated` field
2. Trigger Index Agent: `openclaw cron run [index-agent-job-id]`
3. Hoặc đợi cron 21:00

---

## 📝 Notes

<!-- Free space for Julius -->

---

*Knowledge Base V2 — Powered by OpenClaw (Kara) & Hermes (Connor)*  
*Dashboard auto-updates via Obsidian Dataview plugin*
```

---
