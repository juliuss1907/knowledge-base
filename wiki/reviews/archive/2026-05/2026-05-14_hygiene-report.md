# Hygiene Inspection — 2026-05-14

**Status:** pending
**Issues found:** 14 (8 ERROR, 2 WARNING, 4 INFO)
**Created:** 2026-05-14 23:34:24
**Validator:** hygiene-inspector

**Paths checked:** ~650 (excluding .git, node_modules, venv, __pycache__)

---

## ⚠️ Critical Finding: Spec vs Reality Conflict

The current `folder-structure.md` (v1.0, 2026-05-07) defines idealized agent homes with only identity files + a few skill folders. The deployed Hermes and OpenClaw agents have extensive runtime state (databases, caches, logs, sessions, 25+ Hermes skills, CLI source code in `.hermes/hermes-agent/`). **The spec needs updating to document these as intentional runtime artifacts**, otherwise every daily run will produce dozens of ERROR-level false positives.

**Recommendation:** Update `folder-structure.md` to v1.1 adding sections for "Agent runtime artifacts" under `.openclaw/` and `.hermes/` that whitelist operational files while still catching true structural drift.

---

## Issue 1: Agent runtime files exceed spec (20+ items) — SPEC vs REALITY CONFLICT

**Path:** .hermes/
**Severity:** ERROR
**Category:** Path
**Issue:** Agent runtime files exceed spec (20+ items) — SPEC vs REALITY CONFLICT
**Current:** auth.json, auth.lock, bin/, cache/, channel_directory.json, config.yaml, cron/, gateway.pid, gateway_state.json, hermes-agent/, logs/, memories/, models_dev_cache.json, ollama_cloud_models_cache.json, sessions/, state.db, state.db-shm, state.db-wal, .update_check, .restart_last_processed.json, .skills_prompt_snapshot.json
**Expected:** Only IDENTITY.md, SOUL.md, MEMORY.md, HEARTBEAT.md, skills/
**Suggested fix:** If intentional runtime files, update folder-structure.md §3.2 to document allowed runtime artifacts (state.db, config.yaml, cron/, sessions/, logs/, cache/, hermes-agent/)

---

## Issue 2: Extra skill folders (26 beyond the 3 spec'd) — SPEC vs REALITY CONFLICT

**Path:** .hermes/skills/
**Severity:** ERROR
**Category:** Path
**Issue:** Extra skill folders (26 beyond the 3 spec'd) — SPEC vs REALITY CONFLICT
**Current:** Expected 3 skills (output-validator, format-validator, hygiene-inspector). Found 26 extra: agent-reach, apple, autonomous-ai-agents, creative, data-science, devops, diagramming, dogfood... (+18 more)
**Expected:** Exactly 3 subfolders: output-validator, format-validator, hygiene-inspector
**Suggested fix:** Update folder-structure.md §3.2 to reflect actual deployed Hermes skill set, or remove extra skill folders

---

## Issue 3: Agent runtime files exceed spec (20+ items) — SPEC vs REALITY CONFLICT

**Path:** .openclaw/
**Severity:** ERROR
**Category:** Path
**Issue:** Agent runtime files exceed spec (20+ items) — SPEC vs REALITY CONFLICT
**Current:** agents/, canvas/, completions/, cron/, device-auth.json, device.json, devices/, exec-approvals.json, flows/, identity/, logs/, main.sqlite, media/, memory/, openclaw.json (+8 .bak files), subagents/, tasks/, telegram/, TOOLS.md, update-check.json, USER.md, workspace-state.json
**Expected:** Only IDENTITY.md, SOUL.md, MEMORY.md, HEARTBEAT.md, skills/
**Suggested fix:** If intentional runtime files, update folder-structure.md §3.1 to document allowed runtime artifacts (agents/, cron/, logs/, sessions/, devices/, etc.)

---

## Issue 4: Symlink at root not in whitelist

**Path:** HEARTBEAT.md
**Severity:** ERROR
**Category:** Path
**Issue:** Symlink at root not in whitelist
**Current:** HEARTBEAT.md → .openclaw/HEARTBEAT.md
**Expected:** Root whitelist: AGENTS.md, TAGS.md, README.md, knowledge-base.md only
**Suggested fix:** Remove symlink or add to folder-structure.md whitelist

---

## Issue 5: Symlink at root not in whitelist

**Path:** IDENTITY.md
**Severity:** ERROR
**Category:** Path
**Issue:** Symlink at root not in whitelist
**Current:** IDENTITY.md → .openclaw/IDENTITY.md
**Expected:** Root whitelist: AGENTS.md, TAGS.md, README.md, knowledge-base.md only
**Suggested fix:** Remove symlink or add to folder-structure.md whitelist

---

## Issue 6: Symlink at root not in whitelist

**Path:** SOUL.md
**Severity:** ERROR
**Category:** Path
**Issue:** Symlink at root not in whitelist
**Current:** SOUL.md → .openclaw/SOUL.md
**Expected:** Root whitelist: AGENTS.md, TAGS.md, README.md, knowledge-base.md only
**Suggested fix:** Remove symlink or add to folder-structure.md whitelist

---

## Issue 7: Symlink at root not in whitelist

**Path:** TOOLS.md
**Severity:** ERROR
**Category:** Path
**Issue:** Symlink at root not in whitelist
**Current:** TOOLS.md → .openclaw/TOOLS.md
**Expected:** Root whitelist: AGENTS.md, TAGS.md, README.md, knowledge-base.md only
**Suggested fix:** Remove symlink or add to folder-structure.md whitelist

---

## Issue 8: Symlink at root not in whitelist

**Path:** USER.md
**Severity:** ERROR
**Category:** Path
**Issue:** Symlink at root not in whitelist
**Current:** USER.md → .openclaw/USER.md
**Expected:** Root whitelist: AGENTS.md, TAGS.md, README.md, knowledge-base.md only
**Suggested fix:** Remove symlink or add to folder-structure.md whitelist

---

## Issue 9: File name not in allowed list for skill folders

**Path:** .hermes/skills/output-validator/validation-criteria.md
**Severity:** WARNING
**Category:** Naming
**Issue:** File name not in allowed list for skill folders
**Current:** validation-criteria.md
**Expected:** Allowed files: SKILL.md, workflow.md, examples.md, reference.md
**Suggested fix:** Rename to reference.md or add validation-criteria.md to folder-structure.md §4 whitelist

---

## Issue 10: Extra skill folder beyond the 4 spec'd

**Path:** .openclaw/skills/agent-reach/
**Severity:** WARNING
**Category:** Path
**Issue:** Extra skill folder beyond the 4 spec'd
**Current:** agent-reach/ present in addition to ingest-agent, compile-agent, index-agent, fix-agent
**Expected:** Exactly 4 subfolders: ingest-agent, compile-agent, index-agent, fix-agent
**Suggested fix:** Add agent-reach to folder-structure.md §3.1 or remove

---

## Issue 11: Expected subfolder not yet created

**Path:** wiki/drafts/
**Severity:** INFO
**Category:** Path
**Issue:** Expected subfolder not yet created
**Current:** Folder does not exist
**Expected:** wiki/drafts/ should exist per folder-structure.md §7
**Suggested fix:** Create wiki/drafts/ (tag/topic auto-generated by Index Agent; drafts/ for rejected files; archive/ for old reports)

---

## Issue 12: Expected subfolder not yet created

**Path:** wiki/reviews/archive/
**Severity:** INFO
**Category:** Path
**Issue:** Expected subfolder not yet created
**Current:** Folder does not exist
**Expected:** wiki/reviews/archive/ should exist per folder-structure.md §7
**Suggested fix:** Create wiki/reviews/archive/ (tag/topic auto-generated by Index Agent; drafts/ for rejected files; archive/ for old reports)

---

## Issue 13: Expected subfolder not yet created

**Path:** wiki/tag/
**Severity:** INFO
**Category:** Path
**Issue:** Expected subfolder not yet created
**Current:** Folder does not exist
**Expected:** wiki/tag/ should exist per folder-structure.md §7
**Suggested fix:** Create wiki/tag/ (tag/topic auto-generated by Index Agent; drafts/ for rejected files; archive/ for old reports)

---

## Issue 14: Expected subfolder not yet created

**Path:** wiki/topic/
**Severity:** INFO
**Category:** Path
**Issue:** Expected subfolder not yet created
**Current:** Folder does not exist
**Expected:** wiki/topic/ should exist per folder-structure.md §7
**Suggested fix:** Create wiki/topic/ (tag/topic auto-generated by Index Agent; drafts/ for rejected files; archive/ for old reports)

---

