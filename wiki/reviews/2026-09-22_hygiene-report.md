# Hygiene Inspection — 2026-09-22

**Status:** pending
**Issues found:** 76 (4 ERROR + 72 WARNING + 0 INFO)
**Created:** 2026-09-22 23:30:55 +0700
**Validator:** hygiene-inspector

**Paths checked:** 234,083

---

## Summary

**0 ISSUE RESOLVED vs 09-21** — all 4 ERROR carry-forward.

| Severity | 09-21 | 09-22 | Delta |
|---|---|---|---|
| ERROR | 4 | 4 | 0 |
| WARNING | 68 | 72 | +4 |
| INFO | 0 | 0 | 0 |
| **Total** | **72** | **76** | **+4** |

**Paths checked:** 233,868 (09-21) → 234,083 (09-22) = +215
**memory/ sub-files:** 53 (09-21) → 57 (09-22) = +4

---

## Issue 1: DREAMS.md root orphan — CARRY-FORWARD

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — known root orphan
**Current:** `DREAMS.md` (600 bytes, git-tracked, created 09-17)
**Expected:** Only whitelisted root files allowed
**Suggested fix:** Fix Agent: `git rm DREAMS.md` + commit; identify/fix OpenClaw dreaming process output path
**Consecutive runs:** 24+ (09-09→09-22)

## Issue 2: memory/ root folder — CARRY-FORWARD

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Recurring root folder not in whitelist
**Current:** `memory/` — **57 sub-files** (was 53 on 09-21, +4 new dreaming files: deep/light/rem 09-22 + 1 session-corpus 09-21)
**Expected:** Contents should be in `.openclaw/memory/` (migrated in folder-structure.md v1.2)
**Suggested fix:** Fix Agent: `git rm -r memory/` + commit; fix OpenClaw dreaming process output path
**Consecutive runs:** 28+ (07-03→09-22)

## Issue 3: Migration marker `.migrated.*` at root — CARRY-FORWARD

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** File not in root whitelist — migration marker from OpenClaw runtime
**Current:** 69 bytes, git-tracked since `b5e519fc` (09-08 20:45), no fresh write
**Expected:** Should be gitignored; `.gitignore` needs wildcard pattern `openclaw-workspace-state.json.migrated.*`
**Suggested fix:** Fix Agent: `.gitignore` add `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit
**Consecutive runs:** 14 (from 09-08 addendum)

## Issue 4: wiki/HEARTBEAT.md broken symlink — CARRY-FORWARD

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root — dangling symlink (target `../../.openclaw/HEARTBEAT.md` does not exist)
**Current:** Dangling symlink → `../../.openclaw/HEARTBEAT.md`
**Expected:** HEARTBEAT.md belongs in `.hermes/` or `.openclaw/`; process-level fix required
**Suggested fix:** Fix Agent: remove symlink; process-level fix (sync tool mirroring root HEARTBEAT into wiki/)
**Consecutive runs:** 27+ (08-26→09-22)

---

## WARNING breakdown (72 total)

- **57 memory/ sub-files** — sub-paths of Issue 2 (dreaming deep/light/rem 09-09→09-22, session-corpus 09-08→09-21, 2026-09-17.md). +4 vs 09-21 (53→57).
- **15 archive backup false positives** — unchanged from prior runs. Non-report artifacts in `wiki/reviews/archive/` flagged by scanner naming convention check.

---

## Notes

- **0 new naming violations** — no new files in wiki/ or raw/ since 09-21.
- **0 empty directories.**
- **0 new structural issues.**
- **`openclaw-workspace-state.json` root file**: vắng mặt streak 28+ runs (known — migrated to `~/.openclaw/workspace-state.json` on 09-08 20:42; pitfall #9).
- **Pipeline idle today**: 0 wiki files changed since 09-21 (git log confirms 0 commits adding/removing wiki content).
- **memory/ growth pattern unchanged**: OpenClaw dreaming pipeline writes daily 3 dreaming files (deep/light/rem) + periodic session-corpus files.

---

## Actions needed

1. **KHÔNG xóa `DREAMS.md`** — carry-forward, git-tracked, root-cause known.
2. **KHÔNG xóa `memory/`** — carry-forward, OpenClaw dreaming pipeline active.
3. **KHÔNG re-escalate `[SYSTEMATIC VIOLATION]`** — all carry-forwards from prior reports.
4. **Fix Agent**: `.gitignore` thêm `openclaw-workspace-state.json.migrated.*` + `git rm --cached` marker + commit.
5. **`wiki/HEARTBEAT.md`** — process-level fix (sync tool mirroring); deletion is transient.

---

*Report generated 2026-09-22 23:30:55 +0700 by Hygiene Inspector (hygiene-inspector skill v1.27)*
