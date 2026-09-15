# Hygiene Inspection — 2026-09-15

**Status:** pending
**Issues found:** 47 (4 ERROR, 43 WARNING)
**Created:** 2026-09-15 23:30:31
**Validator:** hygiene-inspector

**Paths checked:** 233744

---

## Summary

**0 ISSUE RESOLVED vs 09-14** — toàn bộ 4 ERROR là carry-forward từ các runs trước:

1. **`DREAMS.md`** root orphan — git-tracked, lần 7 liên tiếp (09-09→09-15). OpenClaw dreaming artifact.
2. **`memory/`** root folder — lần 7 liên tiếp (09-09→09-15). **+4 new dreaming files since 09-14** (deep/light/rem 2026-09-15 logs + session-corpus 2026-09-14). OpenClaw dreaming pipeline tiếp tục viết vào root `memory/`. Tổng 28 sub-files (was 24 on 09-14).
3. **Migration marker** `openclaw-workspace-state.json.migrated.*` — git-tracked since `b5e519fc`, lần 8 liên tiếp từ 09-08 addendum.
4. **`wiki/HEARTBEAT.md`** — broken symlink lần 16 liên tiếp (08-26→09-15).

**WARNING:** 28 memory/ sub-files (sub-paths của Issue 2) + 15 backup files trong archive (false positive — non-report artifacts, scanner áp report naming convention cho tất cả archive files).

**Tin tốt:** `openclaw-workspace-state.json` gốc vắng mặt streak 19+ runs. 0 naming violations mới. 0 empty dir. 0 new root-level orphans. Pipeline relatively quiet — +9 paths since 09-14 (233,735→233,744).

Không `[SYSTEMATIC VIOLATION]` mới. Không `[SPEC CONFLICT]`. Không `[STRUCTURE CHANGE]`.

---

## Issue 1: Known root orphan — DREAMS.md

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: DREAMS.md
**Current:** `DREAMS.md` at KB root (5.1K, git-tracked)
**Expected:** Should be in `wiki/drafts/` or `.openclaw/` (OpenClaw dreaming artifact)
**Suggested fix:** See known issue — no action (proven futile)
**Carry-forward:** Lần 7 liên tiếp (09-09→09-15). Root cause = OpenClaw dreaming pipeline.

---

## Issue 2: Recurring root folder — memory/

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist: memory/
**Current:** `memory/` at KB root — 28 files (7 session-corpus + 7 deep + 7 light + 7 rem)
**Expected:** Root cause = OpenClaw dreaming pipeline writes to root `memory/` instead of `.openclaw/memory/`
**Suggested fix:** Remove directory: rmdir memory/
**Carry-forward:** Lần 7 liên tiếp (09-09→09-15). +4 files since 09-14 (dreaming deep/light/rem 2026-09-15 + session-corpus 2026-09-14).

---

## Issue 3: Migration marker at root

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist
**Current:** Migration marker at KB root (git-tracked since `b5e519fc`)
**Expected:** Should be in `.openclaw/` or gitignored
**Suggested fix:** `.gitignore` add `openclaw-workspace-state.json.migrated.*` + `git rm --cached` + commit
**Carry-forward:** Lần 8 liên tiếp từ 09-08 addendum. Root cause confirmed in vendor source (SKILL.md v1.21 pitfall #9). Git-level clean but marker pollutes repo.

---

## Issue 4: HEARTBEAT.md leak into wiki/

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** `wiki/HEARTBEAT.md` — broken symlink → `../../.openclaw/HEARTBEAT.md`
**Expected:** HEARTBEAT.md belongs in .hermes/ or .openclaw/
**Suggested fix:** Identify and fix the process (sync tool mirroring); then delete this file
**Carry-forward:** Lần 16 liên tiếp (08-26→09-15). Process-level fix needed.

---

## WARNINGs (43 total)

### Memory/ sub-files (28 files)

Sub-paths của Issue 2 — OpenClaw dreaming pipeline files at root `memory/`:

| Subfolder | Files | Date range |
|---|---|---|
| `memory/.dreams/session-corpus/` | 7 (.txt) | 09-08 → 09-14 |
| `memory/dreaming/deep/` | 7 (.md) | 09-09 → 09-15 |
| `memory/dreaming/light/` | 7 (.md) | 09-09 → 09-15 |
| `memory/dreaming/rem/` | 7 (.md) | 09-09 → 09-15 |

All are sub-paths of the recurring `memory/` root folder (Issue 2). Fix the root cause (redirect dreaming pipeline output) and these disappear.

### Archive backup files (15 files)

Non-report artifacts in `wiki/reviews/archive/2026-09/` — Fix Agent backup files from 2026-09-01 rename operation. Scanner flags them as "Archived report naming" but they are not reports — **false positive**.

Files: `anthropic-cybersecurity-skills-backup-2026-09-01.md`, `archify-backup-2026-09-01.md`, `impeccable-backup-2026-09-01.md`, `openviking-backup-2026-09-01.md`, `posthog-backup-2026-09-01.md`, `threeui-backup-2026-09-01.md`, `destination-vs-vehicle-backup-2026-07-20.md`, `is-there-anything-left-to-build-in-crypto-wintermute-backup-2026-07-20.md`, `memory-backup-2026-06-15.md`, `psychic-energy-backup-2026-07-20.md`, `raw-backlog-backup-2026-06-15.md`, `social-attraction-backup-2026-07-20.md`, `src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md`, `src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md`, `temp-content-backup-2026-06-15.md`.

**Action needed:** Fix Agent cleanup or scan script archive exclusion update.
