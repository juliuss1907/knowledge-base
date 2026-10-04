# Hygiene Inspection — 2026-10-01

**Status:** APPLIED — Fix Agent (OpenClaw main) xử lúc 2026-10-02 10:52 +07:00. CJK cleanup 9 file/11 dòng/26 ký tự (giữ 3 file hợp lệ: byte-level-bpe 中, hundred-years-humiliation 百年国耻, chinese-culture-confucianism 国家); rename slug 52→48 ký tự `src_why-youve-lost-your-curiosity-how-to-get-it-back` + 7 file link; vá mắt xích metrics vào src_ai-reflexivity-loop-is-same; 3 compiled_to; 2 broken wikilink bỏ; 9 khoá `- **Trạng thái:**` → `- **Status:** pending`. 4 claim trong báo cáo bị đính chính sau khi đo trực tiếp — xem `.openclaw/MEMORY.md` 2026-10-02.
**Issues found:** 21 nhóm (14 ERROR, 5 WARNING, 2 INFO)
**Created:** 2026-10-01 23:31 +0700
**Validator:** hygiene-inspector
**Paths checked:** 241.162 đường dẫn quét máy. ⚠️ **KHÔNG còn là phạm vi KB — 99,75% là bản cài Hermes Agent nằm nhầm trong KB** (E1, 225.528 tệp / 5,5 GB). Phạm vi KB đúng = **1.655 tệp ổn định** (1.644 vùng nội dung + 11 root, đo bằng `find -type f -o -type l` ⇒ loại socket) + **99 tệp tầng đầu agent home BIẾN ĐỘNG** (lấy mẫu 5×/28 giây đều ra 99, socket đã loại) cộng **34 thư mục** (9 root + 23 vùng nội dung + 2 thư mục L1 agent home — xem E1 và §Định nghĩa đếm).
**Machine findings:** 112 (4 ERROR + 108 WARNING) + 17 ERROR nhóm phát hiện bằng dò tay = 21 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## 🔴 E1 — ERROR MỚI, LỚN NHẤT TỪNG THẤY: **toàn bộ bản cài Hermes Agent nằm bên trong KB** — 225.528 tệp / 5,5 GB / repo git lồng

**Path:** `.hermes/hermes-agent/` · **Severity:** ERROR · **Category:** Orphan / repo hygiene

Đây là nguyên nhân của toàn bộ phép đo rác hôm nay. Không phải KB "phình to" — mà là **một repo git lồng đặt sai chỗ**.

| Bằng chứng | Kết quả |
|---|---|
| `find .hermes/hermes-agent -type f -o -type l` | **225.528 tệp** |
| `du -sh` | **5,5 GB** |
| `test -e .hermes/hermes-agent/.git` | **CÓ — repo git lồng** |
| `git -C .hermes/hermes-agent rev-parse --abbrev-ref HEAD` | `main` |
| HEAD của repo lồng | `990473a79c fmt(js): npm run fix on merge (#106237)` |
| `git ls-tree HEAD -- .hermes/hermes-agent` | **`160000 commit 990473a79c…`** — **gitlink/submodule** |
| `.gitmodules` | **KHÔNG TỒN TẠI** — gitlink không khai báo submodule ⇒ `git submodule` không hoạt động |
| Commit đầu tiên có gitlink | `8695083b` **2026-05-12** |
| `grep -c 'hermes-agent' .gitignore` | **0 — không có rule nào** |
| Repo lồng có `.gitignore` riêng | Có (nó tự lo, nhưng KB không) |

**Vì sao chưa ai báo trong 22 ngày — và vì sao nó cất giấu tốt:** gitlink mode `160000` là **một dòng duy nhất** trong cây KB (chứ không phải 225K dòng), nên `git ls-files -s .hermes/hermes-agent` trả về đúng **1 dòng**. Người đọc dễ tưởng repo sạch. Nhưng `vault backup` vẫn ghi cây lồng khi commit — và đây là **thư mục làm việc hiện tại của chính Hygiene Inspector** (Hermes khởi động với CWD=`.hermes/hermes-agent/`). Repo lồng đang **bẩn**: `DU apps/desktop/electron/main.cjs`, `UU package-lock.json`, `?? wiki/`.

**Hậu quả (theo thứ tự nghiêm trọng):**
1. **Tốn 5,5 GB / 225.528 tệp cho một KB vốn chỉ ~1,7K tệp.** Bất kỳ lượt quét full-tree, backup, hay `git status` nào cũng phải đi qua nó.
2. **`.hermes/` tổng 6,2 GB** — vùng agent home lớn gấp ~4 lần KB thật.
3. **Repo lồng chưa khai báo** ⇒ clone KB trên máy khác sẽ tạo thư mục rỗng, `git submodule update` sẽ lỗi.
4. **Nguy cơ ghi đè dữ liệu:** Hermes đang chạy code từ đây; nếu ai đó `git checkout`/`git pull` trong KB mà gitlink trỏ về commit không tồn tại trên remote ⇒ mất CWD của agent.

**Suggested fix (Fix Agent, theo thứ tự — sau khi Julius duyệt):**
1. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó.** Đây là CWD của tiến trình đang thực hiện báo cáo này.
2. Xác định Hermes được cài bằng cơ chế nào (bootstrap script / `pip`/`uv` target / sync từ repo nguồn) — đó mới là chỗ cần sửa để nó không quay lại.
3. Chọn một: (a) **hợp lệ hoá** — khai báo đúng `.gitmodules` + đẩy repo lồng lên remote riêng; hoặc (b) **chuyển ra ngoài KB** (ví dụ `~/.hermes/hermes-agent/`) rồi sửa đường dẫn trong launcher.
4. Dù đ chọn phương án nào: thêm rule `.hermes/hermes-agent/` vào `.gitignore` **và** `git rm --cached .hermes/hermes-agent` (bỏ gitlink) — nếu phương án (b) thì bỏ hẳn gitlink; nếu (a) thì giữ.
5. Sau khi xử lý: `find . -path ./.git -prune -o -type f -print | wc -l` phải về ~1,7K, không phải 241K.

---

## 🔴 E2 — `vault backup` dừng **7,11 ngày** — CARRY-FORWARD, ngày thứ 8

**Severity:** ERROR · **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08` |
| `git ls-remote --heads origin` (23:31 hôm nay) | `refs/heads/master = e05f00abf29e84c8…` — **remote cũng đứng ở đây** |
| Thời gian | **7,11 ngày** (09-24 20:51 → 10-01 23:31) |
| `git rev-list --count e05f00ab..HEAD` | **0** |
| Nhánh mồi | `origin/main = ead50c82` — **nhánh bị bỏ rơi từ 2026-05-11**, không phải đích sync |

Đã kiểm remote **trước khi** kết luận máy này hỏng (bài học 09-28): remote cũng đứng ở `e05f00ab` ⇒ **lỗi tiến trình backup trên máy chính, không phải push trễ**.

**Trạng thái chờ:** 326 `M` + 8 `D` + **6.903 `??`**.
**Cổng cửa sổ vẫn đóng:** vì backup dừng, E3–E7 **chưa** bị commit thêm. Runtime đang chờ: **6.783 `??` checkpoints + 70 `??` curator_backups**. Số này nhảy ngay khoảnh khắc backup chạy lại.

**Đối chiếu `??` toàn repo (6.903):** 6.783 checkpoints · 70 curator_backups · 43 vùng nội dung (xem E9) · 17 report validator trong `wiki/reviews` (chưa commit từ 09-25) · 8 `.hermes/skills`.

**Suggested fix (thứ tự bắt buộc):** (1) chặn `.gitignore` cho E3–E7 **trước**; (2) xử lý E8/E3 secret; (3) **rồi mới** khởi động lại backup. Validator không push, không commit.

---

## 🔴 E3 — 9 mẫu runtime trong agent home đã tracked, **không mẫu nào có rule** — CARRY-FORWARD từ 09-30

**Severity:** ERROR · **Category:** Path

Đã lặp lại đúng probe hôm nay (10 mẫu, `git ls-files -s` + `check-ignore --no-index`):

| Mẫu | Tracked | Commit | Rule `--no-index` |
|---|---|---|---|
| `.hermes/kanban.db` | 1 | 3 | **NONE** |
| `.hermes/kanban.db-shm` | 1 | **141** | **NONE** |
| `.hermes/kanban.db-wal` | 1 | **141** | **NONE** |
| `.hermes/projects.db` | 1 | 1 | **NONE** |
| `.hermes/verification_evidence.db` | 1 | **345** | **NONE** |
| `.hermes/config.yaml.bak*` (18 tệp) | **18/18** | 11 | **NONE** |
| `.hermes/state-snapshots*` (7 tệp) | 7 | 2 | **NONE** |
| `.hermes/checkpoints*` (repo lồng) | **31** | 9 | **NONE** |
| `.hermes/skills/.curator_backups*` | **245** | 16 | **NONE** |
| `.hermes/auth.json` | 1 | **78** | `:37` **có, vô hiệu** |
| `.hermes/MEMORY.md` | 1 | **172** | `:81` **có, vô hiệu** |
| `.hermes/config.yaml` | 1 | **50** | **NONE** |
| `.hermes/hermes-agent` (E1) | 1 (gitlink) | **5** | **NONE** |

**Khoảng trống đối xứng vẫn đúng:** `.openclaw/*.bak` và `.hermes/state.db*` **có** rule ⇒ **vùng `.hermes/` không được bảo vệ.** 11/13 mẫu không rule.

**WAL sidecar vẫn là mắt xích yếu:** `kanban.db-shm`/`-wal` = 141 commit **mỗi tệp** chỉ vì hai tệp sidecar này.

**Suggested fix:** `.gitignore` theo **mẫu wildcard** cho toàn bộ runtime + `git rm -r --cached` một lượt. Gộp với E1 (bỏ gitlink hoặc hợp lệ hoá).

---

## 🔴 E4 — 7 tệp tên auth đã tracked — CARRY-FORWARD, **không có file mới**

**Severity:** ERROR · **Category:** Path / Secret exposure

Probe theo **tên tệp** (bài học 09-30) trên `git ls-tree -r HEAD`, lọc `skills/`, cho **32 hit** — trong đó 25 là nội dung tri thức (`tokenization`, `secrets-management`…) và **7 là credential thật**:

| Tệp | Vùng |
|---|---|
| `.hermes/auth.json` (11.003 B, 78 commit) | agent home |
| `.hermes/auth.lock` | agent home |
| `.hermes/state-snapshots/20260626-005403-pre-update/auth.json` (8.201 B) | agent home |
| `.openclaw/device-auth.json` | agent home |
| `.openclaw/identity/device-auth.json` | agent home |
| `.openclaw/agents/main/agent/auth-profiles.json` | agent home |
| `.openclaw/agents/main/agent/auth-state.json` | agent home |

Cả 7 nằm trong HEAD `e05f00ab` == remote `master` ⇒ **đã trên GitHub.**

**Giữ nguyên nguyên tắc:** chỉ grep **tên khoá**, không đọc **giá trị** (`access_token`, `refresh_token`, `api_key`, `credential_pool`, `secret_fingerprint` — 09-30 đã ghi nhận). Báo cáo này **không** mở nội dung credential.

**Suggested fix (thứ tự):** (1) Julius kiểm visibility repo — public ⇒ **rotate token trước mọi việc git**; (2) `git rm --cached` cả 7 + commit; (3) rewrite lịch sử nếu token còn hiệu lực (78 + 1×5 commit) — `git-secret-cleanup`; (4) rotate ở provider sau khi rewrite.

---

## 🔴 E5 — `.hermes/checkpoints/` repo git lồng, 62 MB — CARRY-FORWARD, **số chờ đã tăng**

**Severity:** ERROR · **Category:** Orphan / repo hygiene

Bằng chứng hôm nay: **31 tệp tracked**, `store/HEAD` tồn tại, pack **28 MB** (`pack-530333b3b…pack`) đã vào lịch sử, **6.814 tệp trên đĩa**, `6.783` trong số đó là `??` **đang chờ commit**. `grep -c checkpoints .gitignore` = **0**. Cùng commit với E3.

**Consequence:** vì backup dừng (E2), 6.783 tệp này **pending**, chưa commit. Nếu bật backup mà chưa chặn `.gitignore` ⇒ commit kế tiếp nuốt **62 MB**.

---

## 🔴 E6 — `.hermes/skills/.curator_backups/` — CARRY-FORWARD, **leo thang tiếp**

**Severity:** ERROR · **Category:** Orphan

Số tệp `??` trên đĩa: **45 → 52 (09-30) → 70 (hôm nay)**. Đã tracked: **245 tệp** (15 ở `.hermes/skills/.curator_backups/` + 230 ở `.hermes/.curator_backups/`). Không rule `.gitignore`.

**Suggested fix:** gộp với E3/E5.

---

## 🔴 E7 — 2 marker `.migrated.*` — CARRY-FORWARD, **mtime đứng 23 ngày**

**Severity:** ERROR · **Category:** Path

| Vị trí | Cỡ | Disk | Rule |
|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3….e79d1c6c-…` (root) | 69 B | **2026-09-08 20:42** | **NONE** |
| `.openclaw/workspace-state.json.migrated.43c9aa3….fb077b94-…` | 69 B | **2026-09-08 20:42** | **NONE** |

Cùng blob `a0105ac6…`, **23 ngày không đổi**. Đã dò tay tree-wide `find . -name '*.migrated.*'` (bài học 09-25) ⇒ **đúng 2, không có biến thể thứ ba.**

**Suggested fix:** wildcard `*.migrated.*` + `git rm --cached` cả hai + commit.

---

## 🔴 E8 — `.hermes/config.yaml` git-tracked, 50 commit, có tên khoá `api_key` / `secret` / `session_key` — CARRY-FORWARD

**Severity:** ERROR · **Category:** Path / Secret exposure

23.603 B, **50 commit**, mtime 09-24 20:00 ⇒ config đang sửa liên tục, mỗi lần sửa = một commit chứa lại toàn bộ nội dung. Không rule nào khớp. Validator cố tình **không** đọc giá trị.

---

## 🔴 E9 — 43 tệp nội dung `??` chưa commit; 302 tệp `M` do Index Agent viết lại

**Severity:** ERROR · **Category:** Orphan

Phân biệt bằng `git status --porcelain -uall` (bài học 09-28 — `find -newer` đếm cả tệp được sinh lại):

| Nhóm | Số | Ý nghĩa |
|---|---|---|
| `??` vùng nội dung | **43** | **thật** — 9 concept + 5 source + 5 topic + 5 raw + 19 report validator (09-25→10-01) |
| `M` vùng nội dung | **302** | **không phải KB dày thêm** — 283 tệp cùng mtime `2026-10-01 21:09` (Index Agent viết lại toàn bộ topic/tag), 19 tệp rải rác |
| `D` vùng nội dung | **1** | `wiki/topic/brain-threat-detection.md` — xem E10 |

`find raw wiki -newer <09-30 report>` trả **292** — con số này **gây ảo giác**: 283/292 là tệp bị viết lại, chỉ **43** là mới thật. Không có batch ingest mới hôm nay; 9 concept + 5 source đến từ lượt compile 08:07–08:17.

---

## 🔴 E10 — `wiki/topic/brain-threat-detection.md` bị xoá, **7 ngày chưa giải quyết** — CARRY-FORWARD

**Severity:** ERROR · **Category:** Orphan

`git status` ` D` = 8 tệp, **1 nằm trong vùng nội dung**: `wiki/topic/brain-threat-detection.md` (commit cuối `52170426`, 09-21 21:08). 7 tệp còn lại là `.hermes/skills/` runtime. `test -e` ⇒ vắng mặt. **Không có backlink nào trong `wiki/` trỏ tới nó.**

Đây là **mục tri thức thật** đã bị prune bởi Index Agent. Vì backup dừng (E2), **trên GitHub file vẫn còn** — nếu VPS hỏng thì mất thật.

**Suggested fix:** Julius xác nhận prune có chủ ý không. Nếu mất thật ⇒ phục hồi từ `52170426`.

---

## 🔴 E11 — `DREAMS.md` — **7 ngày dreaming chưa commit**

**Path:** `DREAMS.md` (root) · **Severity:** ERROR · **Category:** Path

File thường, **14.530 B** (09-30: 13.738 B → **+792**), git-tracked, mtime **2026-10-01 03:00:16** — writer vẫn chạy đúng 03:00 mỗi đêm. Blob trong HEAD = **8.932 B** ⇒ **5.598 B chênh lệch chưa lên GitHub = 7 ngày dreaming**.

**Suggested fix:** giữ dữ liệu, sửa writer/output path. Xoá file không giải quyết được (proven nhiều lần).

---

## 🔴 E12 — `memory/` — CARRY-FORWARD, **lượt thứ 11 liên tiếp**

**Severity:** ERROR · **Category:** Orphan

**93 tệp, 3 thư mục con** (09-30: 89/6 → **+4 tệp**). Chuỗi: 49→53→57→64→68→72→76→81→85→89→**93**. Phân bố: 2 tệp gốc + `dreaming/{deep,light,rem}` (23 mỗi) + `.dreams/session-corpus/*.txt` (22). `check-ignore --no-index` ⇒ **IGNORED** (`.gitignore:84 memory/`) ⇒ chưa lên GitHub.

**Ghi chú:** 09-30 ghi "6 thư mục con" — hôm nay đếm **3** (`.dreams`, `dreaming` + gốc). Con số 6 của 09-30 bao gồm cả 3 thư mục con *bên trong* `dreaming/`; cùng một cây, khác cách đếm. **Không phải thư mục biến mất.**

---

## 🔴 E13 — `wiki/HEARTBEAT.md` dangling — CARRY-FORWARD, ngày thứ 5

**Path:** `wiki/HEARTBEAT.md` · **Severity:** ERROR · **Category:** Orphan

Xác minh bằng `realpath` + `exists` + `lexists`: `islink=True`, target `../../.openclaw/HEARTBEAT.md`, `realpath` = **`/home/julius/.openclaw/HEARTBEAT.md`**, `exists` = **False**, `lexists` = True ⇒ **DANGLING**, sai một cấp thư mục (đúng phải là `../.openclaw/HEARTBEAT.md`).

Đã kiểm lại **cả 5 symlink ở root**: `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md` → `realpath` tới `<KB>/.openclaw/…`, `exists=True` ⇒ hợp lệ. `HEARTBEAT.md` ở root **vắng mặt** (tuỳ chọn theo §2, không tính lỗi).

---

## ⚠️ W1 — 93 WARNING kỹ thuật dưới `memory/` — hệ quả trực tiếp của E12

**Severity:** WARNING · **Category:** Path

**93 trong 108 WARNING máy** là `"Path not classified by any rule"` — bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào. **Toàn bộ là hệ quả của E12, không phải 93 vấn đề độc lập.**

---

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` · **Severity:** WARNING

**15 tệp, không đổi** (so 09-17→10-01). Tổng archive: **177 tệp**. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.

**Suggested fix:** Julius chốt chính sách (giữ / chuyển / cho phép ngoại lệ §7). Validator **không tự đổi tên bản sao thành báo cáo**.

---

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7 + §6/§7/§3-§4 tự mâu thuẫn

**Severity:** WARNING

(a) Bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`/`format`/`hygiene`. Chỉ tồn tại `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md` — **tồn đọng, không phải phát hiện mới** (không có tệp `spot-check` mới).
(b) §6 cho phép `raw.md` rồi ghi `*` ✗ forbidden; §7 cho phép `wiki.md` rồi ghi "No files at `wiki/` root level"; §7 Rules yêu cầu `meta/` đúng 3 tệp nhưng cây chỉ hiện 2; §3 cho phép runtime tự do, §4 hạn chế nội bộ skills.

**Đính chính:** §7 cây `wiki/meta/` hiện `format-spec.md` + `folder-structure.md` (2 tệp) còn Rules nói đúng 3 — nhưng tệp thứ ba (`index-spec.md`) **có tồn tại** (PASS 15/15 index bắt buộc). Vậy đây là **lỗi trình bày cây trong quy chuẩn**, không phải thiếu tệp.

---

## ⚠️ W4 — [SYSTEMATIC VIOLATION] carry-forward: **cặp topic trùng nghĩa** `cuoc-dua-khong-di-lui.md` / `cuoc-dua-khong-i-lui.md` — **đã tái tạo lại**

**Severity:** WARNING · **Category:** Naming

| Tệp | Cỡ | mtime |
|---|---|---|
| `wiki/topic/cuoc-dua-khong-di-lui.md` | **612 B** (09-30: 611 B) | 2026-10-01 21:09 |
| `wiki/topic/cuoc-dua-khong-i-lui.md` | **644 B** (09-30: 643 B) | 2026-10-01 21:09 |

**Đã tái tạo lại sau 1 ngày** — cùng Index Agent lượt 21:09, cả hai file vẫn cùng mtime. Cùng một chủ đề ("cuốc đua không đi lùi") bị tách làm hai file chỉ mục. Kiểm tra slug chuẩn hoá trên **11 vùng nội dung**: **0 trùng chính xác trong cùng vùng** (83 cặp trùng chênh vùng là concept+topic cùng tên — **đúng thiết kế**).

**Đây là lần escalate thứ 2 — carry-forward, KHÔNG re-escalate mới** (quy tắc carry-forward: vấn đề đã escalate trong báo cáo đang `pending` thì lượt sau chỉ ghi `CARRIED FORWARD`, không block `[SYSTEMATIC VIOLATION]` mới).

**Root-cause:** Index Agent tạo topic từ nhãn chưa canonical hoá ⇒ cùng một cụm tiếng Việt sinh 2 slug khác nhau.
**Suggested fix:** Index Agent SKILL.md — bỏ dấu + gộp `đ`→`d`, `i`→`i` **trước** khi tạo topic; gộp 2 file thành 1. Validator **không** tự gộp.

---

## ⚠️ W5 — Quy tắc miễn kiểm tra agent home che mất **9 nhóm ERROR** (leo thang từ 8 lên 9)

**Severity:** WARNING · **Category:** Path

09-30 ghi "che mất 4 nhóm". Hôm nay: bộ quét báo **4 ERROR**, kiểm tay bằng `git ls-tree`/`ls-files`/`find` cho thấy **≥9 nhóm thực tế** (E1, E3, E4, E5, E6, E7, E8). Nguyên nhân vẫn là quy tắc §3 "bỏ qua `.hermes/`/`.openclaw/` sâu > 1".

**Hôm nay nó che một thứ mới:** **E1** — 225.528 tệp bị bỏ qua, và chính vì bỏ qua nên bộ quét không báo lỗi path nào.

**Đây là lỗi của bộ quét, không phải của KB.** Nói rõ để không tính nhầm thành phát hiện KB mới.
**Suggested fix:** nới quy tắc sang "quét mọi thư mục lồn + mọi tệp có khả năng chứa bí mật/khối lượng lớn" (`*auth*`, `*.json`, `*.db*`, `*.bak*`, `*.pack`, `config.*`, `*.env`, `HEAD`, `.git`) **bất kể độ sâu**; dùng `git ls-files -s` + `check-ignore --no-index` cho từng hit.

---

## ⚠️ INFO I1 — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/` · **Severity:** INFO

**114 tệp `.md`** ở tầng active (09-30: 111 → +3 = 2 report hôm nay + báo cáo này); **38 tệp mtime cũ hơn 2026-09-01**, sớm nhất `2026-06-01_output-report.md`. `wiki/drafts/` = 1 tệp (`analysis-2026-advice.md`). Số lượng phụ thuộc trạng thái approved/applied nên không dùng một số chưa đối chiếu làm quyết định.

---

## ⚠️ INFO I2 — `.hermes/lsp/` đã tracked một cách vô nghĩa

**Path:** `.hermes/lsp/` · **Severity:** INFO

4 tệp đã tracked: `bin/bash-language-server` (**symlink**), `bin/pyright-langserver` (**symlink**), `package.json`, `package-lock.json`. Không có rule `.gitignore`. Commit **1 lần** cho cả 4 (2026-06-17). **Không phải lỗi bảo mật** — nhưng là 4 tệp thừa do cài đặt tool cục bộ nằm trong KB. Gộp vào đợt dọn E3.

---

## 📐 ĐỊNH NGHĨA ĐẾM — đọc trước bảng delta

09-30 công bố "1.825 đường dẫn (1.751 tệp + 74 thư mục)", chỉ 1.653 ổn định. Hôm nay **con số máy 241.162**, nhưng đó **không phải KB** — 225.528/241.162 = **99,8%** là bản cài Hermes Agent (E1).

| | 09-30 | 10-01 | Nguyên nhân chênh |
|---|---|---|---|
| Tệp vùng nội dung | 1.641 | **1.644** | **+3 thật** (1 report hygiene 09-30 + 2 report validator 10-01 đã ghi trước lượt này) |
| Tệp root | 11 | **11** | UNCHANGED |
| **Tệp ổn định** | 1.653 | **1.655** | +2 = tệp ổn định trong `wiki/reviews/` |
| Tệp tầng đầu agent home | 98 (dao động) | **99** (lấy mẫu 5×, đều 99) | +1 = `.openclaw/last-index-success.txt`; `.hermes/gateway.sock` là socket, **đã loại** |
| Tệp vùng nội dung + root | — | **1.655 ổn định** | chỉ phần này nên so sánh |
| Thư mục root | 9 | **9** | UNCHANGED |
| Thư mục vùng nội dung | 23 | **23** | UNCHANGED |
| Thư mục L1 agent home | 42 | **42** | UNCHANGED (27 `.hermes` + 15 `.openclaw`) |
| **Thư mục (tổng)** | 74 | **74** | UNCHANGED — **khớp** lần này |
| *(mới)* Bản cài Hermes lồng | — | **225.528 tệp / 5,5 GB** | E1 |

**Đã xác minh:** 15/15 index bắt buộc tồn tại; 4/4 symlink định danh root có đích thật; 0 thư mục rỗng; **0 lỗi naming/path trong 1.644 tệp vùng nội dung** (1.639 tệp `.md`); 0 trùng slug chuẩn hoá **trong cùng vùng**; `.hermes/.env` được ignore đúng.

---

## Delta so với 09-30

| Hạng mục | 09-30 | 10-01 | Kết luận |
|---|---|---|---|
| Phạm vi (tệp ổn định) | 1.653 | **1.655** | +2 — **không phải KB dày thêm đáng kể** |
| Machine findings | 108 (4E + 104W) | **112 (4E + 108W)** | +4 = `memory/` 89→93 |
| ERROR nhóm | 13 | **14** | **+1 nhóm mới** (E1) |
| **ERROR thực tế (dò tay)** | ≥8 | **≥9** | E1 là nhóm lớn nhất từng thấy |
| `vault backup` | dừng 6,11 ngày | **dừng 7,11 ngày** | remote vẫn `e05f00ab`; 326 `M` + 8 `D` + 6.903 `??` |
| Runtime chờ commit | 6.835 tệp | **6.853 tệp** | checkpoints 6.783 + curator **70** (52→70) |
| `DREAMS.md` | 13.738 B | **14.530 B** | +792; blob HEAD 8.932 B ⇒ **7 ngày** chưa commit |
| `memory/` | 89 tệp / "6 thư mục" | **93 tệp / 3 thư mục** | +4 tệp; **lượt thứ 11**; số thư mục khác cách đếm (đã đính chính) |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, **23 ngày** |
| `wiki/HEARTBEAT.md` | dangling | **dangling** | UNCHANGED, xác minh `realpath`+`exists`+`lexists` |
| Tệp bị xoá (tracked) | 8 (1 `wiki/topic/`) | **8 (1 `wiki/topic/`)** | `brain-threat-detection.md` — **7 ngày** chưa giải quyết |
| Cặp topic trùng nghĩa | 1 cặp | **1 cặp (tái tạo lại)** | W4, cùng mtime 21:09 |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 | 1 | UNCHANGED, tồn đọng |
| Vùng nội dung 24h | 27 tệp mới | **43 `??` / 292 theo `find -newer`** | `find -newer` **gây ảo giác**: 283/292 là Index Agent viết lại |

---

## Actions Needed

1. **🔴 E1 — `.hermes/hermes-agent/` 5,5 GB trong KB.** Xác định cơ chế cài đặt rồi hợp lệ hoá (`.gitmodules` + remote riêng) **hoặc** chuyển ra `~/.hermes/`. **KHÔNG `rm -rf` khi Hermes đang chạy từ đó** — đây là CWD của tiến trình đang viết báo cáo này. Đây là việc nên làm **đầu tiên**: nó xoá 99,9% nhiễu khỏi mọi lượt quét sau.
2. **🔴 E2/E4 — kiểm secret ngay (không cần chờ duyệt).** Repo public hay private? Public ⇒ **rotate token trước mọi việc git**. 7 tệp tên auth đã tracked + `config.yaml` (50 commit). `git-secret-cleanup` có sẵn.
3. **🔴 Chặn `.gitignore` TRƯỚC khi bật lại backup.** 11/13 mẫu runtime chưa có rule (`checkpoints`, `curator_backups`, `state-snapshots`, `kanban.db*`, `projects.db`, `verification_evidence.db`, `config.yaml.bak*`, `.hermes/hermes-agent/`, `.hermes/lsp/`). Bật backup ngay lúc này ⇒ commit kế tiếp nuốt **6.853 tệp / 62 MB**.
4. **🔴 E10 — xác nhận `wiki/topic/brain-threat-detection.md` bị prune có chủ ý không.** 7 ngày chưa giải quyết. Trên GitHub file **vẫn còn** (backup dừng) — còn kịp phục hồi.
5. **🔴 E2 — `vault backup` dừng 7,11 ngày.** Remote cũng đứng ở `e05f00ab` ⇒ lỗi tiến trình backup trên máy chính, không phải push trễ.
6. **Sửa 3 writer** (`memory/` ×3 đường, `DREAMS.md`, mirror `wiki/HEARTBEAT.md`) trước, rồi mới migrate/dọn. Xoá file không dừng được writer — E12 đã 11 lượt, E13 5 lượt, E11 7 lượt.
7. **W4 — Index Agent canonical hoá slug trước khi tạo topic** (cặp `cuoc-dua-khong-{di,i}-lui` đã tái tạo lại sau 1 ngày), và gộp 2 file thành 1.
8. **W5 — nới quy tắc miễn kiểm tra agent home trong bộ quét** (nó đang che 225K tệp); validator tự sửa skill, không đụng `wiki/`.
9. **Chốt chính sách 15 archive backup + loại `spot-check`**, và **thống nhất §6/§7/§3-§4** (W3).

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*