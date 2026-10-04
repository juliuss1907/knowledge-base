# Hygiene Inspection — 2026-10-03

**Status:** approved — Julius duyệt hàng loạt 2026-10-03
**Issues found:** **20 nhóm** — 13 ERROR + 5 WARNING + 2 INFO (gồm 4 ERROR máy + 9 nhóm ERROR agent home bị quy tắc miễn trừ che, xem W5). **0 ERROR mới, 0 issue nào được giải quyết.**
**Created:** 2026-10-03 23:31 +0700
**Validator:** hygiene-inspector
**Paths checked:** **1.680 tệp ổn định trong phạmvi KB** (1.669 vùng nội dung + 11 tệp/symlink root) → **1.681 post-write** (báo cáo này nằm trong vùng nội dung) + **74 thư mục** (9 root + 23 vùng nội dung gồm thư mục gốc vùng + 42 L1 agent home) + **99 tệp tầng đầu agent home — BIẾN ĐỘNG** (77 `.hermes` + 22 `.openclaw`). Quét máy = **242.766** (định nghĩa: prune mọi thư mục `.git` ở mọi độ sâu) — ⚠️ **KHÔNG phải phạm vi kiểm tra**.
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

> **Đính chính header của báo cáo 10-02:** 10-02 ghi *"13 nhóm (5 ERROR, 4 WARNING, 2 INFO)"* — **tổng trong ngoặc bằng 11, không phải 13**. Thân báo cáo 10-02 có đúng **13 mục ERROR** (E1–E13). Đây là lỗi cộng số ở header 10-02, không phải lỗi nội dung. Lượt này công bố tách rõ từng nhóm theo severity. (grep artifact trước rồi mới kết luận — bài học 09-30 #17.)

---

## 🔴 E1 — Toàn bộ bản cài Hermes Agent nằm bên trong KB — 225.530 tệp / 5,5 GB / repo git lồng — CARRY-FORWARD

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

| Bằng chứng | Kết quả (đo lại 10-03 23:31) |
|---|---|
| `find .hermes/hermes-agent \( -type f -o -type l \)` | **225.530 tệp** (10-02: 225.529 → **+1**) |
| `du -sh` | **5,5 GB** |
| `test -e .hermes/hermes-agent/.git` | **CÓ** — repo git lồng (riêng `.git` = 2.074 tệp / 1,6 GB) |
| `git -C … rev-parse --abbrev-ref HEAD` | `main` |
| HEAD của repo lồng | `990473a79c` (**không đổi**) |
| `git ls-tree HEAD -- .hermes/hermes-agent` | **`160000 commit 990473a79c6b0396…`** — gitlink |
| `.gitmodules` | **KHÔNG TỒN TẠI** ⇒ `git submodule` không hoạt động |
| `grep -c 'hermes-agent' .gitignore` | **0 — không có rule nào** |

**Ba trạng thái phải báo riêng (bài học 09-30 #19):** nested `.git` **CÓ** · gitlink `160000` **CÓ** · `.gitmodules` **KHÔNG**. Cả ba trạng thái **không đổi** so với 10-01 và 10-02.

**Vì sao 23 ngày chưa ai báo:** gitlink là **một dòng** trong cây KB (`git ls-files -s` trả đúng 1 dòng) + quy tắc "bỏ qua agent home ở độ sâu > 1" chặn phần còn lại ⇒ mọi probe lượt trước đều sạch.

**Hậu quả:** 5,5 GB / 225.530 tệp cho một KB vốn ~1,7K tệp; repo lồng **chưa khai báo** ⇒ clone trên máy khác tạo thư mục rỗng, `git submodule update` lỗi; **nguy cơ mất CWD của agent** — Hermes đang chạy code từ đây.

**Suggested fix (thứ tự bắt buộc):**
1. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó** — đây là CWD của tiến trình đang viết báo cáo này.
2. Xác định **cơ chế cài đặt** (bootstrap script / target `pip`/`uv` / sync từ repo nguồn) — đó mới là chỗ cần sửa để nó không quay lại.
3. Chọn: (a) **hợp lệ hoá** — khai báo đúng `.gitmodules` + đẩy repo lồng lên remote riêng; hoặc (b) **chuyển ra ngoài KB** (`~/.hermes/hermes-agent/`) rồi sửa launcher.
4. Thêm rule `.hermes/hermes-agent/` vào `.gitignore` **và** `git rm --cached` (bỏ gitlink) — giữ gitlink nếu (a), bỏ hẳn nếu (b).

---

## 🔴 E2 — `vault backup` dừng **9,11 ngày** — CARRY-FORWARD, ngày thứ 10

**Severity:** ERROR · **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08` |
| `git ls-remote --heads origin` (23:31 hôm nay) | `refs/heads/master = e05f00abf29e84c8…` — **remote cũng đứng ở đây** |
| Thời gian | **9,11 ngày** (09-24 20:51 → 10-03 23:31) |

Đã kiểm remote **trước khi** kết luận máy này hỏng (bài học 09-28 #11): remote `master` cũng `e05f00ab` ⇒ **lỗi tiến trình backup trên máy chính, không phải push trễ**.

**Ghi nhận thêm (từ Format Validator 10-03):** remote default branch là `refs/heads/main` = `ead50c82` — nếu tiến trình backup push nhầm nhánh thì đó là nguyên nhân gốc. Nhánh `main` bị bỏ rơi từ 2026-05-11, `master` mới là đích sync.

**Trạng thái chờ:** `git status --porcelain -uall` = **8.496 `??` + 439 `M` + 8 `D` + 1 `R`** (10-02: 6.926 / 347 / 8 / 1).

Phân bổ `??` (8.496): **8.329** `.hermes/checkpoints` · **87** `.hermes/.curator_backups` · **3** `.hermes/skills/.curator_backups` · **9** `.hermes` khác · **68** vùng nội dung (xem E9).

**Cổng cửa sổ vẫn đóng:** vì backup dừng, E3–E7 **chưa** bị commit thêm. Runtime đang chờ **8.428 tệp `??` trong agent home**.

**Suggested fix (thứ tự bắt buộc):** (1) chặn `.gitignore` cho E3–E7 **trước**; (2) xử lý E4/E8 secret; (3) **rồi mới** khởi động lại backup. Validator không push, không commit.

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
| `.hermes/config.yaml.bak*` | **18/18** | 11 | **NONE** |
| `.hermes/state-snapshots*` | 7 | 2 | **NONE** |
| `.hermes/checkpoints*` (repo lồng) | **31** | 9 | **NONE** |
| `.hermes/.curator_backups*` | **230** | 16 | **NONE** |
| `.hermes/skills/.curator_backups*` | 15 | 14 | **NONE** |
| `.hermes/config.yaml` | 1 | **50** | **NONE** |
| `.hermes/auth.json` | 1 | **78** | `:37` **có, vô hiệu** |
| `.hermes/MEMORY.md` | 1 | **172** | `:81` **có, vô hiệu** |

**Bảng này y hệt 10-02** — 0 thay đổi. **Khoảng trống đối xứng vẫn đúng:** `.openclaw/*.bak` và `.hermes/state.db*` **có** rule ⇒ **vùng `.hermes/` không được bảo vệ.**

**WAL sidecar vẫn là mắt xích yếu:** `kanban.db-shm`/`-wal` = 141 commit **mỗi tệp**, chỉ vì hai tệp sidecar này.

**Suggested fix:** `.gitignore` theo **mẫu wildcard** cho toàn bộ runtime + `git rm -r --cached` một lượt. Gộp với E1.

---

## 🔴 E4 — 7 tệp tên auth đã tracked — CARRY-FORWARD, **không có file mới**

**Severity:** ERROR · **Category:** Path / Secret exposure

Probe theo **tên tệp** trên `git ls-tree -r HEAD` (bài học 09-30 #15 — không phải grep tên khoá bên trong một tệp), lọc `skills/`:

`.hermes/auth.json` (11.003 B, 78 commit) · `.hermes/auth.lock` · `.hermes/state-snapshots/20260626-005403-pre-update/auth.json` (8.201 B) · `.openclaw/device-auth.json` · `.openclaw/identity/device-auth.json` · `.openclaw/agents/main/agent/auth-profiles.json` · `.openclaw/agents/main/agent/auth-state.json`

**Giữ nguyên nguyên tắc:** chỉ grep **tên khoá**, không đọc **giá trị**. Báo cáo này **không** mở nội dung credential. Cả 7 nằm trong HEAD `e05f00ab` == remote `master` ⇒ **đã trên GitHub.**

**Đính chính phạm vi grep:** lọc `auth|token|secret|credential|apikey|\.env` còn trả về **29 tệp nội dung KB** (`wiki/concepts/token-*.md`, `wiki/topic/tokenization-llm.md`, …). Đây **không phải credential** — là nội dung tri thức hợp lệ. Danh sách 7 tệp ở trên là kết quả sau khi tách 2 nhóm.

**Suggested fix (thứ tự):** (1) Julius kiểm visibility repo — public ⇒ **rotate token trước mọi việc git**; (2) `git rm --cached` cả 7 + commit; (3) rewrite lịch sử nếu token còn hiệu lực (`git-secret-cleanup`); (4) rotate ở provider sau khi rewrite.

---

## 🔴 E5 — `.hermes/checkpoints/` repo git lồng, 70 MB — CARRY-FORWARD, **đang phình**

**Severity:** ERROR · **Category:** Orphan / repo hygiene

**31 tệp tracked**, `store/HEAD` tồn tại, **8.360 tệp trên đĩa / 70 MB** (10-02: 6.814 tệp / 62 MB ⇒ **+1.546 tệp / +8 MB trong 1 ngày**), `grep -c checkpoints .gitignore` = **0**. Trong đó **8.329 là `??` đang chờ commit**.

**Consequence:** vì backup dừng (E2), 8.329 tệp này **pending**. Bật backup mà chưa chặn `.gitignore` ⇒ commit kế tiếp nuốt **70 MB**.

---

## 🔴 E6 — `.hermes/.curator_backups/` — CARRY-FORWARD, **leo thang tiếp**

**Severity:** ERROR · **Category:** Orphan

Trên đĩa: **317 tệp** (`.hermes/.curator_backups/`, **7,1 MB**) + 15 (`.hermes/skills/.curator_backups/`). Đã tracked: **245** (230 + 15). `??` chờ commit: **90** (87 + 3). Chuỗi leo thang: 45 → 52 → 70 → 79 → **90**. Không rule `.gitignore`.

---

## 🔴 E7 — 2 marker `.migrated.*` — CARRY-FORWARD, **mtime đứng 25 ngày** (MÁY ERROR 1/4)

**Severity:** ERROR · **Category:** Path

| Vị trí | Cỡ | mtime | Rule |
|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3….e79d1c6c-…` (root) | 69 B | **2026-09-08 20:42** | **NONE** |
| `.openclaw/workspace-state.json.migrated.43c9aa3….fb077b94-…` | 69 B | **2026-09-08 20:42** | **NONE** |

Cùng blob `a0105ac6…`, **25 ngày không đổi**. Đã dò tay tree-wide `find . -name '*.migrated.*' -not -path './.git/*'` (bài học 09-25) ⇒ **đúng 2, không có biến thể thứ ba.**

**Suggested fix:** wildcard `*.migrated.*` + `git rm --cached` cả hai + commit.

---

## 🔴 E8 — `.hermes/config.yaml` git-tracked, 50 commit, có tên khoá `api_key` / `secret` / `session_key` — CARRY-FORWARD

**Severity:** ERROR · **Category:** Path / Secret exposure

23.603 B, **50 commit**, không rule nào khớp. Mỗi lần sửa config = một commit chứa lại toàn bộ nội dung. Validator cố tình **không** đọc giá trị.

---

## 🔴 E9 — 68 tệp nội dung `??` chưa commit; 410 tệp `M` do Index Agent viết lại

**Severity:** ERROR · **Category:** Orphan

Phân biệt bằng `git status --porcelain -uall` (bài học 09-28 — `find -newer` đếm cả tệp được sinh lại):

| Nhóm | Số | Ý nghĩa |
|---|---|---|
| `??` vùng nội dung | **68** | **thật** — 25 report validator + 16 concept + 10 topic + 7 source + 5 post + 2 website + 2 article + 1 video |
| `M` vùng nội dung | **410** | **không phải KB dày thêm** — Index Agent full rebuild 21:07 (268 topic + 25 tag regenerate) |
| `D` vùng nội dung | **1** | `wiki/topic/brain-threat-detection.md` — xem E10 |
| `R` (staged) | **1** | `src_why-youve-lost-your-curiosity-and-how-to-get-it-back.md` → `…-curiosity-how-to-get-it-back.md` (Fix Agent 10-02, `R100`) |

---

## 🔴 E10 — `wiki/topic/brain-threat-detection.md` bị xoá, **9 ngày chưa giải quyết** — CARRY-FORWARD

**Severity:** ERROR · **Category:** Orphan

`git status` ` D` = 8 tệp, **1 nằm trong vùng nội dung**: `wiki/topic/brain-threat-detection.md`. `test -e` xác nhận ⇒ **ABSENT** (đo lại trên đĩa, không chép kết luận cũ). 7 tệp còn lại là `.hermes/skills/` runtime.

Đây là **mục tri thức thật** bị prune bởi Index Agent. Vì backup dừng (E2), **trên GitHub file vẫn còn** — nếu VPS hỏng thì mất thật.

**Suggested fix:** Julius xác nhận prune có chủ ý không. Nếu mất thật ⇒ phục hồi từ commit `52170426`.

---

## 🔴 E11 — `DREAMS.md` — **9 ngày dreaming chưa commit** (MÁY ERROR 2/4)

**Path:** `DREAMS.md` (root) · **Severity:** ERROR · **Category:** Path

File thường, **16.216 B** trên đĩa (10-02: 15.323 B → **+893**; 10-01: 14.530 B), git-tracked (`100644`), 12 commit, mtime **2026-10-03 03:00:17** — writer vẫn chạy đúng 03:00 mỗi đêm. `check-ignore --no-index` ⇒ **rc=1, không rule**. Blob trong HEAD = **8.932 B** (không đổi) ⇒ **7.284 B chênh lệch chưa lên GitHub = 9 ngày dreaming**.

**Suggested fix:** giữ dữ liệu, sửa writer/output path. Xoá file không giải quyết được (proven nhiều lần).

---

## 🔴 E12 — `memory/` — CARRY-FORWARD, **lượt thứ 13 liên tiếp** (MÁY ERROR 3/4)

**Severity:** ERROR · **Category:** Orphan

**101 tệp, 7 thư mục** (tính cả thư mục gốc: `memory/` + `dreaming/` + `dreaming/{deep,light,rem}` + `.dreams/` + `.dreams/session-corpus/`). Chuỗi tệp: …93 → 97 → **101**. Phân bổ: `dreaming/{deep,light,rem}` 25 mỗi + `.dreams/session-corpus` 24 + 2 tệp gốc. `check-ignore --no-index` ⇒ **IGNORED** (`.gitignore:84 memory/`), `git ls-files -s memory/` = **0** ⇒ chưa lên GitHub.

**Ghi chú đếm:** 10-01 ghi "3 thư mục con", 10-02 đếm **6**, hôm nay **7** (bao gồm thư mục gốc `memory/` và 3 thư mục con *bên trong* `dreaming/`). Cùng một cây, **khác cách đếm** — không phải thư mục biến mất hay xuất hiện. Con số tái lập được: `find memory -type d | wc -l` = 7. Số tệp **+4** là tăng thật.

---

## 🔴 E13 — `wiki/HEARTBEAT.md` dangling — CARRY-FORWARD, ngày thứ 7 (MÁY ERROR 4/4)

**Path:** `wiki/HEARTBEAT.md` · **Severity:** ERROR · **Category:** Orphan

Xác minh bằng `realpath` + `exists` + `lexists` (bài học 09-28 #10 — không mắt bằng đường dẫn tương đối): `islink=True`, `lexists=True`, target `../../.openclaw/HEARTBEAT.md`, `realpath` = **`/home/julius/.openclaw/HEARTBEAT.md`**, `exists` = **False** ⇒ **DANGLING**, sai một cấp thư mục (đúng phải là `../.openclaw/HEARTBEAT.md`).

Đã kiểm **cả 4 symlink ở root**: `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` → `realpath` tới `<KB>/.openclaw/…`, `exists=True` ⇒ **hợp lệ**. `HEARTBEAT.md` ở root **vắng mặt** (tuỳ chọn theo §2, không tính lỗi).

---

## ⚠️ W1 — 101 WARNING kỹ thuật dưới `memory/` — hệ quả trực tiếp của E12

**Severity:** WARNING · **Category:** Path

Bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào (10-02: 97 ⇒ nay **101**). **Toàn bộ là hệ quả của E12, không phải 101 vấn đề độc lập.**

---

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive — UNCHANGED

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` · **Severity:** WARNING

**15 tệp, không đổi** (so 09-17→10-03). Tổng archive: **177 tệp**. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.

**Suggested fix:** Julius chốt chính sách (giữ / chuyển / cho phép ngoại lệ §7). Validator **không** tự đổi tên bản sao thành báo cáo.

---

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7 + §6/§7/§3-§4 tự mâu thuẫn — UNCHANGED

**Severity:** WARNING

(a) Bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`/`format`/`hygiene`. Chỉ tồn tại `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md` — **tồn đọng, không phải phát hiện mới**.

(b) §6 cho phép `raw.md` rồi ghi `*` ✗ forbidden; §7 cho phép `wiki.md` (dòng 169 ✓ required) rồi ghi "No files at `wiki/` root level"; §4 hạn chế nội bộ skills trong khi §3 cho phép runtime tự do. **Đã kiểm lại theo bài học 10-02 #22:** `wiki/wiki.md` và `raw/raw.md` đều được whitelist ⇒ bộ quét phải `continue` trước khi báo orphan gốc. Hôm nay bộ quét **không** báo nhầm 2 tệp này.

---

## ⚠️ W4 — [SYSTEMATIC VIOLATION] carry-forward: cặp topic trùng nghĩa `cuoc-dua-khong-di-lui.md` / `cuoc-dua-khong-i-lui.md` — **tái tạo lại lần thứ 4**

**Severity:** WARNING · **Category:** Naming

| Tệp | Cỡ | mtime |
|---|---|---|
| `wiki/topic/cuoc-dua-khong-di-lui.md` | **375 B** | 2026-10-03 21:07 |
| `wiki/topic/cuoc-dua-khong-i-lui.md` | **407 B** | 2026-10-03 21:07 |

**Đã tái tạo lại lần thứ 4** (09-30 → 10-01 → 10-02 → **10-03**), cùng Index Agent lượt **21:07**, hai file cùng mtime. Cùng một chủ đề ("cuốc đua không đi lùi") bị tách làm hai file chỉ mục.

**Đây là lần escalate thứ 3 — carry-forward, KHÔNG re-escalate mới** (quy tắc carry-forward 09-01).

**Root-cause:** Index Agent tạo topic từ nhãn chưa canonical hoá ⇒ cùng một cụm tiếng Việt sinh 2 slug khác nhau. **Bằng chứng đã đủ mạnh để kết luận: tái tạo 4 lượt liên tiếp, mỗi lượt một lần Index Agent chạy ⇒ sửa tay không giữ được.** Đây là bằng chứng thứ 4, không phải lần đầu — không có gì mới để escalate.

**Suggested fix:** Index Agent SKILL.md — bỏ dấu + gộp `đ`→`d`, `i`→`i` **trước** khi tạo topic; gộp 2 file thành 1. Validator **không** tự gộp.

---

## ⚠️ W5 — Quy tắc miễn kiểm tra agent home che mất **9 nhóm ERROR**

**Severity:** WARNING · **Category:** Path

Bộ quét hôm nay báo **4 ERROR** (4 path unique). Kiểm tay bằng `git ls-tree` / `ls-files` / `find` cho thấy **13 nhóm thực tế** (E1–E13), trong đó **9 nhóm không có path nào ở tầng quét**. Nguyên nhân vẫn là quy tắc §3 "bỏ qua `.hermes/`/`.openclaw/` sâu > 1".

**Đây là lỗi của bộ quét, không phải của KB.** Nói rõ để không tính nhầm thành phát hiện KB mới.

**Suggested fix:** nới quy tắc sang "quét mọi thư mục lồn + mọi tệp có khả năng chứa bí mật/khối lượng lớn" (`*auth*`, `*.json`, `*.db*`, `*.bak*`, `*.pack`, `config.*`, `*.env`, `HEAD`, `.git`) **bất kể độ sâu**; dùng `git ls-files -s` + `check-ignore --no-index` cho từng hit.

---

## ⚠️ INFO I1 — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/` · **Severity:** INFO

**120 tệp `.md`** ở tầng active (10-02: 117 → +3 = 1 report Format + 1 report Output + 1 report Hygiene hôm nay); **38 tệp mtime cũ hơn 2026-09-01**, sớm nhất `2026-06-01_output-report.md`. `wiki/drafts/` = 1 tệp. Số lượng phụ thuộc trạng thái approved/applied nên không dùng một số chưa đối chiếu làm quyết định.

---

## ⚠️ INFO I2 — `.hermes/lsp/` đã tracked 4 tệp; `node_modules` **được ignore đúng**

**Path:** `.hermes/lsp/` · **Severity:** INFO

4 tệp đã tracked: `bin/bash-language-server` (**symlink**, mode `120000`), `bin/pyright-langserver` (**symlink**, mode `120000`), `package.json`, `package-lock.json`. Không có rule riêng cho `.hermes/lsp/`.

**Xác nhận lại (không lặp lại ảo giác của 10-02):** `node_modules/` bên trong nó có **42 mục tầng đầu** (7.105 tệp) và **ĐÃ được ignore đúng** — `.gitignore:33 node_modules/`, `check-ignore --no-index` ⇒ `.gitignore:33`. **Không phải rò rỉ, không phải KB growth.** Trên đĩa nhiều, trong git chỉ 4.

---

## 📐 ĐỊNH NGHĨA ĐẾM — đọc trước bảng delta

Báo cáo này công bố **hai loại số khác nhau về bản chất** và phải tách rõ, nếu không sẽ tạo ra "tăng trưởng KB" giả:

| Loại số | Giá trị | Định nghĩa |
|---|---|---|
| **Tệp ổn định trong phạm vi** | **1.680 → 1.681 post-write** | 4 vùng nội dung đệ quy (`raw` 229 + `wiki` 1.433 + `context` 2 + `scripts` 5 = 1.669) + 11 tệp/symlink root. Đếm bằng `S_ISREG ∪ S_ISLNK` — **không** phải "không phải thư mục" (bẫy socket, pitfall #18). **Đây là con số duy nhất nên so với lượt trước.** |
| **Tệp tầng đầu agent home** | **99 (77+22)** | L1 của `.hermes/` + `.openclaw/`. **BIẾN ĐỘNG** theo pitfall #18 — không so được, không phải KB tăng/giảm. |
| **Thư mục** | **74** | 9 root + 23 vùng nội dung (**bao gồm thư mục gốc vùng** — `os.walk` bỏ sót, pitfall #21) + 42 L1 agent home (27 `.hermes` + 15 `.openclaw`). |
| **Quét máy (KHÔNG phải phạm vi)** | **242.766** | `find . -type d -name .git -prune -o \( -type f -o -type l \) -print` — prune **mọi** thư mục `.git` ở mọi độ sâu. `.hermes/` chiếm **242.740 / 99,99%**, trong đó 225.530 là bản cài lồng (E1). |

### ⚠️ Vì sao "quét máy" phải nêu định nghĩa prune (bài học 10-02 #20)

Cùng một cây, ba cách prune cho ba con số khác nhau — **tất cả đều đúng theo định nghĩa của nó**:

| Cách prune | Kết quả | Chênh |
|---|---|---|
| Prune mọi `.git` ở mọi độ sâu | **242.766** | (định nghĩa công bố hôm nay) |
| Hình dạng bộ quét (`.git` gốc + `/.git/` trong chuỗi) | 242.752 | −14 |
| Chỉ prune `.git` gốc, **giữ** `.git` của repo lồng | 244.840 | +2.074 (đúng bằng 2.074 tệp trong `.hermes/hermes-agent/.git`) |
| Tính cả `.git` gốc | 244.973 | +133 |

Số 10-02 công bố (**243.267**) khớp **không** định nghĩa nào ở trên ⇒ nó dùng prune khác. Đây chính là lý do báo cáo này **tường minh định nghĩa**: chỉ phần **1.680 tệp ổn định + 74 thư mục** là so sánh được giữa các lượt.

**Đã xác minh PASS:** 15/15 index bắt buộc tồn tại (`req_missing=[]`); 4/4 symlink định danh root có đích thật; 0 thư mục rỗng; **0 lỗi naming/path trong 1.669 tệp vùng nội dung**; 0 trùng slug chuẩn hoá **trong cùng vùng**.

**Ghi chú phương pháp:** hôm nay bộ quét **không** còn báo nhầm `wiki/wiki.md` / `raw/raw.md` là file ở gốc vùng — quy tắc `continue` cho index whitelist đã được áp từ 10-02 (bài học #22). 4 ERROR máy hôm nay là 4 path thật, không có false positive.

---

## Delta so với 10-02

| Hạng mục | 10-02 | 10-03 | Kết luận |
|---|---|---|---|
| **Tệp ổn định trong phạm vi** | 1.669 | **1.680** | **+11** — quy hết cho 11 tệp nội dung `??` mới (10-02: 57 → 10-03: 68) + 3 report validator hôm nay. Không phải KB dày thêm đột biến. |
| Số quét máy | 243.267 | **242.766** | **Không so được** — 10-02 không nêu định nghĩa prune. `.hermes/hermes-agent` đứng yên 225.529 → 225.530. |
| Machine findings | 102 (5E+97W) | **120 (4E+116W)** | ERROR 5→4 = bỏ false positive `wiki.md`; WARNING 97→116 = `memory/` 97→**101** + 15 archive backups |
| **Nhóm ERROR** | 13 | **13** | **0 ERROR mới, 0 resolved** |
| `vault backup` | dừng 8,11 ngày | **dừng 9,11 ngày** | remote vẫn `e05f00ab`; **8.496 `??`** (+1.570) + 439 `M` + 8 `D` + 1 `R` |
| Runtime chờ commit | 6.862 tệp | **8.428 tệp** | checkpoints 6.783→**8.329** (+1.546) · curator 79→**90** (+11) |
| `DREAMS.md` | 15.323 B | **16.216 B** | +893; blob HEAD đứng 8.932 B ⇒ **9 ngày** chưa commit |
| `memory/` | 97 tệp / 6 thư mục | **101 tệp / 7 thư mục** | +4 tệp thật; số thư mục khác cách đếm (nay đã nêu rõ cách đếm); **lượt thứ 13** |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, **25 ngày** |
| `wiki/HEARTBEAT.md` | dangling | **dangling** | UNCHANGED, xác minh `realpath`+`exists`+`lexists` |
| Tệp bị xoá (tracked) | 8 (1 `wiki/topic/`) | **8 (1 `wiki/topic/`)** | `brain-threat-detection.md` — **9 ngày** chưa giải quyết |
| Cặp topic trùng nghĩa | 1 cặp (lần 3) | **1 cặp (lần 4)** | W4, cùng mtime 21:07 |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 | 1 | UNCHANGED, tồn đọng |
| Bản cài Hermes lồng | 225.529 tệp | **225.530 tệp** | +1, UNCHANGED về bản chất |

---

## Actions Needed

1. **🔴 E1 — `.hermes/hermes-agent/` 5,5 GB trong KB.** Xác định cơ chế cài đặt rồi hợp lệ hoá (`.gitmodules` + remote riêng) **hoặc** chuyển ra `~/.hermes/`. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó** — đây là CWD của tiến trình đang viết báo cáo này. Nên làm **đầu tiên**: xoá 99,9% nhiễu khỏi mọi lượt quét sau.
2. **🔴 E2/E4 — kiểm secret ngay (không cần chờ duyệt).** Repo public hay private? Public ⇒ **rotate token trước mọi việc git**. 7 tệp tên auth đã tracked + `config.yaml` (50 commit). `git-secret-cleanup` có sẵn.
3. **🔴 Chặn `.gitignore` TRƯỚC khi bật lại backup.** 11/13 mẫu runtime chưa có rule (`checkpoints`, `curator_backups`, `state-snapshots`, `kanban.db*`, `projects.db`, `verification_evidence.db`, `config.yaml.bak*`, `.hermes/hermes-agent/`). Bật backup ngay lúc này ⇒ commit kế tiếp nuốt **8.428 tệp / 77 MB**.
4. **🔴 E10 — xác nhận `wiki/topic/brain-threat-detection.md` bị prune có chủ ý không.** 9 ngày chưa giải quyết. Trên GitHub file **vẫn còn** (backup dừng) — còn kịp phục hồi.
5. **🔴 E2 — `vault backup` dừng 9,11 ngày.** Remote `master` cũng đứng `e05f00ab` ⇒ lỗi tiến trình backup máy chính, không phải push trễ. **Gợi ý mới cần kiểm:** remote default branch là `main` (`ead50c82`), không phải `master`.
6. **Sửa 3 writer** (`memory/` ×3 đường, `DREAMS.md`, mirror `wiki/HEARTBEAT.md`) trước, rồi mới migrate/dọn. Xoá file không dừng được writer — E12 đã 13 lượt, E13 7 lượt, E11 9 lượt.
7. **W4 — Index Agent canonical hoá slug trước khi tạo topic.** Cặp `cuoc-dua-khong-{di,i}-lui` đã tái tạo **4 lượt liên tiếp** — sửa tay không giữ được, phải sửa SKILL.md; gộp 2 file thành 1.
8. **W5 — nới quy tắc miễn kiểm tra agent home trong bộ quét** (đang che 225K tệp / 9 nhóm ERROR); validator tự sửa skill, không đụng `wiki/`.
9. **Chốt chính sách 15 archive backup + loại `spot-check`**, và **thống nhất §6/§7/§3-§4** (W3).

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*