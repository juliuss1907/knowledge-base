# Hygiene Inspection — 2026-10-19

**Status:** pending
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **5 đã RESOLVED / SẠCH** (E2, E4, E8, E9, E10) + **0 mới** ⇒ **9 ERROR còn hiệu diện**; **0 ERROR mới**. Trong đó **4 ERROR máy** (path thật ở tầng quét) + **5 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-10-19 23:35:00
**Validator:** hygiene-inspector
**Version:** 1.35
**Git commit / HEAD:** `f3812975` (2026-10-19 23:31:32 +0700) — ahead 1 vs GitHub `origin/master` (`87bf00ce`) do commit định kỳ vừa tạo, behind 0. 🟢 `vault backup` cron hoạt động trơn tru (9 commit trong 24h).

**Paths checked:** **1.731 tệp ổn định** trong phạm vi KB lúc quét (1.720 tệp vùng nội dung + 11 tệp/symlink root) → **1.732 tệp post-write** (sau khi ghi báo cáo này vào `wiki/reviews/`) + **74 thư mục** (9 root + 23 vùng nội dung bao gồm thư mục gốc vùng + 42 L1 agent home) + **99 tệp tầng đầu agent home BIẾN ĐỘNG** (77 `.hermes` + 22 `.openclaw`).

---

### Bảng đối chiếu định nghĩa số đếm (tránh hiểu nhầm tăng trưởng kho)

| Định nghĩa | Lệnh / Quy chuẩn | Số đếm 2026-10-19 | Ghi chú |
|---|---|---|---|
| **Phạm vi KB thực tế (tệp ổn định)** | 4 vùng nội dung (`raw/`, `wiki/`, `context/`, `scripts/`) + tệp root | **1.731 tệp** (1.732 post-write) | Tăng +2 tệp vs 10-18 (1.729 → 1.731: +2 báo cáo review hygiene 10-18 và format 10-19). Nợ mới nội dung = 0. |
| **Phạm vi thư mục KB** | 9 root + 23 vùng nội dung (gồm gốc vùng) + 42 L1 agent home | **74 thư mục** | Ổn định, khớp 10-18. |
| **Tệp L1 agent home (biến động)** | `.hermes/*` + `.openclaw/*` (chỉ file tầng 1) | **99 tệp** (77 hermes + 22 openclaw) | Socket loại trừ; file runtime phiên làm việc. |
| **Quét máy (prune mọi `.git`)** | `find . -name .git -prune -o \( -type f -o -type l \) -print` | **234.588 tệp** | Tăng +5 tệp vs 10-18 (234.583): +4 tệp `memory/` (158→162) + 1 báo cáo format 10-19. 99,2% là `.hermes/`. |
| **Quét máy (prune root `.git` + `hermes-agent`)** | Scan script template chuẩn | **11.112 tệp** | Tăng +5 tệp vs 10-18 (11.107). |
| **Quét máy (chỉ prune root `.git`)** | Giữ lại `.hermes/hermes-agent/.git` | **236.663 tệp** | Chênh đúng 2.075 tệp của repo `.git` con trong `hermes-agent`. |

---

## I. Danh sách các nhóm ERROR (14 nhóm: 5 RESOLVED/SẠCH, 9 HIỆU DIỆN)

### E1: Bản cài đặt mã nguồn Hermes Agent lồng trong `.hermes/hermes-agent/` (5,6 GB)
- **Path:** `.hermes/hermes-agent/`
- **Severity:** ERROR (carry-forward từ 10-01)
- **Category:** Path | Orphan
- **Issue:** Thư mục chứa toàn bộ mã nguồn Hermes Agent với 225.529 tệp / 5,6 GB, có repository git riêng lồng bên trong (`.git` con chứa 2.075 tệp / 1,7 GB, branch `main`, commit `990473a79c`).
- **Trạng thái Git:** Đã được bảo vệ an toàn bởi `.gitignore:59` (`.hermes/hermes-agent/`), 0 tệp bị track vào git KB. Gitlink `160000` cũ đã gỡ bỏ hoàn toàn.
- **Khuyến nghị:** Cần dọn dẹp hoặc di dời môi trường chạy Hermes ra ngoài thư mục KB khi có kế hoạch bảo trì. **CẢNH BÁO:** Không chạy `rm -rf` khi tiến trình agent đang chạy từ thư mục này.

### E2: Trạng thái tiến trình `vault backup` cron và đồng bộ Git
- **Path:** Toàn bộ repository (`.git/`)
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Path | Synchronization
- **Issue:** Trạng thái sao lưu tự động `vault backup`.
- **Hiện trạng 2026-10-19:** HEAD commit `f3812975` (2026-10-19 23:31:32) ahead 1 so với `origin/master` trên GitHub (`87bf00ce`) do commit định kỳ vừa tạo cách đây vài phút, đang đợi chu kỳ push tiếp theo. Cron chạy liên tục và tạo 9 commit trong 24h qua.
- **Backlog:** 0 tệp `??` và 0 tệp ` M` trong các vùng nội dung KB. Đồng bộ hoàn hảo.

### E3: 13 mẫu tệp runtime agent home không có quy tắc `.gitignore` bảo vệ
- **Path:** `.hermes/` và `.openclaw/`
- **Severity:** ERROR (carry-forward từ 09-30)
- **Category:** Path | Security & Hygiene
- **Issue:** Tệp runtime sinh ra trong quá trình tác nhân hoạt động.
- **Hiện trạng:** Đã có 9/13 mẫu được bảo vệ an toàn bởi `.gitignore`. Còn **4 mẫu (31 tệp)** vẫn còn bị track trong Git do commit từ trước khi có rule:
  1. `kanban.db*`: 5 tệp tracked (`kanban.db`, `-shm`, `-wal`...)
  2. `projects.db`: 1 tệp tracked
  3. `config.yaml.bak.*`: 18 tệp tracked
  4. `skills/.curator_backups/`: 6 tệp tracked (và 1 `MEMORY.md` tracked)
- **Khuyến nghị:** Chạy `git rm --cached` cho 31 tệp này để đưa về trạng thái untracked, kích hoạt hiệu lực của các quy tắc `.gitignore` đã có.

### E4: Tệp định danh và credential trong `.openclaw/`
- **Path:** `.openclaw/` (các tệp credential)
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security
- **Issue:** Tệp auth trong `.openclaw/` đã từng bị commit trong lịch sử.
- **Hiện trạng:** Toàn bộ 4 tệp auth (`device-auth.json`, `auth-state.json`, v.v.) đã được untrack và bảo vệ triệt để bởi `.gitignore:122`, `:100`, `:101`. Không có nguy cơ rò rỉ mới.

### E5: Thư mục `.hermes/checkpoints/`
- **Path:** `.hermes/checkpoints/`
- **Severity:** ERROR (carry-forward)
- **Category:** Path | Storage
- **Issue:** Chứa 26 tệp / 168 KB checkpoint runtime của Hermes.
- **Hiện trạng:** 0 tệp bị track vào git, được bảo vệ bởi `.gitignore:60`. Không phải repo git lồng (đã đính chính từ 10-04).

### E6: Thư mục sao lưu curator `.curator_backups/`
- **Path:** `.hermes/.curator_backups/` và `.hermes/skills/.curator_backups/`
- **Severity:** ERROR (carry-forward)
- **Category:** Path | Orphan
- **Issue:** Bản sao lưu kỹ năng do Curator tạo ra:
  - `.hermes/.curator_backups/`: 328 tệp / 7,6 MB, 0 tệp tracked, được bảo vệ bởi `.gitignore:61`.
  - `.hermes/skills/.curator_backups/`: 15 tệp / 16 MB, trong đó còn **6 tệp tracked** cần `git rm --cached`.

### E7: 2 tệp migration marker `.migrated.*` còn bị track trong Git
- **Path:** `./openclaw-workspace-state.json.migrated...` và `.openclaw/workspace-state.json.migrated...`
- **Severity:** ERROR (carry-forward từ 09-08)
- **Category:** Path | Orphan
- **Issue:** 2 marker di trú (mỗi tệp 69 B, commit `b5e519fc`, hash blob `a0105ac6...`) vẫn còn bị track trong git KB và chưa có rule trong `.gitignore`.
- **Khuyến nghị:** Chạy `git rm --cached` cho cả 2 tệp và thêm rule `*.migrated.*` vào `.gitignore`.

### E8: Tệp cấu hình `.hermes/config.yaml`
- **Path:** `.hermes/config.yaml`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security
- **Issue:** Tệp cấu hình runtime của Hermes Agent.
- **Hiện trạng:** 0 tệp tracked, được bảo vệ bởi `.gitignore:67`. Duy trì sạch.

### E9: Tồn đọng tệp nội dung chưa commit trong vùng làm việc
- **Path:** `wiki/`, `raw/`, `context/`, `scripts/`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Synchronization
- **Issue:** Kiểm tra tệp nội dung chưa được commit lên git.
- **Hiện trạng:** 0 tệp untracked `??`, 0 tệp modified ` M`. Toàn bộ nội dung KB đã được sao lưu đầy đủ.

### E10: Tệp topic bị xóa `wiki/topic/brain-threat-detection.md`
- **Path:** `wiki/topic/brain-threat-detection.md`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Orphan
- **Issue:** Topic bị xóa khỏi đĩa nhưng còn vết xóa trong git.
- **Hiện trạng:** Vết xóa đã được commit đầy đủ từ đợt dọn 10-04 (`3b891e34`). Không còn tồn đọng.

### E11: Tệp `DREAMS.md` tại thư mục gốc KB
- **Path:** `DREAMS.md`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Tệp sinh ra tại thư mục gốc (16.980 B, mtime 2026-10-19 03:00:04, do OpenClaw dreaming chạy lúc 03:00).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:82`.
- **Khuyến nghị:** Cấu hình tiến trình dreaming của OpenClaw ghi vào `.openclaw/workspace-state/` thay vì KB root.

### E12: Thư mục `memory/` tại thư mục gốc KB
- **Path:** `memory/`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Thư mục ngoài whitelist tại root, chứa 162 tệp / 7 thư mục / 752 KB (tăng +4 tệp so với 10-18: `memory/dreaming/deep/2026-10-19.md` mtime 03:00:04).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:113`.
- **Khuyến nghị:** Chuyển hướng tiến trình ghi nhật ký phiên của OpenClaw vào `.openclaw/memory/`.

### E13: Symlink `wiki/HEARTBEAT.md` hỏng (dangling symlink)
- **Path:** `wiki/HEARTBEAT.md`
- **Severity:** ERROR
- **Category:** Path | Symlink
- **Issue:** `wiki/HEARTBEAT.md` là symlink trỏ về `../../.openclaw/HEARTBEAT.md`. Do thừa một cấp thư mục (`../../`), đường dẫn đích giải quyết thành `/home/julius/.openclaw/HEARTBEAT.md` (không tồn tại ngoài KB). Đích thực tế nằm tại `<KB>/.openclaw/HEARTBEAT.md`.
- **Khuyến nghị:** Fix Agent sửa symlink thành `../.openclaw/HEARTBEAT.md` và tái lập symlink root `HEARTBEAT.md → .openclaw/HEARTBEAT.md`.

### E14: Tổng hợp 31 tệp runtime agent home còn bị track trong Git
- **Path:** `.hermes/`
- **Severity:** ERROR (carry-forward từ 10-04)
- **Category:** Security & Repository Hygiene
- **Issue:** 31 tệp runtime (18 `config.yaml.bak.*`, 5 `kanban.db*`, 1 `projects.db`, 6 `skills/.curator_backups/`, 1 `MEMORY.md`) vẫn còn trong Git index.
- **Khuyến nghị:** Chạy lệnh `git rm -r --cached` một lượt khi bảo trì repository.

---

## II. Danh sách các nhóm WARNING (5 nhóm)

### W1: Khiếm khuyết cấu trúc bên trong thư mục rò rỉ `memory/`
- **Path:** `memory/` (các tệp con)
- **Severity:** WARNING
- **Category:** Naming & Format
- **Issue:** Các tệp nhật ký trong `memory/` vi phạm quy chuẩn đặt tên kebab-case của KB.
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

### W4: Cặp topic trùng nghĩa `cuoc-dua-khong-di-lui.md` và `cuoc-dua-khong-i-lui.md` (Tái tạo lần 14)
- **Path:** `wiki/topic/cuoc-dua-khong-di-lui.md` và `wiki/topic/cuoc-dua-khong-i-lui.md`
- **Severity:** WARNING (carry-forward từ 09-30)
- **Category:** Naming | Slug Normalization
- **Issue:** Hai tệp topic đại diện cho cùng một cụm từ tiếng Việt ("cuộc đua không đi lùi"). Tối nay Index Agent rebuild lúc 21:03:23 (commit `19ac6fd9`) tiếp tục tái tạo cả 2 tệp.
- **Khuyến nghị:** Cần cập nhật mã nguồn Index Agent (`normalize_slug` / `strip_diacritics`) để chuẩn hoá chữ `đ` thành `d` đồng nhất, ngăn chặn việc tái tạo tự động.

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
- **Issue:** Hiện có 144 báo cáo review, trong đó có 75 báo cáo đã lưu trên 30 ngày.
- **Khuyến nghị:** Fix Agent có thể định kỳ chuyển các báo cáo đã duyệt vào `wiki/reviews/archive/YYYY-MM/`.

### I2: Thư mục `.hermes/lsp/node_modules/`
- **Path:** `.hermes/lsp/node_modules/`
- **Severity:** INFO
- **Category:** Audit
- **Issue:** Chứa 7.101 tệp phụ thuộc LSP. Đã được bỏ qua an toàn bởi `.gitignore:63`. Không có vi phạm.

---

## IV. Bảng tổng hợp trạng thái & Khuyến nghị hành động

| Nhóm | Phân loại | Tên / Đường dẫn | Trạng thái 2026-10-19 | Hành động đề xuất |
|---|---|---|---|---|
| **E1** | ERROR | `.hermes/hermes-agent/` (5,6 GB) | Carry-forward (untracked, `:59`) | Giữ nguyên khi chạy, dọn khi bảo trì |
| **E2** | ERROR | `vault backup` cron | **RESOLVED / SẠCH** 🟢 | Cron chạy hoàn hảo (9 commit/24h, ahead 1 chờ push) |
| **E3** | ERROR | 13 mẫu runtime agent home | 4 mẫu còn 31 tệp tracked | `git rm --cached` 31 tệp |
| **E4** | ERROR | Credential trong `.openclaw/` | **RESOLVED / SẠCH** 🟢 | 0 tệp tracked, bảo vệ bởi `:122` |
| **E5** | ERROR | `.hermes/checkpoints/` | Carry-forward (0 tracked, `:60`) | Không cần thao tác |
| **E6** | ERROR | `.curator_backups/` | Carry-forward (6 tệp tracked) | `git rm --cached` 6 tệp |
| **E7** | ERROR | 2 marker `.migrated.*` | Carry-forward (2 tệp tracked) | `git rm --cached` + thêm rule gitignore |
| **E8** | ERROR | `.hermes/config.yaml` | **RESOLVED / SẠCH** 🟢 | Đã bảo vệ bởi `:67` |
| **E9** | ERROR | Backlog nội dung chưa commit | **RESOLVED / SẠCH** 🟢 | 0 tệp tồn đọng |
| **E10** | ERROR | `brain-threat-detection.md` | **RESOLVED / SẠCH** 🟢 | Đã commit hoàn tất |
| **E11** | ERROR | `DREAMS.md` tại root | Carry-forward (0 tracked, `:82`) | Cấu hình OpenClaw đổi path |
| **E12** | ERROR | `memory/` tại root | Carry-forward (0 tracked, `:113`) | Cấu hình OpenClaw đổi path |
| **E13** | ERROR | `wiki/HEARTBEAT.md` dangling | Carry-forward (link lệch 1 cấp) | Sửa symlink trỏ đúng đích |
| **E14** | ERROR | Tổng hợp 31 tệp runtime tracked | Carry-forward | `git rm --cached` một lượt |
| **W1** | WARNING | Lỗi đặt tên trong `memory/` | Carry-forward | Giải quyết theo E12 |
| **W2** | WARNING | 15 tệp backup trong archive | Carry-forward | Lưu trữ, không ảnh hưởng |
| **W3** | WARNING | Xung đột `folder-structure.md` | Carry-forward | Cập nhật spec và gỡ link treo |
| **W4** | WARNING | Cặp topic trùng (lần 14) | Carry-forward (Index 21:03) | Sửa slug normalization ở Index Agent |
| **W5** | WARNING | Miễn trừ agent home che ERROR | Carry-forward | Duy trì kiểm toán định kỳ |
| **I1** | INFO | 75 báo cáo review > 30 ngày | Carry-forward | Lưu trữ định kỳ |
| **I2** | INFO | `.hermes/lsp/node_modules/` | Sạch (đã ignore `:63`) | Không cần thao tác |
