# Hygiene Inspection — 2026-09-27
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 9 nhóm (5 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-09-27 23:30 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,833 đường dẫn trong phạm vi (1,800 tệp + 33 thư mục)
**Machine findings:** 4 (4 ERROR, 0 WARNING) + 1 ERROR phát hiện bằng dò tay ngoài tầm bộ quét = 9 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## Phạm vi và bằng chứng

1. Quét toàn cây từ `/home/julius/knowledge-base`, không đi theo symlink. Loại `.git/`, `.obsidian/`, `node_modules/`. Kiểm tra tầng đầu `.hermes/` và `.openclaw/`; nội bộ sâu hơn tầng đầu miễn kiểm tra theo quy tắc. Không đọc nội dung memory/log — chỉ path và metadata.
2. Bộ quét đi qua 138,679 tệp vì tính nội bộ nhà tác nhân (`.hermes/` một mình 241,109 tệp). **Con số này không phải số đường dẫn kiểm tra** và không được dùng để suy ra tăng/giảm kho.
3. **Số liệu phạm vi so với 09-26 — dùng đúng định nghĩa:** 1.800 tệp (09-26: 1.796) → **+4 tệp**. Con số này so sánh được vì cả hai lần đềm cùng cách (nội dung 5 vùng + tệp root + tầng đầu hai agent home). **Toàn bộ +4 là do `memory/` 72 → 76**, không có tệp nào mới ở `wiki/`, `raw/`, `context/`.
4. Không có lỗi quyền truy cập. Không có thư mục rỗng trong `wiki/`, `raw/`, `context/`, `scripts/`. Toàn bộ index bắt buộc tồn tại: `context/context.md`, `context/USER.md`, `raw/raw.md`, 6 index raw (`articles`→`repos` đều OK), `wiki/wiki.md`, `wiki/meta/` đủ 3 tệp.
5. `find … -newer wiki/reviews/2026-09-26_hygiene-report.md` trên `wiki/sources wiki/concepts wiki/topic wiki/tag raw context` trả về **0 tệp**. Không có ingest/compile nào trong 24h. Đây là lần thứ 2 liên tiếp KB đứng yên hoàn toàn.

---

## ⚠️ Đính chính cách đo — 87 WARNING của 09-26 KHÔNG phải đã được sửa

Báo cáo này có **4 ERROR / 0 WARNING**; 09-26 có **4 ERROR / 87 WARNING**. Sự biến mất 87 cảnh báo **không phải kết quả xử lý** — đó là **thay đổi cách đo**. Bộ quét hôm nay gom toàn bộ tệp con dưới `memory/` thành **một nhóm nguyên nhân duy nhất** (Issue 2) thay vì liệt kê từng tệp. 72 tệp `.dreams/session-corpus/*.txt` + `dreaming/{deep,light,rem}/*.md` vẫn còn nguyên, writer vẫn chạy, không tệp nào bị xóa hay sửa tên.

**Quy tắc đọc số liệu:** "0 WARNING" hôm nay nghĩa là **không có lỗi naming/path mới ngoài các nhóm đã gom**. Không nghĩa là vùng nội dung sạch hơn hôm qua. Nếu báo cáo sau chỉ trích số WARNING mà không nói cách gom nhóm, sẽ tạo ảo giác tiến bộ giả.

---

## Issue 1: DREAMS.md ở root — CARRY-FORWARD, writer VẪN CHẠY (ngày thứ 4)

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File gốc ngoài whitelist §2. Tồn tại từ 09-24; chưa có bằng chứng nào cho thấy đã xử lý.
**Current:** File thường, **11,368 bytes** (09-26 ghi 10,550 → **+818 byte**), git-tracked (`git ls-files -s` → blob `64e5ef05…`), `git check-ignore` exit 1, mtime **2026-09-27 03:00:12 +0700**. Ba commit `vault backup` gần nhất chứa file: `3a10b393` (09-24), `234399ba` (09-23), `3194424d` (09-18).
**Expected:** §2 chỉ liệt kê `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, 5 symlink định danh, `.gitignore`.
**Suggested fix:** Giữ dữ liệu. Sửa writer/output path, hoặc cập nhật §2 nếu giữ ở gốc là chủ ý. **Xóa file không giải quyết được** — writer sinh lại mỗi đêm 03:00 và `vault backup` tự commit.

---

## Issue 2: memory/ ở root — CARRY-FORWARD, vẫn tăng đều 4 file/ngày

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Root folder ngoài whitelist §2. Báo cáo 09-25 từng ghi "đã ngừng sinh file", 09-26 đã đính chính là sai. Hôm nay xác nhận lại: writer chạy **đều đặn mỗi đêm 03:00**.
**Current:** **76 file, 6 subdirectory** (09-26: 72 file, 6 subdir → **+4 file**). Cấu trúc: `memory/dreaming/{deep,light,rem}/`, `memory/.dreams/session-corpus/`. 4 file mới mtime **2026-09-27 03:00**: `dreaming/deep/2026-09-27.md`, `dreaming/light/2026-09-27.md`, `dreaming/rem/2026-09-27.md`, `.dreams/session-corpus/2026-09-26.txt`. Chuỗi tăng: 49→53→57→64→68→72→**76**. Không git-tracked; `.gitignore:84` khớp `memory/`.
**Expected:** Dữ liệu tác nhân nằm trong `.openclaw/memory/` hoặc `.hermes/memories/`; hoặc ngoại lệ được duyệt và ghi vào quy chuẩn.
**Suggested fix:** Không xóa dữ liệu. Sửa writer trước, sau đó lập kế hoạch migrate/cleanup có xác minh. **Đây là 7 lần báo cáo liên tiếp, mối tăng đều 4 file/ngày chưa đổi** — vòng lặp không tự thoát nếu chỉ xóa file.

---

## Issue 3: Marker migration ở root — CARRY-FORWARD, chưa xử lý

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3…c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker vận hành ở root, đã bị Git theo dõi, **không** được ignore.
**Current:** 69 bytes, mtime 2026-09-08 20:42 (**không đổi 19 ngày**). `git ls-files -s` → tracked, blob `a0105ac6…`. `git check-ignore` exit 1.
**Expected:** Không runtime artifact ở root; wildcard migration artifact phải được ignore.
**Suggested fix:** Sau approval: thêm `openclaw-workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached`, commit. `.gitignore:88-89` hiện chỉ chặn đúng tên `openclaw-workspace-state.json` và `.attested` — **không có wildcard**. Validator không sửa.

---

## Issue 4: Marker migration thứ hai trong `.openclaw/` — CARRY-FORWARD từ E1 09-25, chưa xử lý

**Path:** `.openclaw/workspace-state.json.migrated.43c9aa3…c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker thứ hai của cùng một lần migration, nằm trong agent home. **Không xuất hiện trong machine findings** — quy tắc miễn kiểm tra độ sâu > 1 trong agent home bỏ sót; phải dò tay bằng `find . -name '*.migrated.*'`.
**Current:** 69 bytes, mtime 2026-09-08 20:42 (**không đổi 19 ngày**). `git ls-files -s` → tracked, **cùng blob `a0105ac6…`** với marker ở Issue 3. `git check-ignore` exit 1 — **không marker nào được ignore**.
**Expected:** Không runtime artifact dạng file tracked trong agent home.
**Suggested fix:** Wildcard `.gitignore` cho **cả hai vị trí** (`.openclaw/workspace-state.json.migrated.*` và `openclaw-workspace-state.json.migrated.*`) + `git rm --cached` **cả hai** marker + commit. Đây là hạng mục duy nhất từ addendum 09-25 chưa có dấu hiệu đã được động tới sau 2 ngày.

---

## Issue 5: wiki/HEARTBEAT.md — CARRY-FORWARD, symlink trỏ tới file thật

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Heartbeat đặt sai vùng — nằm ngoài agent home. Đây là process leak tái diễn, không phải artifact rơi rác.
**Current:** Symlink `../../.openclaw/HEARTBEAT.md` (28 bytes, tạo 08-26 17:01). **Đích hiện TỒN TẠI**: `.openclaw/HEARTBEAT.md`, 16,688 bytes, mtime 2026-09-09 13:15. Untracked (`git ls-files -s` rỗng) nhưng **đã bị ignore** (`git check-ignore` in ra path, exit 0) — khác 4 ERROR còn lại, nên xóa file chỉ là cleanup, không đụng commit. Vì symlink hợp lệ nên nó hiển thị trong Obsidian như một note thật.
**Expected:** Heartbeat chỉ ở agent home, hoặc ngoại lệ đã được quy chuẩn cho phép.
**Suggested fix:** Xác định và sửa writer/mirror trước — xóa symlink không chặn được tái tạo. Bốn symlink định danh còn lại ở root (`IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`) đều có đích tồn tại. **Root `HEARTBEAT.md` đang vắng mặt** (không phải symlink, không tồn tại) — §2 cho phép tùy chọn nên **không** coi là lỗi.

---

## Issue 6: [SPEC CONFLICT] 15 bản sao lưu trong vùng reviews/archive

**Path:** `wiki/reviews/archive/2026-09/`
**Severity:** WARNING
**Category:** Path
**Issue:** 15 tệp `*-backup-*.md` nằm trong vùng archive. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.
**Current:** 15 tệp, **không đổi** so với 09-17/09-24/09-25/09-26 (danh sách và số lượng giống hệt). Không phải phát hiện mới.
**Expected:** Chính sách rõ: canonical report name, hoặc nơi lưu riêng được cho phép.
**Suggested fix:** Julius chốt chính sách trước; Fix Agent chỉ chuyển/dọn sau khi xác minh dữ liệu. Validator **không tự đổi tên bản sao thành báo cáo** — làm vậy là bịa báo cáo.

---

## Issue 7: [SPEC CONFLICT] Loại `spot-check` lệch danh sách báo cáo ở §7

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Bộ quét chấp nhận `spot-check` như loại report hợp lệ; §7 chỉ liệt kê `output`, `format`, `hygiene`.
**Current:** Tệp lưu trữ đã tồn tại từ 06-15. **Không phải phát hiện mới hôm nay** — không có tệp `spot-check` mới nào.
**Expected:** Script và quy chuẩn có cùng danh sách loại báo cáo.
**Suggested fix:** Cập nhật §7 nếu giữ `spot-check`, hoặc sửa classifier sau khi chính sách rõ. Không tự sửa tệp lịch sử.

---

## Issue 8: [SPEC CONFLICT] Điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Bốn điểm tự mâu thuẫn trong cùng một tài liệu:
- §6 cây `raw/` cho phép `raw.md` rồi lại ghi `*` ✗ forbidden ở `raw/` root.
- §7 cây `wiki/` cho phép `wiki.md` rồi lại ghi "No files at `wiki/` root level".
- §7 Rules yêu cầu `meta/` có đúng 3 tệp (thêm `index-spec.md`), nhưng cây `meta/` chỉ hiển thị 2. Cây thực tế có đủ 3.
- §3 cho phép runtime tự do trong agent home, §4 lại hạn chế nội bộ skills.
**Current:** Đã dùng ngoại lệ cụ thể để không báo nhầm index hợp lệ. Quy chuẩn v1.2 không đổi.
**Expected:** Ngoại lệ và phạm vi nhà tác nhân nêu nhất quán.
**Suggested fix:** Julius/Fix Agent thống nhất văn bản. Validator không sửa quy chuẩn.

---

## Issue 9: INFO — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Vùng active chứa lịch sử nhiều ngày. Số lượng phụ thuộc trạng thái approved/applied nên **không dùng một số chưa đối chiếu làm quyết định**.
**Current:** 102 tệp `.md` ở tầng active; **38 tệp có mtime cũ hơn 2026-08-27** (sớm nhất `2026-06-01_*`), 64 tệp mới hơn. Không có bằng chứng tệp mới gây tồn đọng hôm nay.
**Expected:** Báo cáo hoàn tất nên ở `archive/YYYY-MM/`; báo cáo pending giữ truy vết.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không tự xóa hoặc archive hàng loạt.

---

## Passing / Delta so với 09-26

| Hạng mục | 09-26 (23:30) | 09-27 (23:30) | Kết luận |
|---|---|---|---|
| Tệp trong phạm vi | 1,796 | **1,800** | +4, **toàn bộ** do `memory/` 72→76 |
| Machine findings | 91 (4E + 87W) | **4 (4E + 0W)** | 87W → gom thành 1 nhóm Issue 2, **không phải đã sửa** |
| ERROR nhóm | 5 | **5** | UNCHANGED, 0 resolved, 0 mới |
| Marker `.migrated.*` | 2 (1 trong `.openclaw/`) | 2 | UNCHANGED, cả hai vẫn tracked + không ignored, mtime đứng yên 19 ngày |
| `DREAMS.md` | 10,550 bytes | **11,368 bytes** | +818, vẫn ghi 03:00, vẫn git-tracked |
| `memory/` | 72 file | **76 file** | +4, chuỗi tăng đều 7 lần |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 tệp lưu trữ | 1 | UNCHANGED |
| `wiki/drafts/` | 1 tệp | 1 (`analysis-2026-advice.md`) | UNCHANGED, tên hợp lệ |
| Thư mục rỗng | 0 | 0 | UNCHANGED |
| Tệp mới trong `wiki/`+`raw/`+`context/` | 8 (từ batch 09-26) | **0** | KB đứng yên, lần thứ 2 liên tiếp |
| Lỗi path/naming mới trong `raw/`, `wiki/`, `context/` | 0 | **0** | — |

**Đã xác minh PASS (không chỉ suy đoán):**
- 6/6 index raw tồn tại; `raw/raw.md`, `wiki/wiki.md`, `context/context.md`, `context/USER.md` tồn tại.
- `wiki/meta/` đủ 3 tệp theo §7 Rules.
- 4/5 symlink định danh ở root có đích tồn tại; `HEARTBEAT.md` root vắng mặt (tùy chọn theo §2).
- Không thư mục rỗng trong 4 vùng nội dung.
- 0 tệp mới trong 24h; 0 lỗi naming/path ở vùng nội dung.

**Không phát lại `[SYSTEMATIC VIOLATION]`.** `DREAMS.md`, `memory/`, marker `.migrated.*`, `wiki/HEARTBEAT.md`, bản sao lưu và ba xung đột quy chuẩn đã nêu ở các báo cáo pending. Mọi mục trên đây là CARRY-FORWARD hoặc `[SPEC CONFLICT]`.

---

## Actions Needed

1. **`memory/` — 7 lần báo cáo liên tiếp, mối tăng không đổi (4 file/ngày).** Chuỗi 49→53→57→64→68→72→76 chứng minh xóa file không dừng được writer. Cần sửa **output path của writer** (kể cả đường `memory/.dreams/session-corpus/`), rồi mới migrate/cleanup. Giữ nguyên dữ liệu.
2. **Sau approval, xử lý 2 marker `.migrated.*`:** wildcard `.gitignore` cho cả hai vị trí + `git rm --cached` + commit. Hạng mục tồn đọng từ addendum 09-25, chưa có dấu hiệu đã động tới sau 2 ngày.
3. **Sửa writer `DREAMS.md`** (11,368 bytes, +818/ngày, đã bị `vault backup` commit) và **mirror `wiki/HEARTBEAT.md`**. Xóa file không giải quyết được: `DREAMS.md` được ghi lại 03:00 mỗi đêm; symlink HEARTBEAT trỏ tới file thật nên lọt vào Obsidian.
4. **Chốt chính sách 15 archive backup** (giữ / chuyển / cho phép ngoại lệ §7) và **loại `spot-check`**.
5. **Thống nhất điều khoản mâu thuẫn** §6/§7/§3-§4 trong `folder-structure.md`.
6. **Ghi nhận cách gom nhóm vào báo cáo sau** — nếu không nói rõ, "0 WARNING" sẽ bị đọc nhầm là tiến bộ.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không sửa cấu trúc, không sửa file ngoài `wiki/reviews/`.*
