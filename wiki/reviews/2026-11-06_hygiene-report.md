# Hygiene Inspection — 2026-11-06

**Status:** pending
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **5 đã RESOLVED / SẠCH** (E2, E4, E8, E9, E10) + **0 mới** ⇒ **9 ERROR còn hiệu diện**; **0 ERROR mới**. Tồn đọng trong agent home **TĂNG +1 tệp**: **26 tệp tracked** ở HEAD (19 `config.yaml.bak.*` — tệp mới `config.yaml.bak.20261106_160532` được commit 16:06 hôm nay bởi `vault backup` — 5 `kanban.db*`, 1 `projects.db`, 1 `MEMORY.md`; 0 tệp trong `skills/.curator_backups/`). Trong đó **4 ERROR máy** (path thật ở tầng quét) + **5 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-11-06 23:35:00
**Validator:** hygiene-inspector
**Version:** 1.35
**Git commit / HEAD:** `d14453c4` (2026-11-06 23:22:21 +0700) — in sync 100% vs GitHub `origin/master` (`d14453c4`, ahead 0, behind 0). 🟢 `vault backup` cron hoạt động trơn tru (14 commit trong 24h).

**Paths checked:** **1.774 tệp ổn định** trong phạm vi KB lúc quét (1.763 tệp vùng nội dung + 11 tệp/symlink root) → **1.775 tệp post-write** (sau khi ghi báo cáo này vào `wiki/reviews/`) + **74 thư mục** (9 root + 23 vùng nội dung bao gồm thư mục gốc vùng + 42 L1 agent home) + **100 tệp tầng đầu agent home BIẾN ĐỘNG** (78 `.hermes` + 22 `.openclaw`).

---

### Bảng đối chiếu định nghĩa số đếm (tránh hiểu nhầm tăng trưởng kho)

| Định nghĩa | Lệnh / Quy chuẩn | Số đếm 2026-11-06 | Ghi chú |
|---|---|---|---|
| **Phạm vi KB thực tế (tệp ổn định)** | 4 vùng nội dung (`raw/`, `wiki/`, `context/`, `scripts/`) + tệp root | **1.774 tệp** (1.775 post-write) | Tăng +3 tệp vs 11-05 lúc quét (1.771 → 1.774) / +3 tệp vs 11-05 post-write (1.772 → 1.775): +1 báo cáo Hygiene 11-05, +1 báo cáo Format 11-06 (`2026-11-06_format-report.md`), +1 raw mới `raw/articles/2026-11-04_cognitive-offloading-learning-ai.md` (ingest 11-06 16:10, đã được Format 11-06 ghi nhận — không phải nợ mới Hygiene). Nợ mới nội dung Hygiene = 0. |
| **Phạm vi thư mục KB** | 9 root (gồm `.git`) + 23 vùng nội dung (gồm gốc vùng) + 42 L1 agent home | **74 thư mục** | Ổn định, khớp 11-05 (9 root + 23 content + 27 hermes + 15 openclaw). |
| **Tệp L1 agent home (biến động)** | `.hermes/*` + `.openclaw/*` (chỉ file tầng 1) | **100 tệp** (78 hermes + 22 openclaw) | Socket loại trừ (`gateway.sock`); file runtime phiên làm việc. +1 tệp `.hermes` vs 11-05 (99 → 100: tệp runtime biến động, xem E3 về tệp `.bak` mới được backup). |
| **Quét máy (prune mọi `.git`)** | `find . -name .git -prune -o \( -type f -o -type l \) -print` | **234.718 tệp** (234.719 post-write) | Tăng +18 tệp vs 11-05 (234.700): +4 tệp `memory/` (230→234) do OpenClaw dreaming 11-06, +1 raw mới, +2 báo cáo (Hygiene 11-05 + Format 11-06), phần còn lại là runtime `.hermes/`. 99,2% là `.hermes/`. |
| **Quét máy (prune root `.git` + `hermes-agent`)** | Scan script template chuẩn | **11.257 tệp** (11.258 post-write) | Tăng +11 tệp vs 11-05 (11.246). |
| **Quét máy (chỉ prune root `.git`)** | Giữ lại `.hermes/hermes-agent/.git` | **236.793 tệp** (236.794 post-write) | Chênh đúng 2.075 tệp của repo `.git` con trong `hermes-agent`. |

---

## I. Danh sách các nhóm ERROR (14 nhóm: 5 RESOLVED/SẠCH, 9 HIỆU DIỆN)

### E1: Bản cài đặt mã nguồn Hermes Agent lồng trong `.hermes/hermes-agent/` (5,6 GB)
- **Path:** `.hermes/hermes-agent/`
- **Severity:** ERROR (carry-forward từ 10-01)
- **Category:** Path | Orphan
- **Issue:** Thư mục chứa toàn bộ mã nguồn Hermes Agent với 225.536 tệp / 5,6 GB, có repository git riêng lồng bên trong (`.git` con chứa 2.075 tệp, branch `main`, commit `990473a79c` — không đổi).
- **Trạng thái Git:** Đã được bảo vệ an toàn bởi `.gitignore:59` (`.hermes/hermes-agent/`), 0 tệp bị track vào git KB.
- **Khuyến nghị:** Cần dọn dẹp hoặc di dời môi trường chạy Hermes ra ngoài thư mục KB khi có kế hoạch bảo trì. **CẢNH BÁO:** Không chạy `rm -rf` khi tiến trình agent đang chạy từ thư mục này.

### E2: Trạng thái tiến trình `vault backup` cron và đồng bộ Git
- **Path:** Toàn bộ repository (`.git/`)
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Path | Synchronization
- **Issue:** Trạng thái sao lưu tự động `vault backup`.
- **Hiện trạng 2026-11-06:** HEAD commit `d14453c4` (2026-11-06 23:22:21 +0700) khớp 100% với `origin/master` trên GitHub (`d14453c4`, ahead 0, behind 0). Cron chạy liên tục và tạo 14 commit trong 24h qua.
- **Backlog:** 0 tệp `??` và 0 tệp ` M` trong toàn bộ vùng nội dung KB (`raw/`, `wiki/`, `context/`, `scripts/`). Đồng bộ hoàn hảo.
- **Lưu ý liên quan:** Chính cron backup hoạt động trơn tru này đã commit tệp backup cấu hình mới `config.yaml.bak.20261106_160532` lúc 16:06 (commit `3ee371ee`) — làm E3/E14 tăng +1 tệp tracked. Không phải lỗi đồng bộ; là hệ quả của việc E14 chưa được `git rm --cached`.

### E3: 13 mẫu tệp runtime agent home không có quy tắc `.gitignore` bảo vệ
- **Path:** `.hermes/` và `.openclaw/`
- **Severity:** ERROR (carry-forward từ 09-30) — **TĂNG +1 tệp tracked**
- **Category:** Path | Security & Hygiene
- **Issue:** Tệp runtime sinh ra trong quá trình tác nhân hoạt động.
- **Hiện trạng:** Đã có 9/13 mẫu được bảo vệ an toàn bởi `.gitignore`. Tồn đọng **tăng từ 25 lên 26 tệp tracked** tại HEAD:

| Mẫu tệp | Số tệp tracked | Quy tắc .gitignore | Trạng thái |
|---|---|---|---|
| `.hermes/config.yaml.bak.*` | **19 tệp (+1)** | Chưa có rule | Cần thêm rule + `git rm --cached` — tệp mới `config.yaml.bak.20261106_160532` (23.027 B, mtime 15:32) được commit bởi `vault backup` 16:06 (commit `3ee371ee`) |
| `.hermes/kanban.db*` | 5 tệp (`db`, `shm`, `wal`, 2 `lock`) | Chưa có rule | Cần thêm rule + `git rm --cached` |
| `.hermes/projects.db` | 1 tệp | Chưa có rule | Cần thêm rule + `git rm --cached` |
| `.hermes/MEMORY.md` | 1 tệp | `.gitignore:110` | Rule có hiệu lực nhưng tệp commit trước rule |
| `.hermes/skills/.curator_backups/` | **0 tệp** | `.gitignore:73` | **SẠCH TRÊN GIT** 🟢 |
| 8 mẫu runtime còn lại | **0 tệp** | Đầy đủ rule | An toàn 🟢 |

- **Ghi chú:** Lần tăng này xác nhận lại cơ chế đã ghi ở các báo cáo trước: mỗi lần Hermes tự backup `config.yaml`, một tệp `.bak` mới sinh ra, và `vault backup` commit nó vào repo vì chưa có rule `.gitignore` tương ứng. Tồn đọng sẽ tiếp tục tăng cho đến khi E14 được xử lý.
- **Khuyến nghị:** Fix Agent chạy `git rm -r --cached` cho 26 tệp còn lại và bổ sung các rule còn thiếu vào `.gitignore`.

### E4: Tệp credential và auth state trong `.openclaw/`
- **Path:** `.openclaw/`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security
- **Issue:** Các tệp xác thực của OpenClaw.
- **Hiện trạng:** Cả 4 tệp auth (`device-auth.json`, `identity/device-auth.json`, `agents/main/agent/auth-profiles.json`, `agents/main/agent/auth-state.json`) đều **0 tệp tracked trong Git** (re-probe 11-06: `git ls-files -s` rỗng cho cả 4) và được bảo vệ an toàn bởi `.gitignore`. `.hermes/auth.json` cũng 0 tracked. Không có nguy cơ lộ bí mật.

### E5: Kho lưu trữ checkpoint của Hermes tại `.hermes/checkpoints/`
- **Path:** `.hermes/checkpoints/`
- **Severity:** ERROR (carry-forward từ 09-29)
- **Category:** Path | Runtime Storage
- **Issue:** Kho lưu trữ đối tượng checkpoint (25 tệp / ~31 KB).
- **Trạng thái Git:** 0 tệp tracked trong Git, được bảo vệ bởi `.gitignore:60`. Không phải repo git lồng (không có `.git`, chỉ có `store/HEAD`). Không cần hành động khẩn cấp.

### E6: Thư mục sao lưu của Curator tại `.hermes/skills/.curator_backups/` và `.hermes/.curator_backups/`
- **Path:** `.hermes/skills/.curator_backups/` và `.hermes/.curator_backups/`
- **Severity:** ERROR (carry-forward từ 09-29)
- **Category:** Path | Backup Artifacts
- **Issue:** Bản sao lưu kỹ năng của Curator.
- **Trạng thái Git:** **0 tệp tracked** tại HEAD (duy trì sạch). Đã có rule `.gitignore:61,73`.
- **Khuyến nghị:** Duy trì theo dõi.

### E7: 2 marker migration của OpenClaw workspace state
- **Path:** `openclaw-workspace-state.json.migrated.43c9aa3d…e79d1c6c…` (root) và `.openclaw/workspace-state.json.migrated…` (.openclaw/)
- **Severity:** ERROR (carry-forward từ 09-08 / 09-25)
- **Category:** Path | Artifact Leak
- **Issue:** 2 tệp marker migration (69 bytes mỗi tệp) bị commit vào Git từ ngày 2026-09-08 (commit `b5e519fc`, cùng blob `a0105ac6…`). Marker root vẫn nằm trong danh sách 11 tệp root hôm nay.
- **Trạng thái Git:** Cả 2 tệp đều còn bị track trong Git (re-probe 11-06: `git ls-files -s` = 1 + 1), chưa có rule wildcard `*.migrated.*` trong `.gitignore`.
- **Khuyến nghị:** Fix Agent chạy `git rm --cached` cho cả 2 tệp và bổ sung `*.migrated.*` vào `.gitignore`.

### E8: Tệp cấu hình `.hermes/config.yaml`
- **Path:** `.hermes/config.yaml`
- **Severity:** ERROR → **RESOLVED / SẠCH** 🟢
- **Category:** Security & Config
- **Issue:** Tệp cấu hình chính của Hermes Agent.
- **Hiện trạng:** 0 tệp tracked trong Git (re-probe 11-06), đã được bảo vệ an toàn bởi `.gitignore:67`.

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
- **Hiện trạng:** `git status` không còn vết `D` (re-probe 11-06). Vết xóa đã được commit đầy đủ từ đợt dọn 10-04. Không còn tồn đọng.

### E11: Tệp `DREAMS.md` tại thư mục gốc KB
- **Path:** `DREAMS.md`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Tệp sinh ra tại thư mục gốc (16.980 B, mtime 2026-11-06 03:00:05 — cập nhật bởi OpenClaw dreaming đêm qua; kích thước không đổi so với 11-05).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:82`.
- **Khuyến nghị:** Cấu hình tiến trình dreaming của OpenClaw ghi vào `.openclaw/workspace-state/` thay vì KB root.

### E12: Thư mục `memory/` tại thư mục gốc KB
- **Path:** `memory/`
- **Severity:** ERROR
- **Category:** Path | Root Whitelist
- **Issue:** Thư mục ngoài whitelist tại root, chứa **234 tệp** / 6 thư mục / **191.112 bytes** (tăng +4 tệp / +668 bytes so với 11-05: 4 tệp do OpenClaw dreaming ghi vào `memory/dreaming/` và `memory/.dreams/session-corpus/` — session-corpus có tệp mới `2026-11-05.txt` mtime 03:00 hôm nay).
- **Trạng thái Git:** 0 tệp tracked, được bảo vệ bởi `.gitignore:113`.
- **Khuyến nghị:** Chuyển hướng tiến trình ghi nhật ký phiên của OpenClaw vào `.openclaw/memory/`.

### E13: Symlink `wiki/HEARTBEAT.md` hỏng (dangling symlink)
- **Path:** `wiki/HEARTBEAT.md`
- **Severity:** ERROR
- **Category:** Path | Symlink
- **Issue:** `wiki/HEARTBEAT.md` là symlink trỏ về `../../.openclaw/HEARTBEAT.md`. Re-probe 11-06: `readlink` = `../../.openclaw/HEARTBEAT.md`, `realpath` = `/home/julius/.openclaw/HEARTBEAT.md`, **`exists` = False** — vẫn dangling (thừa một cấp thư mục `../../`, đích giải quyết ra ngoài KB). Đích thực tế nằm tại `<KB>/.openclaw/HEARTBEAT.md`.
- **Ghi chú:** Symlink root `HEARTBEAT.md` hiện **không tồn tại** trên đĩa (không có trong danh sách 11 tệp root) — khác với khuyến nghị "tái lập" ở các báo cáo trước.
- **Khuyến nghị:** Fix Agent sửa symlink `wiki/HEARTBEAT.md` thành `../.openclaw/HEARTBEAT.md`. Symlink root `HEARTBEAT.md → .openclaw/HEARTBEAT.md` có thể tái lập nếu cần theo spec.

### E14: Tổng hợp 26 tệp runtime agent home còn bị track trong Git
- **Path:** `.hermes/`
- **Severity:** ERROR (carry-forward từ 10-04) — **TĂNG +1 tệp (25 → 26)**
- **Category:** Security & Repository Hygiene
- **Issue:** 26 tệp runtime (19 `config.yaml.bak.*`, 5 `kanban.db*`, 1 `projects.db`, 1 `MEMORY.md`) vẫn còn trong Git index. Tăng +1 do tệp backup cấu hình mới `config.yaml.bak.20261106_160532` được `vault backup` commit lúc 16:06 hôm nay (commit `3ee371ee`).
- **Ghi chú:** Đây là lần tăng đầu tiên kể từ khi tồn đọng ổn định ở mức 25 tệp (10-27 → 11-05, 11 báo cáo liên tiếp). Nếu không xử lý, tồn đọng sẽ tăng đều mỗi lần Hermes rotate backup config.
- **Khuyến nghị:** Chạy lệnh `git rm -r --cached` một lượt khi bảo trì repository, kèm bổ sung rule `.gitignore` trước để chặn tái phát.

---

## II. Danh sách các nhóm WARNING (5 nhóm)

### W1: Khiếm khuyết cấu trúc bên trong thư mục rò rỉ `memory/`
- **Path:** `memory/` (các tệp con)
- **Severity:** WARNING
- **Category:** Naming & Format
- **Issue:** Các tệp nhật ký trong `memory/` (234 tệp) vi phạm quy chuẩn đặt tên kebab-case của KB.
- **Ghi chú:** Đây là hệ quả thứ cấp của E12. Không sửa thủ công từng tệp; giải quyết tận gốc E12 sẽ làm sạch toàn bộ.

### W2: 15 tệp sao lưu `*-backup-*.md` trong thư mục lưu trữ review
- **Path:** `wiki/reviews/archive/2026-09/`
- **Severity:** WARNING
- **Category:** Naming | Review Archive
- **Issue:** 15 tệp bản sao lưu do Fix Agent để lại từ các đợt rename trước đây (re-probe 11-06: vẫn đúng 15 tệp). Đã nằm trong thư mục lưu trữ (`archive/`), không ảnh hưởng hoạt động hàng ngày.

### W3: Xung đột và thiếu sót quy chuẩn trong `folder-structure.md` [SPEC CONFLICT]
- **Path:** `wiki/meta/folder-structure.md`
- **Severity:** WARNING
- **Category:** Specification
- **Issue:**
  1. Loại báo cáo `spot-check-report` xuất hiện trong thực tế nhưng chưa có tên trong whitelist định dạng báo cáo tại §7.
  2. Bảng §7 vừa yêu cầu `wiki.md` / `raw.md` làm index bắt buộc, vừa có dòng ghi "No files at root level".
  3. `raw/raw.md:23` chứa liên kết treo `[[tools]]` trỏ về subfolder đã xoá.
- **Khuyến nghị:** Cập nhật tài liệu `wiki/meta/folder-structure.md` và gỡ bỏ liên kết `[[tools]]`.

### W4: Cặp topic trùng nghĩa `cuoc-dua-khong-di-lui.md` và `cuoc-dua-khong-i-lui.md` (Tái tạo lần 32)
- **Path:** `wiki/topic/cuoc-dua-khong-di-lui.md` và `wiki/topic/cuoc-dua-khong-i-lui.md`
- **Severity:** WARNING (carry-forward từ 09-30)
- **Category:** Naming | Slug Normalization
- **Issue:** Hai tệp topic đại diện cho cùng một cụm từ tiếng Việt ("cuộc đua không đi lùi"). Tối nay Index Agent rebuild lúc 21:01 tiếp tục tái tạo cả 2 tệp (lần thứ 32; cả hai cùng mtime 2026-11-06 21:01:48).
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
- **Issue:** Hiện có 182 báo cáo review (sẽ là 183 sau khi ghi báo cáo Hygiene này), trong đó có 123 báo cáo đã lưu trên 30 ngày (dated <= 2026-10-06).
- **Khuyến nghị:** Fix Agent có thể định kỳ chuyển các báo cáo đã duyệt vào `wiki/reviews/archive/YYYY-MM/`.

### I2: Thư mục `.hermes/lsp/node_modules/`
- **Path:** `.hermes/lsp/node_modules/`
- **Severity:** INFO
- **Category:** Audit
- **Issue:** Chứa 7.101 tệp phụ thuộc LSP. Đã được bỏ qua an toàn bởi `.gitignore:63`. Không có vi phạm.

---

## Kế hoạch xử lý tiếp theo

1. **Julius:** Xem xét phê duyệt báo cáo vệ sinh ngày 2026-11-06: `approve hygiene` hoặc `approve all report`.
2. **Fix Agent:**
   - Chạy `git rm -r --cached` gỡ **26 tệp** runtime agent home (E14 — tăng +1 tệp hôm nay) và 2 marker `.migrated.*` (E7).
   - Thêm các quy tắc tương ứng vào `.gitignore` (`config.yaml.bak.*`, `kanban.db*`, `projects.db`, `*.migrated.*`) **trước** khi `git rm --cached` để chặn tái phát — hôm nay là bằng chứng: một tệp `.bak` mới đã bị commit trong ngày.
   - Sửa symlink `wiki/HEARTBEAT.md` thành `../.openclaw/HEARTBEAT.md` (E13); cân nhắc tái lập symlink root `HEARTBEAT.md` (hiện vắng mặt).
3. **OpenClaw Agent:** Điều chỉnh đường dẫn ghi nhật ký và dreaming vào `.openclaw/` để chấm dứt rò rỉ tại `DREAMS.md` (E11) và `memory/` (E12).
4. **Index Agent:** Chuẩn hoá xử lý ký tự `đ` trong slug generator để giải quyết dứt điểm cặp topic trùng lặp (W4).
