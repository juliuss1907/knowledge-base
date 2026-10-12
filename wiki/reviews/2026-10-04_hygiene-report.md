# Hygiene Inspection — 2026-10-04

**Status:** approved — Julius duyệt 2026-10-12
**Approved by:** Julius
**Issues found:** **21 nhóm** — **14 ERROR + 5 WARNING + 2 INFO** (tổng trong ngoặc = 21 ✅ khớp đúng 21 mục thân báo cáo: E1–E14, W1–W5, I1–I2). Trong 14 mục ERROR: **3 đã RESOLVED** (E2, E8, E10) + **2 giảm** (E5, E6) ⇒ **9 ERROR còn hiệu diện**; **0 ERROR mới**. Trong đó **4 ERROR máy** (path thật ở tầng quét) + **6 nhóm ERROR agent home bị quy tắc miễn trừ che** (xem W5).
**Created:** 2026-10-04 23:31 +0700
**Validator:** hygiene-inspector
**Paths checked:** **1.697 tệp ổn định trong phạm vi KB** (1.686 vùng nội dung + 11 tệp/symlink root) → **1.698 post-write** (báo cáo này nằm trong vùng nội dung) + **74 thư mục** (9 root + 23 vùng nội dung gồm thư mục gốc vùng + 42 L1 agent home) + **98 tệp tầng đầu agent home — BIẾN ĐỘNG** (76 `.hermes` + 22 `.openclaw`). Quét máy = **243.362** (định nghĩa: prune mọi thư mục `.git` ở mọi độ sâu) — ⚠️ **KHÔNG phải phạm vi kiểm tra**.
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

> **Đây là lượt đổi trạng thái lớn nhất kể từ 09-01.** Hai commit thủ công hôm nay đã dọn phần lớn backlog agent home: `3b891e34` (19:14, đóng băng 10 ngày — 496 file, +11.345/−2.077) và `68f644e7` (19:41, `.gitignore` chặn agent home 6,3 GB + gỡ 284 path khỏi tracking). **`vault backup` đã phục hồi** ⇒ E2 (dừng 9,11 ngày) **ĐÓNG**. Báo cáo này đo lại **toàn bộ** 13 nhóm ERROR của 10-03 trên HEAD mới, không chép kết luận cũ.

---

## 🔴 E1 — Bản cài Hermes Agent 225.530 tệp / 5,5 GB — **PHẦN GIT ĐÃ ĐÓNG, phần đĩa còn nguyên**

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-03 | **10-04 23:32 (đo lại)** |
|---|---|---|
| `find … \( -type f -o -type l \)` | 225.530 | **225.530** (đứng yên) |
| `du -sh` | 5,5 GB | **5,5 GB** |
| nested `.git` | CÓ | **CÓ** (2.074 tệp / 1,6 GB) · branch `main` · HEAD `990473a79c` |
| `git ls-tree HEAD \| grep 160000` | **gitlink CÓ** | **KHÔNG CÒN** ✅ |
| `.gitmodules` | không có | **vẫn không có** (nay vô nghĩa — đã không còn gitlink) |
| `git ls-files -s .hermes/hermes-agent` | 1 (gitlink) | **0 — untracked** ✅ |
| `git check-ignore --no-index` | **không rule** | **`.gitignore:59 .hermes/hermes-agent/`** ✅ |

**Kết luận:** vấn đề **cấu trúc git đã được sửa đúng cách** — gỡ gitlink, thêm rule ignore. Phần **đĩa vẫn 5,5 GB** và cơ chế cài đặt vẫn chưa xác định ⇒ nếu Hermes tự cài lại vào CWD này, 5,5 GB quay lại (dù lần này sẽ **không** lên GitHub nữa — đã có rule).

**⚠️ KHÔNG `rm -rf` khi Hermes đang chạy từ đó** — đây là CWD của tiến trình đang viết báo cáo này.

---

## 🔴 E2 — `vault backup` — ✅ **ĐÓNG sau 9,11 ngày**

**Severity:** ERROR → **RESOLVED** · **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `68f644e7` (2026-10-04 19:41:16) |
| `git ls-remote --heads origin` | `refs/heads/master = 68f644e7` — **khớp** ✅ |
| Tuổi backup | **0 ngày** |

Hai commit thủ công: `3b891e34` (19:14, *"KB scope: 10 ngày thay đổi (09-24 → 10-04)"*, 496 file, +11.345/−2.077) + `68f644e7` (19:41, `.gitignore` chặn agent home 6,3 GB, 284 file, −61.184 dòng). Hệ quả: `git diff` hôm nay **phủ đúng 24 giờ** thay vì 10 ngày.

**Việc còn treo (không phải ERROR):** remote default branch vẫn là `refs/heads/main = ead50c82` (bỏ rơi từ 2026-05-11), HEAD local theo `master`. **Cần Julius xác nhận máy chính push đúng nhánh.**

---

## 🔴 E3 — 13 mẫu runtime agent home — **9/13 ĐÃ ĐÓNG, 4 còn lộ (38 tệp)**

**Severity:** ERROR · **Category:** Path

Đo lại hôm nay (`git ls-files -s` + `git check-ignore --no-index -v` — bài học 09-30 #14):

| Mẫu | tracked 10-03 | tracked 10-04 | Rule | Trạng thái |
|---|---|---|---|---|
| `.hermes/kanban.db` | 1 | **1** | **NONE** | ❌ còn lộ (3 commit) |
| `.hermes/kanban.db-shm` | 1 | **1** | **NONE** | ❌ còn lộ (**141 commit**) |
| `.hermes/kanban.db-wal` | 1 | **1** | **NONE** | ❌ còn lộ (**141 commit**) |
| `.hermes/projects.db` | 1 | **1** | **NONE** | ❌ còn lộ (1 commit) |
| `.hermes/config.yaml.bak*` | 18 | **18** | **NONE** | ❌ còn lộ (11 commit) |
| `.hermes/skills/.curator_backups*` | 15 | **15** | `:73` có, **vô hiệu** | ❌ còn lộ (14 commit) |
| `.hermes/MEMORY.md` | 1 | **1** | `:110` có, **vô hiệu** | ❌ còn lộ (172 commit) |
| `.hermes/verification_evidence.db` | 1 (345 commit) | **0** | `:69` | ✅ **đóng** |
| `.hermes/state-snapshots*` | 7 | **0** | `:62` | ✅ **đóng** |
| `.hermes/checkpoints*` | 31 | **0** | `:60` | ✅ **đóng** |
| `.hermes/.curator_backups*` | 230 | **0** | `:61` | ✅ **đóng** |
| `.hermes/config.yaml` | 1 (50 commit) | **0** | `:67` | ✅ **đóng** |
| `.hermes/auth.json` | 1 (78 commit) | **0** | `:37` | ✅ **đóng** |
| `.hermes/lsp/*` | 4 | **0** | `:63` | ✅ **đóng** |

**4 mẫu còn lộ = 38 tệp.** `git rm -r --cached` một lượt cho 4 mẫu này là đủ; **không** cần `.gitignore` mới (3/4 đã có rule nhưng rule không cứu được tệp đã commit trước rule — bài học 09-29 #12b).

---

## 🔴 E4 — Tệp tên auth đã tracked: 7 → **4** (toàn bộ nằm trong `.openclaw/`) — ĐÍNH CHÍNH

**Severity:** ERROR · **Category:** Path / Secret exposure

| Tệp | Size | Commit | Rule | Lịch sử |
|---|---|---|---|---|
| `.openclaw/device-auth.json` | 461 B | 1 | `:86` **vô hiệu** | thêm ở `8695083b` 2026-05-12 |
| `.openclaw/identity/device-auth.json` | 461 B | 1 | `:100` **vô hiệu** | thêm ở `8695083b` |
| `.openclaw/agents/main/agent/auth-profiles.json` | 752 B | 1 | `:101` **vô hiệu** | thêm ở `8695083b` |
| `.openclaw/agents/main/agent/auth-state.json` | 469 B | 1 | `:101` **vô hiệu** | thêm ở `8695083b` |

**Đã đóng 3/7:** `.hermes/auth.json` (untracked), `.hermes/auth.lock` (đã gỡ khỏi tracking), `.hermes/state-snapshots/20260626-005403-pre-update/auth.json` (cả nhóm untracked).

**Đính chính so với 10-03:** 10-03 liệt kê 7 tệp và ghi *"cả 7 nằm trong HEAD ⇒ đã trên GitHub"*. Hôm nay `git log --diff-filter=A` cho thấy **cả 4 tệp `.openclaw/` thêm ở `8695083b` (2026-05-12)** — tức đã trên GitHub **145 ngày**, không phải do commit hôm nay. Bản chất rủi ro **không đổi**, mức độ phơi bày **đã giảm 3/7**.

**Giữ nguyên nguyên tắc:** chỉ grep **tên khoá** (`grep -oE '"[a-z_]*(token|key|secret|credential)[a-z_]*"'` trên `device-auth.json` → `"token"`, `"tokens"`), **không** đọc **giá trị**. Báo cáo này **không** mở nội dung credential.

**Đính chính phạm vi grep (lần 2):** lọc `auth|token|secret|credential|apikey|\.env` trên `git ls-tree -r HEAD` trả về **29 tệp**, trong đó **25 là nội dung tri thức hợp lệ** (`wiki/concepts/token-*.md`, `raw/articles/2026-06-08_tokens-and-tokenization.md`, …) và **6 là script OpenClaw** (`.openclaw/skills/news-brief-skill/*auth*.py`) — không phải credential. Danh sách 4 tệp ở trên là kết quả sau khi tách 3 nhóm.

**Suggested fix (thứ tự):** (1) Julius kiểm visibility repo — public ⇒ **rotate token trước mọi việc git**; (2) `git rm --cached` cả 4 + commit; (3) rewrite lịch sử nếu token còn hiệu lực (`git-secret-cleanup`); (4) rotate ở provider sau khi rewrite.

---

## 🔴 E5 — `.hermes/checkpoints/` — ✅ **GỠ KHỎI TRACKING**, còn lại là kho trên đĩa

**Severity:** ERROR → giảm · **Category:** Orphan / repo hygiene

| Bằng chứng | 10-03 | **10-04** |
|---|---|---|
| Tệp tracked | 31 | **0** ✅ |
| `git check-ignore --no-index` | 0 rule | **`.gitignore:60`** ✅ |
| Tệp trên đĩa | 8.360 / 70 MB | **8.922 / 73 MB** (+562 / +3 MB) |
| `store/HEAD` tồn tại | CÓ | **CÓ** |

**⚠️ Đính chính phát hiện cũ — quan trọng:** 09-29 và 10-03 gọi đây là *"repo git lồng"*. Kiểm lại hôm nay: `.hermes/checkpoints/` **không có thư mục `.git`** (`find -maxdepth 5 -type d -name .git -not -path './.git'` trả **duy nhất** `./.hermes/hermes-agent/.git`). `git -C .hermes/checkpoints rev-parse --git-dir` trả `/home/julius/knowledge-base/.git` ⇒ nó **không phải repo riêng**, chỉ là **git object store của Hermes** đặt nhầm chỗ. Đây là **lỗi phân loại của các lượt trước**, không phải thay đổi dữ liệu hôm nay (grep artifact trước rồi mới kết luận — bài học 09-30 #17).

**Việc còn treo:** 8.922 tệp / 73 MB trong KB. Đã an toàn cho git (rule `:60`), nhưng vẫn là **rác ở tầng đĩa**.

---

## 🔴 E6 — `.hermes/.curator_backups/` — ✅ **GỠ KHỎI TRACKING**, leo thang trên đĩa

**Severity:** ERROR → giảm · **Category:** Orphan

Trên đĩa: **325 tệp / 7,4 MB** (`.hermes/.curator_backups/`, 10-03: 317 / 7,1 MB) + 15 (`.hermes/skills/.curator_backups/`). Đã tracked: **230 → 0** ✅ (rule `.gitignore:61`). Riêng `.hermes/skills/.curator_backups/` **vẫn còn 15 tệp tracked** (rule `:73` có nhưng **vô hiệu**) — thuộc nhóm 38 tệp còn lộ của E3.

---

## 🔴 E7 — 2 marker `.migrated.*` — **26 ngày**, chưa có rule — CARRY-FORWARD

**Severity:** ERROR · **Category:** Path

| Vị trí | Cỡ | mtime | tracked | Rule |
|---|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3….e79d1c6c-…` (root) | 69 B | **2026-09-08 20:42** | **CÓ** | **NONE** |
| `.openclaw/workspace-state.json.migrated.43c9aa3….fb077b94-…` | 69 B | **2026-09-08 20:42** | **CÓ** | **NONE** |

`find . -name '*.migrated.*' -not -path './.git/*'` (bài học 09-25) ⇒ **đúng 2, không có biến thể thứ ba**. `openclaw-workspace-state.json` gốc **KHÔNG còn** (`workspace_state_present: false`) — đúng như root-cause đã biết: OpenClaw ghi state theo CWD, KB root có `AGENTS.md` nên là workspace hợp lệ (pitfall #9, v1.21).

**⚠️ Đáng chú ý:** commit hôm nay `.gitignore` **không** thêm wildcard `*.migrated.*` — nên 2 marker này **vẫn được backup bình thường** mỗi lần chạy. Đây là chỗ duy nhất trong E1–E7 mà công việc dọn hôm nay **bỏ sót có chủ ý hoặc vô tình**.

**Suggested fix:** thêm `*.migrated.*` + `git rm --cached` cả hai + commit.

---

## 🔴 E8 — `.hermes/config.yaml` — ✅ **ĐÓNG** (không còn tracked)

**Severity:** ERROR → **RESOLVED** · **Category:** Path / Secret exposure

`git ls-files -s .hermes/config.yaml` = **rỗng**; `check-ignore --no-index` ⇒ **`.gitignore:67`**. Trước đó: 23.603 B, **50 commit**, có tên khoá `api_key`/`secret`/`session_key`. Lịch sử 51 commit vẫn chứa nội dung ⇒ nếu token còn hiệu lực thì `git-secret-cleanup` vẫn cần (xem E4).

---

## 🔴 E9 — 17 tệp `??` chờ commit + 314 tệp `M` (Index Agent)

**Severity:** ERROR → INFO · **Category:** Orphan

`git status --porcelain -uall`: **17 `??`** + 314 ` M` + 7 ` D` + 1 staged `M`.

Phân bổ `??` (17): **12 `.hermes/skills/`** (4 file `.archive/` mới + `bulk-rewrite-invariants` + 7 `references/` mới của output-validator/openclaw-ops — curator đã dọn skill) + **5 `wiki/`** (`2026-10-04_format-report.md`, `2026-10-04_output-report.md`, 3 topic `ai-ad-creative-system` / `ai-animation-ads-workflow` / `ai-motion-design-pipeline`).

Phân bổ ` M` (314): **296 `wiki/topic` + `wiki/tag`** (Index Agent full rebuild 21:04) + **18 `.hermes`/`.openclaw`** runtime. **Đây KHÔNG phải KB dày thêm** — bài học 09-28 #13: phải tách `??` (thật) với `M` (sinh lại).

**Đối chiếu delta nội dung** (`find … -newer` cho 309 tệp, `git status` chỉ 17 `??` ⇒ 292 là sinh lại — xác nhận lại lần thứ 3):

| Khoảng thời gian | Nội dung |
|---|---|
| `e05f00ab` → `3b891e34` (10 ngày đóng băng) | **+80 tệp mới**: 24 concept + 10 source + 26 report + 10 topic + 10 raw; **−1**: `wiki/topic/brain-threat-detection.md` |
| `3b891e34` → `68f644e7` | **0 thay đổi nội dung** (commit này chỉ đụng `.gitignore` + agent home + `DREAMS.md`) |
| `68f644e7` → nay (24h) | +3 topic (`??`), +2 report validator |

---

## 🔴 E10 — `wiki/topic/brain-threat-detection.md` bị xoá — ✅ **ĐÓNG** (đã commit việc xoá)

**Severity:** ERROR → **RESOLVED** · **Category:** Orphan

`test -e` ⇒ **ABSENT**; `git ls-files -s` ⇒ **rỗng** (không còn tracked); `git log --oneline` cho file này cho thấy `3b891e34` — tức **việc prune đã được commit vào lịch sử**. 10-03 ghi *"trên GitHub file vẫn còn"*; hôm nay GitHub **không còn** ⇒ cửa sổ phục hồi **đã đóng**. Đây là thay đổi do commit đóng băng, không phải do lượt này.

---

## 🔴 E11 — `DREAMS.md` — **đã có `.gitignore` + gỡ khỏi tracking** nhưng writer vẫn chạy (MÁY ERROR 1/4)

**Severity:** ERROR → WARNING · **Category:** Path

**16.980 B** trên đĩa (10-03: 16.216 B → **+764**), mtime **2026-10-04 03:00:14** ⇒ writer vẫn chạy **đúng 03:00 mỗi đêm**, nay là **20,6 giờ** kể từ lần ghi gần nhất. `git ls-files -s DREAMS.md` = **rỗng** ✅ (untracked); `check-ignore --no-index` ⇒ **`.gitignore:82 /DREAMS.md`** ✅. `git ls-tree HEAD DREAMS.md` = **ABSENT** ⇒ **không còn 9 ngày chênh lệch chưa commit** như 10-03.

**Vì sao hạ từ ERROR xuống WARNING:** không còn rủi ro lộ nội dung lên GitHub. **Nhưng dữ liệu vẫn mất** — 13 commit cũ chứa bản sao, bản mới nhất không được đồng bộ, và file **không thuộc KB** nên không có chỗ đúng để lưu.

**Suggested fix:** giữ dữ liệu, sửa **writer output path** (đưa vào `.openclaw/dreams/`). Xoá file không dừng được writer — E11 đã 10 lượt.

---

## 🔴 E12 — `memory/` — **lượt thứ 14 liên tiếp** (MÁY ERROR 2/4)

**Severity:** ERROR · **Category:** Orphan

**106 tệp, 7 thư mục** (tính cả thư mục gốc), **148 KB**. Chuỗi tệp: …97 → 101 → **106**. `check-ignore --no-index` ⇒ **IGNORED** (`.gitignore:84 memory/`), `git ls-files -s memory/` = **0** ⇒ **đã an toàn cho git**. Vẫn là ERROR vì **root folder không có trong whitelist §2** và đang phình đều.

---

## 🔴 E13 — `wiki/HEARTBEAT.md` dangling — **ngày thứ 8** (MÁY ERROR 3/4)

**Severity:** ERROR · **Category:** Orphan

Xác minh bằng `realpath` + `exists` + `lexists` (bài học 09-28 #10 — không mắt bằng đường dẫn tương đối): `islink=True`, `lexists=True`, target `../../.openclaw/HEARTBEAT.md`, `realpath` = **`/home/julius/.openclaw/HEARTBEAT.md`**, `exists` = **False** ⇒ **DANGLING**, sai một cấp thư mục (đúng phải là `../.openclaw/HEARTBEAT.md`). mtime **2026-08-26 17:01** — không đổi, tức đây là symlink **cũ**, mirror từ 08-26 chứ không phải tái tạo mới.

Đã kiểm **cả 4 symlink ở root**: `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` → `realpath` tới `<KB>/.openclaw/…`, `exists=True` ⇒ **hợp lệ**. `HEARTBEAT.md` ở root **vắng mặt** (tuỳ chọn theo §2, không tính lỗi).

---

## 🔴 E14 — 38 tệp runtime/bí-mật **vẫn tracked** trong agent home (ERROR thật, không group riêng ở 10-03)

**Severity:** ERROR · **Category:** Path

Commit hôm nay gỡ 284 path nhưng **còn sót 38 tệp có rule ignore đã tồn tại** (rule thêm sau commit ⇒ vô hiệu):

| Nhóm | Tệp | Vị trí |
|---|---|---|
| `config.yaml.bak.*` | 18 | `.hermes/` |
| `kanban.db` + `-shm` + `-wal` + `.dispatch.lock` + `.init.lock` | 5 | `.hermes/` |
| `skills/.curator_backups/` (5 mốc × 3 tệp) | 15 | `.hermes/skills/` |
| `MEMORY.md` | 1 | `.hermes/` (172 commit — **nguồn `.gitignore:110 MEMORY.md` khớp nhầm file này**) |

**Đây là phần còn lại của E3** — tôi tách thành nhóm riêng vì đây là **toàn bộ mức độ phơi bày thực tế** sau khi các mẫu lớn đã đóng, và con số "38 tệp" là thứ cần hành động, không phải "4 mẫu còn lộ".

**Suggested fix:** `git rm -r --cached` đúng 38 path này rồi commit. **Một lệnh, không cần `.gitignore` mới.**

---

## ⚠️ W1 — 106 WARNING kỹ thuật dưới `memory/` — hệ quả trực tiếp của E12

**Severity:** WARNING · **Category:** Path

Bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào (10-03: 101 ⇒ nay **106**). **Toàn bộ là hệ quả của E12, không phải 106 vấn đề độc lập.**

---

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive — UNCHANGED

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` · **Severity:** WARNING

**15 tệp, không đổi** (so 09-17 → 10-04). Tổng archive: **177 tệp**. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.

**Suggested fix:** Julius chốt chính sách (giữ / chuyển / cho phép ngoại lệ §7). Validator **không** tự đổi tên bản sao thành báo cáo.

---

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7 + §6/§7/§3-§4 tự mâu thuẫn — UNCHANGED

**Severity:** WARNING

(a) Bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`/`format`/`hygiene`. Chỉ tồn tại `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md` — **tồn đọng, không phải phát hiện mới**.

(b) §6 cho phép `raw.md` rồi ghi `*` ✗ forbidden; §7 cho phép `wiki.md` (dòng 169 ✓ required) rồi ghi *"No files at `wiki/` root level"*; §4 hạn chế nội bộ skills trong khi §3 cho phép runtime tự do. **Đã kiểm lại theo bài học 10-02 #22:** `wiki/wiki.md` và `raw/raw.md` đều được whitelist ⇒ bộ quét phải `continue` trước khi báo orphan gốc. Hôm nay bộ quét **không** báo nhầm 2 tệp này.

(c) **Mới:** §6 liệt kê **đúng 6** subfolder; máy thật có **6** (`articles, papers, posts, repos, videos, websites`) ⇒ khớp. Nhưng `raw/raw.md:23` vẫn treo `[[tools]]` **không resolve** (`raw/tools/` không tồn tại) — sub-index mồ côi mà Output Validator 10-04 đã báo, ghi nhận lại ở đây vì nó thuộc tầng cấu trúc.

---

## ⚠️ W4 — [SYSTEMATIC VIOLATION] carry-forward: cặp topic trùng nghĩa `cuoc-dua-khong-di-lui.md` / `cuoc-dua-khong-i-lui.md` — **tái tạo lại lần thứ 5**

**Severity:** WARNING · **Category:** Naming

| Tệp | Cỡ | mtime |
|---|---|---|
| `wiki/topic/cuoc-dua-khong-di-lui.md` | **411 B** | 2026-10-04 21:04 |
| `wiki/topic/cuoc-dua-khong-i-lui.md` | **440 B** | 2026-10-04 21:04 |

**Đã tái tạo lại lần thứ 5** (09-30 → 10-01 → 10-02 → 10-03 → **10-04**), cùng Index Agent lượt **21:04**, hai file cùng mtime. Cả hai **đã tracked** ⇒ mỗi lượt Index Agent chạy là một commit chứa cả hai bản trùng nghĩa.

**Carry-forward, KHÔNG re-escalate mới** (quy tắc carry-forward 09-01) — đây là lần escalate thứ 3, đã đủ bằng chứng.

**Root-cause:** Index Agent tạo topic từ nhãn chưa canonical hoá ⇒ cùng một cụm tiếng Việt sinh 2 slug khác nhau. **Tái tạo 5 lượt liên tiếp ⇒ sửa tay không giữ được.**

**Suggested fix:** Index Agent SKILL.md — bỏ dấu + gộp `đ`→`d` **trước** khi tạo topic; gộp 2 file thành 1. Validator **không** tự gộp.

---

## ⚠️ W5 — Quy tắc miễn kiểm tra agent home che mất **6 nhóm ERROR**

**Severity:** WARNING · **Category:** Path

Bộ quét hôm nay báo **4 ERROR máy** (4 path unique: `wiki/HEARTBEAT.md`, `DREAMS.md`, `memory/`, marker root). Kiểm tay bằng `git ls-files` / `check-ignore --no-index` / `find` cho thấy **10 nhóm thực tế**, trong đó **6 nhóm không có path nào ở tầng quét** (E1, E3, E4, E5, E6, E8, E14). Nguyên nhân vẫn là quy tắc §3 *"bỏ qua `.hermes/`/`.openclaw/` sâu > 1"*.

**Đây là lỗi của bộ quét, không phải của KB.** Nói rõ để không tính nhầm thành phát hiện KB mới.

**Suggested fix:** nới quy tắc sang *"quét mọi thư mục lồn + mọi tệp có khả năng chứa bí mật/khối lượng lớn"* (`*auth*`, `*.db*`, `*.bak*`, `config.*`, `HEAD`, `.git`) **bất kể độ sâu**; dùng `git ls-files -s` + `check-ignore --no-index` cho từng hit.

---

## ⚠️ INFO I1 — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/` · **Severity:** INFO

**123 tệp `.md`** ở tầng active **lúc quét** (10-03: 120 → +3 = 1 report Format + 1 report Output + 1 report Hygiene hôm nay) → **124 post-write** (báo cáo này nằm trong `wiki/reviews/`); **38 tệp mtime cũ hơn 2026-09-01**, sớm nhất `2026-06-01_output-report.md`. `wiki/drafts/` = 1 tệp. Số lượng phụ thuộc trạng thái approved/applied nên không dùng một số chưa đối chiếu làm quyết định.

---

## ⚠️ INFO I2 — `.hermes/lsp/` — **đã untracked hoàn toàn**; `node_modules` được ignore đúng

**Path:** `.hermes/lsp/` · **Severity:** INFO

10-03 ghi 4 tệp đã tracked (`bin/bash-language-server` symlink, `bin/pyright-langserver` symlink, `package.json`, `package-lock.json`). Hôm nay `git ls-files .hermes/lsp` = **0** ⇒ **cả 4 đã được gỡ khỏi tracking** bởi commit `68f644e7` (rule `.gitignore:63`). Trên đĩa `node_modules/` vẫn có **7.101 tệp** và **ĐÃ được ignore đúng** (`check-ignore --no-index` ⇒ `.gitignore:63`) — **không phải rò rỉ, không phải KB growth**. Giữ ở INFO vì phần đĩa vẫn là 7K tệp không cần thiết.

---

## 📐 ĐỊNH NGHĨA ĐẾM — đọc trước bảng delta

Báo cáo này công bố **hai loại số khác nhau về bản chất** và phải tách rõ, nếu không sẽ tạo ra *"tăng trưởng KB"* giả:

| Loại số | Giá trị | Định nghĩa |
|---|---|---|
| **Tệp ổn định trong phạm vi** | **1.697 → 1.698 post-write** | 4 vùng nội dung đệ quy (`raw` 229 + `wiki` 1.450 + `context` 2 + `scripts` 5 = **1.686**) + 11 tệp/symlink root. Đếm bằng `S_ISREG ∪ S_ISLNK` — **không** phải *"không phải thư mục"* (bẫy socket, pitfall #18). Lấy mẫu **3×/9s**: ổn định tuyệt đối. **Đây là con số duy nhất nên so với lượt trước.** |
| **Tệp tầng đầu agent home** | **98 (76+22)** | L1 của `.hermes/` + `.openclaw/`. **BIẾN ĐỘNG** theo pitfall #18 — 10-03 đo 99 (77+22), nay 98 (76+22). Không so được, không phải KB tăng/giảm. |
| **Thư mục** | **74** | 9 root (`.hermes, .openclaw, .obsidian, context, memory, raw, scripts, wiki` + `.`) + 23 vùng nội dung (**bao gồm thư mục gốc vùng** — `os.walk` bỏ sót, pitfall #21) + 42 L1 agent home (27 `.hermes` + 15 `.openclaw`). |
| **Quét máy (KHÔNG phải phạm vi)** | **243.362** | `find . -type d -name .git -prune -o \( -type f -o -type l \) -print` — prune **mọi** thư mục `.git` ở mọi độ sâu. `.hermes/` chiếm **243.314 / 99,99%**, trong đó 225.530 là bản cài lồng (E1). |

### ⚠️ Vì sao "quét máy" phải nêu định nghĩa prune (bài học 10-02 #20)

Cùng một cây, ba cách prune cho ba con số khác nhau — **tất cả đều đúng theo định nghĩa của nó**:

| Cách prune | Kết quả | Chênh |
|---|---|---|
| Prune mọi `.git` ở mọi độ sâu | **243.362** | (định nghĩa công bố hôm nay) |
| Prune `.git` gốc **+ bản cài lồng** (`-name hermes-agent -prune`) | **19.884** | −223.478 |
| Chỉ prune `.git` gốc, **giữ** `.git` của repo lồng | 245.436 | +2.074 (đúng bằng 2.074 tệp trong `.hermes/hermes-agent/.git`) |

Chênh lớn nhất **không phải 2.074** mà là **223.478 tệp cài đặt** — đây là lý do phải công bố kèm định nghĩa. Số 10-03 công bố **242.766** khớp định nghĩa thứ nhất; **+596** hôm nay là drift thật của cây lồng (không phải KB). Số 10-02 (**243.267**) khớp **không** định nghĩa nào ⇒ lỗi công bố của 10-02.

**Đã xác minh PASS:** 15/15 index bắt buộc tồn tại (`req_missing=[]`); 4/4 symlink định danh root có đích thật; 0 thư mục rỗng; **0 lỗi naming/path trong 1.686 tệp vùng nội dung**; 0 trùng slug chuẩn hoá **trong cùng vùng**; `raw/` có đúng 6 subfolder theo §6.

---

## ⚠️ Hai lỗi trong bộ quét của chính lượt này — đã phát hiện và đã sửa logic, ghi lại để lượt sau không lặp

Theo bài học 09-30 #17 (grep artifact trước, rồi mới kết luận bên nào sai):

1. **False positive trên `raw/repos/2026-08-30_tt-a1i_archify.md`.** Regex `RE_RAW_REPOS` dùng `[a-z0-9]+` cho owner ⇒ owner `tt-a1i` có dấu `-` **không khớp**, dù §6 chỉ yêu cầu 2 segment và slug rule cho phép `-`. Đã thử lại với `[a-z0-9][a-z0-9-]*`: **7/8 file hợp lệ, 0 vi phạm**. ⇒ **không có** WARNING naming nào trong `raw/repos/`. Lỗi script, không phải lỗi KB.
2. **`checkpoints` bị gọi nhầm là "repo git lồng"** — xem E5. Không phải lỗi script lượt này (lượt này đã kiểm đúng) mà là **lỗi phân loại đã được sửa trong báo cáo này**.

---

## Delta so với 10-03

| Hạng mục | 10-03 | 10-04 | Kết luận |
|---|---|---|---|
| **Tệp ổn định trong phạm vi** | 1.680 | **1.697** | **+17** = 8 concept + 3 source (biên soạch 08:05) + 3 topic + 2 report validator + 1 `wiki.md` đổi… thực tế `e05f00ab`→`3b891e34` đóng băng **+80 tệp nội dung**, `3b891e34`→nay **+5**. Không phải KB dày thêm đột biến. |
| Số quét máy | 242.766 | **243.362** | +596 — drift của cây lồng trong `.hermes/hermes-agent/`, **không phải** KB |
| Machine findings | 120 (4E+116W) | **7 (4E+1W)** | ERROR 4→4 (cùng 4 path máy); WARNING 116→**1** vì `memory/` nay đã **ignored + untracked** nên bộ quét không còn rơi vào `classify_generic_path()` |
| **Nhóm ERROR** | 13 | **10** | **0 ERROR mới, 9 nhóm đã đóng** |
| `vault backup` | dừng 9,11 ngày | **hoạt động (0 ngày)** | ✅ HEAD `68f644e7` == remote `master`; 2 commit thủ công 19:14 + 19:41 |
| Tệp `??` chờ commit | 8.496 | **17** | −8.479: backup chạy + `.gitignore` chặn agent home |
| Runtime còn tracked trong agent home | ~305 | **38** | −267. Còn lại: `config.yaml.bak*` 18 + kanban 5 + skills curator 15 |
| `DREAMS.md` | 16.216 B, 9 ngày chưa commit | **16.980 B, untracked + ignored** | +764; **không còn chênh lệch chưa commit**; writer vẫn chạy 03:00 |
| `memory/` | 101 tệp / 7 thư mục | **106 tệp / 7 thư mục** | +5 tệp thật; **lượt thứ 14** |
| Marker `.migrated.*` | 2 (25 ngày) | **2 (26 ngày)** | UNCHANGED, **vẫn không có rule** |
| `wiki/HEARTBEAT.md` | dangling | **dangling** | UNCHANGED ngày thứ 8, mtime 08-26 17:01 |
| Tệp bị xoá (tracked) | 8 (1 `wiki/topic/`) | **7 (0 vùng nội dung)** | ✅ `brain-threat-detection.md` đã commit việc xoá |
| Cặp topic trùng nghĩa | 1 cặp (lần 4) | **1 cặp (lần 5)** | W4, cùng mtime 21:04, cả hai đã tracked |
| Archive backups | 15 | 15 | UNCHANGED |
| Bản cài Hermes lồng | 225.530 tệp / gitlink CÓ | **225.530 tệp / gitlink KHÔNG** | ✅ phần git đóng; 5,5 GB đĩa còn nguyên |
| Tệp tên auth tracked | 7 | **4** | ✅ `.hermes/auth.json` + `auth.lock` + state-snapshots đã đóng |

---

## Actions Needed

1. **🟢 Đóng dòng E2 (backup cron) + E8 + E10 + 9/13 mẫu E3.** Backup đã chạy lại; `config.yaml` đã untracked; `brain-threat-detection.md` đã commit việc prune. Nhờ 2 commit 19:14/19:41 — **nguyên nhân chính đã xử lý đúng**.
2. **🔴 E14 — `git rm -r --cached` đúng 38 tệp agent home** (18 `config.yaml.bak.*` + 5 `kanban.db*` + 15 `skills/.curator_backups/` + 1 `MEMORY.md`). **Một lệch duy nhất, không cần `.gitignore` mới.** 3/4 nhóm đã có rule nhưng rule vô hiệu vì tệp commit trước rule.
3. **🔴 E4 — kiểm secret trước (không cần chờ duyệt).** Còn 4 tệp tên auth trong `.openclaw/`, **đã trên GitHub 145 ngày** (`8695083b`, 2026-05-12). Repo public ⇒ **rotate token trước mọi việc git**. `git-secret-cleanup` có sẵn.
4. **🔴 E7 — thêm wildcard `*.migrated.*` + `git rm --cached` 2 marker.** Đây là chỗ **duy nhất** trong E1–E7 mà commit dọn hôm nay bỏ sót ⇒ 2 marker vẫn được backup mỗi lượt.
5. **🔴 E1 — xác định cơ chế cài đặt.** 5,5 GB đĩa vẫn còn, git đã sạch. Nếu Hermes tự cài lại vào CWD thì quay lại — nhưng lần này **không lên GitHub**. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó** (đây là CWD của tiến trình đang viết báo cáo này).
6. **🔴 E12 — `memory/` lượt thứ 14.** 106 tệp, đã ignored+untracked nhưng vẫn ở root ngoài whitelist. Cần writer sửa output path (`.openclaw/memory/`), **không** xoá tay.
7. **🔴 E11 — `DREAMS.md`.** Đã ignored, nhưng writer vẫn ghi 03:00 mỗi đêm và dữ liệu **không được đồng bộ**. Cần đổi writer path sang `.openclaw/dreams/`.
8. **🔴 E13 — `wiki/HEARTBEAT.md` dangling, ngày thứ 8.** Sửa target thành `../.openclaw/HEARTBEAT.md` (thiếu một cấp). Symlink cũ từ 08-26, không phải tái tạo mới.
9. **🟡 E2 — xác nhận máy chính push đúng nhánh.** Remote default branch vẫn là `main` (`ead50c82`, bỏ rơi từ 2026-05-11) trong khi HEAD local theo `master`.
10. **🟡 W4 — Index Agent canonical hoá slug trước khi tạo topic.** Cặp `cuoc-dua-khong-{di,i}-lui` đã tái tạo **5 lượt liên tiếp** và **cả hai đã tracked** ⇒ sửa tay không giữ được, phải sửa SKILL.md; gộp 2 file thành 1.
11. **🟡 W5 — nới quy tắc miễn kiểm tra agent home trong bộ quét** (đang che 6 nhóm ERROR). Validator tự sửa skill, không đụng `wiki/`.
12. **🟡 Chốt chính sách 15 archive backup + loại `spot-check` + `raw/raw.md:23` treo `[[tools]]`**, và **thống nhất §6/§7/§3-§4** (W3).

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*