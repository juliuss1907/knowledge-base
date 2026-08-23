# Hygiene Inspection — 2026-08-22

**Status:** approved
**Approved by:** Julius
**Issues found:** 2
**Created:** 2026-08-22 23:31:42
**Validator:** hygiene-inspector

**Paths checked:** 55809

---

## Issue 1: File not in root whitelist

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Path
**Issue:** Unknown file at KB root — không có trong whitelist §2 của folder-structure.md v1.2. Git-tracked (lần đầu appear trong commit `61316a57` vault backup 2026-08-22 14:24:00), absent khỏi mọi cây lịch sử đã check (07-15, 08-20, 08-21) → xuất hiện lần đầu HÔM NAY. Nội dung là OpenClaw runtime state (`{"version": 1, "setupCompletedAt": "2026-05-12T03:08:10.539Z"}`); mtime 14:20 nằm đúng cửa sổ phiên Fix Agent 08-22 (batch applied 14:40, session commits 15:09–15:19). Cùng lớp lỗi với rò rỉ `memory/`: tiến trình OpenClaw ghi runtime state vào KB root thay vì `.openclaw/`.
**Current:** `openclaw-workspace-state.json` (JSON 69 byte, mode 600, git-tracked)
**Expected:** Root chỉ cho phép AGENTS.md, TAGS.md, README.md, knowledge-base.md, 5 identity symlinks, .gitignore. Runtime state thuộc về `.openclaw/`.
**Suggested fix:** Root-cause — xác định tiến trình OpenClaw đã materialize file (nghi vấn: session runtime của fix-agent ngày 2026-08-22) và redirect output path về `.openclaw/`, sau đó `git rm openclaw-workspace-state.json` + commit. Xóa file đơn thuần là không đủ: file đã git-tracked, `vault backup` (~5 phút/lần) giữ nó trong lịch sử và bất kỳ checkout/sync nào đều hồi sinh.

---

## Issue 2: Draft filename: lowercase-hyphen only

**Path:** wiki/drafts/fixagent-regen-tags.py
**Severity:** WARNING
**Category:** Naming
**Issue:** File non-markdown trong wiki/drafts/. Spec §7 chỉ cho phép `<slug>.md` trong drafts/. Đây là script Python để lại từ phiên Fix Agent 2026-08-22 (helper regen tag file; mtime 15:18, committed 15:19 qua `3d5d40c5`). Slug tuân thủ lowercase-hyphen — violation nằm ở phần mở rộng `.py` / kiểu nội dung.
**Current:** `wiki/drafts/fixagent-regen-tags.py`
**Expected:** `wiki/drafts/<slug>.md` — drafts/ chỉ chứa markdown draft bị reject; utility script thuộc `scripts/`
**Suggested fix:** Chuyển sang `scripts/fixagent-regen-tags.py` (zone được whitelist cho utility scripts) hoặc xóa nếu công việc session đã xong.

---

## Summary

**Total issues:** 2 (1 ERROR, 1 WARNING, 0 INFO)
**Paths checked:** 55809
**Report limit:** 20 (not truncated)

**Delta from 2026-08-21 (previous hygiene report):** −17 issues (19→2). Cả hai orphan cũ đã được giải quyết: `memory/` (16 files) + `state/` biến mất sau khi Fix Agent apply batch 2026-08-22 14:40 — lần đầu sạch hoàn toàn kể từ streak 08-11→08-13. Không còn HEARTBEAT leak ở bất kỳ đâu (wiki/, wiki/reviews/, raw/). Cả 2 issue mới đều sinh ra HÔM NAY trong cùng cửa sổ phiên Fix Agent (14:20–15:19): 1 runtime-state file mới ở root + 1 script sót lại trong drafts/. Paths checked +2198 (53611→55809) — toàn bộ tăng trưởng nằm trong `.hermes/` (54,948 files), thuộc catch-all agent-home zone của spec, không cần hành động. raw/, wiki/ (concepts/sources/tag/topic/meta/reviews), context/, scripts/: sạch, không naming violation nào khác.

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Pattern: OpenClaw runtime tiếp tục nhả process artifacts vào KB root. `memory/` đã leak 6 lần từ tháng 7 (được sửa 2026-08-22 14:40); vài giờ sau đó, artifact MỚI cùng lớp xuất hiện tại root — `openclaw-workspace-state.json` (14:20), cộng thêm 1 script `.py` sót lại trong `wiki/drafts/` (15:18). Cả hai đều git-tracked qua `vault backup` auto-commit (~5 phút/lần), nên xóa file hệ thống đơn thuần không thể khắc phục.
Likely cause: Session runtime của OpenClaw (phiên batch fix-agent ngày 2026-08-22) mặc định ghi file làm việc/state vào CWD (= KB root) thay vì agent home `.openclaw/`.
Recommendation: Sửa cấu hình working-dir/output-path của session runtime (file state → `.openclaw/`, script tạm → ngoài KB hoặc `scripts/` kèm dọn dẹp cuối session), sau đó `git rm` cả 2 file + commit. Trước khi thay đổi default của writer, mỗi session agent tương lai có nguy cơ leak artifact mới vào root.
```

```
[STRUCTURE CHANGE]
Không phát hiện thay đổi whitelist trong lần chạy này. folder-structure.md vẫn v1.2 (2026-05-17); dictionary quét đồng bộ với spec. Chênh lệch so với 08-21 chỉ là orphan churn + tăng trưởng runtime `.hermes/`.
```
