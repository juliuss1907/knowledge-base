# Hygiene Inspection — 2026-10-30

**Status:** pending
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **5 đã RESOLVED / SẠCH** (E2, E4, E8, E9, E10) + **0 mới** ⇒ **9 ERROR còn hiệu diện**; **0 ERROR mới**. Tồn đọng trong agent home giữ nguyên ở mức **25 tệp tracked** ở HEAD (18 `config.yaml.bak.*`, 5 `kanban.db*`, 1 `projects.db`, 1 `MEMORY.md`; 0 tệp trong `skills/.curator_backups/`). Trong đó **4 ERROR máy** (path thật ở tầng quét) + **5 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-10-30 23:35:00
**Validator:** hygiene-inspector
**Version:** 1.35
**Git commit / HEAD:** `a9f1e3fb` (2026-10-30 23:21:40 +0700) — in sync 100% vs GitHub `origin/master` (`a9f1e3fbff81d5f200640d56d53d8e33d194d539`). 🟢 `vault backup` cron hoạt động trơn tru (29 commit trong 24h).

**Paths checked:** **1.753 tệp ổn định** trong phạm vi KB lúc quét (1.742 tệp vùng nội dung + 11 tệp/symlink root) → **1.754 tệp post-write** (sau khi ghi báo cáo này vào `wiki/reviews/`) + **74 thư mục** (9 root + 23 vùng nội dung bao gồm thư mục gốc vùng + 42 L1 agent home) + **99 tệp tầng đầu agent home BIẾN ĐỘNG** (77 `.hermes` + 22 `.openclaw`).

---

### Bảng đối chiếu định nghĩa số đếm (tránh hiểu nhầm tăng trưởng kho)

| Định nghĩa | Lệnh / Quy chuẩn | Số đếm 2026-10-30 | Ghi chú |
|---|---|---|---|
| **Phạm vi KB thực tế (tệp ổn định)** | 4 vùng nội dung (`raw/`, `wiki/`, `context/`, `scripts/`) + tệp root | **1.753 tệp** (1.754 post-write) | Tăng +2 tệp vs 10-29 lúc quét (1.751 → 1.753: +1 báo cáo Hygiene 10-29, +1 báo cáo Format 10-30). Nợ mới nội dung = 0. |
| **Phạm vi thư mục KB** | 9 root + 23 vùng nội dung (gồm gốc vùng) + 42 L1 agent home | **74 thư mục** | Ổn định, khớp 10-29 (9 root + 23 content + 27 hermes + 15 openclaw). |
| **Tệp L1 agent home (biến động)** | `.hermes/*` + `.openclaw/*` (chỉ file tầng 1) | **99 tệp** (77 hermes + 22 openclaw) | Socket loại trừ (`gateway.sock`); file runtime phiên làm việc. Khớp 10-29. |
| **Quét máy (prune mọi `.git`)** | `find . -name .git -prune -o \( -type f -o -type l \) -print` | **234.658 tệp** | Tăng +6 tệp vs 10-29 (234.652): +4 tệp `memory/` (202→206) do OpenClaw dreaming 10-30, +1 review format 10-30, +1 review hygiene 10-29. 99,2% là `.hermes/`. |
| **Quét máy (prune root `.git` + `hermes-agent`)** | Scan script template chuẩn | **11.204 tệp** | Tăng +6 tệp vs 10-29 (11.198): +4 tệp `memory/` + 1 review format + runtime artifacts. |
| **Quét máy (chỉ prune root `.git`)** | Giữ lại `.hermes/hermes-agent/.git` | **236.733 tệp** | Chênh đúng 2.075 tệp của repo `.git` con trong `hermes-agent`. |

---

## I. Danh sách các nhóm ERROR (14 nhóm: 5 RESOLVED/SẠCH, 9 HIỆU DIỆN)

### E1: Bản cài đặt mã nguồn Hermes Agent lồng trong `.hermes/hermes-agent/` (5,6 GB)
- **Path:** `.hermes/hermes-agent/`
- **Severity:** ERROR (carry-forward từ 10-01)
- **Category:** Path | Orphan
- **Issue:** Thư mục chứa toàn bộ mã nguồn Hermes Agent với 225.408 tệp / 5,6 GB, có repository git riêng lồng bên trong (`.git` con chứa 2.075 tệp / 1,7 GB, branch `main`, commit `990473a79c`).
- **Trạng thái Git:** Đã được bảo vệ an toàn bởi `.gitignore:59` (`.hermes/hermes-agent/`), 0 tệp bị track vào git KB. Gitlink `160000` cũ đã gỡ bỏ hoàn toàn.
- **Khuyến nghị:** Cần dọn dẹp hoặc di dời môi trường chạy Hermes ra ngoài thư mục KB khi có kế hoạch bảo trì. **CẢNH BÁO:** Không chạy `rm -rf` khi tiến trình agent đang chạy từ thư mục này.

### E2: Trạng thái tiến trình `vault backup` cron và đồng bộ Git
- **Path:** Toàn bộ repository (`.git/`)
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Path | Synchronization
- **Issue:** Trạng thái sao lưu tự động `vault backup`.
- **Hiện trạng 2026-10-30:** HEAD commit `a9f1e3fb` (2026-10-30 23:21:40 +0700) hoàn toàn đồng bộ với `origin/master` trên GitHub (`a9f1e3fbff81d5f200640d56d53d8e33d194d539`). Cron chạy liên tục và tạo 29 commit trong 24h qua.
- **Backlog:** 0 tệp `??` và 0 tệp ` M` trong các vùng nội dung KB (`raw/`, `wiki/`, `context/`, `scripts/`). Đồng bộ hoàn hảo.

### E3: 13 mẫu tệp runtime agent home không có quy tắc `.gitignore` bảo vệ
- **Path:** `.hermes/` và `.openclaw/`
- **Severity:** ERROR (carry-forward từ 09-30)
- **Category:** Path | Security & Hygiene
- **Issue:** Tệp runtime sinh ra trong quá trình tác nhân hoạt động.
- **Hiện trạng:** Đã có 9/13 mẫu được bảo vệ an toàn bởi `.gitignore`. Tồn đọng giữ nguyên ở mức **25 tệp tracked** tại HEAD:

| Mẫu tệp | Số tệp tracked | Quy tắc .gitignore | Trạng thái |
|---|---|---|---|
| `.hermes/config.yaml.bak.*` | 18 tệp | Chưa có rule | Cần thêm rule + `git rm --cached` |
| `.hermes/kanban.db*` | 5 tệp (`db`, `shm`, `wal`, 2 `lock`) | Chưa có rule | Cần thêm rule + `git rm --cached` |
| `.hermes/projects.db` | 1 tệp | Chưa có rule | Cần thêm rule + `git rm --cached` |
| `.hermes/MEMORY.md` | 1 tệp | `.gitignore:110` | Rule có hiệu lực nhưng tệp commit trước rule |
| `.hermes/skills/.curator_backups/` | **0 tệp** | `.gitignore:73` | **SẠCH TRÊN GIT** 🟢 (commit `5c428364` đã xoá) |
| 8 mẫu runtime còn lại | **0 tệp** | Đầy đủ rule | An toàn 🟢 |

- **Khuyến nghị:** Fix Agent chạy `git rm -r --cached` cho 25 tệp còn lại và bổ sung các rule còn thiếu vào `.gitignore`.

### E4: Tệp credential và auth state trong `.openclaw/`
- **Path:** `.openclaw/`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security
- **Issue:** Các tệp xác thực của OpenClaw.
- **Hiện trạng:** Cả 4 tệp auth (`device-auth.json`, `identity/device-auth.json`, `agents/main/agent/auth-profiles.json`, `agents/main/agent/auth-state.json`) đều **0 tệp tracked trong Git** và được bảo vệ an toàn bởi `.gitignore:100,101,122`. Không có nguy cơ lộ bí mật.

### E5: Kho lưu trữ checkpoint của Hermes tại `.hermes/checkpoints/`
- **Path:** `.hermes/checkpoints/`
- **Severity:** ERROR (carry-forward từ 09-29)
- **Category:** Path | Runtime Storage
- **Issue:** Kho lưu trữ đối tượng checkpoint (26 tệp / 168 KB).
- **Trạng thái Git:** 0 tệp tracked trong Git, được bảo vệ bởi `.gitignore:60`. Không phải repo git lồng (không có `.git`, chỉ có `store/HEAD`). Không cần hành động khẩn cấp.

### E6: Thư mục sao lưu của Curator tại `.hermes/skills/.curator_backups/` và `.hermes/.curator_backups/`
- **Path:** `.hermes/skills/.curator_backups/` và `.hermes/.curator_backups/`
- **Severity:** ERROR (carry-forward từ 09-29)
- **Category:** Path | Backup Artifacts
- **Issue:** Bản sao lưu kỹ năng của Curator.
- **Trạng thái Git:** **0 tệp tracked** tại HEAD (đã duy trì sạch sau khi commit `5c428364` xoá các tệp dư thừa). Đã có rule `.gitignore:61,73`.
- **Khuyến nghị:** Duy trì theo dõi để đảm bảo Curator không vô tình commit bản sao lưu mới vào Git.

### E7: 2 marker migration của OpenClaw workspace state
- **Path:** `openclaw-workspace-state.json.migrated...` (root) và `.openclaw/workspace-state.json.migrated...` (.openclaw/)
- **Severity:** ERROR (carry-forward từ 09-08 / 09-25)
- **Category:** Path | Artifact Leak
- **Issue:** 2 tệp marker migration (69 bytes mỗi tệp) bị commit vào Git từ ngày 2026-09-08 (commit `b5e519fc`, blob `a0105ac6...`).
- **Trạng thái Git:** Cả 2 tệp đều còn bị track trong Git, chưa có rule wildcard `*.migrated.*` trong `.gitignore`.
- **Khuyến nghị:** Fix Agent chạy `git rm --cached` cho cả 2 tệp và bổ sung `*.migrated.*` vào `.gitignore`.

### E8: Tệp cấu hình `.hermes/config.yaml`
- **Path:** `.hermes/config.yaml`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security & Config
- **Issue:** Tệp cấu hình chính của Hermes Agent.
- **Hiện trạng:** 0 tệp tracked trong Git, đã được bảo vệ an toàn bởi `.gitignore:67`.

### E9: Backlog tệp nội dung chưa được commit vào Git
- **Path:** `raw/`, `wiki/`, `context/`, `scripts/`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Synchronization
- **Issue:** Tồn đọng tệp chưa commit.
- **Hiện trạng:** `git status --porcelain raw/ wiki/ context/ scripts/` sạch 100% (0 tệp `??`, 0 tệp ` M`). Mọi nội dung tri thức đã được sao lưu đầy đủ.

### E10: Tệp `wiki/topic/brain-threat-detection.md` bị xóa khỏi đĩa
- **Path:** `wiki/topic/brain-threat-detection.md`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Orphan
- **Issue:** Topic bị xóa khỏi đĩa nhưng còn vết xóa trong git.
- **Hiện trạng:** Vết xóa đã được commit đầy đủ từ đợt dọn 10-04 (`3b891e34`). Không còn tồn đọng.

### E11: Tệp `DREAMS.md` tại thư mục gốc KB
- **Path:** `DREAMS.md`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Tệp sinh ra tại thư mục gốc (16.980 B, mtime 2026-10-28 03:00:04, do OpenClaw dreaming ghi nhận).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:82`.
- **Khuyến nghị:** Cấu hình tiến trình dreaming của OpenClaw ghi vào `.openclaw/workspace-state/` thay vì KB root.

### E12: Thư mục `memory/` tại thư mục gốc KB
- **Path:** `memory/`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Thư mục ngoài whitelist tại root, chứa 206 tệp / 6 thư mục / 184.414 bytes (tăng +4 tệp so với 10-29: 4 tệp do OpenClaw dreaming ghi vào `memory/dreaming/` và `memory/.dreams/session-corpus/`).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:113`.
- **Khuyến nghị:** Chuyển hướng tiến trình ghi nhật ký phiên của OpenClaw vào `.openclaw/memory/`.

### E13: Symlink `wiki/HEARTBEAT.md` hỏng (dangling symlink)
- **Path:** `wiki/HEARTBEAT.md`
- **Severity:** ERROR
- **Category:** Path | Symlink
- **Issue:** `wiki/HEARTBEAT.md` là symlink trỏ về `../../.openclaw/HEARTBEAT.md`. Do thừa một cấp thư mục (`../../`), đường dẫn đích giải quyết thành `/home/julius/.openclaw/HEARTBEAT.md` (không tồn tại ngoài KB). Đích thực tế nằm tại `<KB>/.openclaw/HEARTBEAT.md`.
- **Khuyến nghị:** Fix Agent sửa symlink thành `../.openclaw/HEARTBEAT.md` và tái lập symlink root `HEARTBEAT.md → .openclaw/HEARTBEAT.md`.

### E14: Tổng hợp 25 tệp runtime agent home còn bị track trong Git
- **Path:** `.hermes/`
- **Severity:** ERROR (carry-forward từ 10-04)
- **Category:** Security & Repository Hygiene
- **Issue:** 25 tệp runtime (18 `config.yaml.bak.*`, 5 `kanban.db*`, 1 `projects.db`, 1 `MEMORY.md`) vẫn còn trong Git index.
- **Khuyến nghị:** Chạy lệnh `git rm -r --cached` một lượt khi bảo trì repository.

---

## II. Danh sách các nhóm WARNING (5 nhóm)

### W1: Khiếm khuyết cấu trúc bên trong thư mục rò rỉ `memory/`
- **Path:** `memory/` (các tệp con)
- **Severity:** WARNING
- **Category:** Naming & Format
- **Issue:** Các tệp nhật ký trong `memory/` (206 tệp) vi phạm quy chuẩn đặt tên kebab-case của KB.
- **Ghi chú:** Đây là hệ quả thứ cấp của E12. Không sửa thủ công từng tệp; giải quyết tận gốc E12 sẽ làm sạch toàn bộ.

### W2: 15 tệp sao lưu `*-backup-*.md` trong thư mục lưu trữ review
- **Path:** `wiki/reviews/archive/2026-09/`
- **Severity:** WARNING
- **Category:** Naming | Review Archive
- **Issue:** 15 tệp bản sao lưu do Fix Agent để lại từ các đợt rename trước đây. Đã nằm trong thư mục lưu trữ (`archive/`), không ảnh hưởng hoạt động hàng ngày.

### W3: Xung đột và thiếu sót quy chuẩn trong `folder-structure.md` [SPEC CONFLICT]
- **Path:** `wiki/meta/folder-structure.md`
- **Severity:** WARNING
- **Category:** Specification
- **Issue:**
  1. Loại báo cáo `spot-check-report` xuất hiện trong thực tế nhưng chưa có tên trong whitelist định dạng báo cáo tại §7.
  2. Bảng §7 vừa yêu cầu `wiki.md` / `raw.md` làm index bắt buộc, vừa có dòng ghi "No files at root level".
  3. `raw/raw.md:23` chứa liên kết treo `[[tools]]` trỏ về subfolder đã xoá.
- **Khuyến nghị:** Cập nhật tài liệu `wiki/meta/folder-structure.md` và gỡ bỏ liên kết `[[tools]]`.

### W4: Cặp topic trùng nghĩa `cuoc-dua-khong-di-lui.md` và `cuoc-dua-khong-i-lui.md` (Tái tạo lần 25)
- **Path:** `wiki/topic/cuoc-dua-khong-di-lui.md` và `wiki/topic/cuoc-dua-khong-i-lui.md`
- **Severity:** WARNING (carry-forward từ 09-30)
- **Category:** Naming | Slug Normalization
- **Issue:** Hai tệp topic đại diện cho cùng một cụm từ tiếng Việt ("cuộc đua không đi lùi"). Tối nay Index Agent rebuild lúc 21:05 (commit `8b847de0`) tiếp tục tái tạo cả 2 tệp (lần thứ 25).
- **Khuyến nghị:** Cần cập nhật mã nguồn Index Agent (`normalize_slug` / `strip_diacritics`) để chuẩn hoá chữ `đ` thành `d` đồng nhất, ngăn chặn việc tái tạo tự động. Tiếp tục carry-forward, KHÔNG re-escalate `[SYSTEMATIC VIOLATION]`.

### W5: Quy tắc miễn trừ agent home che khuất 5 nhóm ERROR
- **Path:** `.hermes/` và `.openclaw/`
- **Severity:** WARNING
- **Category:** Whitelist & Audit
- **Issue:** Quy tắc kiểm tra bỏ qua độ sâu > 1 trong agent home che khuất các tệp rò rỉ runtime và gitlink lồng.
- **Khuyến nghị:** Duy trì các lệnh quét chuyên sâu theo chu kỳ để giám sát các tệp rò rỉ bên trong agent home.

---

## III. Danh sách các nhóm INFO (2 nhóm)

### I1: Báo cáo cũ trong `wiki/reviews/`
- **Path:** `wiki/reviews/`
- **Severity:** INFO
- **Category:** Maintenance
- **Issue:** Hiện có 166 báo cáo review (sẽ là 167 sau khi ghi báo cáo Hygiene này), trong đó có 75 báo cáo đã lưu trên 30 ngày.
- **Khuyến nghị:** Fix Agent có thể định kỳ chuyển các báo cáo đã duyệt vào `wiki/reviews/archive/YYYY-MM/`.

### I2: Thư mục `.hermes/lsp/node_modules/`
- **Path:** `.hermes/lsp/node_modules/`
- **Severity:** INFO
- **Category:** Audit
- **Issue:** Chứa 7.101 tệp phụ thuộc LSP. Đã được bỏ qua an toàn bởi `.gitignore:63`. Không có vi phạm.
