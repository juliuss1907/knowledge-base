# Knowledge Base V2

Personal knowledge management system powered by AI agents.

---

## Overview

**Stack:**
- **Obsidian** — Frontend (graph view, tag explorer)
- **OpenClaw (Kara, AX400)** — Automation engine
- **Hermes (Connor, RK800)** — Validation agent

**Pipeline:**
```
INGEST → COMPILE → INDEX → VALIDATION
(OpenClaw) (OpenClaw) (OpenClaw) (Hermes)
```

---

## Quick Start

### 1. Ingest Content

**Via Telegram:**
- Send link → OpenClaw saves to `raw/[type]/YYYY-MM-DD_[slug].md`
- Send file → OpenClaw saves with frontmatter

**Manual:**
```bash
openclaw ingest [url]
```

---

### 2. Compile (Automatic)

**Daily 08:00:**
- OpenClaw scans `raw/` for files with `status: unprocessed`
- Transforms to `wiki/sources/` (per-source notes)
- Extracts to `wiki/concepts/` (knowledge atoms)
- Assigns tags according to `TAGS.md`

**Manual trigger:**
```bash
openclaw compile all new      # All unprocessed files
openclaw compile [filename]   # Specific file
```

---

### 3. Validate (Automatic)

**Daily 22:00-23:00:**
- **22:00** — Hermes Output Validator (content quality)
- **22:30** — Hermes Format Validator (structure)
- **23:00** — Hermes Hygiene Inspector (folder structure)

**Reports written to:**
- `wiki/reviews/YYYY-MM-DD_output-report.md`
- `wiki/reviews/YYYY-MM-DD_format-report.md`
- `wiki/reviews/YYYY-MM-DD_hygiene-report.md`

**Summary in:**
- `wiki/reviews/_action-required.md`

---

### 4. Review & Approve

**Check Telegram notification:**
- Hermes sends summary after validation

**Review reports:**
- Open `wiki/reviews/_action-required.md`
- Read individual reports for details

**Approve via Telegram:**
```
approve output      # Approve Output Validator report
approve format      # Approve Format Validator report
approve hygiene     # Approve Hygiene Inspector report
```

**View full report:**
```
show output
show format
show hygiene
```

**Reject:**
```
reject output
reject format
reject hygiene
```

---

### 5. Apply Fixes (Manual)

After approving Hermes reports:

```bash
openclaw fix apply
```

Fix Agent:
- Reads approved reports
- Applies corrections
- Updates file status
- Archives reports

---

## Folder Structure

```
knowledge-base/
├── AGENTS.md                 # Global system rules
├── TAGS.md                   # Tag taxonomy (2 pools)
├── README.md                 # This file
├── knowledge-base.md         # Dashboard (Dataview metrics)
│
├── .openclaw/                # OpenClaw agent home
│   ├── IDENTITY.md           # Who is OpenClaw
│   ├── SOUL.md               # Personality and values
│   ├── MEMORY.md             # Operation log (auto-generated)
│   ├── HEARTBEAT.md          # Status check (auto-generated)
│   └── skills/
│       ├── ingest-agent/
│       ├── compile-agent/
│       ├── index-agent/
│       └── fix-agent/
│
├── .hermes/                  # Hermes agent home
│   ├── IDENTITY.md           # Who is Hermes
│   ├── SOUL.md               # Personality and values
│   ├── MEMORY.md             # Validation log (auto-generated)
│   ├── HEARTBEAT.md          # Status check (auto-generated)
│   └── skills/
│       ├── output-validator/
│       ├── format-validator/
│       └── hygiene-inspector/
│
├── context/
│   ├── context.md            # System context index
│   └── USER.md               # Julius profile (agent-readable)
│
├── raw/                      # Ingest layer (read-only after ingest)
│   ├── articles/
│   ├── posts/
│   ├── websites/
│   ├── videos/
│   ├── papers/
│   └── repos/
│
└── wiki/                     # Knowledge layer (compiled output)
    ├── meta/
    │   ├── format-spec.md    # Format Validator ground truth
    │   └── folder-structure.md  # Hygiene Inspector ground truth
    ├── sources/              # Per-source notes (src_*.md)
    ├── concepts/             # Knowledge atoms
    ├── tag/                  # Tag indexes (auto-generated)
    ├── topic/                # Topic indexes (auto-generated)
    └── reviews/              # Hermes reports
        ├── _action-required.md  # Pending actions
        ├── YYYY-MM-DD_output-report.md
        ├── YYYY-MM-DD_format-report.md
        ├── YYYY-MM-DD_hygiene-report.md
        └── archive/          # Old reports (>30 days)
```

---

## Common Tasks

### Ingest a Link

1. Send link to Telegram bot
2. OpenClaw saves to `raw/[type]/YYYY-MM-DD_[slug].md`
3. Frontmatter attached: `status: unprocessed`
4. Compile runs next day 08:00

---

### Review Pending Files

1. Check `wiki/reviews/_action-required.md`
2. Read individual reports in `wiki/reviews/`
3. Approve via Telegram: `approve output/format/hygiene`
4. Trigger Fix Agent: `openclaw fix apply`

---

### Add New Tag

1. OpenClaw proposes via Telegram notification
2. Julius reviews proposal
3. Approve via Telegram
4. OpenClaw adds to `TAGS.md`
5. Index Agent creates `wiki/tag/[tag].md` at next run (21:00)

---

### Change Folder Structure

1. Update `wiki/meta/folder-structure.md`
2. Commit changes to git
3. Create/delete/rename folders
4. Next Hygiene Inspector run (23:00) validates

**For temporary testing:**
- Use `.tmp-` prefix for folders
- Hygiene Inspector reports WARNING (not ERROR)
- Delete when done or promote to permanent

---

### Check System Health

**Manual heartbeat:**
```bash
openclaw heartbeat
```

Returns:
- `HEARTBEAT_OK` — all systems normal
- Brief report — issues detected (max 3 bullets)

**Automatic heartbeat:**
- Runs every 30 minutes
- Logs to `.openclaw/MEMORY.md`

---

## Agent Commands

### OpenClaw (via Telegram or Terminal)

```bash
# Ingest
openclaw ingest [url]

# Compile
openclaw compile all new      # All unprocessed files
openclaw compile [filename]   # Specific file

# Index
openclaw index update         # Manual index update

# Fix
openclaw fix apply            # Apply approved Hermes reports

# Health
openclaw heartbeat            # Manual health check
```

---

### Hermes (via Telegram)

```bash
# Approve reports
approve output
approve format
approve hygiene

# Reject reports
reject output
reject format
reject hygiene

# View full reports
show output
show format
show hygiene
```

---

## Troubleshooting

### Raw Backlog Building Up

**Symptoms:**
- Many files in `raw/` with `status: unprocessed`
- Files older than 24 hours

**Solutions:**
1. Check OpenClaw heartbeat: `openclaw heartbeat`
2. Manual trigger: `openclaw compile all new`
3. Check `.openclaw/MEMORY.md` for compile errors
4. Verify files have correct frontmatter

---

### Hermes Reports Not Appearing

**Symptoms:**
- No new entries in `wiki/reviews/_action-required.md`
- No Telegram notification after 23:00

**Solutions:**
1. Check Hermes last validation timestamp in `.hermes/MEMORY.md`
2. Verify files have correct status (`draft` or `ready_review`)
3. Check files are in correct folders (`wiki/concepts/` or `wiki/sources/`)
4. Verify Hermes scheduled tasks running

---

### Tags Not in Taxonomy

**Symptoms:**
- OpenClaw proposes new tag via Telegram
- Compile blocked waiting for approval

**Solutions:**
1. Review tag proposal in Telegram
2. Approve or reject via Telegram
3. If approved, OpenClaw adds to `TAGS.md`
4. Index Agent creates `wiki/tag/[tag].md` at next run
5. Compile resumes automatically

---

### Obsidian Dataview Not Working

**Symptoms:**
- `knowledge-base.md` shows raw Dataview code instead of tables
- Metrics not updating

**Solutions:**
1. Install Dataview plugin in Obsidian
2. Enable Dataview in Settings → Community Plugins
3. Reload Obsidian
4. Open `knowledge-base.md` again

---

### Fix Agent Errors

**Symptoms:**
- Fix Agent fails to apply approved reports
- Files not updated after `openclaw fix apply`

**Solutions:**
1. Check `.openclaw/MEMORY.md` for error details
2. Verify reports are approved (status: `approved` in report frontmatter)
3. Check file permissions (Fix Agent needs write access)
4. Manual fix: edit files directly, then archive reports

---

## Maintenance

### Daily
- Check Telegram notifications
- Review `_action-required.md` if notified
- Ingest new content as needed

### Weekly
- Approve pending Hermes reports (Friday evening)
- Review tag taxonomy proposals
- Check system health metrics in `knowledge-base.md`

### Monthly
- Review `.openclaw/MEMORY.md` and `.hermes/MEMORY.md` for patterns
- Archive old reports (>30 days) to `wiki/reviews/archive/`
- Update agent skills if needed
- Check for orphaned files via Hygiene Inspector

---

## Requirements

### Software
- **Obsidian** — latest version
- **Dataview plugin** — for live metrics in `knowledge-base.md`
- **Git** — for version control
- **Python 3.8+** — for agent scripts (OpenClaw, Hermes)

### Optional
- **Telegram bot** — for agent communication
- **Readwise account** — for automatic article sync

---

## Setup (First Time)

### 1. Clone Repository

```bash
git clone https://github.com/juliuss1907/knowledge-base.git
cd knowledge-base
```

---

### 2. Install Obsidian Plugins

1. Open Obsidian
2. Settings → Community Plugins → Browse
3. Install: **Dataview**
4. Enable Dataview

---

### 3. Configure Agents

**OpenClaw:**
```bash
cd .openclaw
cp config.example.yml config.yml
# Edit config.yml with your settings
```

**Hermes:**
```bash
cd .hermes
cp config.example.yml config.yml
# Edit config.yml with your settings
```

---

### 4. Set Up Cron Jobs (Optional)

For automatic scheduled tasks:

```bash
# Edit crontab
crontab -e

# Add these lines:
0 7 * * * /path/to/openclaw readwise-sync
0 8 * * * /path/to/openclaw compile all new
0 21 * * * /path/to/openclaw index update
0 22 * * * /path/to/hermes validate output
30 22 * * * /path/to/hermes validate format
0 23 * * * /path/to/hermes validate hygiene
```

---

### 5. Initial Compile

```bash
# Compile existing raw files
openclaw compile all new

# Update indexes
openclaw index update

# Verify in Obsidian
open knowledge-base.md
```

---

## Support

**Documentation:**
- `AGENTS.md` — system rules
- `TAGS.md` — tag taxonomy
- `.openclaw/skills/` — OpenClaw workflows
- `.hermes/skills/` — Hermes validation criteria

**Logs:**
- `.openclaw/MEMORY.md` — OpenClaw operation log
- `.hermes/MEMORY.md` — Hermes validation log

**Contact:**
- System owner: Julius
- GitHub: https://github.com/juliuss1907/knowledge-base

---

*Knowledge Base V2 — Powered by OpenClaw & Hermes*  
*Built with Obsidian, Python, and AI agents*
