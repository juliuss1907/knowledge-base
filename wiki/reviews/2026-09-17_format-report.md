# Format Validation — 2026-09-17

**Status:** pending
**Issues found:** 402
**Created:** 2026-09-17 23:15:43
**Validator:** format-validator
**Files checked:** 1063 (583 concepts + 201 sources + 34 indexes + 245 topics)
**ERRORs**: 0
**WARNINGS**: 402
**INFOS:** 0
**Total issues**: 402

Files checked: 1063
Total issues: 402

Δ from 2026-09-16 23:16:30 — báo cáo đã được Julius duyệt lúc 2026-09-17 08:57 +0700: tổng cảnh báo không đổi, 402→402. Tệp tăng 1060→1063 (+3); liên kết hỏng riêng lẻ 383→383; nhóm liên kết hỏng 19→19; đích riêng biệt trong các cảnh báo riêng lẻ 272→272. Danh sách 20 đích được tham chiếu nhiều nhất giữ nguyên cả tên và số đếm. Kho tri thức tăng; tồn đọng liên kết chưa giảm. Không kết luận toàn bộ nội dung wiki bất biến.

---

## Tổng hợp thay đổi

| Chỉ số | 09-16 | 09-17 | Chênh lệch |
|---|---:|---:|---:|
| Tệp đã kiểm tra | 1060 | 1063 | +3 |
| Lỗi nghiêm trọng | 0 | 0 | 0 |
| Cảnh báo | 402 | 402 | 0 |
| Cảnh báo liên kết riêng lẻ | 383 | 383 | 0 |
| Cảnh báo gộp theo tệp | 19 | 19 | 0 |
| Đích riêng biệt được nêu tên | 272 | 272 | 0 |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1063 | 583 | 201 | 34 | 245 |

Phạm vi: toàn bộ 784 tệp nguồn/khái niệm; thêm 34 chỉ mục và 245 trang chủ đề theo phân luồng của chương trình. Không có lỗi đọc tệp. Trang chủ đề kiểm tra nhẹ, không áp quy tắc chỉ mục điều hướng. Bỏ qua bản nháp và `context/USER.md` theo quy trình.

Git xác nhận 3 tệp mới, không tệp bị xóa trong các thư mục wiki được đối chiếu kể từ lần chạy trước:

1. `wiki/concepts/behavioral-evals.md` — `10d1ced0`, 08:09.
2. `wiki/sources/src_googletech-behavioral-evals-harness-engineering.md` — `10d1ced0`, 08:09.
3. `wiki/topic/behavioral-evals-harness-engineering.md` — `ed802949`, 21:14.

Cả 3 không xuất hiện trong kết quả cảnh báo. `harness-engineering.md` là tệp cập nhật, không tính thành tệp mới. Có 3 bài mới trong `raw/articles/` qua `3fc46ce8` và `798aa59f`; không cộng vào số tệp wiki.

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

Ví dụ vị trí cần xử lý khi được duyệt:

1. `wiki/concepts/nash-equilibrium.md`: `[[game-theory]]` chưa có đích. Kiểm tra khả năng biên soạn từ nguồn có sẵn; không thay bằng khái niệm gần nghĩa khi chưa đối chiếu.
2. `wiki/concepts/framing-mental-model.md`: `[[confirmation-bias]]` chưa có đích. Áp dụng cùng quy trình.
3. `wiki/concepts/operant-conditioning.md`: `[[src_the-power-of-incentives-hidden-forces-shape-behavior]]` chưa có đích. Kiểm tra tên nguồn thực tế trước khi đổi; không mặc định đây là khái niệm chờ biên soạn.
4. `wiki/sources/src_llm-need-sleep-consolidation.md`: `[[2026-05-27_llm-need-sleep-consolidation]]` chưa được chương trình phân giải. Kiểm tra tên và vị trí bản gốc; không mặc định thiếu khái niệm.

## Escalations

Không nâng mức cảnh báo mới. Các chỉ số tồn đọng giữ nguyên so với báo cáo đã duyệt; số đích được nêu tên giữ mức 272 qua 4 lần chạy liên tiếp. Không khẳng định mọi liên kết sẽ tự lành khi biên soạn thêm.

Chương trình không phát hiện cảnh báo `parent` thiếu dấu ngoặc kép. Ví dụ không có dấu ngoặc kép vẫn tồn tại trong `index-spec.md`; đây là xung đột đã biết, không phải lỗi mới của đợt này.

## Verification

- [x] Đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md` làm căn cứ.
- [x] Chạy `validate.py` toàn bộ phạm vi: 1063 tệp, 0 lỗi đọc, 402 cảnh báo, 0 lỗi nghiêm trọng.
- [x] Chạy `parse_issues.py`: 383 mục riêng lẻ + 19 nhóm = 402; 272 đích được nêu tên.
- [x] Đếm trực tiếp từ dữ liệu quét: 195 tệp có cảnh báo riêng lẻ, không sao chép số tệp sai từ báo cáo cũ.
- [x] Đối chiếu Git: +1 khái niệm, +1 nguồn, +1 chủ đề, không xóa tệp; 1060 + 3 = 1063.
- [x] Báo cáo 09-16 và `_action-required.md` cùng ghi đã duyệt; không cần hòa giải trạng thái.
- [x] Không sửa tệp nội dung, chỉ mục hay đặc tả. Việc sửa thuộc tác nhân biên soạn/sửa lỗi sau phê duyệt.

Kết quả là kiểm tra định dạng bằng chương trình hiện hành, không phải xác nhận độ chính xác nội dung. Báo cáo trình bày nhóm vi phạm và 20 đích ưu tiên; số đếm luôn bao gồm toàn bộ kết quả quét.
