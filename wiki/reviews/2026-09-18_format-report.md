# Format Validation — 2026-09-18

**Status:** pending
**Issues found:** 403
**Created:** 2026-09-18 23:16:17
**Validator:** format-validator
**Files checked:** 1072 (586 concepts + 204 sources + 34 indexes + 248 topics)
**ERRORs**: 1
**WARNINGS**: 402
**INFOS:** 0
**Total issues**: 403

Files checked: 1072
Total issues: 403

Δ from 2026-09-17 23:15:43 (pending — prior run): tổng issues tăng 402→403 (+1 ERROR mới). Tệp tăng 1063→1072 (+9: 3 khái niệm + 3 nguồn + 3 chủ đề — batch 09-18). Cảnh báo không đổi 402→402; cảnh báo liên kết riêng lẻ 383→383; nhóm liên kết hỏng 19→19; đích riêng biệt 272→272. Danh sách 20 đích ưu tiên giữ nguyên cả tên và số đếm. ERROR mới: `wiki/tag/tag.md` thiếu `## Overview` — sụt giảm do Index Agent cập nhật file 09-18 mà không giữ đủ cấu trúc L2. Streak ERROR sạch bị phá (16 ngày liên tiếp không lỗi → nay có 1).

---

## Tổng hợp thay đổi

| Chỉ số | 09-17 | 09-18 | Chênh lệch |
|---|---:|---:|---:|
| Tệp đã kiểm tra | 1063 | 1072 | +9 |
| Lỗi nghiêm trọng | 0 | 1 | +1 |
| Cảnh báo | 402 | 402 | 0 |
| Cảnh báo liên kết riêng lẻ | 383 | 383 | 0 |
| Cảnh báo gộp theo tệp | 19 | 19 | 0 |
| Đích riêng biệt được nêu tên | 272 | 272 | 0 |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1072 | 586 | 204 | 34 | 248 |

Phạm vi: toàn bộ 790 tệp nguồn/khái niệm; thêm 34 chỉ mục và 248 trang chủ đề theo phân luồng của chương trình. Không có lỗi đọc tệp. Trang chủ đề kiểm tra nhẹ, không áp quy tắc chỉ mục điều hướng. Bỏ qua bản nháp và `context/USER.md` theo quy trình.

Git xác nhận 9 tệp mới, không tệp bị xóa trong các thư mục wiki được đối chiếu kể từ lần chạy trước:

1. `wiki/concepts/ai-lab-business-model.md` — `35d60bc9`, 08:09.
2. `wiki/concepts/oaat-model.md` — `be79135a`, 08:04.
3. `wiki/concepts/system-design-concepts-2026.md` — `35d60bc9`, 08:09.
4. `wiki/sources/src_50-system-design-concepts-explained-simply.md` — `35d60bc9`, 08:09.
5. `wiki/sources/src_how-ai-labs-eventually-make-money.md` — `35d60bc9`, 08:09.
6. `wiki/sources/src_im-begging-you-to-manage-your-goals-like-this.md` — `be79135a`, 08:04.
7. `wiki/topic/ai-lab-business-model.md` — `ac41b89b`, 21:04.
8. `wiki/topic/oaat-goal-model.md` — `ac41b89b`, 21:04.
9. `wiki/topic/system-design-concepts-2026.md` — `ac41b89b`, 21:04.

Cả 9 không xuất hiện trong kết quả cảnh báo. `wiki/tag/tag.md` là tệp cập nhật (không tính thành tệp mới) — đây là nguồn gốc của ERROR mới.

## Vấn đề 1: Liên kết chưa có đích — cảnh báo

**Mức độ:** cảnh báo.
**Nhóm:** cú pháp Markdown / liên kết nội bộ.
**Hiện trạng:** 383 cảnh báo riêng lẻ trên 195 tệp (160 khái niệm + 35 nguồn), cùng 19 cảnh báo gộp theo tệp (2 khái niệm + 17 nguồn).
**Yêu cầu:** `wiki/meta/format-spec.md` §2.4, §6.1–6.2: liên kết phải trỏ tới tệp tồn tại; đích không tồn tại được ghi cảnh báo.
**Đề xuất:** kiểm tra đích đúng trước khi đổi liên kết. Chỉ biên soạn khái niệm mới khi có nguồn phù hợp. Không xóa hàng loạt liên kết, không tạo tệp rỗng để làm giảm số đếm.

402 là số mục cảnh báo, không phải tổng số lần xuất hiện liên kết hỏng: mỗi nhóm được tính một mục. 272 là số đích được nêu tên trong 383 mục riêng lẻ; các nhóm không liệt kê tên đích nên con số này không đại diện đầy đủ mọi đích trong kho.

### 20 đích ưu tiên theo số cảnh báo riêng lẻ

| Đích | Số cảnh báo |
|---|---:|
| `[[game-theory]]` | 10 |
| `[[confirmation-bias]]` | 8 |
| `[[deep-work]]` | 5 |
| `[[ai-coding-agents]]` | 5 |
| `[[career-design]]` | 5 |
| `[[decision-making]]` | 5 |
| `[[attention-economy]]` | 3 |
| `[[ai-assisted-development]]` | 3 |
| `[[ai-hype-vs-reality]]` | 3 |
| `[[economic-inequality]]` | 3 |
| `[[intellectual-humility]]` | 3 |
| `[[network-effects]]` | 3 |
| `[[goal-setting]]` | 3 |
| `[[naval-ravikant]]` | 3 |
| `[[risk-parity]]` | 3 |
| `[[second-law-of-thermodynamics]]` | 3 |
| `[[homeostasis]]` | 3 |
| `[[saying-no]]` | 3 |
| `[[cognitive-dissonance]]` | 3 |
| `[[power-imbalance]]` | 3 |

## Vấn đề 2: Thiếu section bắt buộc — lỗi

**Mức độ:** lỗi nghiêm trọng.
**Nhóm:** cấu trúc section.
**Hiện trạng:** `wiki/tag/tag.md` thiếu `## Overview` — section bắt buộc theo index-spec.md §4.2 cho chỉ mục Tầng 2.
**Yêu cầu:** `wiki/meta/index-spec.md` §4.2: chỉ mục Tầng 2 phải có `## Overview`, `## Parent`, `## Stats`, `## Items`, `## Notes`.
**Hiện tại:** File có `## Parent`, `## Stats`, `## Items` — thiếu `## Overview` và `## Notes`.
**Nguyên nhân:** `wiki/tag/tag.md` được cập nhật hôm nay (09-18 21:04, `ac41b89b`) — likely do Index Agent tái tạo mà không giữ đủ cấu trúc L2.
**Đề xuất:** Fix Agent thêm `## Overview` section (mô tả ngắn về tags index) và `## Notes` section (tùy chọn, có thể rỗng) vào `wiki/tag/tag.md`.

## Escalations

- **ERROR streak broken:** 16 ngày liên tiếp không lỗi (09-01 → 09-17) đã bị phá. ERROR duy nhất hôm nay là `wiki/tag/tag.md` thiếu section — sụt giảm từ Index Agent, không phải Compile Agent.
- Không nâng mức cảnh báo mới. Các chỉ số tồn đọng giữ nguyên so với báo cáo đã duyệt; số đích được nêu tên giữ mức 272 qua 5 lần chạy liên tiếp.
- Chương trình không phát hiện cảnh báo `parent` thiếu dấu ngoặc kép. Đây là xung đột đã biết, không phải lỗi mới của đợt này.

## Verification

- [x] Đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md` làm căn cứ.
- [x] Chạy `validate.py` toàn bộ phạm vi: 1072 tệp, 0 lỗi đọc, 402 cảnh báo, 1 lỗi nghiêm trọng.
- [x] Chạy `parse_issues.py`: 383 mục riêng lẻ + 19 nhóm = 402 cảnh báo; 272 đích được nêu tên.
- [x] Đếm trực tiếp từ dữ liệu quét: 195 tệp có cảnh báo riêng lẻ, không sao chép số tệp sai từ báo cáo cũ.
- [x] Đối chiếu Git: +3 khái niệm, +3 nguồn, +3 chủ đề, không xóa tệp; 1063 + 9 = 1072.
- [x] Kiểm tra `wiki/tag/tag.md` — xác nhận thiếu `## Overview` và `## Notes`.
- [x] Báo cáo 09-17 đang chờ duyệt; dùng làm baseline delta.
- [x] Không sửa tệp nội dung, chỉ mục hay đặc tả. Việc sửa thuộc tác nhân biên soạn/sửa lỗi sau phê duyệt.

Kết quả là kiểm tra định dạng bằng chương trình hiện hành, không phải xác nhận độ chính xác nội dung. Báo cáo trình bày nhóm vi phạm và 20 đích ưu tiên; số đếm luôn bao gồm toàn bộ kết quả quét.
