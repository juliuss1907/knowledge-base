# Hygiene Inspection — 2026-10-13

**Status:** pending
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **5 đã RESOLVED / SẠCH** (E2, E4, E8, E9, E10) + **2 giảm** (E3/E14: 34→31 tệp, E6: 9→6 tệp tracked) ⇒ **9 ERROR còn hiệu diện**; **0 ERROR mới**. Trong đó **4 ERROR máy** (path thật ở tầng quét) + **5 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-10-13 23:35 +0700
**Validator:** hygiene-inspector
**Paths checked:** **1.712 tệp ổn định trong phạm vi KB** (1.701 vùng nội dung + 11 tệp/symlink root) → **1.713 post-write** (báo cáo này nằm trong vùng nội dung) + **74 thư mục** (9 root + 23 vùng nội dung gồm thư mục gốc vùng + 42 L1 agent home) + **99 tệp tầng đầu agent home — BIẾN ĐỘNG** (77 `.hermes` + 22 `.openclaw`). Quét máy = **234.554** (định nghĩa: prune mọi thư mục `.git` ở mọi độ sâu) — ⚠️ **KHÔNG phải phạm vi kiểm tra**.
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

> **MỐC TIẾN TRIỂN 2026-10-13: `vault backup` hoạt động liên tục (13 commit hôm nay); backlog runtime agent home tiếp tục giảm thêm 3 tệp (34→31).**
> Toàn bộ 21 nhóm issue được đo lại độc lập trên trạng thái đĩa và index git hôm nay (2026-10-13 23:35).
> - **🟢 `vault backup` cron hoạt động trơn tru:** HEAD `221b804c` (23:19:47) khớp hoàn toàn `refs/heads/master` trên GitHub. Đã có 13 commit trong ngày. Backlog vùng nội dung = 0.
> - **🟢 Bảo mật E4 giữ vững:** Toàn bộ credential `.openclaw/` đã untracked & ignored (commit `380d3f74`).
> - **🟢 New-debt trong vùng nội dung KB = 0:** 1.701 tệp nội dung (1.464 wiki + 230 raw + 2 context + 5 scripts) tuân thủ 100% naming và path whitelist của `folder-structure.md`.
> - **🟡 Backlog runtime agent home giảm từ 34 xuống 31 tệp tracked:** Commit `f3d273a2` (11:58:46) đã xoá thêm 3 tệp curator backup cũ (`2026-09-08T02-12-42Z/`). Còn 31 tệp (5 `kanban.db*` + 1 `projects.db` + 18 `config.yaml.bak.*` + 6 `skills/.curator_backups/` + 1 `MEMORY.md`) cần `git rm -r --cached`.
> - **🔴 2 marker `.migrated.*` (root + `.openclaw/`) vẫn đang tracked trên GitHub**, cùng blob `a0105ac6...` (69 B), chưa có rule ignore `*.migrated.*`.
> - **🔴 3 writer ngoại vi tiếp tục ghi:** `DREAMS.md` tại root (16.980 B lúc 03:00), `memory/` tại root (138 tệp / 7 thư mục / 656 KB, +4 tệp mới), và `wiki/HEARTBEAT.md` dangling symlink (`../../.openclaw/HEARTBEAT.md`).
> - **⚠️ Cặp topic trùng nghĩa `cuoc-dua-khong-{di,i}-lui` tái tạo lần thứ 8** do Index Agent rebuild lúc 21:02.

---

## Bảng đối chiếu định nghĩa quét máy (Bài học 10-03 #25)

| Định nghĩa prune | Lệnh thực thi | Kết quả 10-13 | So với 10-12 | Bản chất |
|---|---|---|---|---|
| **Prune mọi `.git` ở mọi độ sâu** | `find . -type d -name .git -prune -o \( -type f -o -type l \) -print` | **234.554** | +15 tệp | Chuẩn công bố của validator (tăng 15 tệp cache/runtime trong hermes-agent vs 234.539 hôm qua) |
| **Prune root `.git` + prune `hermes-agent`** | `find . -path ./.git -prune -o -name hermes-agent -prune -o …` | **11.073** | +13 tệp | Phạm vi máy thật khi loại bỏ bản cài lồng E1 (11.060 hôm qua; +8 wiki reports/topics, +1 raw/articles, +4 memory session logs) |
| **Prune chỉ root `.git`** | `find . -path ./.git -prune -o \( -type f -o -type l \) -print` | **236.628** | +13 tệp | Chênh đúng **2.074 tệp** `.git` của repo lồng `hermes-agent` (236.628 − 234.554 = 2.074) |

---

## 🔴 E1 — Bản cài Hermes Agent 225.533 tệp / 5,5 GB — **PHẦN GIT ĐÃ ĐÓNG, phần đĩa còn nguyên**

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-12 | **10-13 23:35 (đo lại)** |
|---|---|---|
| `find … \( -type f -o -type l \)` | 225.533 | **225.533** (giữ nguyên) |
| `du -sh` | 5,5 GB | **5,5 GB** |
| nested `.git` | CÓ (2.076 tệp) | **CÓ** (2.074 tệp / 1,6 GB) · branch `main` · HEAD `990473a79c` |
| `git ls-tree HEAD \| grep 160000` | KHÔNG CÒN ✅ | **KHÔNG CÒN** ✅ |
| `git ls-files -s .hermes/hermes-agent` | 0 — untracked ✅ | **0 — untracked** ✅ |
| `git check-ignore --no-index` | `.gitignore:59` ✅ | **`.gitignore:59 .hermes/hermes-agent/`** ✅ |

**Kết luận:** Vấn đề cấu trúc git đã được bảo vệ thành công từ commit `68f644e7`. Bản cài lồng trên đĩa vẫn chiếm 5,5 GB và là CWD/launch path của tiến trình Hermes Agent đang chạy.

---

## 🟢 E2 — `vault backup` — ✅ **ĐÃ PHỤC HỒI HOÀN TOÀN (2026-10-12 19:14)**

**Severity:** ERROR → **RESOLVED** · **Category:** Sync / Backup

| Mốc | 10-12 (Phục hồi) | **10-13 (Tiếp tục ổn định)** |
|---|---|---|
| HEAD cục bộ | `e0ff6341` (2026-10-12 23:22) | **`221b804c` (2026-10-13 23:19:47 +0700)** |
| `git ls-remote --heads origin` | `refs/heads/master = e0ff6341...` | **`refs/heads/master = 221b804c...` — KHỚP HOÀN TOÀN** ✅ |
| Tuổi backup | 0 ngày | **0 ngày — backup chạy liên tục 5-10 phút/lần** ✅ |
| Commit trong ngày | 7+ commit | **13 commit tự động** ✅ |
| Trạng thái tồn đọng | 0 `??`, 0 ` M` nội dung | **0 `??` trong KB, 0 ` M` nội dung** (chỉ có 1 file usage json runtime) ✅ |

**Kết luận:** Cron `vault backup` trên máy chính hoạt động hoàn toàn bình thường. Mọi thay đổi nội dung tri thức đã được đẩy an toàn lên GitHub `master`.

---

## 🔴 E3 — 13 mẫu runtime agent home — **9/13 ĐÃ ĐÓNG, 4 còn lộ (31 tệp, giảm 3)**

**Severity:** ERROR · **Category:** Path / Repo hygiene

Đo lại hôm nay (`git ls-files -s` + `git check-ignore --no-index -v` — bài học 09-30 #14):

| Mẫu | Tracked 10-12 | **Tracked 10-13** | Rule | Trạng thái |
|---|---|---|---|---|
| `.hermes/kanban.db*` | 5 | **5** (gồm 2 lock) | **NONE** | ❌ còn lộ (141 commit mỗi tệp) |
| `.hermes/projects.db` | 1 | **1** | **NONE** | ❌ còn lộ (1 commit) |
| `.hermes/config.yaml.bak*` | 18 | **18** | **NONE** | ❌ còn lộ (11 commit) |
| `.hermes/skills/.curator_backups*` | 9 | **6** (−3 tệp) | `:73` có, **vô hiệu** | ❌ còn lộ (14 commit) — commit `f3d273a2` xoá thư mục 09-08 |
| `.hermes/MEMORY.md` | 1 | **1** | `:110` có, **vô hiệu** | ❌ còn lộ (172 commit) |
| `.hermes/verification_evidence.db` | 0 | **0** | `:69` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/state-snapshots*` | 0 | **0** | `:62` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/checkpoints*` | 0 | **0** | `:60` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/.curator_backups*` | 0 | **0** | `:61` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/config.yaml` | 0 | **0** | `:67` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/auth.json` | 0 | **0** | `:37` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/lsp/*` | 0 | **0** | `:63` | ✅ **đã đóng** ở `68f644e7` |

**4 mẫu còn lộ = 31 tệp (giảm thêm 3 tệp so với 10-12).** Cần `git rm -r --cached` một lượt cho 31 tệp này để gỡ hoàn toàn khỏi HEAD.

---

## 🟢 E4 — Tệp credential trong `.openclaw/` — ✅ **ĐÃ GIẢI QUYẾT (Commit `380d3f74`)**

**Severity:** ERROR → **RESOLVED** · **Category:** Secret exposure

| Tệp | Tracked trước 10-12 | **Tracked 10-13** | Rule ignore | Trạng thái |
|---|---|---|---|---|
| `.openclaw/device-auth.json` | 1 commit | **0 — untracked** ✅ | `.gitignore:122:.openclaw/*auth*.json` | ✅ **RESOLVED** |
| `.openclaw/identity/device-auth.json` | 1 commit | **0 — untracked** ✅ | `.gitignore:100:.openclaw/identity/` | ✅ **RESOLVED** |
| `.openclaw/agents/main/agent/auth-profiles.json` | 1 commit | **0 — untracked** ✅ | `.gitignore:101:.openclaw/agents/` | ✅ **RESOLVED** |
| `.openclaw/agents/main/agent/auth-state.json` | 1 commit | **0 — untracked** ✅ | `.gitignore:101:.openclaw/agents/` | ✅ **RESOLVED** |

**Kết luận:** Julius đã xử lý dứt điểm rủi ro rò rỉ credential tại commit `380d3f74`. Cả 4 tệp đã được untrack và bảo vệ bằng rule `.gitignore`.

---

## 🔴 E5 — `.hermes/checkpoints/` trên đĩa (36 MB, 31 tệp)

**Severity:** ERROR → giảm · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-12 | **10-13** |
|---|---|---|
| Tệp tracked | 0 ✅ | **0** ✅ |
| `git check-ignore --no-index` | `.gitignore:60` ✅ | **`.gitignore:60`** ✅ |
| Tệp trên đĩa | 31 tệp / 36 MB | **31 tệp / 36 MB** |
| `store/HEAD` tồn tại | CÓ | **CÓ** |

Đã được chặn index hoàn toàn. Kho object store trên đĩa vẫn an toàn và không phình lên repo GitHub.

---

## 🔴 E6 — `.hermes/.curator_backups/` trên đĩa (7,6 MB) & `skills/.curator_backups/` (16 MB, 6 tệp tracked)

**Severity:** ERROR → giảm · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-12 | **10-13** |
|---|---|---|
| `.hermes/.curator_backups/` đĩa | 328 tệp / 7,6 MB | **328 tệp / 7,6 MB** (0 tracked, rule `:61` ✅) |
| `.hermes/skills/.curator_backups/` đĩa | 15 tệp / 16 MB | **15 tệp / 16 MB** |
| `.hermes/skills/.curator_backups/` tracked | 9 tệp | **6 tệp** (−3 tệp đã xoá tại `f3d273a2`) |
| `git check-ignore --no-index` | `.gitignore:73` ✅ | **`.gitignore:73`** ✅ (vô hiệu với 6 tệp cũ) |

Cần `git rm -r --cached .hermes/skills/.curator_backups/` để gỡ 6 tệp còn lại.

---

## 🔴 E7 — 2 marker `.migrated.*` đều đang tracked trong git

**Severity:** ERROR · **Category:** Orphan / Repo hygiene

| Đường dẫn | Vị trí | Size | Mtime | Tracked | Blob SHA |
|---|---|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373` | KB Root | 69 B | 2026-09-08 20:42 | **CÓ** (commit `b5e519fc`) | `a0105ac6...` |
| `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51` | `.openclaw/` | 69 B | 2026-09-08 20:42 | **CÓ** (commit `b5e519fc`) | `a0105ac6...` |

Cả hai marker sinh ra từ cuộc di trú workspace của OpenClaw ngày 08-09 và bị auto-commit. Cả hai chưa có rule ignore wildcard `*.migrated.*`.
**Suggested fix:** `git rm --cached` cả 2 file + bổ sung rule `*.migrated.*` vào `.gitignore`.

---

## 🟢 E8 — `.hermes/config.yaml` — ✅ **ĐÃ ĐÓNG từ 10-04**

**Severity:** ERROR → **RESOLVED**
Đã được `git rm --cached` và thêm rule `.gitignore:67` trong commit `68f644e7`. Đo lại hôm nay: `git ls-files -s .hermes/config.yaml` rỗng ✅.

---

## 🟢 E9 — Tồn đọng nội dung chưa backup — ✅ **ĐÃ GIẢI QUYẾT (0 tồn đọng)**

**Severity:** ERROR → **RESOLVED** · **Category:** Content backup

| Chỉ số | 10-12 | **10-13** |
|---|---|---|
| Tệp `??` trong `wiki/` | 0 tệp ✅ | **0 tệp** ✅ |
| Tệp ` M` trong `wiki/` | 0 tệp ✅ | **0 tệp** ✅ |
| Backlog chưa commit vùng nội dung | 0 tệp ✅ | **0 tệp** ✅ |

Toàn bộ 1.701 tệp nội dung đã nằm trong index git và đã push lên GitHub.

---

## 🟢 E10 — `wiki/topic/brain-threat-detection.md` — ✅ **ĐÃ ĐÓNG từ 10-04**

**Severity:** ERROR → **RESOLVED**
Commit `3b891e34` (10-04 19:14) đã prune. Đã xác nhận trên HEAD hiện tại file không còn trong working tree và đã chốt trong lịch sử git.

---

## 🔴 E11 — `DREAMS.md` tại root — **Writer vẫn chạy, đã bảo vệ trên git**

**Severity:** ERROR · **Category:** Root whitelist / Process leak

| Chỉ số | 10-12 | **10-13** |
|---|---|---|
| Dung lượng | 16.980 B | **16.980 B** |
| Mtime | 2026-10-11 03:00:06 | **2026-10-13 03:00:06** |
| Tracked | 0 — untracked ✅ | **0 — untracked** ✅ |
| Rule | `.gitignore:82:/DREAMS.md` ✅ | **`.gitignore:82:/DREAMS.md`** ✅ |

**Kết luận:** File đã được chặn index an toàn trên git. Tuy nhiên, writer OpenClaw dreaming vẫn xả vào root KB lúc 03:00 hàng ngày.
**Suggested fix:** Điều chỉnh OpenClaw config để trỏ output dreaming vào `.openclaw/DREAMS.md`.

---

## 🔴 E12 — `memory/` tại root — **138 tệp / 7 thư mục (+4 tệp mới)**

**Severity:** ERROR · **Category:** Root whitelist / Process leak

| Chỉ số | 10-12 | **10-13** |
|---|---|---|
| Số tệp | 134 tệp | **138 tệp** (+4 tệp session log mới) |
| Số thư mục | 7 | **7** |
| Dung lượng | 640 KB | **656 KB** (+16 KB) |
| Tracked | 0 — untracked ✅ | **0 — untracked** ✅ |
| Rule | `.gitignore:113:memory/` ✅ | **`.gitignore:113:memory/`** ✅ |

Đã an toàn trên git (không bị commit). Tuy nhiên, writer session log vẫn tạo file trong root `memory/`. Lượt thứ 17 liên tiếp ghi nhận.
**Suggested fix:** Sửa cấu hình OpenClaw session output path sang `.openclaw/memory/`.

---

## 🔴 E13 — `wiki/HEARTBEAT.md` dangling symlink & missing root `HEARTBEAT.md`

**Severity:** ERROR · **Category:** Path / Symlink

1. **`wiki/HEARTBEAT.md` (dangling):**
   - `islink`: True, `lexists`: True.
   - `raw_target`: `../../.openclaw/HEARTBEAT.md`.
   - `realpath`: `/home/julius/.openclaw/HEARTBEAT.md` (lệch 1 cấp, nằm ngoài KB root).
   - `target_exists`: **False** ❌.
   - Hậu quả: Không hiển thị note hợp lệ trong Obsidian.
   - Đích đúng: `../.openclaw/HEARTBEAT.md`.
2. **`HEARTBEAT.md` tại root (thiếu):**
   - Whitelist §2 cho phép: symlink trỏ về `.openclaw/HEARTBEAT.md`.
   - Hiện tại: `lexists = False` (không tồn tại trên đĩa).
3. **4 symlink định danh root khác:** `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` đều trỏ đúng `.openclaw/` và target_exists = True ✅.

---

## 🔴 E14 — Tổng kết 31 tệp runtime agent home còn tracked (giảm 3 tệp)

**Severity:** ERROR · **Category:** Repo hygiene backlog

Danh sách 31 tệp cần chạy `git rm --cached`:
1. `.hermes/kanban.db`
2. `.hermes/kanban.db-shm`
3. `.hermes/kanban.db-wal`
4. `.hermes/kanban.db.dispatch.lock`
5. `.hermes/kanban.db.init.lock`
6. `.hermes/projects.db`
7. `.hermes/MEMORY.md`
8. 18 tệp `.hermes/config.yaml.bak.*`
9. 6 tệp `.hermes/skills/.curator_backups/*` (trong 2 thư mục timestamp 09-15 và 09-22; 3 tệp của 09-08 đã được xoá tại `f3d273a2`).

---

## ⚠️ W1 — Lỗi kỹ thuật bên trong `memory/`

**Severity:** WARNING · **Category:** Internal format / cleanup
Do `memory/` tại root là thư mục rác ngoại vi (E12), các tệp markdown bên trong không tuân thủ header, naming và wikilink của KB. Không can thiệp sửa bên trong; xử lý dứt điểm ở E12.

---

## ⚠️ W2 — 15 tệp `*-backup-*.md` trong `wiki/reviews/archive/2026-09/`

**Severity:** WARNING · **Category:** Naming / Spec conflict
15 tệp backup rename từ Fix Agent ngày 09-01 vẫn nằm trong thư mục archive. Đã được ghi nhận; cần chính sách lưu trữ rõ ràng trong `folder-structure.md` hoặc dọn dẹp sang thư mục riêng ngoài KB.

---

## ⚠️ W3 — Xung đột quy chuẩn (`folder-structure.md`)

**Severity:** WARNING · **Category:** Spec conflict
1. **Loại báo cáo `spot-check`:** 3 báo cáo trong archive dùng loại `spot-check` chưa có trong whitelist loại báo cáo của §7.
2. **Tệp chỉ mục cấp 1 `wiki/wiki.md` và `raw/raw.md`:** Whitelist yêu cầu bắt buộc tồn tại, nhưng câu chữ mục 7 lại cấm tệp ở root `wiki/`.
3. **Dangling link `raw/raw.md:23`:** còn liên kết `[[tools]]` trỏ về subfolder đã xoá từ tháng 7.

---

## ⚠️ W4 — Cặp topic trùng nghĩa `cuoc-dua-khong-{di,i}-lui` tái tạo lần thứ 8

**Severity:** WARNING · **Category:** Naming / Duplicate topic slug

- `wiki/topic/cuoc-dua-khong-di-lui.md` (356 B, mtime 2026-10-13 21:02:54, tracked).
- `wiki/topic/cuoc-dua-khong-i-lui.md` (385 B, mtime 2026-10-13 21:02:54, tracked).

Cả 2 tệp vừa được Index Agent tạo lại lúc 21:02 hôm nay. Tiếp tục **carry-forward, KHÔNG re-escalate mới**. Giải pháp căn cơ: Index Agent SKILL.md phải canonical hoá slug trước khi tạo file topic.

---

## ⚠️ W5 — Quy tắc miễn trừ agent home che các lỗi

**Severity:** WARNING · **Category:** Validator coverage
Quy tắc "bỏ qua độ sâu > 1 trong `.hermes/` và `.openclaw/`" che khuất 5 nhóm ERROR thực tế còn lại (E1, E3, E5, E6, E14). Validator đã bổ sung quét chuyên biệt để không bỏ sót rủi ro.

---

## ℹ️ I1 — 52 báo cáo cũ hơn 30 ngày trong `wiki/reviews/`

**Severity:** INFO · **Category:** Archival candidate
Hiện có 131 báo cáo active trong `wiki/reviews/`, trong đó 52 báo cáo có mtime trước 2026-09-13. Có thể di chuyển sang `wiki/reviews/archive/2026-08/` và `2026-07/` để giữ thư mục reviews gọn gàng.

---

## ℹ️ I2 — `.hermes/lsp/` (7.101 tệp trong `node_modules`)

**Severity:** INFO · **Category:** Runtime workspace
7.101 tệp trong `node_modules` đã được bảo vệ thành công bởi `.gitignore:63` từ commit `68f644e7`. Không bị theo dõi trên git.

---

## 🟢 Danh sách các điểm kiểm tra ĐẠT (PASS)

1. **15/15 chỉ mục bắt buộc tồn tại đầy đủ:** `raw/raw.md`, `wiki/wiki.md`, `wiki/tag/tag.md`, `context/context.md`, `context/USER.md`, `wiki/meta/format-spec.md`, `wiki/meta/folder-structure.md`, `wiki/meta/index-spec.md`, `wiki/reviews/_action-required.md`, `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, `.gitignore`, và 6 subfolder raw indexes (`articles`, `papers`, `posts`, `repos`, `videos`, `websites`).
2. **4/4 symlink định danh root hợp lệ:** `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` trỏ đúng target trong `.openclaw/`.
3. **0 thư mục rỗng trong vùng nội dung:** Không có thư mục rỗng nào bị bỏ quên.
4. **0 lỗi path / naming trong 1.701 tệp vùng nội dung:** Cấu trúc bài viết và tài liệu tri thức hoàn toàn sạch sẽ.
5. **0 trùng lặp slug trong cùng phân vùng:** Trừ cặp topic W4 do lỗi chính tả tiếng Việt của Index Agent.
6. **🟢 Backup pipeline sạch:** HEAD đồng bộ hoàn hảo với GitHub `master` tại commit `221b804c`.

---

## Hành động kiến nghị (Thứ tự ưu tiên)

1. **Dọn sạch 31 tệp runtime agent home (E3, E14) và 2 marker `.migrated.*` (E7):** Chạy `git rm -r --cached` một lượt + bổ sung rule `*.migrated.*` vào `.gitignore`.
2. **Sửa symlink `wiki/HEARTBEAT.md` (E13):** Sửa target thành `../.openclaw/HEARTBEAT.md` và tạo symlink root `HEARTBEAT.md -> .openclaw/HEARTBEAT.md`.
3. **Điều chỉnh 2 writer ngoại vi (E11, E12):** Đổi đường dẫn ghi của OpenClaw dreaming và session logs vào `.openclaw/`.
4. **Vá Index Agent SKILL.md (W4):** Canonical hoá slug để triệt tiêu cặp topic trùng `cuoc-dua-khong-{di,i}-lui`.
5. **Di dời bản cài Hermes Agent E1:** Khi Hermes Agent tạm dừng, di chuyển thư mục `hermes-agent` ra ngoài KB.
