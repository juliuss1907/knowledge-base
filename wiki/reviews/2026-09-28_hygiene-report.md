# Hygiene Inspection — 2026-09-28
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 11 nhóm (6 ERROR, 4 WARNING, 1 INFO)
**Created:** 2026-09-28 23:34 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,803 đường dẫn trong phạm vi (1,733 tệp + 70 thư mục) — định nghĩa: 4 vùng nội dung + tệp root + tầng đầu hai agent home
**Machine findings:** 100 (4 ERROR, 96 WARNING) + 2 ERROR phát hiện bằng dò tay ngoài tầm bộ quét = 11 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## Phạm vi và bằng chứng

1. Quét toàn cây từ `/home/julius/knowledge-base`, không đi theo symlink. Loại `.git/`, `.obsidian/`, `node_modules/`. Kiểm tra tầng đầu `.hermes/` và `.openclaw/`; nội bộ sâu hơn tầng đầu miễn kiểm tra theo quy tắc. Không đọc nội dung memory/log — chỉ path và metadata.
2. Bộ quét đi qua **138,734 tệp** vì tính nội bộ nhà tác nhân (`.hermes/` một mình 241,111 tệp). **Con số này không phải số đường dẫn kiểm tra** và không được dùng để suy ra tăng/giảm kho.
3. **Đính chính số liệu phạm vi so với 09-27.** 09-27 công bố 1,833 đường dẫn (1,800 tệp + 33 thư mục) — **không tái lập được** từ định nghĩa nào mà báo cáo đó nêu. Hôm nay dùng định nghĩa tường minh ở trên: **1,733 tệp** (context 2 + raw 224 + wiki 1,391 + scripts 5 + tệp root 11 + tầng đầu agent home 100) và 70 thư mục. Chênh −67 tệp so với 1,800 của 09-27 là **khác phạm vi đếm, không phải KB co lại**. Từ báo cáo này trở đi, chỉ so sánh được khi hai báo cáo dùng cùng định nghĩa.
4. Không có lỗi quyền truy cập. Không có thư mục rỗng trong `wiki/`, `raw/`, `context/`, `scripts/`. Toàn bộ index bắt buộc tồn tại: `context/context.md`, `context/USER.md`, `raw/raw.md`, 6 index raw (`articles`→`repos` đều OK), `wiki/wiki.md`, `wiki/meta/` đủ 3 tệp.
5. **KB đã chuyển động trở lại sau 2 ngày đứng yên.** `find -newer` trả về 293 tệp, nhưng phân rã bằng `git status --porcelain -uall` cho thấy: **chỉ 10 tệp thực sự mới** (untracked) + **290 tệp bị Index Agent ghi lại** (tracked, mtime đồng loạt 21:06). Không lấy 293 làm "293 tệp mới".

---

## 🔴 Phát hiện mới — `vault backup` dừng 4 ngày, 311 entry chưa lên GitHub

Đây là hạng mục mới, không phải carry-forward. Ba validator ngày 09-28 đã phát hiện `git log` không đổi nhưng chưa nêu nguyên nhân; hôm nay đã xác minh bằng `git ls-remote`.

**Path:** repo `juliuss1907/knowledge-base` (nhánh `master`)
**Severity:** ERROR
**Category:** Orphan

**Current — bằng chứng read-only, không fetch:**

| Mốc | Giá trị |
|---|---|
| HEAD cục bộ | `e05f00ab vault backup: 2026-09-24 20:51:08 +0700` |
| `git ls-remote` (hôm nay 23:33) | `refs/heads/master = e05f00ab…` — **remote cũng đứng ở đây** |
| Commit/ngày gần nhất | 09-24: 22 commit → 09-25…09-28: **0 commit** |
| `git ls-files` tối đa | `.hermes/MEMORY.md` (đúng 1 dòng ` M` cho phần repo) |
| Entry chưa commit | **300 tệp `M`** (259 topic + 25 tag + 3 concept + 3 index raw + 10 khác) + **11 report `??`** (09-25→09-28 hygiene/format/output) |

Lưu ý: nhánh `main` trên remote là **nhánh cũ** (`ead50c82`, 2026-05-11, "KB v2 skeleton"), không phải nơi đồng bộ. `master` mới là nhánh đang dùng. Không phải lỗi nhánh.

**Expected:** commit tự động mỗi ~10 phút do Obsidian Git plugin trên máy chính (`autoCommitInterval` 5 phút, `autoPushInterval` 10 phút, `commitMessage: "vault backup: {{date}}"` — đọc từ `.obsidian/plugins/obsidian-git/data.json`).

**Rủi ro:** toàn bộ công việc 09-25→09-28 đang chỉ nằm trên đĩa VPS. Mất máy hoặc mất thư mục là mất 11 báo cáo validator + 300 tệp index đã regenerate + 4 raw ingest mới. Đây là rủi ro mất dữ liệu, không phải vấn đề hình thức.

**Suggested fix:** **Julius** — kiểm tra máy chính: Obsidian còn mở không, Git plugin còn bật không, push có bị chặn bởi conflict hay token hết hạn không. `.gitignore` **không** ignore 11 report `??` (đã xác minh `check-ignore` exit 1), nên chúng sẽ được commit ngay khi backup chạy lại — không cần can thiệp. Validator không push, không commit, không gọi Obsidian.

---

## ⚠️ Đính chính — `wiki/HEARTBEAT.md` **dangling**, các báo cáo 09-26 và 09-27 đã khẳng định sai

Hai báo cáo trước nói "đích hiện TỒN TẠI (16,688 bytes)". Hôm nay kiểm tra bằng `os.path.realpath` thay vì so đường dẫn tương đối — **kết luận sai**.

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan

**Current:** symlink (28 byte) → `../../.openclaw/HEARTBEAT.md`. Phân giải từ `wiki/` cho `../../.openclaw/HEARTBEAT.md` = `/home/julius/.openclaw/HEARTBEAT.md` — **KHÔNG tồn tại** (`os.path.exists` → `False`, `lexists` → `True`). File thật nằm ở `<KB>/.openclaw/HEARTBEAT.md` (16,688 byte, tồn tại) — tức symlink **sai một cấp thư mục**, đúng đường dẫn phải là `../.openclaw/HEARTBEAT.md`.

**Hệ quả thực tế:** symlink hỏng thì Obsidian **không** hiển thị nó như note thật. Nhận định 09-27 "vì symlink hợp lệ nên nó hiển thị trong Obsidian như một note thật" **không còn đúng**. Đây là lý do vì sao không thấy nó trong graph view.

**Trạng thái git:** untracked (`git ls-files -s` rỗng) nhưng **đã bị ignore** — `.gitignore:78:HEARTBEAT.md` khớp. Nên xóa chỉ là cleanup, không đụng commit.

**Suggested fix:** xác định và sửa writer/mirror trước — nó vẫn là process leak tái tạo. Root `HEARTBEAT.md` đang **vắng mặt** (§2 cho phép tùy chọn, không tính lỗi). Bốn symlink định danh còn lại ở root (`IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`) đều có đích tồn tại — đã xác minh.

---

## Issue 1: `DREAMS.md` ở root — CARRY-FORWARD, writer VẪN CHẠY (ngày thứ 5)

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path

**Issue:** File gốc ngoài whitelist §2. Tồn tại từ 09-24; chưa có bằng chứng nào cho thấy đã xử lý.
**Current:** File thường, **12,231 bytes** (09-27 ghi 11,368 → **+863 byte**), git-tracked, `git check-ignore` exit 1 (không ignored), mtime **2026-09-28 03:00:12 +0700** — writer vẫn chạy đúng 03:00 mỗi đêm.
**Expected:** §2 chỉ liệt kê `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, 5 symlink định danh, `.gitignore`.
**Suggested fix:** Giữ dữ liệu. Sửa writer/output path, hoặc cập nhật §2 nếu giữ ở gốc là chủ ý. **Xóa file không giải quyết được.** Lưu ý mới: vì `vault backup` đã dừng, nội dung hiện tại (blob `a623d6fc…`) **chưa** được commit — bản committed còn là blob `64e5ef05…` từ 09-24. Khi backup chạy lại, ~4 ngày dreaming sẽ đổ một lần.

---

## Issue 2: `memory/` ở root — CARRY-FORWARD, +5 file, 8 lần báo cáo liên tiếp

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan

**Issue:** Root folder ngoài whitelist §2. 09-25 từng ghi "đã ngừng sinh file", 09-26 đã đính chính là sai. Hôm nay xác nhận lại lần nữa: writer chạy **đều đặn mỗi đêm 03:00**.
**Current:** **81 tệp, 7 thư mục** (09-27: 76 tệp, 6 thư mục → **+5 tệp, +1 thư mục**). Chuỗi tăng: 49→53→57→64→68→72→76→**81**. 5 tệp mới: `memory/dreaming/{deep,light,rem}/2026-09-28.md` (03:00), `memory/.dreams/session-corpus/2026-09-27.txt` (03:00), `memory/2026-09-28.md` (20:45 — **3,125 byte, ghi "Ingest session (Julius, ~19:50–20:40 GMT+7)"**). Cộng thêm `memory/2026-09-17.md` (4,845 byte) là tệp gốc thứ hai. Không git-tracked; `.gitignore:84` khớp `memory/`.
**Expected:** Dữ liệu tác nhân nằm trong `.openclaw/memory/` hoặc `.hermes/memories/`; hoặc ngoại lệ được duyệt và ghi vào quy chuẩn.
**Suggested fix:** Không xóa dữ liệu. Sửa writer trước, sau đó mới lập kế hoạch migrate/cleanup có xác minh. **Đường ghi `memory/YYYY-MM-DD.md` ở tầng gốc là đường thứ 3** sau `.dreams/session-corpus/` và `dreaming/*` — sửa writer phải bao phủ cả ba.

---

## Issue 3: Marker migration ở root — CARRY-FORWARD, mtime đứng 20 ngày

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3…c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path

**Current:** 69 byte, mtime 2026-09-08 20:42 (**không đổi 20 ngày**). `git ls-files -s` → tracked, blob `a0105ac6…`. `git check-ignore` exit 1.
**Expected:** Không runtime artifact ở root; wildcard migration artifact phải được ignore.
**Suggested fix:** Sau approval: thêm `openclaw-workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached`, commit. `.gitignore:88-89` hiện chỉ chặn đúng tên `openclaw-workspace-state.json` và `.attested` — **không có wildcard**. Validator không sửa.

---

## Issue 4: Marker migration thứ hai trong `.openclaw/` — CARRY-FORWARD từ E1 09-25

**Path:** `.openclaw/workspace-state.json.migrated.43c9aa3…c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51`
**Severity:** ERROR
**Category:** Path

**Issue:** Marker thứ hai của cùng một lần migration, nằm trong agent home. **Không xuất hiện trong machine findings** — quy tắc miễn kiểm tra độ sâu > 1 trong agent home bỏ sót; phải dò tay bằng `find . -name '*.migrated.*'`.
**Current:** 69 byte, mtime 2026-09-08 20:42 (**không đổi 20 ngày**). Tracked, **cùng blob `a0105ac6…`** với Issue 3. `git check-ignore` exit 1.
**Expected:** Không runtime artifact dạng file tracked trong agent home.
**Suggested fix:** Wildcard `.gitignore` cho **cả hai vị trí** + `git rm --cached` **cả hai** + commit. Tồn đọng từ addendum 09-25, chưa có dấu hiệu đã được động tới sau 3 ngày.

---

## Issue 5: [SPEC CONFLICT] 15 bản sao lưu trong vùng reviews/archive

**Path:** `wiki/reviews/archive/2026-09/`
**Severity:** WARNING
**Category:** Path

**Issue:** 15 tệp `*-backup-*.md` trong vùng archive. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.
**Current:** 15 tệp, **không đổi** so với 09-17/09-24/09-25/09-26/09-27. Không phải phát hiện mới.
**Suggested fix:** Julius chốt chính sách trước; Fix Agent chỉ chuyển/dọn sau khi xác minh dữ liệu. Validator **không tự đổi tên bản sao thành báo cáo** — làm vậy là bịa báo cáo.

---

## Issue 6: [SPEC CONFLICT] Loại `spot-check` lệch danh sách báo cáo ở §7

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming

**Issue:** Bộ quét chấp nhận `spot-check` là loại report hợp lệ; §7 chỉ liệt kê `output`, `format`, `hygiene`.
**Current:** Tệp lưu trữ tồn tại từ 06-15. **Không phải phát hiện mới** — không có tệp `spot-check` mới nào (đã kiểm bằng `find`).
**Suggested fix:** Cập nhật §7 nếu giữ `spot-check`, hoặc sửa classifier sau khi chính sách rõ. Không tự sửa tệp lịch sử.

---

## Issue 7: [SPEC CONFLICT] Điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md`
**Severity:** WARNING
**Category:** Path

**Issue:** Bốn điểm tự mâu thuẫn trong cùng một tài liệu:
- §6 cây `raw/` cho phép `raw.md` rồi lại ghi `*` ✗ forbidden ở `raw/` root.
- §7 cây `wiki/` cho phép `wiki.md` rồi lại ghi "No files at `wiki/` root level".
- §7 Rules yêu cầu `meta/` có đúng 3 tệp (thêm `index-spec.md`), nhưng cây `meta/` chỉ hiển thị 2. Cây thực tế có đủ 3.
- §3 cho phép runtime tự do trong agent home, §4 lại hạn chế nội bộ skills.

**Current:** Quy chuẩn v1.2 không đổi. Đã dùng ngoại lệ cụ thể để không báo nhầm index hợp lệ.
**Suggested fix:** Julius/Fix Agent thống nhất văn bản. Validator không sửa quy chuẩn.

---

## Issue 8: 81 WARNING kỹ thuật dưới `memory/` — gom 1 nhóm nguyên nhân, **KHÔNG phải 81 lỗi riêng**

**Path:** `memory/.dreams/session-corpus/*.txt`, `memory/dreaming/{deep,light,rem}/*.md`
**Severity:** WARNING
**Category:** Path

**Issue:** 81 trong 96 WARNING máy là `"Path not classified by any rule"` — bộ quét đi tới `classify_generic_path()` vì `memory/` không nằm trong bất kỳ classifier nào. **Toàn bộ là hệ quả của Issue 2**, không phải 81 vấn đề độc lập.
**Current:** 81 tệp: 2 tệp ở tầng gốc `memory/`, 19 tệp `.dreams/session-corpus/*.txt`, 60 tệp `dreaming/{deep,light,rem}/*.md` (20 mỗi nhánh).
**Suggested fix:** Xử lý cùng Issue 2. Nếu sửa output path writer, 81 WARNING này tự động biến mất — **không cần Fix Agent đụng từng tệp**. 15 WARNING còn lại là nhóm archive backup (Issue 5).

---

## Issue 9: INFO — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/`
**Severity:** INFO
**Category:** Orphan

**Issue:** Vùng active chứa lịch sử nhiều ngày. Số lượng phụ thuộc trạng thái approved/applied nên **không dùng một số chưa đối chiếu làm quyết định**.
**Current:** 105 tệp `.md` ở tầng active; **38 tệp có mtime cũ hơn 2026-08-28** (sớm nhất `2026-06-01_format-report.md`), 67 tệp mới hơn. Không có bằng chứng tệp mới gây tồn đọng hôm nay.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không tự xóa hoặc archive hàng loạt.

---

## Delta so với 09-27

| Hạng mục | 09-27 (23:30) | 09-28 (23:34) | Kết luận |
|---|---|---|---|
| Định nghĩa phạm vi | 1,800 tệp + 33 thư mục (không tái lập được) | **1,733 tệp + 70 thư mục** | **Đổi định nghĩa** — không so sánh chéo |
| Machine findings | 4 (4E + 0W) | **100 (4E + 96W)** | 96W = 81 `memory/` + 15 archive, **không phải lỗi mới** |
| ERROR nhóm | 5 | **6** | **+1 MỚI** (`vault backup` dừng 4 ngày) |
| `wiki/HEARTBEAT.md` | "đích tồn tại" | **dangling**, symlink sai 1 cấp | **ĐÍNH CHÍNH** 09-26 + 09-27 |
| HEAD git | `e05f00ab` (09-24 20:51) | `e05f00ab` (09-24 20:51) | **4 ngày không commit**; remote cũng vậy |
| Entry chưa commit | 5 tệp `??` | **300 `M` + 11 report `??`** | Tích tụ trên đĩa VPS |
| `DREAMS.md` | 11,368 byte | **12,231 byte** | +863, vẫn ghi 03:00, chưa được commit |
| `memory/` | 76 tệp / 6 thư mục | **81 tệp / 7 thư mục** | +5, chuỗi tăng đều 8 lần |
| Marker `.migrated.*` | 2 | 2 | UNCHANGED, cả hai tracked + không ignored, mtime đứng 20 ngày |
| Tệp mới trong vùng nội dung | 0 | **10** (4 raw ingest hôm nay + 6 batch 09-26 còn `??`) | Tầng raw chạy lại |
| Tệp Index Agent regenerate | 0 | **290** (259 topic + 25 tag + 6 khác), mtime đồng loạt 21:06 | Không tính là "tệp mới" |
| Lỗi naming/path ở vùng nội dung | 0 | **0** | 10 tệp mới đều hợp lệ |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 tệp lưu trữ | 1 | UNCHANGED |
| `wiki/drafts/` | 1 tệp | 1 (`analysis-2026-advice.md`) | UNCHANGED |
| Thư mục rỗng | 0 | 0 | UNCHANGED |

**Đã xác minh PASS (không chỉ suy đoán):**
- 6/6 index raw + `raw/raw.md` + `wiki/wiki.md` + `context/` đủ 2 tệp + `wiki/meta/` đủ 3 tệp theo §7 Rules.
- 4/4 symlink định danh ở root có đích tồn tại; `HEARTBEAT.md` root vắng mặt (tùy chọn theo §2).
- 0 thư mục rỗng trong 4 vùng nội dung.
- **0 lỗi naming/path trong `wiki/sources`, `wiki/concepts`, `wiki/topic`, `wiki/tag`, `wiki/drafts`, `raw/`, `context/`** — 10 tệp mới đều tuân thủ (kiểm bằng cả classifier của bộ quét lẫn kiểm tra slug độc lập).
- 4 tệp raw ingest hôm nay (`interconnects-ai`, `the-second-derivative`, `why-your-evenings`, `atom-project`) đều theo đúng pattern `YYYY-MM-DD_<slug>.md`.

**Không phát lại `[SYSTEMATIC VIOLATION]`.** `DREAMS.md`, `memory/`, marker `.migrated.*`, `wiki/HEARTBEAT.md`, bản sao lưu và ba xung đột quy chuẩn đã nêu ở các báo cáo pending. Mọi mục là CARRY-FORWARD hoặc `[SPEC CONFLICT]`.

---

## Actions Needed

1. **🔴 Kiểm tra `vault backup` trên máy chính — ưu tiên cao nhất.** 4 ngày không commit, 311 entry chưa lên GitHub, 11 báo cáo validator chỉ nằm trên đĩa VPS. Đây là rủi ro mất dữ liệu, không phải vấn đề hình thức. `.gitignore` không chặn 11 report nên chúng sẽ vào commit đầu tiên khi backup chạy lại.
2. **`memory/` — 8 lần báo cáo liên tiếp, mối tăng không đổi.** Chuỗi 49→…→76→**81** chứng minh xóa file không dừng được writer. Cần sửa **output path của writer** — nay có **3 đường ghi**: `memory/YYYY-MM-DD.md` (tầng gốc), `memory/.dreams/session-corpus/*.txt`, `memory/dreaming/{deep,light,rem}/*.md`. Sửa xong 81 WARNING kèm theo tự biến mất. Giữ nguyên dữ liệu.
3. **Sau approval, xử lý 2 marker `.migrated.*`:** wildcard `.gitignore` cho cả hai vị trí + `git rm --cached` + commit. Tồn đọng từ addendum 09-25, chưa động tới sau 3 ngày.
4. **Sửa writer `DREAMS.md`** (+863 byte/ngày, chưa được commit) và **mirror `wiki/HEARTBEAT.md`** (nay đã dangling vì sai cấp thư mục — sửa writer trước, xóa symlink không chặn được tái tạo).
5. **Chốt chính sách 15 archive backup** (giữ / chuyển / cho phép ngoại lệ §7) và **loại `spot-check`**.
6. **Thống nhất điều khoản mâu thuẫn** §6/§7/§3-§4 trong `folder-structure.md`.
7. **Báo cáo sau phải công bố định nghĩa đếm phạm vi** — nếu không, 1,733 vs 1,800 sẽ bị đọc nhầm là KB co lại 67 tệp.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không sửa cấu trúc, không commit/push, không sửa file ngoài `wiki/reviews/`.*
