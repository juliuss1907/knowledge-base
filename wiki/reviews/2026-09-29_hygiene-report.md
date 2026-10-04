# Hygiene Inspection — 2026-09-29
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 17 nhóm (10 ERROR, 6 WARNING, 1 INFO)
**Created:** 2026-09-29 23:30 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,805 đường dẫn trong phạm vi (1,735 tệp + 70 thư mục) — định nghĩa: 4 vùng nội dung + 11 tệp/symlink ở root + tầng đầu hai agent home + 9 thư mục root. Đây là số **ổn định, tái lập được** (đo bằng `find -type f -o -type l`, tức loại socket); xem mục 3 về hai nguồn trôi số liệu.
**Machine findings:** 104 (4 ERROR, 100 WARNING) + 6 ERROR mới phát hiện bằng dò tay ngoài tầm bộ quét = 17 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## Phạm vi và bằng chứng

1. Quét toàn cây từ `/home/julius/knowledge-base`. Loại `.git/`, `.obsidian/`, `node_modules/`. Tầng đầu `.hermes/` + `.openclaw/` được kiểm; nội bộ sâu hơn tầng đầu miễn kiểm tra theo quy tắc — **và đó chính là nơi 3 ERROR mới bị bỏ sót** (xem E1–E3, E10).
2. Bộ quét đi qua **241,104 tệp** (nội bộ `.hermes/` chiếm phần lớn). **Con số này không phải số đường dẫn kiểm tra** và không dùng để suy ra tăng/giảm.
3. **Đối chiếu định nghĩa đếm với 09-28 — giữ nguyên, có thể so sánh.** 09-28 dùng định nghĩa "4 vùng nội dung + tệp root + tầng đầu hai agent home" và công bố 1,733 tệp + 70 thư mục. Hôm nay **cùng định nghĩa** cho **1,735 tệp + 70 thư mục** (1.626 vùng nội dung + 98 tầng đầu agent home + 11 root). Chênh +2 tệp = 2 báo cáo validator hôm nay (format/output) — **không phải KB tăng nội dung**.
   **Hai nguồn trôi số liệu — cả hai đều tái lập được, không phải KB biến đổi. Báo cáo này dùng số ổn định (1.735) và công bố cả hai nguồn trôi:**
   - *Do chính lượt ghi:* báo cáo nằm trong `wiki/reviews/` — thuộc vùng nội dung — nên **1.734 lúc quét → 1.735 sau ghi**.
   - *Do socket runtime:* `.hermes/gateway.sock` là **socket thật** (`stat.S_ISSOCK` = True; `os.path.isfile` và `islink` đều **False**; `file` = `socket`). Nếu đếm bằng "mọi entry không phải thư mục" thì socket **bị tính nhầm thành tệp** và cho ra 99 thay vì 98 — và con số đó còn dao động theo vòng đời socket. Số **98** là số tệp/symlink thật, đo bằng `find -type f -o -type l`, ổn định qua 5 lần lấy mẫu liên tiếp.
   **Bài học cho lượt sau:** muốn số đếm tái lập được thì định nghĩa phải **loại socket**, không chỉ loại thư mục. Ba lượt verify liên tiếp của chính lượt chạy này đã lộ ra điều đó (100 → 99 → 98) — mỗi lần là một FAIL *giả* do cách đếm, không phải do KB.
4. Không có lỗi quyền truy cập. **0 thư mục rỗng** trong `context/`, `raw/`, `wiki/`, `scripts/`. Toàn bộ 14 index bắt buộc tồn tại: `context/context.md`, `context/USER.md`, `raw/raw.md`, 6 index raw, `wiki/wiki.md`, `wiki/meta/` đủ 3 tệp, `wiki/tag/tag.md`.
5. **0 lỗi naming/path trong `wiki/sources` (212), `wiki/concepts` (605), `wiki/topic` (261), `wiki/tag` (25), `wiki/drafts` (1), `raw/` (224), `context/` (2).** Kiểm bằng cả classifier của bộ quét lẫn kiểm tra slug độc lập.

---

## 🔴 E1 — ERROR MỚI, NGHIÊM TRỌNG: `.hermes/auth.json` git-tracked **và đã push lên GitHub**

Đây là phát hiện mới, không phải carry-forward. Các báo cáo trước chưa từng kiểm tra nội dung được track trong agent home.

**Path:** `.hermes/auth.json` (11,003 byte), `.hermes/auth.lock` (0 byte)
**Severity:** ERROR
**Category:** Path / Secret exposure

**Bằng chứng (không đọc giá trị bí mật, chỉ metadata + tên khoá):**

| Kiểm tra | Kết quả |
|---|---|
| `git ls-tree -r HEAD` | `.hermes/auth.json` **có trong HEAD** |
| Blob trong HEAD | `f9000fc8…`, **11,003 byte** |
| `git log -- .hermes/auth.json` | **78 commit**, commit đầu `8695083b` 2026-05-12 19:17 |
| HEAD cục bộ vs remote | `e05f00ab…` == `git ls-remote refs/heads/master` = `e05f00ab…` ⇒ **đã trên GitHub** |
| `git status` | **không hiện `M`** ⇒ nội dung trên đĩa khớp bản đã commit |
| `.gitignore:36-38` | CÓ rule `.hermes/auth.json` + `auth.lock` — **nhưng vô hiệu** |
| Tên khoá trong file | `access_token`, `refresh_token`, `api_key`, `tokens`, `credential_pool`, `secret_fingerprint` (grep **tên khoá**, không đọc giá trị) |

**Vì sao rule `.gitignore` không cứu được:** file đã được commit **2026-05-12**, rule `.gitignore` thêm **sau đó**. Git không hề áp dụng `.gitignore` cho tệp đã tracked. Xác minh bằng `git check-ignore --no-index` (bỏ qua trạng thái index) ⇒ rule **có** khớp; nhưng `git ls-files -s` vẫn trả về dòng ⇒ tệp vẫn tracked. Đây là cơ chế quen thuộc, không phải lỗi cấu hình.

**Rủi ro:** nếu repo là **public**, toàn bộ `access_token` / `refresh_token` / `api_key` đã công khai từ 2026-05-12 và có hiệu lực tới lúc token hết hạn. Repo gọi tên `juliuss1907/knowledge-base`; `gh` không xác minh được visibility (HTTP 401, token hợp lệ không có) nên **validator không khẳng định được public hay private — Julius phải tự kiểm tra**.

**Suggested fix (Fix Agent, sau khi Julius duyệt — theo thứ tự):**
1. **Julius: kiểm tra visibility repo.** Nếu public → coi như sự cố lộ dữ liệu, **thu hồi/rotate token ngay**, không chờ sửa git.
2. `git rm --cached .hermes/auth.json .hermes/auth.lock` + commit.
3. **Quyết định có rewrite lịch sử hay không.** Nếu token còn hiệu lực: rewrite bắt buộc, vì 78 commit chứa nó. `git-secret-cleanup` skill đã có sẵn cho việc này — Julius đã từng chọn phương án "làm cho đúng một lần" thay vì vá tạm.
4. Rotate token ở provider sau khi rewrite, không chỉ xoá khỏi index.

**Validator không sửa, không commit, không rotate.**

---

## 🔴 E2 — ERROR MỚI: `.hermes/checkpoints/` là git repo lồng nhau, đã commit 29 MB pack và còn 6.783 tệp `??`

**Path:** `.hermes/checkpoints/`
**Severity:** ERROR
**Category:** Orphan / repo hygiene

**Current:**

| Kiểm tra | Kết quả |
|---|---|
| Dung lượng đĩa | **62 MB**; riêng `store/objects/pack` = **29 MB** |
| Tệp trên đĩa | **6.814** |
| `git ls-files .hermes/checkpoints` | **31 tệp ĐÃ tracked** (HEAD, config, hooks mẫu, 2 pack file, 2 ledger, 2 project) |
| Blob pack đã commit | **28,899,905 byte** (`.pack`) + 452 KB (`.idx`) + 64 KB (`.rev`) |
| Tệp `??` chưa track | **6.783 tệp, 13,0 MB** |
| Commit đưa vào | `5d47208d vault backup: 2026-09-24 08:31:38` |
| `.gitignore` | **không có** bất kỳ rule nào chứa `checkpoints` (grep = 0 hit) |
| Cấu trúc | có `store/HEAD` ⇒ **bare git repo lồng bên trong repo chính** |

**Expected:** agent home chỉ chứa skill + config + runtime state. Runtime state đã được liệt kê ignore ở `.gitignore:36-53` (`state.db*`, `logs/`, `sessions/`, `cron/`, `cache/`…) — nhưng `checkpoints/` **không nằm trong danh sách đó**, nên nó trượt qua.

**Hậu quả cụ thể khi `vault backup` chạy lại:** commit kế tiếp sẽ nuốt **6.783 tệp / 13 MB** runtime artifact, và mỗi lần checkpoint store repack lại là một lần churn thêm. Pack 29 MB đã vào lịch sử thì `.gitignore` không gỡ được.

**Suggested fix (Fix Agent):** thêm `.hermes/checkpoints/` vào `.gitignore`, `git rm -r --cached .hermes/checkpoints`, commit. Quyết định rewrite lịch sử cho 29 MB pack thuộc cùng câu hỏi với E1 — **làm chung một lần**, không tách.

---

## 🔴 E3 — ERROR MỚI: `.hermes/.curator_backups/` — 230 blob đã tracked, còn 45 tệp `??`

**Path:** `.hermes/.curator_backups/`
**Severity:** ERROR
**Category:** Orphan

**Current:** 4,4 MB trên đĩa. `git ls-files` = **230 blob đã tracked**; `??` = **45 tệp, 1,4 MB**. Không có rule `.gitignore` (grep `curator` = 0 hit). Cùng commit với E2: `5d47208d` 09-24 08:31.
**Expected:** runtime backup của skill curator thuộc agent home, không nằm trong kho.
**Suggested fix:** `.gitignore` + `git rm -r --cached`. Gộp với đợt E1/E2.

---

## 🔴 E4 — ERROR MỚI: 7 tệp đã tracked bị **xoá khỏi đĩa**, chưa commit

**Path:** `.hermes/skills/`
**Severity:** ERROR
**Category:** Orphan

**Current (`git status` = `D`, tức có trong HEAD nhưng không còn trên đĩa):**

| Tệp | Commit cuối |
|---|---|
| `.hermes/skills/note-taking/obsidian/SKILL.md` | `32b4c6ba` 09-09 11:48 |
| `.hermes/skills/autonomous-ai-agents/computer-use/SKILL.md` | `32b4c6ba` 09-09 11:48 |
| `.hermes/skills/devops/hermes-state-recovery/SKILL.md` | `48752127` 06-27 10:01 |
| `.hermes/skills/devops/hermes-state-recovery/references/recovery-log-20260627.md` | — |
| `.hermes/skills/.curator_backups/2026-08-23T06-02-56Z/{cron-jobs.json, manifest.json, skills.tar.gz}` | `944a66a2` 08-23 13:03 |

Đã xác minh trên đĩa: thư mục `note-taking/obsidian/`, `devops/hermes-state-recovery/`, `.curator_backups/2026-08-23T06-02-56Z/` đều **không tồn tại**.

**Expected:** skill đã cài thì không tự biến mất. Ba skill bị xoá cùng commit `32b4c6ba` (09-09) — nghi vấn curator dọn skill, nhưng **validator không đọc log nội bộ để xác nhận**, chỉ nêu mốc thời gian.
**Rủi ro:** vì `vault backup` đã dừng 5 ngày, việc xoá này **chưa lên GitHub** — nên nếu máy VPS hỏng, 3 SKILL.md vẫn còn trên GitHub; ngược lại nếu backup chạy lại, chúng sẽ biến mất khỏi cả hai nơi.
**Suggested fix:** Julius xác nhận 3 skill này là cố ý gỡ hay curator xoá nhầm. Nếu cố ý → commit xoá. Nếu nhầm → phục hồi từ `e05f00ab`.

---

## 🔴 E5 — ERROR MỚI: 18 bản sao `config.yaml.bak.*` + `verification_evidence.db` + `MEMORY.md` đã tracked

**Path:** `.hermes/config.yaml.bak.*` (18 tệp), `.hermes/verification_evidence.db`, `.hermes/MEMORY.md`
**Severity:** ERROR
**Category:** Path

**Current:**
- 18 tệp `config.yaml.bak.*` (mtime 06-14 → 08-21) đã tracked. `git check-ignore --no-index` ⇒ **RULE-ALLOWS** (không có rule nào chặn). `.openclaw/*.bak` **có** rule (`.gitignore:73`) — nhưng `.hermes/` thì không. Đây là **khoảng trống đối xứng** trong `.gitignore`.
- `.hermes/verification_evidence.db` đã tracked, `RULE-ALLOWS`. Cỡ không xác định (không đọc nội dung).
- `.hermes/MEMORY.md` đã tracked, dù `.gitignore:81` có rule `MEMORY.md` — **vô hiệu vì đã commit trước rule**, cùng cơ chế với E1.

**Expected:** bản sao config và DB runtime không thuộc kho. **Lưu ý:** `config.yaml` bản chính cũng đã tracked; nếu nó chứa khoá API thì phải xử lý như E1 — validator không đọc nội dung để đánh giá.
**Suggested fix:** wildcard `.hermes/config.yaml.bak.*` + `.hermes/verification_evidence.db` vào `.gitignore`, `rm --cached`. Kiểm tra khoá trong `config.yaml` như một phần của đợt E1.

---

## 🔴 E6 — `vault backup` dừng **5,11 ngày** — CARRY-FORWARD, ngày thứ 6, leo thang

**Severity:** ERROR | **Category:** Orphan

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08` |
| `git ls-remote` (hôm nay 23:33) | `refs/heads/master = e05f00ab…` — **remote cũng đứng ở đây** |
| Số ngày | **5,11** (09-24 20:51 → 09-29 23:30) |
| Commit mới kể tắt HEAD | `git rev-list --count e05f00ab..HEAD` = **0** |
| Entry chưa commit | **313 `M`** (291 trong vùng nội dung: 259 topic + 25 tag + 3 concept + 1 reviews + 3 raw; 22 trong `.hermes`/`.openclaw`) + **7 `D`** + **6.859 `??`** (6.783 checkpoints + 45 curator + 13 report + 11 nội dung + 8 skill) |

**Điểm mới hôm nay:** vì backup dừng, các runtime artifact ở E2/E3 **chưa** bị commit thêm — nên E2/E3 mới chỉ ở mức "31 tệp đã lọt vào lịch sử" chứ chưa phải "hàng nghìn tệp". **Khi backup chạy lại, con số sẽ nhảy từ 31 lên 6.814.** Đây là lý do phải chặn `.gitignore` *trước khi* bật lại backup, không phải sau.

**Suggested fix:** (1) chặn `.gitignore` cho E2/E3/E5 **trước**; (2) xử lý E1; (3) rồi mới khởi động lại backup. Validator không push, không commit.

---

## 🔴 E7 — `DREAMS.md` — CARRY-FORWARD, writer vẫn chạy, chênh lệch commit đã lên 5 ngày

**Path:** `DREAMS.md` | **Severity:** ERROR | **Category:** Path
**Current:** file thường, **12,990 byte** (09-28: 12,231 → **+759**), git-tracked, `check-ignore` exit 1 (không ignored), mtime **2026-09-29 03:00:12** — writer vẫn chạy đúng 03:00 mỗi đêm. Blob đã commit trong HEAD là `64e5ef05…` = **8,932 byte** ⇒ **4,058 byte chênh lệch chưa lên GitHub**, không phải 1 ngày mà là 5 ngày dreaming.
**Expected:** §2 không liệt kê.
**Suggested fix:** giữ dữ liệu, sửa writer/output path. **Xoá file không giải quyết được** (proven nhiều lần).

---

## 🔴 E8 — `memory/` — CARRY-FORWARD, +4 tệp, **9 lần báo cáo liên tiếp**

**Path:** `memory/` | **Severity:** ERROR | **Category:** Orphan
**Current:** **85 tệp, 6 thư mục** (09-28: 81/7 → **+4 tệp, −1 thư mục**). Chuỗi: 49→53→57→64→68→72→76→81→**85**. 4 tệp mới 03:00 hôm nay: `memory/dreaming/{deep,light,rem}/2026-09-29.md` + `memory/.dreams/session-corpus/2026-09-28.txt` (11,544 byte). **2 tệp tầng gốc**: `2026-09-17.md`, `2026-09-28.md`. `check-ignore` ⇒ **IGNORED** (`.gitignore:84`).
**Expected:** dữ liệu tác nhân ở `.openclaw/memory/` hoặc `.hermes/memories/`.
**Suggested fix:** sửa **3 đường ghi** writer trước, rồi mới migrate. Không xoá dữ liệu.

---

## 🔴 E9 — Marker `.migrated.*` — CARRY-FORWARD, mtime đứng **21 ngày**

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3…c72b.e79d1c6c-…` (root) + `.openclaw/workspace-state.json.migrated.…fb077b94-…`
**Severity:** ERROR | **Category:** Path
**Current:** mỗi tệp 69 byte, mtime **2026-09-08 20:42 — không đổi 21 ngày**. Cả hai tracked, **cùng blob `a0105ac6…`**, `check-ignore` exit 1. `.gitignore:88-89` chỉ chặn đúng tên `openclaw-workspace-state.json` + `.attested` — **không có wildcard**.
**Suggested fix:** wildcard `openclaw-workspace-state.json.migrated.*` + `git rm --cached` **cả hai** + commit. Marker thứ hai nằm trong `.openclaw/` nên bộ quét bỏ sót — phải dò tay bằng `find . -name '*.migrated.*'`.

---

## 🔴 E10 — `wiki/HEARTBEAT.md` dangling — CARRY-FORWARD, **ngày thứ 3 sau khi đính chính**

**Path:** `wiki/HEARTBEAT.md` | **Severity:** ERROR | **Category:** Orphan
**Current:** symlink (28 byte) → `../../.openclaw/HEARTBEAT.md`. Kiểm bằng `realpath` + `exists` + `lexists`: `realpath` = `/home/julius/.openclaw/HEARTBEAT.md`, `exists` = **False**, `lexists` = True ⇒ **DANGLING**, sai một cấp thư mục. Đúng phải là `../.openclaw/HEARTBEAT.md`. File thật ở `<KB>/.openclaw/HEARTBEAT.md` tồn tại.
**Trạng thái git:** untracked, `check-ignore` ⇒ **IGNORED** (`.gitignore:78`). Xoá chỉ là cleanup, không đụng commit.
**Khẳng định sửa từ 09-28 vẫn đúng:** symlink hỏng ⇒ Obsidian **không** hiển thị nó như note thật. Các báo cáo 09-26/09-27 nói "đích tồn tại" là sai, 09-28 đã đính chính — hôm nay xác minh lại, **đính chính vẫn giữ**.
**4/4 symlink định danh còn lại ở root** (`IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`) đều `realpath` tới `<KB>/.openclaw/…` và `exists=True`. `HEARTBEAT.md` ở root **vắng mặt** — tùy chọn theo §2, không tính lỗi.
**Suggested fix:** sửa writer/mirror trước; xoá symlink không chặn được tái tạo.

---

## ⚠️ W1 — 85 WARNING kỹ thuật dưới `memory/` — gom 1 nhóm nguyên nhân

**Path:** `memory/.dreams/session-corpus/*.txt`, `memory/dreaming/{deep,light,rem}/*.md`, 2 tệp tầng gốc
**Severity:** WARNING | **Category:** Path
**Issue:** **85 trong 100 WARNING máy** là `"Path not classified by any rule"` — bộ quét rơi vào `classify_generic_path()` vì `memory/` không thuộc classifier nào. **Toàn bộ là hệ quả trực tiếp của E8**, không phải 85 vấn đề độc lập.
**Current:** 85 tệp — 2 tầng gốc + 21 `.dreams/session-corpus/*.txt` + 62 `dreaming/*` (mỗi nhánh 20-21).
**Suggested fix:** sửa output path writer ở E8 → 85 WARNING tự biến mất, **Fix Agent không cần đụng từng tệp**.

## ⚠️ W2 — [SPEC CONFLICT] 15 bản sao lưu trong vùng archive

**Path:** `wiki/reviews/archive/2026-09/*-backup-*.md` | **Severity:** WARNING
**Issue:** §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.
**Current:** **15 tệp, không đổi** so 09-17/09-24/09-25/09-26/09-27/09-28. Tổng archive = 177 tệp.
**Suggested fix:** Julius chốt chính sách trước (giữ / chuyển / cho phép ngoại lệ §7). Validator **không tự đổi tên bản sao thành báo cáo** — làm vậy là bịa báo cáo.

## ⚠️ W3 — [SPEC CONFLICT] Loại `spot-check` lệch §7

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Issue:** bộ quét chấp nhận `spot-check`; §7 chỉ liệt kê `output`, `format`, `hygiene`.
**Current:** tồn tại từ 06-15. `find` xác nhận **không có tệp `spot-check` mới** — không phải phát hiện tồn đọng.
**Suggested fix:** cập nhật §7 hoặc sửa classifier. Không tự sửa tệp lịch sử.

## ⚠️ W4 — [SPEC CONFLICT] Điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md` (v1.2, không đổi)
**Issue:** (a) §6 cây `raw/` cho phép `raw.md` rồi lại ghi `*` ✗ forbidden ở root; (b) §7 cây `wiki/` cho phép `wiki.md` rồi lại ghi "No files at `wiki/` root level"; (c) §7 Rules yêu cầu `meta/` có đúng 3 tệp nhưng cây chỉ hiển thị 2; (d) §3 cho phép runtime tự do trong agent home, §4 lại hạn chế nội bộ skills.
**Current:** đã dùng ngoại lệ cụ thể cho từng trường hợp để không báo nhầm index hợp lệ.
**Suggested fix:** Julius/Fix Agent thống nhất văn bản. **Lưu ý:** §3 (cho phép runtime trong agent home) chính là lý do E1–E3 lọt qua bộ quét — quy tắc miễn kiểm tra độ sâu >1 quá rộng.

## ⚠️ W5 — [SPEC CONFLICT] Quy tắc miễn kiểm tra agent home che mất 3 ERROR hôm nay

**Severity:** WARNING | **Category:** Path
**Issue:** quy tắc "skip `.hermes/`/`.openclaw/` at depth > 1" bỏ sót E1, E2, E3, E5 — toàn bộ nằm ở tầng đầu hoặc sâu hơn nhưng lọt qua `classify_generic_path()`.
**Current:** bộ quét báo **4 ERROR**, thực tế agent home chứa **ít nhất 4 ERROR chưa được báo** + hàng nghìn tệp runtime untracked.
**Suggested fix:** nới quy tắc sang "kiểm tra tệp có khả năng chứa bí mật hoặc khối lượng lớn" (`*.json`, `*.db`, `*.pack`, `config.*`) bất kể độ sâu. Đây là **lỗi của bộ quét, không phải của KB** — nói rõ để không tính nhầm thành phát hiện KB mới.

## ⚠️ W6 — INFO — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/`
**Issue:** số lượng phụ thuộc trạng thái approved/applied nên **không dùng một số chưa đối chiếu làm quyết định**.
**Current:** **108 tệp `.md`** ở tầng active (09-28: 105 → +3 = 2 report hôm nay + `_action-required.md`); **38 tệp mtime cũ hơn 2026-08-30** (sớm nhất `2026-06-01_output-report.md`), 70 tệp mới hơn. `wiki/drafts/` = 1 tệp (`analysis-2026-advice.md`), không đổi.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không xoá hoặc archive hàng loạt.

---

## Delta so với 09-28

| Hạng mục | 09-28 (23:34) | 09-29 (23:30) | Kết luận |
|---|---|---|---|
| Định nghĩa phạm vi | 1,733 tệp + 70 thư mục | **1,735 tệp + 70 thư mục** | **CÙNG định nghĩa** — +2 = 2 báo cáo validator hôm nay, so sánh được |
| Machine findings | 100 (4E + 96W) | **104 (4E + 100W)** | +4 = `memory/` 81→85 |
| ERROR nhóm | 6 | **10** | **+4 MỚI** (E1–E5: secret, checkpoints, curator, xoá skill, config backups) |
| `vault backup` | dừng 4 ngày | **dừng 5,11 ngày** | remote vẫn `e05f00ab`; 313 `M` + 7 `D` + 6.859 `??` |
| `DREAMS.md` | 12.231 B | **12.990 B** | +759; blob HEAD 8.932 B ⇒ **5 ngày dreaming chưa commit** |
| `memory/` | 81 tệp / 7 thư mục | **85 tệp / 6 thư mục** | +4 tệp, −1 thư mục; chuỗi 9 lần |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, 21 ngày, cùng blob |
| `wiki/HEARTBEAT.md` | dangling (đính chính) | **dangling, xác minh lại** | Đính chính 09-28 vẫn đúng |
| `openclaw-workspace-state.json` | vắng mặt | **vắng mặt** | UNCHANGED |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 | 1 | UNCHANGED |
| Tệp nội dung mới 24h | 10 (4 raw + 6 batch 09-26) | **0** | 7 `.md` mới = 1 `DREAMS.md` + 3 `memory/` + 3 báo cáo validator; **vùng nội dung đứng yên** |
| Thư mục rỗng | 0 | 0 | UNCHANGED |
| Lỗi naming/path vùng nội dung | 0 | **0** | Kiểm bằng classifier + slug độc lập |

**Đã xác minh PASS (không chỉ suy đoán):** 14/14 index bắt buộc; 4/4 symlink định danh root có đích tồn tại; 0 thư mục rỗng; **0 lỗi naming/path** trong 7 vùng nội dung (1.725 tệp); 15 archive backup + 1 `spot-check` là tồn đọng đã biết, không phải phát hiện mới.

**Không phát lại `[SYSTEMATIC VIOLATION]`.** E6–E10 là CARRY-FORWARD hoặc `[SPEC CONFLICT]`. E1–E5 là phát hiện mới nhưng thuộc loại *cấu hình* (gitignore/visibility) — chưa đủ căn cứ gọi là vi phạm hệ thống, nếu lượt sau còn y hệt thì **khi đó** mới escalate.

---

## Actions Needed

1. **🔴 E1 — kiểm tra `auth.json` ngay (ưu tiên cao nhất, không cần chờ duyệt).** Repo public hay private? Nếu public → **rotate token trước khi làm bất cứ việc git nào**, vì `access_token`/`refresh_token`/`api_key` đã công khai từ 2026-05-12 qua 78 commit. Sau đó mới `git rm --cached` và cân nhắc rewrite lịch sử (`git-secret-cleanup` skill đã có sẵn).
2. **🔴 Chặn `.gitignore` cho E2/E3/E5 TRƯỚC khi bật lại backup.** Hiện `.gitignore` không có rule nào cho `.hermes/checkpoints/`, `.hermes/.curator_backups/`, `.hermes/config.yaml.bak.*`, `.hermes/verification_evidence.db`. Bật lại backup bây giờ ⇒ commit kế tiếp nuốt **6.828 tệp / 14,4 MB** runtime artifact. Đây là việc 1 phút chặn 1 thất bại lớn.
3. **🔴 Xác nhận 3 SKILL.md bị xoá** (`note-taking/obsidian`, `autonomous-ai-agents/computer-use`, `devops/hermes-state-recovery`) là cố ý gỡ hay curator xoá nhầm. Commit chứa chúng: `32b4c6ba` 09-09 11:48.
4. **Sửa writer `memory/` (3 đường ghi) và writer `DREAMS.md`** trước, rồi mới migrate/dọn. Xoá file không dừng được writer — đã chứng minh qua 9 lượt báo cáo.
5. **Sau approval: xử lý 2 marker `.migrated.*`** — wildcard `.gitignore` + `git rm --cached` cả hai vị trí. Tồn đọng 21 ngày.
6. **Sửa mirror `wiki/HEARTBEAT.md`** (dangling vì sai cấp thư mục) + sửa `quick-scan.sh` mục 4 theo phát hiện của Output Validator 09-29.
7. **Nới quy tắc miễn kiểm tra agent home trong bộ quét** (W5) — bỏ sót 4 ERROR có thật. Validator tự sửa skill; không đụng `wiki/`.
8. **Chốt chính sách 15 archive backup + loại `spot-check`** và **thống nhất §6/§7/§3-§4**.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không đọc **giá trị** bí mật (E1 chỉ grep **tên khoá**), không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*
