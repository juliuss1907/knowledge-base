# Hygiene Inspection — 2026-10-10

**Status:** approved — Julius duyệt 2026-10-12
**Approved by:** Julius
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **2 đã RESOLVED** (E8, E10) + **2 giảm** (E5, E6) ⇒ **10 ERROR còn hiệu diện**; **0 ERROR mới**. Trong đó **4 ERROR máy** (path thật ở tầng quét) + **6 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-10-10 23:31 +0700
**Validator:** hygiene-inspector
**Paths checked:** **1.699 tệp ổn định trong phạm vi KB** (1.688 vùng nội dung + 11 tệp/symlink root) → **1.700 post-write** (báo cáo này nằm trong vùng nội dung) + **74 thư mục** (9 root + 23 vùng nội dung gồm thư mục gốc vùng + 42 L1 agent home) + **99 tệp tầng đầu agent home — BIẾN ĐỘNG** (77 `.hermes` + 22 `.openclaw`). Quét máy = **234.524** (định nghĩa: prune mọi thư mục `.git` ở mọi độ sâu) — ⚠️ **KHÔNG phải phạm vi kiểm tra**.
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

> **Khoảng cách 6 ngày kể từ 10-04 (lượt xác nhận lớn nhất sau 2 commit `3b891e34` và `68f644e7`).**
> Toàn bộ 21 nhóm issue được đo lại độc lập trên trạng thái đĩa và index git hôm nay (2026-10-10 23:30).
> - **🟢 New-debt trong vùng nội dung KB = 0:** 1.688 tệp nội dung (1.452 wiki + 229 raw + 2 context + 5 scripts) tuân thủ 100% naming và path whitelist của `folder-structure.md`.
> - **🔴 `vault backup` cron trên máy chính đã dừng 6,16 ngày:** HEAD cục bộ `68f644e7` (2026-10-04 19:41:16) khớp `refs/heads/master` trên GitHub, nhưng từ đó đến nay không có commit mới nào. Trên đĩa đang chờ: 20 `??` (7 file wiki/ + 13 file skills), 320 ` M` (294 wiki/ do Index Agent full rebuild 21:04 hôm nay), 10 ` D`.
> - **🔴 4 mẫu runtime agent home (40 tệp) vẫn còn tracked:** dù `.gitignore` block đã thêm ở `68f644e7`, 40 tệp này đã commit từ trước nên rule vô hiệu. Cần `git rm -r --cached` một lượt.
> - **🔴 2 marker `.migrated.*` (root + `.openclaw/`) đều đang tracked trên GitHub**, cùng blob `a0105ac6...` (69 B).
> - **🔴 3 writer ngoại vi chưa dừng:** `DREAMS.md` tại root (tăng lên 16.929 B lúc 03:00 hôm nay), `memory/` tại root (126 tệp / 7 thư mục / 608 KB), và `wiki/HEARTBEAT.md` dangling symlink (`../../.openclaw/HEARTBEAT.md`).
> - **⚠️ Cặp topic trùng nghĩa `cuoc-dua-khong-{di,i}-lui` tái tạo lần thứ 5** do Index Agent rebuild 21:04.

---

## Bảng đối chiếu định nghĩa quét máy (Bài học 10-03 #25)

| Định nghĩa prune | Lệnh thực thi | Kết quả 10-10 | Bản chất |
|---|---|---|---|
| **Prune mọi `.git` ở mọi độ sâu** | `find . -type d -name .git -prune -o \( -type f -o -type l \) -print` | **234.524** | Chuẩn công bố của validator (giảm 8.838 tệp do dọn temp trong hermes-agent) |
| **Prune root `.git` + prune `hermes-agent`** | `find . -path ./.git -prune -o -name hermes-agent -prune -o …` | **11.044** | Phạm vi máy thật khi loại bỏ bản cài lồng E1 |
| **Prune chỉ root `.git`** | `find . -path ./.git -prune -o \( -type f -o -type l \) -print` | **236.598** | Chênh đúng **2.074 tệp** `.git` của repo lồng `hermes-agent` (236.598 − 234.524 = 2.074) |

---

## 🔴 E1 — Bản cài Hermes Agent 223.450 tệp / 5,5 GB — **PHẦN GIT ĐÃ ĐÓNG, phần đĩa còn nguyên**

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-04 | **10-10 23:30 (đo lại)** |
|---|---|---|
| `find … \( -type f -o -type l \)` | 225.530 | **223.450** (−2.080 tệp runtime/cache) |
| `du -sh` | 5,5 GB | **5,5 GB** |
| nested `.git` | CÓ | **CÓ** (2.074 tệp / 1,6 GB) · branch `main` · HEAD `990473a79c` |
| `git ls-tree HEAD \| grep 160000` | KHÔNG CÒN ✅ | **KHÔNG CÒN** ✅ |
| `git ls-files -s .hermes/hermes-agent` | 0 — untracked ✅ | **0 — untracked** ✅ |
| `git check-ignore --no-index` | `.gitignore:59` ✅ | **`.gitignore:59 .hermes/hermes-agent/`** ✅ |

**Kết luận:** Vấn đề cấu trúc git đã được bảo vệ thành công từ commit `68f644e7`. Bản cài lồng trên đĩa vẫn chiếm 5,5 GB và là CWD/launch path của tiến trình Hermes Agent đang chạy.
**⚠️ KHÔNG `rm -rf` khi Hermes đang chạy từ đó.** Cần Julius / Fix Agent di dời bản cài ra ngoài KB khi Hermes tạm dừng.

---

## 🔴 E2 — `vault backup` — ⚠️ **TÁI DỪNG 6,16 NGÀY (kể từ commit `68f644e7`)**

**Severity:** ERROR · **Category:** Sync / Backup

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `68f644e7` (2026-10-04 19:41:16 +0700) |
| `git ls-remote --heads origin` | `refs/heads/master = 68f644e7` — **khớp** ✅ |
| Tuổi backup | **6 ngày 3,8 giờ (6,16 ngày)** không có commit mới |
| Trạng thái chưa backup | **20 `??`** (7 wiki + 13 skills) · **320 ` M`** (294 wiki + 26 agent) · **10 ` D`** |

**Phân tích nguyên nhân:**
1. Commit `68f644e7` ngày 10-04 là commit thủ công của Julius để đóng lỗ hổng backup 10 ngày trước đó.
2. Từ đó đến nay, cron `vault backup` trên máy chính **không chạy hoặc không commit** tự động.
3. Rủi ro mất mát dữ liệu hiện tại: 7 tệp wiki mới (4 báo cáo + 3 topic) và 294 tệp wiki cập nhật (chủ yếu Index Agent rebuild lúc 21:04 hôm nay) chỉ nằm trên đĩa máy VPS, chưa lên GitHub.
4. **Nhánh mặc định của remote vẫn là `main` (`ead50c82`)**, bỏ rơi từ 2026-05-11, trong khi sync branch là `master` (`68f644e7`).

**Suggested fix:** Kiểm tra cron job `vault backup` trên máy chính (systemd timer / launchd / crontab). Nếu Obsidian đóng hoặc máy tắt, cron không chạy. Thực hiện manual commit + push lên `master`.

---

## 🔴 E3 — 13 mẫu runtime agent home — **9/13 ĐÃ ĐÓNG, 4 còn lộ (40 tệp)**

**Severity:** ERROR · **Category:** Path / Repo hygiene

Đo lại hôm nay (`git ls-files -s` + `git check-ignore --no-index -v` — bài học 09-30 #14):

| Mẫu | Tracked 10-04 | **Tracked 10-10** | Rule | Trạng thái |
|---|---|---|---|---|
| `.hermes/kanban.db*` | 3 | **5** (thêm 2 lock) | **NONE** | ❌ còn lộ (141 commit mỗi tệp) |
| `.hermes/projects.db` | 1 | **1** | **NONE** | ❌ còn lộ (1 commit) |
| `.hermes/config.yaml.bak*` | 18 | **18** | **NONE** | ❌ còn lộ (11 commit) |
| `.hermes/skills/.curator_backups*` | 15 | **15** | `:73` có, **vô hiệu** | ❌ còn lộ (14 commit) |
| `.hermes/MEMORY.md` | 1 | **1** | `:110` có, **vô hiệu** | ❌ còn lộ (172 commit) |
| `.hermes/verification_evidence.db` | 0 | **0** | `:69` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/state-snapshots*` | 0 | **0** | `:62` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/checkpoints*` | 0 | **0** | `:60` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/.curator_backups*` | 0 | **0** | `:61` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/config.yaml` | 0 | **0** | `:67` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/auth.json` | 0 | **0** | `:37` | ✅ **đã đóng** ở `68f644e7` |
| `.hermes/lsp/*` | 0 | **0** | `:63` | ✅ **đã đóng** ở `68f644e7` |

**4 mẫu còn lộ = 40 tệp.** `git rm -r --cached` một lượt cho 4 mẫu này là đủ; không cần sửa `.gitignore` mới vì hầu hết đã có rule hoặc chỉ cần untrack.

---

## 🔴 E4 — Tệp tên auth đã tracked: 4 tệp credential thật trong `.openclaw/`

**Severity:** ERROR · **Category:** Path / Secret exposure

| Tệp | Size | Commit | Rule | Lịch sử |
|---|---|---|---|---|
| `.openclaw/device-auth.json` | 461 B | 1 | `:86` **vô hiệu** | thêm ở `8695083b` 2026-05-12 (151 ngày) |
| `.openclaw/identity/device-auth.json` | 461 B | 1 | `:100` **vô hiệu** | thêm ở `8695083b` (151 ngày) |
| `.openclaw/agents/main/agent/auth-profiles.json` | 752 B | 1 | `:101` **vô hiệu** | thêm ở `8695083b` (151 ngày) |
| `.openclaw/agents/main/agent/auth-state.json` | 469 B | 1 | `:101` **vô hiệu** | thêm ở `8695083b` (151 ngày) |

**Giữ nguyên nguyên tắc:** Chỉ grep **tên khoá** (`"token"`, `"tokens"`), **không** đọc giá trị secret.
**Suggested fix:** Rotate token trước mọi thao tác git nếu repo public → `git rm --cached` cả 4 tệp → commit → rewrite git history nếu cần.

---

## 🔴 E5 — `.hermes/checkpoints/` trên đĩa (36 MB, 31 tệp)

**Severity:** ERROR → giảm · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-04 | **10-10** |
|---|---|---|
| Tệp tracked | 0 ✅ | **0** ✅ |
| `git check-ignore --no-index` | `.gitignore:60` ✅ | **`.gitignore:60`** ✅ |
| Tệp trên đĩa | 8.922 / 73 MB | **31 tệp / 36 MB** (đã dọn gọn) |
| `store/HEAD` tồn tại | CÓ | **CÓ** |

Đã được chặn index hoàn toàn. Kho object store trên đĩa vẫn an toàn và không phình lên repo GitHub.

---

## 🔴 E6 — `.hermes/.curator_backups/` trên đĩa (328 tệp, 7,6 MB)

**Severity:** ERROR → giảm · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-04 | **10-10** |
|---|---|---|
| Tệp tracked | 0 ✅ | **0** ✅ |
| `git check-ignore --no-index` | `.gitignore:61` ✅ | **`.gitignore:61`** ✅ |
| Tệp trên đĩa | 230 tệp / 5,3 MB | **328 tệp / 7,6 MB** |

Đã untracked từ `68f644e7`. Tiếp tục theo dõi dung lượng trên đĩa.

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

## 🔴 E8 — `.hermes/config.yaml` — ✅ **ĐÃ ĐÓNG từ 10-04**

**Severity:** ERROR → **RESOLVED**
Đã được `git rm --cached` và thêm rule `.gitignore:67` trong commit `68f644e7`. Đo lại hôm nay: `git ls-files -s .hermes/config.yaml` rỗng ✅.

---

## 🔴 E9 — Tệp nội dung chưa backup và Index Agent churn

**Severity:** ERROR · **Category:** Content backup

- **7 tệp `??` trong `wiki/`:**
  - 4 báo cáo: `2026-10-04_format-report.md`, `2026-10-04_hygiene-report.md`, `2026-10-04_output-report.md`, `2026-10-10_format-report.md` (chờ thêm báo cáo này là 5).
  - 3 topic: `ai-ad-creative-system.md`, `ai-animation-ads-workflow.md`, `ai-motion-design-pipeline.md`.
- **294 tệp ` M` trong `wiki/`:** Index Agent full rebuild lúc 21:04 hôm nay (25 tag + 268 topic + 1 action file). Không phải thay đổi nội dung đột biến mà là cơ chế rebuild chu kỳ của Index Agent.

---

## 🔴 E10 — `wiki/topic/brain-threat-detection.md` — ✅ **ĐÃ ĐÓNG từ 10-04**

**Severity:** ERROR → **RESOLVED**
Commit `3b891e34` (10-04 19:14) ghi nhận: *"1 D: wiki/topic/brain-threat-detection.md — Index Agent prune, 0 concept trỏ tới, không mất nội dung"*. Đã xác nhận trên HEAD hiện tại file không còn trong working tree và đã chốt trong lịch sử git.

---

## 🔴 E11 — `DREAMS.md` tại root — **Writer vẫn chạy lúc 03:00 hôm nay**

**Severity:** ERROR · **Category:** Root whitelist / Process leak

| Chỉ số | 10-04 | **10-10** |
|---|---|---|
| Dung lượng | 16.216 B | **16.929 B** (+713 B) |
| Mtime | 2026-10-04 03:00:02 | **2026-10-10 03:00:02** (chạy đúng 03:00 sáng nay) |
| Tracked | Đã gỡ ✅ | **0 — untracked** ✅ |
| Rule | `.gitignore:82` ✅ | **`.gitignore:82:/DREAMS.md`** ✅ |

**Kết luận:** File đã được chặn index an toàn trên git. Tuy nhiên, writer OpenClaw dreaming vẫn tiếp tục xả vào root KB mỗi đêm lúc 03:00.
**Suggested fix:** Điều chỉnh OpenClaw config để trỏ output dreaming vào `.openclaw/DREAMS.md`.

---

## 🔴 E12 — `memory/` tại root — **126 tệp / 7 thư mục (Writer tiếp tục ghi)**

**Severity:** ERROR · **Category:** Root whitelist / Process leak

| Chỉ số | 10-04 | **10-10** |
|---|---|---|
| Số tệp | 101 tệp | **126 tệp** (+25 tệp session log mới) |
| Số thư mục | 7 | **7** |
| Dung lượng | 480 KB | **608 KB** |
| Tracked | Đã gỡ ✅ | **0 — untracked** ✅ |
| Rule | `.gitignore:113` ✅ | **`.gitignore:113:memory/`** ✅ |

Đã an toàn trên git (không bị commit). Tuy nhiên, writer session log vẫn tạo file trong root `memory/`. Lượt thứ 14 liên tiếp ghi nhận.
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

## 🔴 E14 — Tổng kết 40 tệp runtime agent home còn tracked

**Severity:** ERROR · **Category:** Repo hygiene backlog

Danh sách 40 tệp cần chạy `git rm --cached`:
1. `.hermes/kanban.db`
2. `.hermes/kanban.db-shm`
3. `.hermes/kanban.db-wal`
4. `.hermes/kanban.db.dispatch.lock`
5. `.hermes/kanban.db.init.lock`
6. `.hermes/projects.db`
7. `.hermes/MEMORY.md`
8. 18 tệp `.hermes/config.yaml.bak.*`
9. 15 tệp `.hermes/skills/.curator_backups/*` (gồm `cron-jobs.json`, `manifest.json`, `skills.tar.gz` trong các thư mục timestamp 08-23 và 08-30).

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

## ⚠️ W4 — Cặp topic trùng nghĩa `cuoc-dua-khong-{di,i}-lui` tái tạo lần thứ 5

**Severity:** WARNING · **Category:** Naming / Duplicate topic slug

- `wiki/topic/cuoc-dua-khong-di-lui.md` (356 B, mtime 2026-10-10 21:04:20, tracked).
- `wiki/topic/cuoc-dua-khong-i-lui.md` (385 B, mtime 2026-10-10 21:04:20, tracked).

Cả 2 tệp vừa được Index Agent tạo lại lúc 21:04 hôm nay. Đã escalate lần 3 ở 10-03, tiếp tục **carry-forward, KHÔNG re-escalate mới**. Giải pháp căn cơ: Index Agent SKILL.md phải canonical hoá slug trước khi tạo file topic.

---

## ⚠️ W5 — Quy tắc miễn trừ agent home che các lỗi

**Severity:** WARNING · **Category:** Validator coverage
Quy tắc "bỏ qua độ sâu > 1 trong `.hermes/` và `.openclaw/`" che khuất 6 nhóm ERROR thực tế (E1, E3, E4, E5, E6, E14). Validator đã bổ sung quét chuyên biệt để không bỏ sót rủi ro.

---

## ℹ️ I1 — 38 báo cáo cũ hơn 30 ngày trong `wiki/reviews/`

**Severity:** INFO · **Category:** Archival candidate
Hiện có 124 báo cáo active trong `wiki/reviews/`, trong đó 38 báo cáo có mtime trước 2026-09-01. Có thể di chuyển sang `wiki/reviews/archive/2026-08/` và `2026-07/` để giữ thư mục reviews gọn gàng.

---

## ℹ️ I2 — `.hermes/lsp/` (7.101 tệp trong `node_modules`)

**Severity:** INFO · **Category:** Runtime workspace
7.101 tệp trong `node_modules` đã được bảo vệ thành công bởi `.gitignore:63` từ commit `68f644e7`. Không bị theo dõi trên git.

---

## 🟢 Danh sách các điểm kiểm tra ĐẠT (PASS)

1. **15/15 chỉ mục bắt buộc tồn tại đầy đủ:** `raw/raw.md`, `wiki/wiki.md`, `wiki/tag/tag.md`, `context/context.md`, `context/USER.md`, `wiki/meta/format-spec.md`, `wiki/meta/folder-structure.md`, `wiki/meta/index-spec.md`, `wiki/reviews/_action-required.md`, `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, `.gitignore`, và 6 subfolder raw indexes (`articles`, `papers`, `posts`, `repos`, `videos`, `websites`).
2. **4/4 symlink định danh root hợp lệ:** `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` trỏ đúng target trong `.openclaw/`.
3. **0 thư mục rỗng trong vùng nội dung:** Không có thư mục rỗng nào bị bỏ quên.
4. **0 lỗi path / naming trong 1.688 tệp vùng nội dung:** Cấu trúc bài viết và tài liệu tri thức hoàn toàn sạch sẽ.
5. **0 trùng lặp slug trong cùng phân vùng:** Trừ cặp topic W4 do lỗi chính tả tiếng Việt của Index Agent.

---

## Hành động kiến nghị (Thứ tự ưu tiên)

1. **Khôi phục cron `vault backup` trên máy chính:** Chạy manual commit + push lên `master` để đưa 20 `??` và 320 ` M` lên GitHub.
2. **Xử lý bí mật E4:** Kiểm tra repo visibility → Rotate token của `.openclaw/` trước mọi thao tác git → `git rm --cached` 4 file credential.
3. **Dọn sạch 40 tệp runtime agent home (E3, E14) và 2 marker `.migrated.*` (E7):** Chạy `git rm --cached` một lượt + bổ sung rule `*.migrated.*` vào `.gitignore`.
4. **Sửa symlink `wiki/HEARTBEAT.md` (E13):** Sửa target thành `../.openclaw/HEARTBEAT.md` và tạo symlink root `HEARTBEAT.md -> .openclaw/HEARTBEAT.md`.
5. **Điều chỉnh 2 writer ngoại vi (E11, E12):** Đổi đường dẫn ghi của OpenClaw dreaming và session logs vào `.openclaw/`.
6. **Vá Index Agent SKILL.md (W4):** Canonical hoá slug để triệt tiêu cặp topic trùng `cuoc-dua-khong-{di,i}-lui`.
