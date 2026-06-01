# Output Validation — 2026-06-01

**Status:** pending
**Issues found:** 4 systemic issues
**Created:** 2026-06-01 08:15
**Validator:** Connor (Hermes-RK800) — output-validator

---

## Summary

**Scope:** 172 concepts + 38 sources = 210 files total
**Result: REVISE** — 4 systemic issues across all files. Không có individual issues — toàn bộ là pattern errors.

---

## Issue 1: Summary chỉ 1 dòng — toàn bộ 210 files

**Severity:** ERROR
**Dimension:** Completeness
**Files affected:** 172 concepts + 38 sources (100%)
**Issue:** Tất cả 210 files đều có Summary section chỉ 1 dòng (hoặc 0 dòng có nội dung thực tế). Spec yêu cầu 3-5 sentences.
**Evidence:** `awk` scan xác nhận: avg = 0-1 lines/file, 0 files đạt 2+ lines.
**Suggested fix:** Compile Agent cần được yêu cầu tạo Summary 3-5 câu cho mỗi file. Đây là lỗi trong compile prompt, không phải lỗi từng file.

---

## Issue 2: Key Points dưới 3 items — 17 files

**Severity:** WARNING
**Dimension:** Completeness
**Files affected:** 17/172 concepts
**Issue:** 17 concepts có ít hơn 3 Key Points. Trung bình toàn bộ 172 concepts là 5.3 points — tốt — nhưng 17 files dưới ngưỡng tối thiểu.
**Suggested fix:** Review từng file có <3 Key Points, bổ sung thêm.

---

## Issue 3: Sources section trống — 3 concepts

**Severity:** ERROR
**Dimension:** Completeness
**Files affected:** 3 concepts
**Issue:** 3 concepts có Sources section không chứa backlink nào. Concept cần có ít nhất 1 source trích dẫn.
**Suggested fix:** Xác định 3 file và thêm backlink đến source tương ứng.

---

## Issue 4: Toàn bộ 210 files status = draft

**Severity:** INFO
**Dimension:** Completeness
**Files affected:** 210/210 (100%)
**Issue:** Tất cả 210 files đều có `status: draft`. Điều này đúng nếu Compile Agent mới tạo và chưa có file nào được review. Tuy nhiên, sau nhiều vòng validation, nên có ít nhất một số file đã chuyển sang `reviewed`.
**Suggested fix:** Sau khi Julius approve fixes, Compile Agent nên cập nhật status của các file đã được sửa thành `reviewed`.

---

## ✅ Passing

- Không có `status: stub` — đã được fix từ các lần trước
- Không có MT artifacts detectable
- Tất cả files có type đúng (`concept` trong concepts/, `source` trong sources/)
- Định nghĩa section có mặt trong 100% concepts
- Không có contradictions rõ ràng với cited sources

---

## Verdict

**REVISE** — 2 ERROR + 1 WARNING + 1 INFO. Tất cả đều là systemic issues.

Issue #1 (Summary 1 dòng) là critical nhất — ảnh hưởng 100% files. Cần update Compile Agent prompt để tạo Summary 3-5 câu. Issues #2 và #3 là minor, có thể fix theo batch.
