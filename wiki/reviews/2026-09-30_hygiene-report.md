# Hygiene Inspection — 2026-09-30
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 19 nhóm (13 ERROR, 5 WARNING, 1 INFO)
**Created:** 2026-09-30 23:30 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1.825 đường dẫn trong phạm vi = **1.751 tệp** + 74 thư mục. ⚠️ **Chỉ 1.653 tệp là ổn định** (1.641 vùng nội dung + 11 tệp root, đo bằng `find -type f -o -type l` ⇒ loại socket); **98 tệp tầng đầu agent home là SỐ BIẾN ĐỘNG** (99 lúc quét, 98 lúc verify — xem mục 3). Định nghĩa: 4 vùng nội dung + 11 tệp/symlink ở root + tầng đầu hai agent home.
**Machine findings:** 108 (4 ERROR + 104 WARNING) + 15 ERROR nhóm mới phát hiện bằng dò tay = 19 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## ⚠️ ĐỔI ĐỊNH NGHĨA ĐẾM — đọc trước bảng delta

09-29 công bố "1.735 tệp + 70 thư mục". Hôm nay **74 thư mục, không tái lập được từ 70**. Không suy ra KB thay đổi cấu trúc.

| | 09-29 | 09-30 | Nguyên nhân chênh |
|---|---|---|---|
| Tệp vùng nội dung | 1.626 | **1.641** | +15 thật: +7 concept, +4 source, +2 topic, +2 report validator (xem E7) |
| Tệp tầng đầu agent home | 98 | **98 → 99 rồi về 98** | **BIẾN ĐỘNG, không so được**: 99 lúc quét do `.openclaw/last-index-success.txt` (mtime 21:03, Index Agent tạo, 25 B) mới xuất hiện; 98 lúc verify do `.hermes/.skills_prompt_snapshot.json` (artifact tạm theo session) biến mất. 46/98 tệp có dấu hiệu runtime biến động. **Đây KHÔNG phải KB tăng/giảm.** |
| Tệp root | 11 | 11 | UNCHANGED |
| **Tệp (tổng)** | 1.735 | **1.751** | +16, trong đó **+15 là vùng nội dung (thật)**; phần agent home **dao động ±1, không tính là tăng** |
| Thư mục root | 9 | 9 | UNCHANGED |
| Thư mục vùng nội dung (đệ quy) | — | 23 | 09-29 không công bố riêng |
| Thư mục tầng đầu agent home | — | 42 | 09-29 không công bố riêng |
| **Thư mục (tổng)** | 70 | **74** | 9 + 23 + 42. **70 của 09-29 không khớp bất kỳ tổ hợp nào hôm nay** |

**Kết luận:** chênh **+15 tệp vùng nội dung** là khớp với kiểm chứng độc lập bằng `git status` (§ Delta): +7 concept, +4 source, +2 topic, +2 report validator. Chênh **+4 thư mục** **không tái lập được** — đây là lỗi đếm của lượt trước, không phải KB dày thêm.

**🔴 BA NGUỒN TRÔI SỐ LIỆU — cả ba đều tái lập được, không phải KB biến đổi:**

1. *Do chính lượt ghi:* báo cáo nằm trong `wiki/reviews/` — thuộc vùng nội dung — nên **1.641 → 1.642 vùng nội dung** sau khi ghi ⇒ tổng **1.752**.
2. *Do socket:* hôm nay có **2 socket** (`.hermes/gateway.sock`, `.hermes/state/gateway.loop-tick.1299.sock`), `stat.S_ISSOCK` = True, `os.path.isfile` và `islink` đều **False**. Đếm bằng "mọi entry không phải thư mục" sẽ tính nhầm 2 socket thành tệp ⇒ **1.753**. Số đã loại socket là **98**, lấy mẫu 5 lần liên tiếp đều ra 98.
3. 🆕 **Do agent runtime tạo/xoá tệp tạm ở tầng đầu agent home** — nguồn này **hôm nay mới phát hiện** và nó làm hỏng khả năng tái lập của tổng: lúc quét (23:30) tầng đầu agent home có **99** tệp, lúc verify (23:55) còn **98**. Tệp biến mất là `.hermes/.skills_prompt_snapshot.json` (mtime 23:15, **artifact tạm theo session** — không phải file cấu hình), đồng thời có 3 tệp `state.db.malformed-backup-20260617_082024{,-shm,-wal}` xuất hiện. Trong 98 tệp tầng đầu, **46 có dấu hiệu biến động** (`.db*`, `-shm`, `-wal`, `.lock`, `.pid`, `.sock`, `*cache*`, `.log`, `spawn-ledger`, `gateway_state`) — đây là runtime đang sống, không phải nội dung kho.

**Vì vậy báo cáo này phân biệt rõ hai loại số:**
- **Ổn định (dùng để so sánh): 1.653 tệp** = 1.641 vùng nội dung + 11 tệp root, cộng **74 thư mục**. Đây là phần duy nhất nên so với 09-29.
- **Biến động (không nên so): 98 tệp tầng đầu agent home.**

**Bài học cho lượt sau:** muốn một con số tái lập được thì phải **loại socket** (như 09-29 đã học) **và** hoặc loại luôn tầng đầu agent home, **hoặc** chấp nhận nó biến động và công bố riêng. Nếu phải công bố tổng, phải ghi rõ **phần nào ổn định, phần nào không** — không được để người đọc tưởng tổng là số đếm ổn định.

---

## 🔴 E1 — `.hermes/auth.json` git-tracked **và đã push** — CARRY-FORWARD, **đính chính bằng chứng**

**Path:** `.hermes/auth.json` (11.003 B) · **Severity:** ERROR · **Category:** Path / Secret exposure

Không thay đổi so 09-29: 78 commit, blob `f9000fc8…`, commit đầu `8695083b` 2026-05-12, HEAD `e05f00ab` == `git ls-remote refs/heads/master` ⇒ **đã trên GitHub**. Tên khoá (grep **tên khoá**, không đọc giá trị): `access_token`, `refresh_token`, `api_key`, `tokens`, `credential_pool`, `secret_fingerprint`.

**🔧 ĐÍNH CHÍNH BẰNG CHỨNG — lỗi phương pháp của lượt 09-29:** báo cáo 09-29 ghi *"`check-ignore` exit 1"* cho các marker và *".gitignore:36-38 CÓ rule"* cho `auth.json`, suy ra rule vô hiệu vì commit trước rule. **Hai lệnh đó dùng `git check-ignore` dạng thường, mà git BỎ QUA file đã tracked** (git docs: tracked files are not shown). Chứng minh:

| Lệnh | `.hermes/auth.json` |
|---|---|
| `git check-ignore -v` (thường) | `rc=1` — **không có output** (bị bỏ qua vì tracked) |
| `git check-ignore --no-index -v` | `.gitignore:37:.hermes/auth.json` `rc=0` |

**Phán quyết thay đổi:** với file **đã tracked**, `rc=1` của `check-ignore` thường **không chứng minh gì** — phải dùng `--no-index` để biết rule có tồn tại không, và `git ls-files -s` để biết file còn tracked không. Mọi lượt trước đã dùng exit code thường cho file tracked. **Kết luận của 09-29 vẫn đúng** (file tracked, rule không cứu được) nhưng **bằng chứng thì sai** — hôm nay đã lặp lại probe trên 21 tệp.

**Suggested fix (Fix Agent, sau khi Julius duyệt — theo thứ tự):** (1) Julius kiểm visibility repo — public ⇒ coi là sự cố lộ dữ liệu, **rotate token trước mọi việc git**; (2) `git rm --cached .hermes/auth.json .hermes/auth.lock` + commit; (3) rewrite lịch sử nếu token còn hiệu lực (78 commit chứa nó) — `git-secret-cleanup`; (4) rotate ở provider sau khi rewrite.

---

## 🔴 E2 — ERROR MỚI: **4 tệp auth trong `.openclaw/` + 1 trong `.hermes/state-snapshots/`** đều git-tracked

Đây là phần 09-29 **không** tìm ra: E1 chỉ soi `access_token`/`api_key` ở `auth.json`. Hôm nay quét `git ls-tree -r HEAD` theo **tên tệp** trong cả hai agent home (trừ `skills/`), ra **7 tệp tên auth đã tracked**, 5 tệp dưới đây là **mới**:

| Tệp | Blob | Commit | Rule `.gitignore` (`--no-index`) | Verdict |
|---|---|---|---|---|
| `.openclaw/device-auth.json` | 461 B | 1 | `:57` có | **rule có, vô hiệu** |
| `.openclaw/identity/device-auth.json` | 461 B | 1 | `:71 .openclaw/identity/` có | **rule có, vô hiệu** |
| `.openclaw/agents/main/agent/auth-profiles.json` | 752 B | 1 | `:72 .openclaw/agents/` có | **rule có, vô hiệu** |
| `.openclaw/agents/main/agent/auth-state.json` | 469 B | 1 | `:72 .openclaw/agents/` có | **rule có, vô hiệu** |
| `.hermes/state-snapshots/20260626-005403-pre-update/auth.json` | 8.201 B | 1 | **không có rule nào** | tracked, không rule |

**Blast radius:** mỗi tệp 1 commit ⇒ commit phải xem là nào (chưa truy, không đọc nội dung). Cả 5 đều nằm trong HEAD `e05f00ab` == remote ⇒ **đã trên GitHub**.

**Suggested fix:** `git rm --cached` cả 5 + commit; thêm rule `.openclaw/agents/`, `.openclaw/identity/`, `.hermes/state-snapshots/` dạng wildcard. Gộp với đợt E1 — một lần rewrite lịch sử xử lý tất cả.

---

## 🔴 E3 — ERROR MỚI: `.hermes/config.yaml` git-tracked, 50 commit, 23.603 B, chứa tên khoá `api_key` / `secret` / `session_key`

**Path:** `.hermes/config.yaml` · **Severity:** ERROR · **Category:** Path / Secret exposure

09-29 có nhắc "config.yaml bản chính cũng đã tracked; nếu chứa khoá API thì phải xử lý như E1 — validator không đọc nội dung". Hôm nay đã kiểm **tên khoá** (không đọc giá trị): `api_key` (2 chỗ), `secret`, `session_key`, `access_token_env`, `tokens`, `record_key`, `redact_secrets`. **Không có rule `.gitignore` nào** khớp. 50 commit, mtime 09-24 20:00 — tức config **đang được sửa liên tục** và mỗi lần sửa là một commit mới chứa lại toàn bộ nội dung.

**Rủi ro chưa định lượng:** validator **không** biết các giá trị `api_key`/`secret` có phải khoá thật hay placeholder (không đọc giá trị theo nguyên tắc). Nhưng vì `redact_secrets` và `access_token_env` cùng nằm trong file, khả năng cao ít nhất một số là thật.

**Suggested fix:** xử lý như E1 (cùng đợt rewrite). **Julius nên tự xem `config.yaml`** — validator cố tình không đọc nội dung.

---

## 🔴 E4 — `.hermes/checkpoints/` git repo lồng, 62 MB — CARRY-FORWARD

**Severity:** ERROR · **Category:** Orphan / repo hygiene

UNCHANGED về cấu trúc: **62 MB** đĩa (`store/objects/pack` ~29 MB), **31 tệp đã tracked**, `store/HEAD` tồn tại ⇒ bare repo lồng. **6.783 tệp `??`** đang chờ commit. `.gitignore` **không có rule nào** chứa `checkpoints` (grep = 0). Pack đã vào lịch sử ở `5d47208d` (09-24 08:31).

**Số chờ commit đã tăng** (xem E10): tổng runtime pending nay là **6.835 tệp / ~34 MB**.

**Suggested fix:** `.gitignore` + `git rm -r --cached .hermes/checkpoints`. **Phải làm TRƯỚC khi bật lại backup** (E10).

---

## 🔴 E5 — `.hermes/.curator_backups/` — CARRY-FORWARD, **đang lớn lên**

**Severity:** ERROR · **Category:** Orphan

230 blob đã tracked (không đổi), nhưng tệp `??` **45 → 52** (09-29: 45). 5,0 MB đĩa. Không rule `.gitignore`. Cùng commit với E4.

**Suggested fix:** `.gitignore` + `git rm -r --cached`. Gộp với E4.

---

## 🔴 E6 — ERROR MỚI (nhóm gộp): **runtime DB + snapshot + bản sao config đã tracked, không rule nào chặn**

Đây là phần mở rộng của E5 của 09-29. Hôm nay probe đầy đủ họ `.db`/`.sqlite`/`.bak`:

| Tệp / thư mục | Đã tracked | Commit | Rule `--no-index` | Ghi chú |
|---|---|---|---|---|
| `.hermes/kanban.db` | có | 3 | **không có** | runtime DB |
| `.hermes/kanban.db-shm` | có | **141** | **không có** | WAL sidecar |
| `.hermes/kanban.db-wal` | có | **141** | **không có** | WAL sidecar |
| `.hermes/projects.db` | có | 1 | **không có** | runtime DB |
| `.hermes/verification_evidence.db` | có | **345** | **không có** | 09-29 đã nêu, xác nhận 345 commit |
| `.hermes/state-snapshots/` (7 tệp, 4,1 MB) | có | 1 | **không có rule `state-snapshots`** | gồm 1 `auth.json` (E2) + `state.db` |
| `.hermes/config.yaml.bak.*` (18 tệp) | **18/18** | 1 mỗi | **không có** | đối xứng thiếu: `.openclaw/*.bak` **có** rule (`.gitignore:73`) |
| `.hermes/MEMORY.md` | có | **172** | `:81 MEMORY.md` có, **vô hiệu** | carry-forward từ 09-29 |

**Khoảng trống đối xứng đã xác nhận bằng grep:** `checkpoints`, `curator_backups`, `config.yaml.bak`, `verification_evidence`, `state-snapshots`, `kanban`, `projects.db`, `auth-profiles`, `auth-state` ⇒ **9 mẫu, không mẫu nào có rule**. Chỉ `.hermes/state.db*` (`:40`) và `.openclaw/main.sqlite` (`:56`) được bảo vệ.

**Consequence phát sinh mới:** `kanban.db-shm`/`-wal` là **WAL sidecar** — mỗi lần Hermes ghi là một blob mới trong commit ⇒ 141 commit chỉ vì hai tệp sidecar này. Tương lai gần như chắc chắn tiếp tục tăng.

**Suggested fix:** thêm rule wildcard cho cả 9 mẫu + `git rm --cached`. **Làm trong cùng đợt với E1–E3, trước khi bật lại backup.**

---

## 🔴 E7 — ERROR MỚI (phần vùng nội dung): **8 tệp đã tracked bị xoá khỏi đĩa**, trong đó **1 tệp nằm trong `wiki/topic/`**

**Severity:** ERROR · **Category:** Orphan

09-29 báo 7 tệp, **toàn bộ trong `.hermes/`**. Hôm nay `git status` cho `D` = **8**, và một tệp **nằm trong vùng nội dung**:

| Tệp | Commit cuối | Vùng |
|---|---|---|
| `wiki/topic/brain-threat-detection.md` | `52170426` 09-21 21:08 | ⚠️ **wiki/topic/** — nội dung tri thức |
| `.hermes/skills/note-taking/obsidian/SKILL.md` | `32b4c6ba` 09-09 | agent home |
| `.hermes/skills/autonomous-ai-agents/computer-use/SKILL.md` | `32b4c6ba` 09-09 | agent home |
| `.hermes/skills/devops/hermes-state-recovery/SKILL.md` | `32b4c6ba` / `48752127` | agent home |
| `.hermes/skills/devops/hermes-state-recovery/references/recovery-log-20260627.md` | — | agent home |
| `.hermes/skills/.curator_backups/2026-08-23T06-02-56Z/{cron-jobs.json,manifest.json,skills.tar.gz}` | `944a66a2` 08-23 | agent home |

**Xác minh trên đĩa:** `test -e` ⇒ **vắng mặt**. Không có tệp `brain-threat` tương tự trong `wiki/topic/` (263 tệp).

**Điểm khác biệt quan trọng:** 7 tệp kia là runtime của agent home (sẽ tự tái tạo hoặc không đáng kể). `wiki/topic/brain-threat-detection.md` là **mục tri thức thật** — mất nó là mất liên kết chỉ mục, và nó đã bị **prune bởi Index Agent** (Format Validator 09-30 ghi nhận độc lập: 258 tracked + 5 `??` = 263 ✓). **Không có backlink nào trong `wiki/` trỏ tới nó** (grep: chỉ 2 validator report nhắc tên) ⇒ mất nó **gần như không để lại dấu vết trong KB**.

**Suggested fix:** Julius xác nhận prune có chủ ý không. Nếu là nội dung thật bị mất ⇒ phục hồi từ `52170426` hoặc compile lại từ raw. **Vì `vault backup` dừng 6 ngày, việc xoá này chưa lên GitHub** — nghĩa là **trên GitHub file vẫn còn**; nếu máy VPS hỏng, mất thật. Ngược lại nếu bật backup, file sẽ biến mất ở cả hai nơi.

---

## 🔴 E8 — 2 marker `.migrated.*` — CARRY-FORWARD, **mtime đứng 22 ngày**, bằng chứng đã đính chính

**Severity:** ERROR · **Category:** Path

| Vị trí | Blob | Commit | Disk | `check-ignore --no-index` |
|---|---|---|---|---|
| `openclaw-workspace-state.json.migrated.43c9aa3….e79d1c6c-…` (root) | `a0105ac6…` | 1 | 69 B · **2026-09-08 20:42** | **không có rule** |
| `.openclaw/workspace-state.json.migrated.43c9aa3….fb077b94-…` | `a0105ac6…` | 1 | 69 B · **2026-09-08 20:42** | **không có rule** |

Cả hai cùng blob `a0105ac6…`, **22 ngày không đổi**, không có rule nào khớp (`.gitignore:88-89` chỉ chặn đúng tên không có hậu tố). Phần bỏ sót vị trí thứ hai là do quy tắc miễn kiểm tra agent home — phải dò tay bằng `find . -name '*migrated*'` (đã làm, ra đúng 2).

**Suggested fix:** wildcard `openclaw-workspace-state.json.migrated.*` **và** `.openclaw/workspace-state.json.migrated.*` + `git rm --cached` cả hai + commit.

---

## 🔴 E9 — `vault backup` dừng **6,11 ngày** — CARRY-FORWARD, ngày thứ 7, leo thang

**Severity:** ERROR · **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08` |
| `git ls-remote --heads origin` (23:30 hôm nay) | `refs/heads/master = e05f00abf29e84c8…` — **remote cũng đứng ở đây** |
| Thời gian | **6,11 ngày** |
| `git rev-list --count e05f00ab..HEAD` | **0** |
| Trạng thái | **324 `M`** (302 vùng nội dung: 258 topic + 25 tag + 15 concept + 1 raw×3 + 1 reviews) + **8 `D`** (E7) + **6.883 `??`** |

**Cổng cửa sổ đang đóng:** vì backup dừng, E4/E5/E6 **chưa** bị commit thêm. Runtime đang chờ: **6.783 `??` checkpoints + 52 `??` curator_backups = 6.835 tệp / ~34 MB**. **Số này nhảy ngay khoảnh khắc backup chạy lại.**

**Đối chiếu `??` toàn repo (6.883):** 6.783 checkpoints · 52 curator_backups · 16 `wiki/reviews` (report chưa commit) · 9 `wiki/concepts` · 8 `.hermes/skills` · 5 `wiki/topic` · 5 `wiki/sources` · 2 `raw/websites` · 2 `raw/posts` · 1 `raw/articles`.

**Suggested fix (thứ tự bắt buộc):** (1) chặn `.gitignore` cho E2–E6, E8 **trước**; (2) xử lý E1/E2/E3; (3) **rồi mới** khởi động lại backup. Validator không push, không commit.

---

## 🔴 E10 — `DREAMS.md` — CARRY-FORWARD, **6 ngày dreaming chưa commit**

**Path:** `DREAMS.md` · **Severity:** ERROR · **Category:** Path

File thường, **13.738 B** (09-29: 12.990 B → **+748**), git-tracked, `check-ignore` exit 1, mtime **2026-09-30 03:00:12** — writer vẫn chạy đúng 03:00 mỗi đêm. Blob đã commit trong HEAD là `64e5ef05…` = **8.932 B** ⇒ **4.806 B chênh lệch chưa lên GitHub**, tức **6 ngày** dreaming.

**Suggested fix:** giữ dữ liệu, sửa writer/output path. Xoá file không giải quyết được (proven nhiều lần).

---

## 🔴 E11 — `memory/` — CARRY-FORWARD, +4 tệp, **10 lượt báo cáo liên tiếp**

**Path:** `memory/` · **Severity:** ERROR · **Category:** Orphan

**89 tệp, 6 thư mục con** (09-29: 85/6 → **+4 tệp**). Chuỗi: 49→53→57→64→68→72→76→81→85→**89**. 4 tệp mới lúc 03:00 hôm nay: `memory/dreaming/deep/2026-09-30.md` (154 B), `.../light/2026-09-30.md` (37 B), `.../rem/2026-09-30.md` (958 B), `memory/.dreams/session-corpus/2026-09-29.txt` (1.461 B). `check-ignore --no-index` ⇒ **IGNORED** (`.gitignore:84 memory/`), nên **chưa lên GitHub** và sẽ không lên nếu writer không đổi.

**Expected:** dữ liệu tác nhân ở `.openclaw/memory/` hoặc `.hermes/memories/`.
**Suggested fix:** sửa **3 đường ghi** writer trước, rồi mới migrate. Không xoá dữ liệu.

---

## 🔴 E12 — `wiki/HEARTBEAT.md` dangling — CARRY-FORWARD, **ngày thứ 4 sau khi đính chính**

**Path:** `wiki/HEARTBEAT.md` · **Severity:** ERROR · **Category:** Orphan

Kiểm bằng `realpath` + `exists` + `lexists`: `islink=True`, target `../../.openclaw/HEARTBEAT.md`, `realpath` = **`/home/julius/.openclaw/HEARTBEAT.md`**, `exists` = **False**, `lexists` = True ⇒ **DANGLING**, sai một cấp thư mục (đúng phải là `../.openclaw/HEARTBEAT.md`). File thật ở `<KB>/.openclaw/HEARTBEAT.md` tồn tại.

**Trạng thái git:** untracked, `--no-index` ⇒ **IGNORED** (`.gitignore:78`). Xoá chỉ là cleanup, không đụng commit.
**Đính chính 09-28 vẫn đúng:** symlink hỏng ⇒ Obsidian **không** hiển thị nó như note thật. Các báo cáo 09-26/09-27 khẳng định "đích tồn tại" là sai.

**4/4 symlink định danh còn lại ở root** (`IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`) đều `realpath` tới `<KB>/.openclaw/…`, `exists=True` ⇒ hợp lệ. `HEARTBEAT.md` ở root vắng mặt — tuỳ chọn theo §2, không tính lỗi.
**Suggested fix:** sửa writer/mirror trước; xoá symlink không chặn được tái tạo.

---

## ⚠️ W1 — 89 WARNING kỹ thuật dưới `memory/` — hệ quả trực tiếp của E11

**Severity:** WARNING · **Category:** Path

**89 trong 104 WARNING máy** là `"Path not classified by any rule"` — bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào. Phân bố: 2 tệp tầng gốc + `dreaming/{deep,light,rem}` + `.dreams/session-corpus/*.txt`. **Toàn bộ là hệ quả của E11**, không phải 89 vấn đề độc lập.
**Suggested fix:** sửa output path writer ở E11 → 89 WARNING tự biến mất, Fix Agent không cần đụng từng tệp.

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` · **Severity:** WARNING
§7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung. **15 tệp, không đổi** (so 09-17→09-29). Tổng archive 177 tệp / 5 thư mục tháng.
**Suggested fix:** Julius chốt chính sách (giữ / chuyển / cho phép ngoại lệ §7). Validator **không tự đổi tên bản sao thành báo cáo**.

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7 + điều khoản tự mâu thuẫn

**Severity:** WARNING
(a) Bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`/`format`/`hygiene`. Tệp `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md` tồn tại từ 06-15, `find` xác nhận **không có tệp `spot-check` mới** — tồn đọng, không phải phát hiện mới.
(b) §6 cây `raw/` cho phép `raw.md` rồi ghi `*` ✗ forbidden ở root; §7 cây `wiki/` cho phép `wiki.md` rồi ghi "No files at `wiki/` root level"; §7 Rules yêu cầu `meta/` đúng 3 tệp nhưng cây chỉ hiện 2; §3 cho phép runtime tự do trong agent home, §4 lại hạn chế nội bộ skills.
**Suggested fix:** thống nhất văn bản. **Lưu ý:** §3 chính là nguyên nhân gốc khiến E1–E7 lọt qua bộ quét.

## ⚠️ W4 — WARNING MỚI: **cặp topic trùng nghĩa** `cuoc-dua-khong-di-lui.md` / `cuoc-dua-khong-i-lui.md`

**Path:** `wiki/topic/` · **Severity:** WARNING · **Category:** Naming

Phát hiện bằng kiểm tra mới: chuẩn hoá slug (bỏ dấu + hạ chữ thường) trên **toàn bộ 10 vùng nội dung** để tìm trùng. Kết quả: **0 trùng chính xác** — nhưng phát hiện **1 cặp gần trùng do 2 cách phiên tự khác nhau cho cùng một câu tiếng Việt**:

| Tệp | Cỡ | Nội dung |
|---|---|---|
| `wiki/topic/cuoc-dua-khong-di-lui.md` | 611 B | `topic: cuoc-dua-khong-di-lui` · **Concepts (1)** → `[[cuoc-dua-khong-di-lui]]` |
| `wiki/topic/cuoc-dua-khong-i-lui.md` | 643 B | `topic: cuoc-dua-khong-i-lui` · **Concepts (0)**, **Sources (1)** → `[[src_cuoc-ua…]]` |

Cả hai mốc `auto_generated`, `last_updated: 2026-09-30`, **cùng mtime 21:03:45** — Index Agent tạo cùng một lượt. Cùng một chủ đề ("cuốc đua không đi lùi") bị **tách làm hai file chỉ mục**, nội dung nằm rải rác: một bên chỉ có concept, bên kia chỉ có source.
**Suggested fix:** Index Agent nên canonical hoá slug trước khi tạo topic (bỏ dấu thống nhất). Gộp 2 file thành 1. Validator **không** tự gộp — cần kiểm tra concept/source bên dưới có trùng nội dung không.

## ⚠️ W5 — Quy tắc miễn kiểm tra agent home che mất **4 nhóm ERROR mới hôm nay** (leo thang từ 4 lên 8)

**Severity:** WARNING · **Category:** Path

09-29 ghi "che mất 4 ERROR". Hôm nay, sau khi dò tay bằng `git ls-tree`/`ls-files`, tổng ERROR **thực tế** trong agent home là **8** (E1, E2, E3, E4, E5, E6, E8) — bộ quét chỉ báo **4**. **Bằng chứng:** các mẫu không ai dò trước đây (`device-auth`, `auth-profiles`, `auth-state`, `state-snapshots`, `kanban.db-wal`, `config.yaml.bak.*`) **không nằm trong tên tệp mà các lượt trước đã grep**.

**Đây là lỗi của bộ quét, không phải của KB** — nói rõ để không tính nhầm thành phát hiện KB mới.
**Suggested fix:** nới quy tắc sang "kiểm mọi tệp có khả năng chứa bí mật hoặc khối lượng lớn" (`*auth*`, `*.json`, `*.db*`, `*.bak*`, `*.pack`, `config.*`, `*.env`) **bất kể độ sâu**, và dùng `git ls-files -s` + `check-ignore --no-index` cho từng hit (E1).

## ⚠️ W6 — INFO — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/` · **Severity:** INFO
**111 tệp `.md`** ở tầng active (09-29: 108 → +3 = 2 report hôm nay + báo cáo này); **38 tệp mtime cũ hơn 2026-08-30** (sớm nhất `2026-06-01_output-report.md`), không đổi. `wiki/drafts/` = 1 tệp (`analysis-2026-advice.md`), không đổi.
**Số lượng phụ thuộc trạng thái approved/applied** nên không dùng một số chưa đối chiếu làm quyết định.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không xoá hoặc archive hàng loạt.

---

## 🔺 [SYSTEMATIC VIOLATION] — **lần đầu escalate**: runtime artifact trong agent home không có `.gitignore`

09-29 đã đặt ngưỡng rõ: *"E1–E5 là phát hiện mới nhưng thuộc loại cấu hình — chưa đủ căn cứ gọi là vi phạm hệ thống, nếu lượt sau còn y hệt thì khi đó mới escalate."* Lượt sau **không còn y hệt** — nó **lớn lên và mở rộng**:

- Nhóm E4/E5 tăng: curator_backups `??` 45 → **52**.
- Mở rộng sang **5 mẫu chưa từng ai kiểm**: `kanban.db` + 2 WAL sidecar (141 commit mỗi tệp), `projects.db`, `state-snapshots/`, `config.yaml.bak.*` 18/18.
- Mở rộng sang **auth ở `.openclaw/`** (4 tệp) + **snapshot trong `.hermes/`** (1 tệp).
- **9/9 mẫu runtime** không có rule nào, trong khi `.openclaw/*.bak` và `.hermes/state.db*` thì có ⇒ **vùng `.hermes/` không được bảo vệ.**

**Root-cause:** `.gitignore` được viết theo danh sách tệp đã biết, không phải theo mẫu; và agent runtime **sinh thêm loại tệp mới** (WAL sidecar, snapshot, backup) ngoài danh sách đó. Hai điều kiện cùng giữ ⇒ lỗi tái lặp có hệ thống.

**Recommendation:** (1) `.gitignore` theo **mẫu wildcard** cho toàn bộ runtime, không liệt kê tệp; (2) `git rm --cached` một lượt cho cả nhóm; (3) kiểm định lại bằng `git ls-files .hermes .openclaw | wc -l` sau khi sửa — mục tiêu **chỉ còn lại skill + tài liệu**; (4) thêm kiểm tra này vào **Output/Format Validator** để phát hiện sớm hơn 1 ngày.

---

## Delta so với 09-29

| Hạng mục | 09-29 (23:30) | 09-30 (23:30) | Kết luận |
|---|---|---|---|
| Định nghĩa phạm vi | 1.735 tệp + 70 thư mục | **1.751 tệp + 74 thư mục = 1.825** (chỉ **1.653 tệp** ổn định) | **ĐỔI định nghĩa thư mục** (70 không tái lập được); tệp vùng nội dung **+15** khớp kiểm chứng `git status`; phần agent home **dao động ±1** |
| Machine findings | 104 (4E + 100W) | **108 (4E + 104W)** | +4 = `memory/` 85→89 |
| ERROR nhóm | 10 | **13** | **+3 nhóm mới** (E2, E3, E6); E7 mở rộng sang vùng nội dung |
| **ERROR thực tế (dò tay)** | ≥4 trong agent home | **≥8 trong agent home** | +4 nhóm bị bộ quét che; 9/9 mẫu runtime không rule |
| `vault backup` | dừng 5,11 ngày | **dừng 6,11 ngày** | remote vẫn `e05f00ab`; 324 `M` + 8 `D` + 6.883 `??` |
| Runtime chờ commit | 6.828 tệp / 14,4 MB | **6.835 tệp / ~34 MB** | checkpoints 6.783 + curator 52 |
| `DREAMS.md` | 12.990 B | **13.738 B** | +748; blob HEAD 8.932 B ⇒ **6 ngày** chưa commit |
| `memory/` | 85 tệp / 6 thư mục | **89 tệp / 6 thư mục** | +4 tệp; **lượt thứ 10** |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, **22 ngày**, bằng chứng đã đính chính |
| `wiki/HEARTBEAT.md` | dangling | **dangling** | UNCHANGED, xác minh lại bằng `realpath`+`exists`+`lexists` |
| Tệp bị xoá (tracked) | 7 (đều `.hermes/`) | **8 (1 trong `wiki/topic/`)** | `brain-threat-detection.md` — mất nội dung thật |
| `config.yaml.bak.*` | "18 tệp đã tracked" | **18/18 tracked, 0 rule** | xác nhận đầy đủ |
| `.hermes/MEMORY.md` | tracked | tracked, **172 commit** | rule `:81` vô hiệu |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 | 1 | UNCHANGED, tồn đọng |
| Trùng chuẩn hoá slug | chưa kiểm | **0 trùng, 1 cặp gần trùng** | kiểm mới (W4) |
| Thư mục rỗng | 0 | **0** | UNCHANGED |
| Lỗi naming/path vùng nội dung | 0 | **0** | 1.641 tệp, kiểm bằng classifier + slug độc lập |
| Vùng nội dung 24h | 0 tệp mới | **27 tệp mới** (5 raw + 19 concept + 4 source + 5 topic) | batch đầu tiên sau 6 ngày; Compile Agent chạy 08:07–08:17 |

**Đã xác minh PASS (không chỉ suy đoán):** 14/14 index bắt buộc; 4/4 symlink định danh root có đích tồn tại; 0 thư mục rỗng; **0 lỗi naming/path** trong 1.641 tệp nội dung; 0 trùng slug chuẩn hoá trên 10 vùng; `.hermes/.env` **được ignore đúng** (`*.env`, `rc=0`) dù chứa `GOOGLE_API_KEY`/`TELEGRAM_BOT_TOKEN` — không phải lỗi; 15 archive backup + 1 `spot-check` là tồn đọng đã biết.

---

## Actions Needed

1. **🔴 E1/E2/E3 — kiểm tra secret ngay (không cần chờ duyệt).** Repo public hay private? Public ⇒ **rotate token trước mọi việc git**: `auth.json` (11.003 B, 78 commit) + **4 tệp auth trong `.openclaw/`** + 1 trong `state-snapshots` + `config.yaml` (23.603 B, 50 commit, có `api_key`/`secret`/`session_key`). Tổng 7 tệp tên auth đã tracked. `git-secret-cleanup` có sẵn.
2. **🔴 Chặn `.gitignore` TRƯỚC khi bật lại backup.** 9 mẫu runtime chưa có rule: `checkpoints`, `curator_backups`, `state-snapshots`, `kanban.db*`, `projects.db`, `verification_evidence.db`, `config.yaml.bak.*`, `.openclaw/agents/`, `.openclaw/identity/`. Bật backup ngay lúc này ⇒ commit kế tiếp nuốt **6.835 tệp / ~34 MB**. Việc 1 phút chặn 1 thất bại lớn.
3. **🔴 E7 — xác nhận `wiki/topic/brain-threat-detection.md` bị prune có chủ ý không.** Đây là lần đầu trong 2 ngày mà việc xoá **chạm vùng nội dung**, không chỉ agent home. Trên GitHub file **vẫn còn** (backup dừng) — nếu muốn phục hồi thì còn kịp.
4. **🔴 E9 — `vault backup` dừng 6,11 ngày.** Remote cũng đứng ở `e05f00ab` ⇒ lỗi tiến trình backup, không phải push trễ. 324 tệp `M` + 8 `D` + 6.883 `??` đang chờ.
5. **Sửa 3 writer** (`memory/` ×3 đường, `DREAMS.md`, mirror `wiki/HEARTBEAT.md`) trước, rồi mới migrate/dọn. Xoá file không dừng được writer — E11 đã 10 lượt, E12 4 lượt, E10 6 lượt.
6. **W4 — Index Agent canonical hoá slug trước khi tạo topic** (cặp `cuoc-dua-khong-{di,i}-lui`), và gộp 2 file thành 1.
7. **W5 — nới quy tắc miễn kiểm tra agent home trong bộ quét**; validator tự sửa skill, không đụng `wiki/`.
8. **Chốt chính sách 15 archive backup + loại `spot-check`**, và **thống nhất §6/§7/§3-§4**.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*
