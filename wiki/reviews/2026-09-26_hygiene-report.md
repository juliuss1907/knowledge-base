# Hygiene Inspection — 2026-09-26
- **Status:** approved — Julius duyệt hàng loạt 2026-10-02; Connor verify mẫu 6 report (earliest+latest mỗi validator) khớp validator sống; chi tiết xem `wiki/reviews/_action-required.md`
**Issues found:** 9 nhóm (5 ERROR, 3 WARNING, 1 INFO)
**Created:** 2026-09-26 23:30 +0700
**Validator:** hygiene-inspector
**Paths checked:** 1,870 đường dẫn trong phạm vi (1,796 tệp + 74 thư mục)
**Machine findings:** 91 (4 ERROR, 87 WARNING) + 1 ERROR phát hiện bằng dò tay ngoài tầm bộ quét = 9 nhóm báo cáo
**Quy chuẩn:** `wiki/meta/folder-structure.md` v1.2 (đọc đầy đủ 301 dòng)

---

## Phạm vi và bằng chứng

1. Quét toàn cây từ `/home/julius/knowledge-base`, không đi theo symlink. Loại `.git/`, `.obsidian/`, `node_modules/`. Kiểm tra tầng đầu `.hermes/` và `.openclaw/`; nội bộ sâu hơn tầng đầu miễn kiểm tra theo quy tắc. Không đọc nội dung memory/log — chỉ path và metadata.
2. Bộ quét đi qua 241,056 tệp vì tính nội bộ nhà tác nhân. **Con số này không phải số đường dẫn kiểm tra** và không được dùng để suy ra tăng/giảm kho.
3. **Số liệu phạm vi so với 09-25 — cần đọc đúng:** 1,796 tệp (09-25: 1,785) → **+11 tệp**, đây là con số dùng để so sánh tăng trưởng. 74 thư mục là con số **theo định nghĩa lần này** (bao gồm 42 thư mục tầng-đầu bên trong `.hermes/`+`.openclaw/`); con số 33 của 09-25 loại bớt nhóm đó. Không suy ra kho tăng/giảm từ chênh lệch định nghĩa đếm. Tổng 1,870 chỉ dùng làm con số quét.
4. Không có lỗi quyền truy cập. Không có thư mục rỗng trong `wiki/`, `raw/`, `context/`, `scripts/`. Toàn bộ index bắt buộc (`context/context.md`, `USER.md`, `raw/raw.md`, 6 index raw, `wiki/wiki.md`, `wiki/meta/` 3 tệp) đều tồn tại.
5. **Ba khẳng định của báo cáo 09-25 hôm nay bị bằng chứng bác bỏ.** Chi tiết ở mục "Đính chính" bên dưới. `memory/` đã tăng trở lại; `DREAMS.md` vẫn tiếp tục được ghi; symlink HEARTBEAT không còn dangling.

---

## Issue 1: DREAMS.md ở root — CARRY-FORWARD, writer VẪN CHẠY

**Path:** `DREAMS.md`
**Severity:** ERROR
**Category:** Path
**Issue:** File gốc ngoài whitelist §2. Tồn tại từ 09-24; chưa có bằng chứng nào cho thấy đã xử lý.
**Current:** File thường, **10,550 bytes** (09-25 ghi 8,881 → **+1,669 byte**), git-tracked (`git ls-files -s` → blob `64e5ef05…`), `git check-ignore` exit 1, mtime **2026-09-26 03:00:13 +0700**. Ba commit `vault backup` gần nhất chứa file: `3a10b393` (09-24), `234399ba` (09-23), `3194424d` (09-18).
**Expected:** §2 chỉ liệt kê `AGENTS.md`, `TAGS.md`, `README.md`, `knowledge-base.md`, 5 symlink định danh, `.gitignore`.
**Suggested fix:** Giữ dữ liệu. Sửa writer/output path, hoặc cập nhật §2 nếu giữ ở gốc là chủ ý. **Xóa file không giải quyết được** — writer sinh lại mỗi đêm 03:00 và `vault backup` tự commit.

---

## Issue 2: memory/ ở root — CARRY-FORWARD, ĐÃ TĂNG TRỞ LẠI

**Path:** `memory/`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Root folder ngoài whitelist §2. Báo cáo 09-25 addendum ghi "đã ngừng sinh file" — **khẳng định đó sai**, xem Đính chính #1.
**Current:** **72 file, 6 subdirectory** (09-25: 68 file, 6 subdir → **+4 file**). Cấu trúc: `memory/dreaming/{deep,light,rem}/`, `memory/.dreams/session-corpus/`. 4 file mới đều mtime **2026-09-26 03:00**. Không git-tracked; `.gitignore:84` khớp `memory/`.
**Expected:** Dữ liệu tác nhân nằm trong `.openclaw/memory/` hoặc `.hermes/memories/`; hoặc ngoại lệ được duyệt và ghi vào quy chuẩn.
**Suggested fix:** Không xóa dữ liệu. Sửa writer trước, sau đó lập kế hoạch migrate/cleanup có xác minh. 72 cảnh báo tệp con ở Issue 6 là cùng một root cause, **không phải 72 lỗi độc lập**.

---

## Issue 3: Marker migration ở root — CARRY-FORWARD, chưa xử lý

**Path:** `openclaw-workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.e79d1c6c-d9cd-4f3c-b9eb-65b970017373`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker vận hành ở root, đã bị Git theo dõi, **không** được ignore.
**Current:** 69 bytes, mtime 2026-09-08 20:42 (không đổi). `git ls-files -s` → tracked, blob `a0105ac6…`. `git check-ignore` exit 1.
**Expected:** Không runtime artifact ở root; wildcard migration artifact phải được ignore.
**Suggested fix:** Sau approval: thêm `openclaw-workspace-state.json.migrated.*` vào `.gitignore`, `git rm --cached`, commit. `.gitignore:88-89` hiện chỉ chặn đúng tên `openclaw-workspace-state.json` và `.attested` — **không có wildcard**. Validator không sửa.

---

## Issue 4: Marker migration thứ hai trong `.openclaw/` — CARRY-FORWARD từ E1 09-25, chưa xử lý

**Path:** `.openclaw/workspace-state.json.migrated.43c9aa3dead1239e131cfd1ddf1a21fed91f1640ba72aeaf94714c3a31d1c72b.fb077b94-2792-4ca2-b7d8-fc10c5575d51`
**Severity:** ERROR
**Category:** Path
**Issue:** Marker thứ hai của cùng một lần migration, nằm trong agent home. **Không xuất hiện trong machine findings** — quy tắc miễn kiểm tra độ sâu > 1 trong agent home bỏ sót; phải dò tay bằng `find . -name '*.migrated.*'`.
**Current:** 69 bytes, mtime 2026-09-08 20:42 (không đổi). `git ls-files -s` → tracked, **cùng blob `a0105ac6…`** với marker ở Issue 3. `git check-ignore` exit 1 — **không marker nào được ignore**.
**Expected:** Không runtime artifact dạng file tracked trong agent home.
**Suggested fix:** Wildcard `.gitignore` cho **cả hai vị trí** (`.openclaw/workspace-state.json.migrated.*` và `openclaw-workspace-state.json.migrated.*`) + `git rm --cached` **cả hai** marker + commit. Đây là hạng mục duy nhất từ addendum 09-25 chưa có dấu hiệu đã xử lý.

---

## Issue 5: wiki/HEARTBEAT.md — CARRY-FORWARD, mô tả cũ đã sai

**Path:** `wiki/HEARTBEAT.md`
**Severity:** ERROR
**Category:** Orphan
**Issue:** Heartbeat đặt sai vùng — nằm ngoài agent home. Đây là process leak tái diễn, không phải artifact rơi rác.
**Current:** Symlink `../../.openclaw/HEARTBEAT.md` (28 bytes, tạo 08-26 17:01). **Đích hiện TỒN TẠI**: `.openclaw/HEARTBEAT.md`, 16,688 bytes, mtime 2026-09-09 13:15. Untracked (`git ls-files -s` rỗng) nhưng **đã bị ignore** (`git check-ignore` in ra path, exit 0) — khác với 4 ERROR còn lại, nên xóa file chỉ là cleanup, không đụng commit.
**Expected:** Heartbeat chỉ ở agent home, hoặc ngoại lệ đã được quy chuẩn cho phép.
**Suggested fix:** Xác định và sửa writer/mirror trước — xóa symlink không chặn được tái tạo. Bốn symlink định danh ở root (`IDENTITY.md`, `SOUL.md`, `TOOLS.md`, `USER.md`) đều có đích tồn tại. Root `HEARTBEAT.md` đang vắng mặt; §2 cho phép tùy chọn nên **không** coi là lỗi.

---

## Issue 6: [nhóm WARNING] 72 tệp con dưới memory/ — cùng root cause Issue 2

**Path:** `memory/**` (72 tệp, gồm `memory/.dreams/session-corpus/*.txt` và `memory/dreaming/{deep,light,rem}/*.md`)
**Severity:** WARNING
**Category:** Path
**Issue:** Bộ quét không phân loại được path này (memory/ nằm ngoài whitelist, không thuộc vùng nào). 72 cảnh báo máy — **một nguyên nhân**, không phải 72 vấn đề độc lập.
**Current:** 72/87 WARNING máy. 4 file mới 2026-09-26 03:00.
**Expected:** Xử lý cùng Issue 2. Không tách riêng.
**Suggested fix:** Không hành động độc lập. Đếm đúng: **72 phát hiện máy / 1 nhóm nguyên nhân**.

---

## Issue 7: [SPEC CONFLICT] 15 bản sao lưu trong vùng reviews/archive

**Path:** `wiki/reviews/archive/2026-09/`
**Severity:** WARNING
**Category:** Path
**Issue:** 15 tệp `*-backup-*.md` nằm trong vùng archive. §7 nói `reviews/` chỉ chứa đầu ra Hermes; quy chuẩn **chưa quy định ngoại lệ** cho bản sao nội dung.
**Current:** 15 tệp, **không đổi** so với 09-17/09-24/09-25 (danh sách và số lượng giống hệt). Không phải phát hiện mới.
**Expected:** Chính sách rõ: canonical report name, hoặc nơi lưu riêng được cho phép.
**Suggested fix:** Julius chốt chính sách trước; Fix Agent chỉ chuyển/dọn sau khi xác minh dữ liệu. Validator **không tự đổi tên bản sao thành báo cáo** — làm vậy là bịa báo cáo.

---

## Issue 8: [SPEC CONFLICT] Loại `spot-check` lệch danh sách báo cáo ở §7

**Path:** `wiki/reviews/archive/2026-06/2026-06-15_spot-check-report.md`
**Severity:** WARNING
**Category:** Naming
**Issue:** Bộ quét chấp nhận `spot-check` như loại report hợp lệ; §7 chỉ liệt kê `output`, `format`, `hygiene`.
**Current:** Tệp lưu trữ đã tồn tại từ 06-15. **Không phải phát hiện mới hôm nay** — không có tệp `spot-check` mới nào.
**Expected:** Script và quy chuẩn có cùng danh sách loại báo cáo.
**Suggested fix:** Cập nhật §7 nếu giữ `spot-check`, hoặc sửa classifier sau khi chính sách rõ. Không tự sửa tệp lịch sử.

---

## Issue 9: [SPEC CONFLICT] Điều khoản quy chuẩn tự mâu thuẫn

**Path:** `wiki/meta/folder-structure.md`
**Severity:** WARNING
**Category:** Path
**Issue:** Ba điểm tự mâu thuẫn trong cùng tài liệu:
- §6 cây `raw/` cho phép `raw.md` rồi lại ghi `*` ✗ forbidden ở `raw/` root.
- §7 cây `wiki/` cho phép `wiki.md` rồi lại ghi "No files at `wiki/` root level".
- §7 Rules yêu cầu `meta/` có đúng 3 tệp (thêm `index-spec.md`), nhưng cây `meta/` chỉ hiển thị 2. Cây thực tế có đủ 3.
- §3 cho phép runtime tự do trong agent home, §4 lại hạn chế nội bộ skills.
**Current:** Đã dùng ngoại lệ cụ thể để không báo nhầm index hợp lệ. Quy chuẩn v1.2 không đổi.
**Expected:** Ngoại lệ và phạm vi nhà tác nhân nêu nhất quán.
**Suggested fix:** Julius/Fix Agent thống nhất văn bản. Validator không sửa quy chuẩn.

---

## Issue 10: INFO — 38 báo cáo cũ hơn 30 ngày trong vùng active

**Path:** `wiki/reviews/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Vùng active chứa lịch sử nhiều ngày. Số lượng phụ thuộc trạng thái approved/applied nên **không dùng một số chưa đối chiếu làm quyết định**.
**Current:** 100 tệp `.md` ở tầng active; **38 tệp có mtime cũ hơn 2026-08-27** (sớm nhất `2026-06-01_*`), 62 tệp mới hơn. Không có bằng chứng tệp mới gây tồn đọng hôm nay.
**Expected:** Báo cáo hoàn tất nên ở `archive/YYYY-MM/`; báo cáo pending giữ truy vết.
**Suggested fix:** Fix Agent đối chiếu trạng thái từng báo cáo trước khi chuyển. Không tự xóa hoặc archive hàng loạt.

---

## Đính chính — ba khẳng định của báo cáo 09-25 bị bác bỏ

Bằng chứng hôm nay không khớp ba điểm đã viết. Ghi lại công khai, không lặng lẽ gộp vào carry-forward.

**Đính chính #1 — `memory/` "đã ngừng sinh file" (SAI).** Addendum 09-25 ghi: *"`memory/` **đã ngừng sinh file** kể từ 18:14"*. Hôm nay có 4 file mới, tất cả mtime **2026-09-26 03:00**: `memory/dreaming/deep/2026-09-26.md`, `light/2026-09-26.md`, `rem/2026-09-26.md`, `memory/.dreams/session-corpus/2026-09-25.txt`. 68 → 72 file. **Nhận định "đã ngừng" sai; writer vẫn chạy, chỉ nghỉng ban đêm rồi chạy lại 03:00.** Hệ quả: kế hoạch xử lý `memory/` phải tính cả đường ghi `memory/.dreams/session-corpus/` — một đường ghi mới, tách biệt với `memory/dreaming/`.

**Đính chính #2 — `wiki/HEARTBEAT.md` "đích vẫn missing (dangling)" (SAI).** Addendum 09-25 ghi đích vẫn missing. Hôm nay `.openclaw/HEARTBEAT.md` tồn tại: 16,688 bytes, mtime 2026-09-09 13:15. **Symlink không dangling** — nó trỏ tới file có thật, nghĩa là lọt vào Obsidian như một note thật. Đây là lý do lỗi nặng hơn mô tả cũ: không phải liên kết chết cần dọn, mà là nội dung agent đang hiển thị sai vùng.

**Đính chính #3 — số liệu phạm vi (KHÔNG SO SÁNH ĐƯỢC).** Báo cáo 09-25 chốt 1,818 và gọi 1,859 là sai. Lần này quét lại ra **1,796 tệp + 74 thư mục = 1,870**. Chênh lệch nằm ở **định nghĩa đếm thư mục**: con số này gồm 42 thư mục tầng-đầu trong `.hermes/`+`.openclaw/`, con số 33 của 09-25 thì không. **Số liệu dùng để so sánh tăng trưởng là số tệp: 1,785 → 1,796 (+11).** Tổng 1,870 và 1,818 là hai phép đo khác nhau, không dùng để kết luận kho tăng hay giảm.

---

## Passing / Delta so với 09-25

| Hạng mục | 09-25 (23:32) | 09-26 (23:30) | Kết luận |
|---|---|---|---|
| Machine findings | 87 (4E + 83W) | **91 (4E + 87W)** | +4, **toàn bộ** do `memory/` 68→72 |
| Tệp trong phạm vi | 1,785 | **1,796** | +11 tệp, hợp lệ |
| ERROR nhóm | 4 | **5** | +1 do dò tay, không phải do bộ quét |
| Marker `.migrated.*` | 2 (1 trong `.openclaw/`) | 2, **không đổi** | Cả hai vẫn tracked, cả hai vẫn không ignored |
| Archive backups | 15 | 15 | UNCHANGED |
| `spot-check` | 1 tệp lưu trữ | 1 | UNCHANGED |
| `wiki/drafts/` | 1 tệp | 1 (`analysis-2026-advice.md`) | UNCHANGED, tên hợp lệ |
| Thư mục rỗng | 0 | 0 | UNCHANGED |
| Lỗi path/naming mới trong `raw/`, `wiki/`, `context/` | 0 | **0** | — |

**Tệp mới hôm nay — đã kiểm tra, sạch:**
- `raw/posts/2026-09-24_do-less.md` — khớp §6 `YYYY-MM-DD_<slug>.md`, đã có trong `raw/posts/posts.md`.
- `wiki/sources/src_do-less.md` — khớp §8.1 `src_<slug>.md`.
- 5 concept mới: `boredom-as-dopamine-reset.md`, `busywork-vs-deep-work.md`, `creative-incubation.md`, `one-thing-daily-priority.md`, `stress-habituation.md` — tất cả lowercase-hyphen, đúng §7.
- 2 topic mới: `doing-less-mind-space.md`, `ai-trading-agent-safety.md` — đúng §7.
- 26 index `wiki/tag/*` + 261 `wiki/topic/*` được Index Agent viết lại (mtime mới, **không phải file mới**: 25/25 tag đã tracked, 259/261 topic đã tracked).

**Không phát lại `[SYSTEMATIC VIOLATION]`.** `DREAMS.md`, `memory/`, marker `.migrated.*`, `wiki/HEARTBEAT.md`, bản sao lưu và ba xung đột quy chuẩn đã nêu ở các báo cáo pending. Mọi mục trên đây là CARRY-FORWARD hoặc `[SPEC CONFLICT]`.

---

## Actions Needed

1. **Sửa writer `memory/` trước khi migrate** — nó vẫn ghi, và nay có thêm đường `memory/.dreams/session-corpus/`. Giữ nguyên dữ liệu. Đừng coi là đã xử lý dựa trên nhận định 09-25.
2. **Sau approval, xử lý 2 marker `.migrated.*`:** wildcard `.gitignore` cho cả hai vị trí + `git rm --cached` + commit. Đây là hạng mục duy lại từ addendum 09-25, chưa có dấu hiệu đã động tới.
3. **Sửa writer/mirror tạo `DREAMS.md` và `wiki/HEARTBEAT.md`.** Xóa file không giải quyết được: `DREAMS.md` được ghi lại 03:00 mỗi đêm và đã bị `vault backup` commit; symlink HEARTBEAT đang trỏ tới file thật nên lọt vào Obsidian.
4. **Chốt chính sách 15 archive backup** (giữ / chuyển / cho phép ngoại lệ §7) và **loại `spot-check`**.
5. **Thống nhất điều khoản mâu thuẫn** §6/§7/§3-§4 trong `folder-structure.md`.

---

*Validator chỉ đọc path và metadata; không đọc nội dung memory/log, không sửa cấu trúc, không sửa file ngoài `wiki/reviews/`.*
