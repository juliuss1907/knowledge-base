# Hygiene Inspection — 2026-08-24

**Status:** applied
**Applied by:** fix-agent
**Applied at:** 2026-08-25 10:18
**Approved by:** Julius
**Issues found:** 1
**Created:** 2026-08-24 23:33:11
**Validator:** hygiene-inspector

**Paths checked:** 55845

---

## Issue 1: Known root orphan — openclaw-workspace-state.json (LẦN 3 LIÊN TIẾP)

**Path:** openclaw-workspace-state.json
**Severity:** ERROR
**Category:** Orphan
**Issue:** OpenClaw runtime workspace state file ở KB root — không thuộc root whitelist (folder-structure.md §2). Lần thứ 3 liên tiếp bị flag (08-22, 08-23, 08-24).
**Current:** File tồn tại trên disk (69 bytes, mtime 10:00 hôm nay), gitignored (.gitignore dòng 88–89) và KHÔNG còn được track trong index.
**Expected:** Không được tồn tại ở KB root. State của OpenClaw runtime phải nằm trong agent home (`.openclaw/` hoặc `~/.openclaw/`).
**Suggested fix:** Root-cause bắt buộc — xem escalation bên dưới. Deletion + gitignore đã được áp dụng lại sáng nay (removal commit `b568979f` 09:52) nhưng runtime recreate lúc 10:00 cùng ngày → recycle < 1h, nhanh hơn cả chu kỳ 12h trước đây. Deletion đơn thuần vô hiệu hoàn toàn.

---

## Escalation

```
[SYSTEMATIC VIOLATION]
Pattern: openclaw-workspace-state.json tái diễn lần 3 liên tiếp (08-22 → 08-24).
         Mỗi lần apply sáng hôm sau đều bị runtime recreate trong ngày
         (08-23: recycle < 12h; 08-24: recycle < 1h — 10:00 so với removal 09:52).
Likely cause: OpenClaw session/runtime state writer ghi ra KB root thay vì agent home.
         Writer vẫn active trên OpenClaw 2026.7.1-2. Gitignore guard đang giữ repo
         sạch (file untracked + ignored), nhưng disk-level orphan tiếp tục tái diễn.
Recommendation: Hai lựa chọn cho Julius:
  (1) Chờ OpenClaw update có SQLite workspace-state refactor (theo note 08-23 —
      sẽ hết hẳn); hoặc
  (2) Tìm process ghi file này và redirect output path về ~/.openclaw/.
Không cần action thêm từ Fix Agent cho đến khi có một trong hai fix trên —
việc xóa lại file lần 4 không thay đổi kết quả.
```

**Ghi chú git:** File vẫn còn trong lịch sử git (các commit `vault backup` trước 09:52 hôm nay). Đây chỉ là vấn đề thẩm mỹ lịch sử — index hiện tại sạch nhờ git rm + gitignore. Không khuyến nghị rewrite history.

---

## Clean checks

| Kiểm tra | Kết quả |
|---|---|
| `memory/` root | Vắng mặt — chạy sạch thứ 3 liên tiếp (08-22 → 08-24) |
| `state/` root | Vắng mặt — chạy sạch thứ 3 liên tiếp |
| HEARTBEAT leak (`wiki/`, `wiki/reviews/`, `raw/.last_heartbeat`) | Không phát hiện |
| Naming violations (raw/, wiki/, drafts/, reviews/) | Không phát hiện |
| Path whitelist (root, context/, raw/, wiki/, scripts/) | Sạch ngoài 1 ERROR trên |
| Empty directories | Không phát hiện |

---

## Comparison với run trước

| Run | Paths | Issues | Ghi chú |
|---|---|---|---|
| 08-22 | 55809 | 2 (1E+1W) | Lần đầu thấy root json + script sót drafts/ |
| 08-23 | 55832 | 1 (1E) | Root json lần 2; memory/state sạch lần 2 |
| **08-24** | **55845** | **1 (1E)** | Root json lần 3; memory/state sạch lần 3 |

KB grew +13 paths vs 08-23. Debt giữ nguyên 1 ERROR duy nhất — không có regression mới, không có violation mới.
