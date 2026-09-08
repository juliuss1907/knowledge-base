# Hygiene Inspection — 2026-09-08

**Status:** pending
**Issues found:** 12
**Created:** 2026-09-08 08:15:30
**Validator:** hygiene-inspector

**Paths checked:** 56020

**Context:** Fresh run cho 09-08 (report trước: 09-02; 6 ngày gap — 09-03/09-04 vault backup vẫn chạy, 09-05→09-07 không có commit, auto-commit resumed 09-08 08:13). 0 file raw mới kể từ 09-02; wiki/ có mtime churn trên topic pages (Index Agent 09-03) nhưng chỉ +9 paths net. Tất cả 12 issues đều là carry-forward đã biết — 0 issue mới, 0 naming violation mới, 0 empty directory, 0 INFO.

---

## Issue 1: Known root orphan — openclaw-workspace-state.json (CARRIED FORWARD — lần 12 liên tiếp)

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** Known root orphan: openclaw-workspace-state.json
**Current:** File 69 bytes vẫn ở KB root
**Expected:** OpenClaw runtime state home (.openclaw/ hoặc ~/.openclaw/)
**Suggested fix:** KHÔNG xóa lần 13 — deletion proven futile x3 (recycle < 1h). Root cause ĐÃ CONFIRM trong vendor source (SKILL.md v1.21 pitfall #9): OpenClaw treats any dir with AGENTS.md as workspace; state path resolves CWD-relative by design (dist/workspace-DkQ7irPD.js). .gitignore guard giữ repo sạch (untracked + ignored) — chỉ disk-level orphan persists. Fix = redirect writer output path HOẶC chờ OpenClaw SQLite workspace-state refactor. KHÔNG re-escalate — tham chiếu pitfall #9.

**Trạng thái liên tiếp:** 08-22 → 09-08, 12 lần liên tiếp (lần 11 tại run 09-02).

---

## Issue 2: HEARTBEAT.md leaked into wiki/ root (CARRIED FORWARD — lần 8 liên tiếp)

**Path:** wiki/HEARTBEAT.md
**Severity:** ERROR
**Category:** Orphan
**Issue:** HEARTBEAT.md leaked into wiki/ root (recurring process leak)
**Current:** Symlink wiki/HEARTBEAT.md → ../../.openclaw/HEARTBEAT.md
**Expected:** HEARTBEAT.md belongs in .hermes/ hoặc .openclaw/; file deletion là transient — writing process phải được fix
**Suggested fix:** Process-level fix: xác định sync tool đang mirror root symlink HEARTBEAT.md → .openclaw/HEARTBEAT.md vào wiki/ và sửa output path; sau đó mới xóa file. Untracked + gitignored — không vào commit.

**Trạng thái liên tiếp:** 08-26 → 09-08, 8 lần liên tiếp (lần 7 tại run 09-02).

---

## Issue 3: Repos file naming — uppercase owner (CARRIED FORWARD từ 09-02)

**Path:** raw/repos/2026-08-30_MengTo_threeui.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: owner segment phải lowercase (folder-structure.md §8 slug rule)
**Current:** `2026-08-30_MengTo_threeui.md`
**Expected:** `2026-08-30_mengto_threeui.md`
**Suggested fix:** Rename owner segment → lowercase (`mengto_threeui`). Fix Agent action đã deferred từ run 09-02, chưa thực hiện. Two-step fix nuance: thêm owner segment KHÔNG đủ — owner cũng phải lowercase.

---

## Issue 4: Repos file naming — uppercase owner (CARRIED FORWARD từ 09-02)

**Path:** raw/repos/2026-08-30_PostHog_posthog.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Repos file naming: owner segment phải lowercase (folder-structure.md §8 slug rule)
**Current:** `2026-08-30_PostHog_posthog.md`
**Expected:** `2026-08-30_posthog_posthog.md`
**Suggested fix:** Rename owner segment → lowercase (`posthog_posthog`). Fix Agent action đã deferred từ run 09-02, chưa thực hiện.

---

## Issue 5: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_anthropic-cybersecurity-skills-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_anthropic-cybersecurity-skills-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 1/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 (original escalation: run 2026-09-02, 8 files — Fix Agent tạo pre-rename backups 09-01 09:57). Fix Agent: archive/xóa sau khi xác nhận rename thành công + cập nhật Fix Agent SKILL.md backup policy (đặt backup ngoài wiki/drafts/). Hermes KHÔNG tự xóa — write zone chỉ wiki/reviews/.

---

## Issue 6: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_archify-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_archify-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 2/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 7: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_impeccable-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_impeccable-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 3/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 8: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_openviking-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_openviking-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 4/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 9: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_posthog-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_posthog-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 5/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 10: Draft filename — Fix Agent backup artifact (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/2026-08-30_threeui-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix + underscore + `-backup-` suffix vi phạm `<slug>.md` naming
**Current:** `2026-08-30_threeui-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 6/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 11: Draft filename — Fix Agent backup artifact, `src_` prefix (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: date-prefix... — file này dùng `src_` prefix + `-backup-` suffix, vi phạm draft naming trên 2 trục
**Current:** `src_ai-engineering-skills-map-building-deploying-ai-applications-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 7/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Issue 12: Draft filename — Fix Agent backup artifact, `src_` prefix (CARRIED FORWARD từ 09-02)

**Path:** wiki/drafts/src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md
**Severity:** WARNING
**Category:** Naming
**Issue:** Draft filename: `src_` prefix + `-backup-` suffix, vi phạm draft naming trên 2 trục
**Current:** `src_ai-engineering-skills-map-software-engineering-fundamentals-backup-2026-09-01.md`
**Expected:** `<lowercase-hyphen-slug>.md`
**Suggested fix:** 8/8 backup files từ [SYSTEMATIC VIOLATION] 09-02 — xem Issue 5.

---

## Carry-forward log

Theo carry-forward rule (SKILL.md, 2026-09-01): KHÔNG issue nào trong 12 issues trên được escalate mới.

| Issue nhóm | Original escalation | Trạng thái |
|---|---|---|
| `openclaw-workspace-state.json` (Issue 1) | Root cause confirmed 08-25, pitfall #9 — KHÔNG re-escalate | Chờ process fix / SQLite refactor |
| `wiki/HEARTBEAT.md` (Issue 2) | Process leak — flagged mỗi run từ 08-26 | Chờ process-level fix |
| 2 repos casing files (Issues 3-4) | Deferred Fix Agent tại run 09-02 | Chưa có Fix Agent action |
| 8 backup files `wiki/drafts/` (Issues 5-12) | [SYSTEMATIC VIOLATION] original 2026-09-02 (8 files) | Chưa có Fix Agent action — carried forward |

**Tin tốt:** `memory/` + `state/` vắng mặt — chạy sạch lần **11** liên tiếp (08-14 → 09-08). 0 empty directory. 0 file raw mới. 0 naming violation mới ngoài nhóm carry-forward. Không có [SPEC CONFLICT] mới. Không có [STRUCTURE CHANGE].

**Actions needed (cho Julius):**
1. KHÔNG xóa `openclaw-workspace-state.json` lần 13 (pitfall #9 — proven futile).
2. KHÔNG re-escalate 2 orphan đã biết.
3. Fix Agent — 2 items deferred từ 09-02 vẫn outstanding: (1) rename 2 repos files lowercase owner (`mengto_threeui`, `posthog_posthog`); (2) dọn 8 backup files trong `wiki/drafts/` + cập nhật Fix Agent SKILL.md backup policy.
4. Không có action mới nào khác — KB structure sạch so với 09-02.
