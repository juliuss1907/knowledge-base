# Hygiene Inspection — 2026-07-02

**Status:** approved
**Approved by:** Julius — 2026-07-05
**Issues found:** 1
**Created:** 2026-07-02 23:30:00 +0700
**Validator:** hygiene-inspector

**Paths checked:** 51,618

---

## Overall health

KB structure đạt 99.998% compliance (1/51,618 paths with issue). Tất cả active content zones — `context/`, `raw/`, `wiki/` (meta, sources, concepts, tag, topic, drafts, reviews), agent homes — đều 100% compliant với `folder-structure.md` v1.2.

**Delta from 2026-07-01 (PENDING):**
- ✅ `index_wiki.py` ở root → đã resolved (không còn xuất hiện)
- ✅ HEARTBEAT.md leak → vẫn resolved (ổn định 4 ngày từ 06-28)
- ⚠️ NEW: `state/` empty directory — tái xuất hiện (đã resolve 06-27, tạo lại 07-02 10:28)

---

## Issue 1: Empty directory at root level

**Path:** `state/`
**Severity:** INFO
**Category:** Orphan
**Issue:** Empty directory at root level — not in root whitelist
**Current:** `state/` (empty, created 2026-07-02 10:28)
**Expected:** Root may only contain: `.git`, `.obsidian`, `.openclaw`, `.hermes`, `context`, `raw`, `wiki`, `scripts`
**Suggested fix:** Remove empty directory (`rmdir state/`)

**Recurrence note:** `state/` was previously flagged as ERROR on 2026-06-25, resolved by 2026-06-27, then recreated on 2026-07-02. The creating process should be identified to prevent future recurrence. If the directory needs to exist, move it inside `.hermes/` or `.openclaw/`.

---

## Zone-by-zone summary

| Zone | Status | Details |
|---|---|---|
| Root level | ⚠️ 1 INFO | `state/` empty directory |
| `context/` | ✅ Clean | `context.md`, `USER.md` — đúng whitelist |
| `raw/` | ✅ Clean | 6 subfolders, tất cả naming conventions compliant |
| `wiki/meta/` | ✅ Clean | `format-spec.md`, `folder-structure.md`, `index-spec.md` |
| `wiki/sources/` | ✅ Clean | Tất cả `src_<slug>.md`, naming 100% compliant |
| `wiki/concepts/` | ✅ Clean | Lowercase-hyphen slugs, không vi phạm |
| `wiki/tag/` | ✅ Clean | Auto-generated files, naming compliant |
| `wiki/topic/` | ✅ Clean | Auto-generated files, naming compliant |
| `wiki/drafts/` | ✅ Clean | Không .bak, không .tmp, không .gitkeep orphan |
| `wiki/reviews/` | ✅ Clean | Reports đúng format, archive YYYY-MM/ OK |
| `.hermes/` | ✅ Clean | Agent home, deep internals skipped |
| `.openclaw/` | ✅ Clean | Agent home, deep internals skipped |
| `scripts/` | ✅ Clean | Utility scripts in whitelist |

---

## HEARTBEAT status

✅ **No HEARTBEAT leak detected.** `wiki/reviews/HEARTBEAT.md` absent — resolved since 2026-06-28, confirmed stable through 4 consecutive runs (06-29, 06-30, 07-01, 07-02).

---

## Recommendations

1. **Remove `state/`**: `rmdir state/` (hoặc `rm -rf state/` nếu tương lai có file). Thư mục trống, không chứa dữ liệu.
2. **Investigate recurrence**: `state/` đã bị xóa trước đó nhưng được tạo lại 2026-07-02 10:28 — xác định process nào tạo thư mục này và sửa output path.
3. **Scan script gap**: `classify_root_folder()` không được gọi từ `main()` — root folders chỉ bị bắt qua empty directory check (INFO), không qua path whitelist check (ERROR). Cân nhắc patch để folder không whitelist ở root bị flag là ERROR thay vì INFO.

---

**Scan script:** `/tmp/hygiene_scan.py` (production template from `hygiene-inspector/references/scan-script.py`)
**Ground truth:** `wiki/meta/folder-structure.md` v1.2
**Report:** `wiki/reviews/2026-07-02_hygiene-report.md`
