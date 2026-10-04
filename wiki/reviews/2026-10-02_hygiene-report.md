# Hygiene Inspection — 2026-10-02
- **Status:** APPLIED — Fix Agent (Kara AX400, OpenClaw main) xử lúc 2026-10-03 09:27 +07:00. Đã sửa 4 file: ai-lab-business-model.md (stub bullet + bỏ quotes 3 body wikilink + merge 3 bullet Google → 2 + dịch 4 cụm English lẫn), harness-engineering.md (bỏ quotes 3 body wikilink), ai-evals.md (bỏ .md khỏi 4 wikilink), raw/articles/articles.md (159/0, stale sau compile 08:08). Verify: validate.py 1138 files, ERROR 0, WARNING 402. Issue 1 nói target ai-capex-as-credit-cycle không tồn tại — SAI, file có thật (compile 09-30); stub bullet vẫn là defect thật. Chưa xử: Issue 5 Defect B (cần chốt mức trùng lặp), Issue 4 (2 forward-ref raw=0), Issue 3 tồn dư 19 file + 78/82 wikilink .md. Chi tiết: .openclaw/MEMORY.md 2026-10-03.
**Issues found:** 13 nhóm (5 ERROR, 4 WARNING, 2 INFO) — gồm 5 ERROR máy + 8 ERROR nhóm dò tay trong agent home (bộ quét không thấy, xem W5)
**Created:** 2026-10-02 23:31 +0700
**Validator:** hygiene-inspector
**Paths checked:** **243.267 tệp quét máy** (`find . -path ./.git -prune -o \( -type f -o -type l \) -print`) — ⚠️ **KHÔNG phải phạm vi KB; 99,2% là agent home** (`.hermes/` = 241.182, trong đó 225.529 là bản cài lồng E1). Phạm vi KB đúng = **1.669 tệp ổn định** (1.658 vùng nội dung + 11 root) + **tệp tầng đầu agent home BIẾN ĐỘNG (99 lúc quét → 96–98 lúc verify)** + **74 thư mục** (9 root + 23 vùng nội dung gồm thư mục gốc vùng + 42 L1 agent home).
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## 🔴 E1 — ERROR MỚI, LỚN NHẤT TỪNG THẤY: **toàn bộ bản cài Hermes Agent nằm bên trong KB** — 225.529 tệp / 5,5 GB / repo git lồng

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

Đây là nguyên nhân của toàn bộ phép đo rác hôm nay. Không phải KB "phình to" — mà là **một repo git lồng đặt sai chỗ**.

| Bằng chứng | Kết quả |
|---|---|
| `find .hermes/hermes-agent \( -type f -o -type l \)` | **225.529 tệp** (10-01: 225.528) |
| `du -sh` | **5,5 GB** |
| `test -e .hermes/hermes-agent/.git` | **CÓ — repo git lồng** (riêng `.git` = 2.074 tệp / 1,6 GB) |
| `git -C … rev-parse --abbrev-ref HEAD` | `main` |
| HEAD của repo lồng | `990473a79c` |
| `git ls-tree HEAD -- .hermes/hermes-agent` | **`160000 commit 990473a79c…`** — **gitlink/submodule** |
| `.gitmodules` | **KHÔNG TỒN TẠI** ⇒ `git submodule` không hoạt động |
| `grep -c 'hermes-agent' .gitignore` | **0 — không có rule nào** |
| `git -C … status --porcelain` | `DU apps/desktop/electron/main.cjs`, `UU package-lock.json`, `?? wiki/` |

**Ba trạng thái phải báo riêng** (bài học 09-30 #19): nested `.git` **CÓ** · gitlink mode `160000` **CÓ** · `.gitmodules` **KHÔNG**. Thiếu trạng thái thứ ba là lý do "225K tệp" chưa bao giờ hiện như một rò rỉ.

**Vì sao 22 ngày chưa ai báo:** gitlink là **một dòng** trong cây KB nên `git ls-files -s` trả về đúng 1 dòng; còn quy tắc "bỏ qua agent home ở độ sâu > 1" chặn phần còn lại. Mọi probe lượt trước đều trả về sạch.

**Hậu quả (theo thứ tự nghiêm trọng):**
1. **5,5 GB / 225.529 tệp cho một KB vốn ~1,7K tệp.** Mọi lượt quét full-tree, backup, `git status` đều phải đi qua nó.
2. Repo lồng **chưa khai báo** ⇒ clone trên máy khác tạo thư mục rỗng, `git submodule update` lỗi.
3. Repo lồng **đang bẩn** (`DU`/`UU` = conflict chưa giải quyết).
4. **Nguy cơ mất CWD của agent:** Hermes đang chạy code từ đây; `git checkout`/`pull` trong KB khi gitlink trỏ commit không có trên remote ⇒ mất thư mục làm việc.

**Suggested fix (Fix Agent, sau khi Julius duyệt — thứ tự bắt buộc):**
1. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó.** Đây là CWD của tiến trình đang viết báo cáo này.
2. Xác định **cơ chế cài đặt** (bootstrap script / `pip`/`uv` target / sync từ repo nguồn) — đó mới là chỗ cần sửa để nó không quay lại.
3. Chọn: (a) **hợp lệ hoá** — khai báo đúng `.gitmodules` + đẩy repo lồng lên remote riêng; hoặc (b) **chuyển ra ngoài KB** (`~/.hermes/hermes-agent/`) rồi sửa launcher.
4. Thêm rule `.hermes/hermes-agent/` vào `.gitignore` **và** `git rm --cached` (bỏ gitlink) — giữ gitlink nếu chọn (a), bỏ hẳn nếu chọn (b).
5. Sau khi xử lý: quét máy phải về ~2K, không phải 243K.

---

## 🔴 E2 — `vault backup` dừng **8,11 ngày** — CARRY-FORWARD, ngày thứ 9

**Severity:** ERROR · **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08` |
| `git ls-remote --heads origin` (23:31 hôm nay) | `refs/heads/master = e05f00abf29e84c8…` — **remote cũng đứng ở đây** |
| Thời gian | **8,11 ngày** (09-24 20:51 → 10-02 23:31) |
| Nhánh mồi | `origin/main = ead50c82` — nhánh bị bỏ rơi từ 2026-05-11, không phải đích sync |

Đã kiểm remote **trước khi** kết luận máy này hỏng (bài học 09-28): remote cũng đứng ở `e05f00ab` ⇒ **lỗi tiến trình backup trên máy chính, không phải push trễ**.

**Trạng thái chờ:** `git status --porcelain -uall` = **6.926 `??` + 347 `M` + 8 `D` + 1 `R`**.

Phân bổ `??` (6.926): **6.783** `.hermes/checkpoints` · **79** `.hermes/.curator_backups` · **57** vùng nội dung (xem E9) · 10 `.hermes/skills`/runtime.

**Cổng cửa sổ vẫn đóng:** vì backup dừng, E3–E7 **chưa** bị commit thêm. Runtime đang chờ **6.862 tệp `??`**. Số này nhảy ngay khoảnh khắc backup chạy lại.

**Suggested fix (thứ tự bắt buộc):** (1) chặn `.gitignore` cho E3–E7 **trước**; (2) xử lý E8/E4 secret; (3) **rồi mới** khởi động lại backup. Validator không push, không commit.

---

## 🔴 E3 — 13 mẫu runtime trong agent home đã tracked, **11 mẫu không có rule** — CARRY-FORWARD

**Severity:** ERROR · **Category:** Path

Đã lặp lại đúng probe hôm nay (`git ls-files -s` + `git check-ignore --no-index -v` — bài học 09-30 #14: `check-ignore` dạng thường **bỏ qua tệp đã tracked**, nên phải cả hai):

| Mẫu | Tracked | Commit | Rule `--no-index` |
|---|---|---|---|
| `.hermes/kanban.db` | 1 | 3 | **NONE** |
| `.hermes/kanban.db-shm` | 1 | **141** | **NONE** |
| `.hermes/kanban.db-wal` | 1 | **141** | **NONE** |
| `.hermes/projects.db` | 1 | 1 | **NONE** |
| `.hermes/verification_evidence.db` | 1 | **345** | **NONE** |
| `.hermes/config.yaml.bak*` (18 tệp) | **18/18** | 11 | **NONE** |
| `.hermes/state-snapshots*` | 7 | 2 | **NONE** |
| `.hermes/checkpoints*` (repo lồng) | **31** | 9 | **NONE** |
| `.hermes/.curator_backups*` | **230** | 16 | **NONE** |
| `.hermes/skills/.curator_backups*` | 15 | 14 | **NONE** |
| `.hermes/config.yaml` | 1 | **50** | **NONE** |
| `.hermes/auth.json` | 1 | **78** | `:37` **có, vô hiệu** |
| `.hermes/MEMORY.md` | 1 | **172** | `:81` **có, vô hiệu** |

**Khoảng trống đối xứng vẫn đúng:** `.openclaw/*.bak` và `.hermes/state.db*` **có** rule ⇒ **vùng `.hermes/` không được bảo vệ.**

**WAL sidecar vẫn là mắt xích yếu:** `kanban.db-shm`/`-wal` = 141 commit **mỗi tệp**, chỉ vì hai tệp sidecar này.

**Suggested fix:** `.gitignore` theo **mẫu wildcard** cho toàn bộ runtime + `git rm -r --cached` một lượt. Gộp với E1.

---

## 🔴 E4 — 7 tệp tên auth đã tracked — CARRY-FORWARD, **không có file mới**

**Severity:** ERROR · **Category:** Path / Secret exposure

Probe theo **tên tệp** trên `git ls-tree -r HEAD`, lọc `skills/` — **7 credential thật**:

`.hermes/auth.json` (11.003 B, 78 commit) · `.hermes/auth.lock` · `.hermes/state-snapshots/20260626-005403-pre-update/auth.json` (8.201 B) · `.openclaw/device-auth.json` · `.openclaw/identity/device-auth.json` · `.openclaw/agents/main/agent/auth-profiles.json` · `.openclaw/agents/main/agent/auth-state.json`

Cả 7 nằm trong HEAD `e05f00ab` == remote `master` ⇒ **đã trên GitHub.**

**Giữ nguyên nguyên tắc:** chỉ grep **tên khoá**, không đọc **giá trị**. Báo cáo này **không** mở nội dung credential.

**Suggested fix (thứ tự):** (1) Julius kiểm visibility repo — public ⇒ **rotate token trước mọi việc git**; (2) `git rm --cached` cả 7 + commit; (3) rewrite lịch sử nếu token còn hiệu lực (`git-secret-cleanup`); (4) rotate ở provider sau khi rewrite.

---

## 🔴 E5 — `.hermes/checkpoints/` repo git lồng, 62 MB — CARRY-FORWARD, **số chờ đứng yên**

**Severity:** ERROR · **Category:** Orphan / repo hygiene

**31 tệp tracked**, `store/HEAD` tồn tại, **6.814 tệp trên đĩa** (62 MB), `grep -c checkpoints .gitignore` = **0**. Trong đó **6.783 là `??` đang chờ commit**.

**Consequence:** vì backup dừng (E2), 6.783 tệp này **pending**. Bật backup mà chưa chặn `.gitignore` ⇒ commit kế tiếp nuốt **62 MB**.

---

## 🔴 E6 — `.hermes/.curator_backups/` — CARRY-FORWARD, **leo thang tiếp**

**Severity:** ERROR · **Category:** Orphan

Trên đĩa: **306 tệp** (`.hermes/.curator_backups/`) + 15 (`.hermes/skills/.curator_backups/`). Đã tracked: **245** (230 + 15). `??` chờ commit: **79** (10-01: 70). Không rule `.gitignore`. Chuỗi leo thang: 45 → 52 → 70 → **79**.

---

## 🔴 E7 — 2 marker `.migrated.*` — CARRY-FORWARD, **mtime đứng 24 ngày**

**Severity:** ERROR · **Category:** Path

| Vị trí | Cỡ | Disk | Rule |
|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3….e79d1c6c-…` (root) | 69 B | **2026-09-08 20:42** | **NONE** |
| `.openclaw/workspace-state.json.migrated.43c9aa3….fb077b94-…` | 69 B | **2026-09-08 20:42** | **NONE** |

Cùng blob `a0105ac6…`, **24 ngày không đổi**. Đã dò tay tree-wide `find . -name '*.migrated.*' -not -path './.git/*'` (bài học 09-25) ⇒ **đúng 2, không có biến thể thứ ba.**

**Suggested fix:** wildcard `*.migrated.*` + `git rm --cached` cả hai + commit.

---

## 🔴 E8 — `.hermes/config.yaml` git-tracked, 50 commit, có tên khoá `api_key` / `secret` / `session_key` — CARRY-FORWARD

**Severity:** ERROR · **Category:** Path / Secret exposure

23.603 B, **50 commit**, không rule nào khớp. Mỗi lần sửa config = một commit chứa lại toàn bộ nội dung. Validator cố tình **không** đọc giá trị.

---

## 🔴 E9 — 57 tệp nội dung `??` chưa commit; 321 tệp `M` do Index Agent viết lại

**Severity:** ERROR · **Category:** Orphan

Phân biệt bằng `git status --porcelain -uall` (bài học 09-28 — `find -newer` đếm cả tệp được sinh lại):

| Nhóm | Số | Ý nghĩa |
|---|---|---|
| `??` vùng nội dung | **57** | **thật** — 13 concept + 6 source + 9 topic + 7 raw + 22 report validator (09-25→10-02) |
| `M` vùng nội dung | **321** | **không phải KB dày thêm** — 292 tệp cùng mtime `2026-10-02 21:06` (Index Agent full rebuild: 267 topic + 25 tag) |
| `D` vùng nội dung | **1** | `wiki/topic/brain-threat-detection.md` — xem E10 |
| `R` (staged) | **1** | `src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md` → `…-curiosity-how-to-get-it-back.md` (Fix Agent 10-02, `R100`) |

`find raw wiki -newer <báo cáo 10-01>` trả **310** — con số này **gây ảo giác**: phần lớn là tệp bị viết lại, chỉ **57** là mới thật.

---

## 🔴 E10 — `wiki/topic/brain-threat-detection.md` bị xoá, **8 ngày chưa giải quyết** — CARRY-FORWARD

**Severity:** ERROR · **Category:** Orphan

`git status` ` D` = 8 tệp, **1 nằm trong vùng nội dung**: `wiki/topic/brain-threat-detection.md`. `test -e` ⇒ **ABSENT**. 7 tệp còn lại là `.hermes/skills/` runtime.

Đây là **mục tri thức thật** bị prune bởi Index Agent. Vì backup dừng (E2), **trên GitHub file vẫn còn** — nếu VPS hỏng thì mất thật.

**Suggested fix:** Julius xác nhận prune có chủ ý không. Nếu mất thật ⇒ phục hồi từ commit `52170426`.

---

## 🔴 E11 — `DREAMS.md` — **8 ngày dreaming chưa commit**, vẫn đang lớn

**Path:** `DREAMS.md` (root) · **Severity:** ERROR · **Category:** Path

File thường, **15.323 B** trên đĩa (10-01: 14.530 B → **+793**), git-tracked (`100644`), 12 commit, mtime **2026-10-02 03:00:16** — writer vẫn chạy đúng 03:00 mỗi đêm. `check-ignore --no-index` ⇒ **rc=1, không rule**. Blob trong HEAD = **8.932 B** ⇒ **6.391 B chênh lệch chưa lên GitHub = 8 ngày dreaming**.

**Suggested fix:** giữ dữ liệu, sửa writer/output path. Xoá file không giải quyết được (proven nhiều lần).

---

## 🔴 E12 — `memory/` — CARRY-FORWARD, **lượt thứ 12 liên tiếp**

**Severity:** ERROR · **Category:** Orphan

**97 tệp, 6 thư mục con**. Chuỗi: …76→81→85→89→93→**97**. Phân bố: `dreaming/{deep,light,rem}` + `.dreams/session-corpus` + 2 tệp gốc. `check-ignore --no-index` ⇒ **IGNORED** (`.gitignore:84 memory/`), `git ls-files -s memory/` = **0** ⇒ chưa lên GitHub.

**Ghi chú đếm:** 10-01 ghi "3 thư mục con", hôm nay đếm **6** (bao gồm 3 thư mục con *bên trong* `dreaming/`); 09-30 ghi "6". Cùng một cây, khác cách đếm — **không phải thư mục biến mất hay xuất hiện.** Số tệp **+4** là tăng thật.

---

## 🔴 E13 — `wiki/HEARTBEAT.md` dangling — CARRY-FORWARD, ngày thứ 6

**Path:** `wiki/HEARTBEAT.md` · **Severity:** ERROR · **Category:** Orphan

Xác minh bằng `realpath` + `exists` + `lexists` (bài học 09-28 #10 — không mắt bằng đường dẫn tương đối): `islink=True`, target `../../.openclaw/HEARTBEAT.md`, `realpath` = **`/home/julius/.openclaw/HEARTBEAT.md`**, `exists` = **False**, `lexists` = True ⇒ **DANGLING**, sai một cấp thư mục (đúng phải là `../.openclaw/HEARTBEAT.md`).

Đã kiểm **cả 4 symlink ở root**: `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` → `realpath` tới `<KB>/.openclaw/…`, `exists=True` ⇒ **hợp lệ**. `HEARTBEAT.md` ở root **vắng mặt** (tuỳ chọn theo §2, không tính lỗi).

---

## ⚠️ W1 — 97 WARNING kỹ thuật dưới `memory/` — hệ quả trực tiếp của E12

**Severity:** WARNING · **Category:** Path

Bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào. **Toàn bộ là hệ quả của E12, không phải 97 vấn đề độc lập.**

---

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive — UNCHANGED

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` · **Severity:** WARNING

**15 tệp, không đổi** (so 09-17→10-02). Tổng archive: **177 tệp**. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.

**Suggested fix:** Julius chốt chính sách (giữ / chuyển / cho phép ngoại lệ §7). Validator **không** tự đổi tên bản sao thành báo cáo.

---

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7 + §6/§7/§3-§4 tự mâu thuẫn — UNCHANGED

**Severity:** WARNING

(a) Bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`/`format`/`hygiene`. Chỉ tồn tại `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md` — **tồn đọng, không phải phát hiện mới**.

(b) §6 cho phép `raw.md` rồi ghi `*` ✗ forbidden; §7 cho phép `wiki.md` rồi ghi "No files at `wiki/` root level"; §4 hạn chế nội bộ skills trong khi §3 cho phép runtime tự do.

---

## ⚠️ W4 — [SYSTEMATIC VIOLATION] carry-forward: **cặp topic trùng nghĩa** `cuoc-dua-khong-di-lui.md` / `cuoc-dua-khong-i-lui.md` — **tái tạo lại lần thứ 3**

**Severity:** WARNING · **Category:** Naming

| Tệp | Cỡ | mtime |
|---|---|---|
| `wiki/topic/cuoc-dua-khong-di-lui.md` | **375 B** | 2026-10-02 21:06:08.467367865 |
| `wiki/topic/cuoc-dua-khong-i-lui.md` | **407 B** | 2026-10-02 21:06:08.467457232 |

**Đã tái tạo lại lần thứ 3** (09-30 → 10-01 → 10-02), cùng Index Agent lượt **21:06**, hai file cùng mtime chênh lẻ 90 µs. Cùng một chủ đề ("cuốc đua không đi lùi") bị tách làm hai file chỉ mục. Kiểm tra slug chuẩn hoá trên **11 vùng nội dung**: **0 trùng chính xác trong cùng vùng**.

**Đây là lần escalate thứ 2 — carry-forward, KHÔNG re-escalate mới** (quy tắc carry-forward).

**Root-cause:** Index Agent tạo topic từ nhãn chưa canonical hoá ⇒ cùng một cụm tiếng Việt sinh 2 slug khác nhau. **Bằng chứng đã đủ mạnh để kết luận: tái tạo 3 lượt liên tiếp, mỗi lượt một lần Index Agent chạy ⇒ sửa tay không giữ được.**

**Suggested fix:** Index Agent SKILL.md — bỏ dấu + gộp `đ`→`d`, `i`→`i` **trước** khi tạo topic; gộp 2 file thành 1. Validator **không** tự gộp.

---

## ⚠️ W5 — Quy tắc miễn kiểm tra agent home che mất **8 nhóm ERROR** (leo thang lên 13)

**Severity:** WARNING · **Category:** Path

Bộ quét hôm nay báo **5 ERROR** (4 path unique). Kiểm tay bằng `git ls-tree`/`ls-files`/`find` cho thấy **13 nhóm thực tế** (E1, E3–E13). Nguyên nhân vẫn là quy tắc §3 "bỏ qua `.hermes/`/`.openclaw/` sâu > 1".

**Đây là lỗi của bộ quét, không phải của KB.** Nói rõ để không tính nhầm thành phát hiện KB mới.

**Suggested fix:** nới quy tắc sang "quét mọi thư mục lồn + mọi tệp có khả năng chứa bí mật/khối lượng lớn" (`*auth*`, `*.json`, `*.db*`, `*.bak*`, `*.pack`, `config.*`, `*.env`, `HEAD`, `.git`) **bất kể độ sâu**; dùng `git ls-files -s` + `check-ignore --no-index` cho từng hit.

---

## ⚠️ INFO I1 — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/` · **Severity:** INFO

**117 tệp `.md`** ở tầng active (10-01: 114 → +3 = 1 report hygiene 10-01 + 2 report validator hôm nay); **38 tệp mtime cũ hơn 2026-09-01**, sớm nhất `2026-06-01_output-report.md`. `wiki/drafts/` = 1 tệp. Số lượng phụ thuộc trạng thái approved/applied nên không dùng một số chưa đối chiếu làm quyết định.

---

## ⚠️ INFO I2 — `.hermes/lsp/` đã tracked 4 tệp; `node_modules` **được ignore đúng**

**Path:** `.hermes/lsp/` · **Severity:** INFO

4 tệp đã tracked: `bin/bash-language-server` (**symlink**), `bin/pyright-langserver` (**symlink**), `package.json`, `package-lock.json`. Không có rule riêng cho `.hermes/lsp/`.

**Đính chính so với ảo giác dễ có:** `node_modules/` bên trong nó có **7.105 tệp / 55 MB** nhưng **ĐÃ được ignore đúng** — `.gitignore:33 node_modules/`, `check-ignore --no-index` rc=0, `git status --porcelain --ignored` xếp `!!`. **Không phải rò rỉ, không phải KB growth.** Trên đĩa tổng 7.105 tệp, trong git chỉ 4.

---

## 📐 ĐỊNH NGHĨA ĐẾM — đọc trước bảng delta

Báo cáo này công bố **hai loại số khác nhau về bản chất** và phải tách rõ, nếu không sẽ tạo ra "tăng trưởng KB" giả:

| Loại số | Giá trị | Định nghĩa |
|---|---|---|
| **Số quét máy** | **243.267** | `find . -path ./.git -prune -o \( -type f -o -type l \) -print` — **không phải phạm vi kiểm tra**. 99,2% là `.hermes/` (241.182), trong đó 225.529 là bản cài lồng (E1). |
| **Tệp ổn định trong phạm vi** | **1.669** | 4 vùng nội dung (`raw` 226 + `wiki` 1.425 + `context` 2 + `scripts` 5 = 1.658) + 11 tệp/symlink root. **Đây là con số duy nhất nên so với lượt trước.** |
| **Tệp tầng đầu agent home** | **99 → 96–98** | Lấy mẫu 5×/16 giây lúc quét: đều 99. Lúc verify lại dao động **99 → 96 → 98**. **BIẾN ĐỘNG theo đúng pitfall #18** — runtime ghi lại `state.db*`, `kanban.db-shm/-wal`, `verification_evidence.db` (mtime 23:57–00:00). Socket đã loại (`find -type f -o -type l`, không phải "không phải thư mục"). **Đây không phải KB tăng/giảm và không phải issue nào được giải quyết.** |
| **Thư mục** | **74** | 9 root + 23 vùng nội dung (**bao gồm chính thư mục gốc vùng**) + 42 L1 agent home (27 `.hermes` + 15 `.openclaw`). |

### ⚠️ Đính chính: số 241.162 của báo cáo 10-01 **không tái lập được**

10-01 công bố "241.162 đường dẫn quét máy". Hôm nay đo lại cùng định nghĩa (`-type f -o -type l`, `.git` đã prune) cho **243.267**. Chênh **+2.105**, và **không tập hợp con nào** trong cây hôm nay cho ra 241.162 (`.hermes/` = 241.182 là số gần nhất, lệch 20; cộng `raw`+`wiki`+`context`+`scripts`+root = 242.840).

Theo quy tắc 09-28 #12 và 09-30 #17 — **grep artifact trước, rồi mới kết luận ai sai**: đây là **lỗi công bố của báo cáo 10-01** (định nghĩa đếm không được nêu đủ để tái lập), **không phải** KB tăng trưởng. Hôm nay công bố định nghĩa tường minh ở bảng trên để lượt sau tái lập được.

**Đã xác minh PASS:** 15/15 index bắt buộc tồn tại (`req_missing=[]`); 4/4 symlink định danh root có đích thật; 0 thư mục rỗng; **0 lỗi naming/path trong 1.658 tệp vùng nội dung**; 0 trùng slug chuẩn hoá **trong cùng vùng** (`collisions={}`); `.hermes/.env` được ignore đúng.

**Ghi chú phương pháp:** lượt này bộ quét báo nhầm `wiki/wiki.md` là "file ở root `wiki/`" — sai, §7 dòng 169 whitelist nó là index bắt buộc. Đã sửa quy tắc trong bộ quét và quét lại. **Đây là lỗi script, không phải lỗi KB.**

---

## Delta so với 10-01

| Hạng mục | 10-01 | 10-02 | Kết luận |
|---|---|---|---|
| **Tệp ổn định trong phạm vi** | 1.655 | **1.669** | **+14** — quy hết cho 14 tệp nội dung `??` mới (10-01: 43 → 10-02: 57). Không phải KB dày thêm đột biến. |
| Số quét máy | 241.162 | **243.267** | **Không so được** — định nghĩa 10-01 không tái lập được (xem đính chính). `.hermes/` đứng yên 241.182 ở cả hai lượt. |
| Machine findings | 112 (4E+108W) | **102 (5E+97W)** | WARNING 108→97 = `memory/` 93→97 và bỏ false positive `wiki.md` |
| ERROR nhóm | 14 | **13** | **−1** (nhóm `wiki.md` của máy bị loại) — không có ERROR mới nào |
| **ERROR thực tế (dò tay)** | ≥9 | **13** | 5 máy + 8 nhóm agent home bị quy tắc miễn trừ che |
| `vault backup` | dừng 7,11 ngày | **dừng 8,11 ngày** | remote vẫn `e05f00ab`; 6.926 `??` + 347 `M` + 8 `D` + 1 `R` |
| Runtime chờ commit | 6.853 tệp | **6.862 tệp** | checkpoints 6.783 (đứng) + curator **79** (70→79) |
| `DREAMS.md` | 14.530 B | **15.323 B** | +793; blob HEAD 8.932 B ⇒ **8 ngày** chưa commit |
| `memory/` | 93 tệp / "3 thư mục" | **97 tệp / 6 thư mục** | +4 tệp thật; số thư mục khác cách đếm (đã đính chính); **lượt thứ 12** |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, **24 ngày** |
| `wiki/HEARTBEAT.md` | dangling | **dangling** | UNCHANGED, xác minh `realpath`+`exists`+`lexists` |
| Tệp bị xoá (tracked) | 8 (1 `wiki/topic/`) | **8 (1 `wiki/topic/`)** | `brain-threat-detection.md` — **8 ngày** chưa giải quyết |
| Cặp topic trùng nghĩa | 1 cặp | **1 cặp (tái tạo lần 3)** | W4, cùng mtime 21:06:08 |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 | 1 | UNCHANGED, tồn đọng |
| Bản cài Hermes lồng | 225.528 tệp | **225.529 tệp** | +1, UNCHANGED về bản chất |

---

## Actions Needed

1. **🔴 E1 — `.hermes/hermes-agent/` 5,5 GB trong KB.** Xác định cơ chế cài đặt rồi hợp lệ hoá (`.gitmodules` + remote riêng) **hoặc** chuyển ra `~/.hermes/`. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó** — đây là CWD của tiến trình đang viết báo cáo này. Nên làm **đầu tiên**: xoá 99,9% nhiễu khỏi mọi lượt quét sau.
2. **🔴 E2/E4 — kiểm secret ngay (không cần chờ duyệt).** Repo public hay private? Public ⇒ **rotate token trước mọi việc git**. 7 tệp tên auth đã tracked + `config.yaml` (50 commit). `git-secret-cleanup` có sẵn.
3. **🔴 Chặn `.gitignore` TRƯỚC khi bật lại backup.** 11/13 mẫu runtime chưa có rule (`checkpoints`, `curator_backups`, `state-snapshots`, `kanban.db*`, `projects.db`, `verification_evidence.db`, `config.yaml.bak*`, `.hermes/hermes-agent/`). Bật backup ngay lúc này ⇒ commit kế tiếp nuốt **6.862 tệp / 62 MB**.
4. **🔴 E10 — xác nhận `wiki/topic/brain-threat-detection.md` bị prune có chủ ý không.** 8 ngày chưa giải quyết. Trên GitHub file **vẫn còn** (backup dừng) — còn kịp phục hồi.
5. **🔴 E2 — `vault backup` dừng 8,11 ngày.** Remote cũng đứng ở `e05f00ab` ⇒ lỗi tiến trình backup trên máy chính, không phải push trễ.
6. **Sửa 3 writer** (`memory/` ×3 đường, `DREAMS.md`, mirror `wiki/HEARTBEAT.md`) trước, rồi mới migrate/dọn. Xoá file không dừng được writer — E12 đã 12 lượt, E13 6 lượt, E11 8 lượt.
7. **W4 — Index Agent canonical hoá slug trước khi tạo topic.** Cặp `cuoc-dua-khong-{di,i}-lui` đã tái tạo **3 lượt liên tiếp** — sửa tay không giữ được, phải sửa SKILL.md; gộp 2 file thành 1.
8. **W5 — nới quy tắc miễn kiểm tra agent home trong bộ quét** (đang che 225K tệp / 8 nhóm ERROR); validator tự sửa skill, không đụng `wiki/`.
9. **Chốt chính sách 15 archive backup + loại `spot-check`**, và **thống nhất §6/§7/§3-§4** (W3).

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*