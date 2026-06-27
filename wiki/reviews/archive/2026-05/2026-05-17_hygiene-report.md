# Hygiene Inspection — 2026-05-17

**Status:** pending
**Issues found:** 20 (2 ERROR, 18 WARNING, 0 INFO)
**Created:** 2026-05-17 23:35:00
**Validator:** hygiene-inspector

**Paths checked:** 1290

---

## Issue 1: Folder not in root whitelist: memory

**Path:** memory/
**Severity:** ERROR
**Category:** Path
**Issue:** Folder not in root whitelist
**Current:** memory/
**Expected:** Only allowed at root: .git, .hermes, .obsidian, .openclaw, context, raw, scripts, wiki
**Suggested fix:** This appears to be a non-standard folder. Either remove it or add to folder-structure.md root whitelist (requires Julius approval). Contains heartbeat polls and session notes from Hermes.

---

## Issue 2: File not in wiki/meta/ whitelist: index-spec.md

**Path:** wiki/meta/index-spec.md
**Severity:** ERROR
**Category:** Path
**Issue:** File not in wiki/meta/ whitelist
**Current:** index-spec.md
**Expected:** Only format-spec.md and folder-structure.md allowed in wiki/meta/ (§7 of folder-structure.md)
**Suggested fix:** This is listed as a ground-truth reference in AGENTS.md. Either add index-spec.md to wiki/meta/ whitelist in folder-structure.md, or clarify its intended location.

---

## Issue 3: Directory name uses underscores: ISO-IEC29500-4_2016

**Path:** .hermes/skills/productivity/powerpoint/scripts/office/schemas/ISO-IEC29500-4_2016/
**Severity:** WARNING
**Category:** Naming
**Issue:** Directory name uses underscores
**Current:** ISO-IEC29500-4_2016
**Expected:** lowercase-hyphen format
**Suggested fix:** Rename to iso-iec29500-4-2016 (or consider that this is a vendored ISO standard schema reference — may want to whitelist as-is)

---

## Issue 4: Temporary/backup file: jobs.json.bak

**Path:** .openclaw/cron/jobs.json.bak
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary/backup file left behind
**Current:** jobs.json.bak
**Expected:** Clean up temp files after use
**Suggested fix:** Remove .openclaw/cron/jobs.json.bak if current version is authoritative

---

## Issue 5: Temporary file: paired.json UUID tmp

**Path:** .openclaw/devices/paired.json.80f096b3-1f67-4a08-891c-25398297ceca.tmp
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary file left behind (atomic write residue)
**Current:** paired.json UUID tmp
**Expected:** Clean up temp files
**Suggested fix:** Remove .openclaw/devices/paired.json.80f096b3-...tmp

---

## Issue 6: Temporary/backup file: paired.json.bak

**Path:** .openclaw/devices/paired.json.bak
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file left behind
**Current:** paired.json.bak
**Expected:** Clean up backup files
**Suggested fix:** Remove .openclaw/devices/paired.json.bak

---

## Issue 7: Temporary/backup file: pending.json.bak

**Path:** .openclaw/devices/pending.json.bak
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file left behind
**Current:** pending.json.bak
**Expected:** Clean up backup files
**Suggested fix:** Remove .openclaw/devices/pending.json.bak

---

## Issue 8: Temporary file: pending.json UUID tmp

**Path:** .openclaw/devices/pending.json.e214dff1-9be9-4999-8364-784f48146d4b.tmp
**Severity:** WARNING
**Category:** Orphan
**Issue:** Temporary file left behind (atomic write residue)
**Current:** pending.json UUID tmp
**Expected:** Clean up temp files
**Suggested fix:** Remove .openclaw/devices/pending.json UUID tmp

---

## Issue 9: Temporary/backup file: openclaw.json.bak

**Path:** .openclaw/openclaw.json.bak
**Severity:** WARNING
**Category:** Orphan
**Issue:** Backup file at .openclaw/ root
**Current:** openclaw.json.bak
**Expected:** Clean up backup files
**Suggested fix:** Remove .openclaw/openclaw.json.bak (current .openclaw/openclaw.json is authoritative)

---

## Issue 10: Unexpected dotfile in .hermes/: .update_check

**Path:** .hermes/.update_check
**Severity:** WARNING
**Category:** Path
**Issue:** Non-standard runtime file in .hermes/
**Current:** .update_check
**Expected:** Runtime artifacts or identity files only
**Suggested fix:** This is a legitimate Hermes runtime file. Add to folder-structure.md whitelist for .hermes/ runtime files.

---

## Issue 11: Unexpected folder in .hermes/: bin

**Path:** .hermes/bin/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .hermes/ whitelist
**Current:** bin/
**Expected:** Expected: cron, hermes-agent, sessions, skills
**Suggested fix:** This is a legitimate Hermes runtime folder (contains tirith binary). Add to folder-structure.md .hermes/ whitelist.

---

## Issue 12: Unexpected folder in .hermes/: cache

**Path:** .hermes/cache/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .hermes/ whitelist
**Current:** cache/
**Expected:** Expected: cron, hermes-agent, sessions, skills
**Suggested fix:** Legitimate Hermes runtime cache folder. Add to folder-structure.md .hermes/ whitelist.

---

## Issue 13: Unexpected folder in .hermes/: logs

**Path:** .hermes/logs/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .hermes/ whitelist
**Current:** logs/
**Expected:** Expected: cron, hermes-agent, sessions, skills
**Suggested fix:** Legitimate Hermes runtime log folder. Add to folder-structure.md .hermes/ whitelist.

---

## Issue 14: Unexpected folder in .hermes/: memories

**Path:** .hermes/memories/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .hermes/ whitelist
**Current:** memories/
**Expected:** Expected: cron, hermes-agent, sessions, skills
**Suggested fix:** Legitimate Hermes persistent memory folder. Add to folder-structure.md .hermes/ whitelist.

---

## Issue 15: Unexpected file in .openclaw/: TOOLS.md

**Path:** .openclaw/TOOLS.md
**Severity:** WARNING
**Category:** Path
**Issue:** File not in .openclaw/ identity whitelist
**Current:** TOOLS.md
**Expected:** Expected identity files: IDENTITY.md, SOUL.md, MEMORY.md, HEARTBEAT.md
**Suggested fix:** This is symlinked at KB root. If it's an OpenClaw identity file, update folder-structure.md to allow it. Otherwise remove.

---

## Issue 16: Unexpected file in .openclaw/: USER.md

**Path:** .openclaw/USER.md
**Severity:** WARNING
**Category:** Path
**Issue:** File not in .openclaw/ identity whitelist
**Current:** USER.md
**Expected:** Expected identity files: IDENTITY.md, SOUL.md, MEMORY.md, HEARTBEAT.md
**Suggested fix:** This is symlinked at KB root. If it's an OpenClaw identity file, update folder-structure.md. Otherwise remove.

---

## Issue 17: Unexpected folder in .openclaw/: canvas

**Path:** .openclaw/canvas/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .openclaw/ whitelist
**Current:** canvas/
**Expected:** Expected: agents, cron, memory, skills
**Suggested fix:** Legitimate OpenClaw runtime folder. Add to folder-structure.md .openclaw/ whitelist.

---

## Issue 18: Unexpected folder in .openclaw/: completions

**Path:** .openclaw/completions/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .openclaw/ whitelist
**Current:** completions/
**Expected:** Expected: agents, cron, memory, skills
**Suggested fix:** Legitimate OpenClaw shell completions folder. Add to folder-structure.md.

---

## Issue 19: Unexpected folder in .openclaw/: devices

**Path:** .openclaw/devices/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .openclaw/ whitelist
**Current:** devices/
**Expected:** Expected: agents, cron, memory, skills
**Suggested fix:** Legitimate OpenClaw device pairing folder. Add to folder-structure.md.

---

## Issue 20: Unexpected folder in .openclaw/: flows

**Path:** .openclaw/flows/
**Severity:** WARNING
**Category:** Path
**Issue:** Folder not in .openclaw/ whitelist
**Current:** flows/
**Expected:** Expected: agents, cron, memory, skills
**Suggested fix:** Legitimate OpenClaw runtime folder. Add to folder-structure.md whitelist.

---

## Escalation

### Folder-structure.md conflicts

**[SPEC CONFLICT — wiki/meta/**
Section 7 says: `meta/` contains exactly 2 files (`format-spec.md` + `folder-structure.md`)
But AGENTS.md §4.2 and §6 list `wiki/meta/index-spec.md` as a "ground-truth reference."

**Issue:** index-spec.md exists in wiki/meta/ but is not whitelisted in folder-structure.md.
**Recommendation:** Either add index-spec.md to §7 meta/ whitelist, or move it elsewhere.

**[SPEC CONFLICT — .openclaw/ and .hermes/ runtime folders**
folder-structure.md §3.1 and §3.2 limit .openclaw/ to 4 folders (skills, agents, cron, memory) and .hermes/ to 4 folders (skills, sessions, cron, hermes-agent). Many legitimate OpenClaw and Hermes runtime folders exist outside this narrow whitelist (canvas, completions, devices, flows, logs, bin, cache, memories, etc.).

**Pattern:** 10+ WARNINGs are legitimate runtime folders, not structural violations.
**Recommendation:** Expand §3.1 and §3.2 to use broader categories like "runtime folders" or add a catch-all "additional runtime folders allowed" clause. Previous v1.1 update from 2026-05-14 addressed some runtime artifacts but didn't cover all.
