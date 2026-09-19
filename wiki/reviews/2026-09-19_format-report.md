# Format Validation — 2026-09-19

**Status:** pending
**Issues found:** 403
**Created:** 2026-09-19 23:15:20
**Validator:** format-validator
**Files checked:** 1072 (586 concepts + 204 sources + 34 indexes + 248 topics)
**ERRORs**: 1
**WARNINGS**: 402
**INFOS:** 0
**Total issues**: 403

Files checked: 1072
Total issues: 403

Δ from 2026-09-18 23:16:17 (pending — prior run): exact-zero-flat. Tổng issues không đổi 403→403; ERROR 1→1; WARNING 402→402; cá nhân 383→383; nhóm forward-ref 19→19; đích riêng biệt 272→272. Top-20 giữ nguyên cả tên lẫn số đếm. Git xác nhận 0 tệp thêm, 0 tệp xóa trong wiki/ kể từ lần chạy trước. Pipeline tĩnh — không biên soạn, không chủ đề mới.

---

## Tổng hợp thay đổi

| Chỉ số | 09-18 | 09-19 | Chênh lệch |
|---|---:|---:|---:|
| Tệp đã kiểm tra | 1072 | 1072 | 0 |
| Lỗi nghiêm trọng | 1 | 1 | 0 |
| Cảnh báo | 402 | 402 | 0 |
| Cảnh báo liên kết riêng lẻ | 383 | 383 | 0 |
| Cảnh báo gộp theo tệp | 19 | 19 | 0 |
| Đích riêng biệt được nêu tên | 272 | 272 | 0 |

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1072 | 586 | 204 | 34 | 248 |

Phạm vi: toàn bộ 790 tệp nguồn/khái niệm; thêm 34 chỉ mục và 248 trang chủ đề. Không có lỗi đọc tệp. Trang chủ đề kiểm tra nhẹ, không áp quy tắc chỉ mục điều hướng. Bỏ qua bản nháp và `context/USER.md` theo quy trình.

Git xác nhận 0 tệp mới, 0 tệp bị xóa trong các thư mục wiki được đối chiếu kể từ lần chạy trước. Pipeline biên soạn tĩnh — không có tệp mới nào được thêm vào.

---

## 20 lỗi nghiêm trọng nhất

### Lỗi nghiêm trọng (1)

| # | Tệp | Vấn đề |
|---|---|---|
| 1 | `wiki/tag/tag.md` | Thiếu section bắt buộc `## Overview` — ERROR duy nhất, carry-forward từ 09-18 (Index Agent cập nhật file mà không giữ cấu trúc L2) |

### Cảnh báo liên kết hỏng — 20 đích phổ biến nhất (19 nhóm, 383 cá nhân)

| # | Đích | Số lần |
|---|---|---|
| 1 | `[[game-theory]]` | 10 |
| 2 | `[[confirmation-bias]]` | 8 |
| 3 | `[[deep-work]]` | 5 |
| 4 | `[[ai-coding-agents]]` | 5 |
| 5 | `[[career-design]]` | 5 |
| 6 | `[[decision-making]]` | 5 |
| 7 | `[[attention-economy]]` | 3 |
| 8 | `[[ai-assisted-development]]` | 3 |
| 9 | `[[ai-hype-vs-reality]]` | 3 |
| 10 | `[[economic-inequality]]` | 3 |
| 11 | `[[intellectual-humility]]` | 3 |
| 12 | `[[network-effects]]` | 3 |
| 13 | `[[goal-setting]]` | 3 |
| 14 | `[[naval-ravikant]]` | 3 |
| 15 | `[[risk-parity]]` | 3 |
| 16 | `[[second-law-of-thermodynamics]]` | 3 |
| 17 | `[[homeostasis]]` | 3 |
| 18 | `[[saying-no]]` | 3 |
| 19 | `[[cognitive-dissonance]]` | 3 |
| 20 | `[[power-imbalance]]` | 3 |

### Nhóm liên kết hỏng — 19 nhóm forward-reference

| # | Tệp | Số liên kết hỏng |
|---|---|---|
| 1 | `wiki/concepts/third-order-thinking.md` | 6 |
| 2 | `wiki/concepts/thought-experiment.md` | 6 |
| 3 | `wiki/sources/src_11-minutes-hack-github.md` | 4 |
| 4 | `wiki/sources/src_ai-future-skills.md` | 4 |
| 5 | `wiki/sources/src_code-as-agent-harness-arxiv-2605-18747.md` | 6 |
| 6 | `wiki/sources/src_farnam-street-mental-models-biology-series.md` | 6 |
| 7 | `wiki/sources/src_farnam-street-mental-models-systems-thinking.md` | 6 |
| 8 | `wiki/sources/src_feedback-loops-mental-model.md` | 4 |
| 9 | `wiki/sources/src_fs-blog-mental-models.md` | 7 |
| 10 | `wiki/sources/src_global-macro-investing.md` | 4 |
| 11 | `wiki/sources/src_hermes-polymarket-btc-trading-agent.md` | 4 |
| 12 | `wiki/sources/src_incentives-hidden-forces.md` | 6 |
| 13 | `wiki/sources/src_mental-models-of-art.md` | 9 |
| 14 | `wiki/sources/src_mental-models-of-economics.md` | 9 |
| 15 | `wiki/sources/src_probabilistic-thinking.md` | 6 |
| 16 | `wiki/sources/src_the-cost-of-discretion.md` | 4 |
| 17 | `wiki/sources/src_the-seed-and-the-machine.md` | 4 |
| 18 | `wiki/sources/src_thought-experiment.md` | 9 |
| 19 | `wiki/sources/src_tribute-system-new-world-order.md` | 4 |

---

## Phân tích

**Trạng thái: exact-zero-flat lần thứ 2 liên tiếp.**

Tổng issues giữ nguyên 403→403 trên mọi trục: ERROR (1→1), WARNING (402→402), cá nhân 383→383, nhóm 19→19, đích riêng biệt 272→272. Top-20 danh sách giống hệt 09-18 cả về tên lẫn số đếm. Git xác nhận 0 tệp wiki thêm/xóa — pipeline biên soạn hoàn toàn tĩnh.

- **ERROR duy nhất**: `wiki/tag/tag.md` thiếu `## Overview` — section bắt buộc L2 theo index-spec §4.2. Carry-forward từ 09-18, lần thứ 2 liên tiếp. Index Agent cập nhật file 09-18 nhưng không duy trì cấu trúc section cần thiết.
- **Cảnh báo**: 100% là broken wikilinks — forward-references tới các concept chưa được biên soạn. Không có lỗi cấu trúc, naming, hay YAML mới.
- **Dự báo**: Tổng issues sẽ giảm khi Fix Agent sửa `wiki/tag/tag.md` (−1 ERROR) hoặc Compile Agent biên soạn các raw files hiện có (giảm forward-refs). Không có raw files mới chờ compile.

---

## Lỗi đọc tệp

Không có. 0 lỗi đọc.

## Cảnh báo phân loại

| Loại | Số lượng |
|---|---|
| Liên kết hỏng cá nhân | 383 |
| Nhóm liên kết hỏng (forward-reference) | 19 |
| Tổng | 402 |

## Lỗi phân loại

| Loại | Số lượng |
|---|---|
| Lỗi cấu trúc section | 1 |
| Tổng | 1 |

## Tiếp theo

1. **Fix Agent**: Thêm `## Overview` và `## Notes` vào `wiki/tag/tag.md` để loại bỏ ERROR duy nhất.
2. **Compile Agent**: Tiếp tục biên soạn raw files để giảm backlog forward-reference WARNINGs (272 đích riêng biệt).
3. **Theo dõi**: `[[game-theory]]` (10 refs) + `[[confirmation-bias]]` (8 refs) vẫn là 2 đích được tham chiếu nhiều nhất chưa biên soạn.

---

## Escalations

Không có escalation mới. ERROR `wiki/tag/tag.md` đã được ghi nhận ở lần chạy trước (09-18) và đang chờ Fix Agent xử lý.

## Verification

- [x] Đọc `format-spec.md` (ground truth)
- [x] Quét toàn bộ `wiki/sources/` + `wiki/concepts/`
- [x] Kiểm tra `wiki/tag/` + `wiki/topic/` (index files)
- [x] Dispatch theo type field (concept → format-spec, index → index-spec)
- [x] Kiểm tra frontmatter, sections, naming, markdown
- [x] Kiểm tra broken wikilinks (resolve raw subdirs)
- [x] Kiểm tra `wiki/tag/tag.md` ERROR (missing `## Overview`)
- [x] So sánh với report trước (09-18) — exact-zero-flat confirmed
- [x] Git reconciliation: 0 files added, 0 deleted since 09-18 23:15
- [x] Report ghi vào `wiki/reviews/2026-09-19_format-report.md`
