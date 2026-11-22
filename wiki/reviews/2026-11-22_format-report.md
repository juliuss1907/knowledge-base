# Format Validation — 2026-11-22

**Status:** pending
**Issues found:** 394
**Created:** 2026-11-22 23:15:35 +0700
**Validator:** format-validator
**Files checked:** 1197 (648 concepts, 232 sources, 34 indexes, 283 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1197
Total issues: 394

Δ from 2026-11-21 23:15:24 run (approved): thêm ròng 6 tệp; tổng cảnh báo, số mục đơn, nhóm và số đích riêng trong các mục đơn không đổi. Không có đầu ra đầy đủ của lượt trước để xác nhận thành phần cảnh báo hoàn toàn không đổi. Đã duyệt không có nghĩa đã sửa.

| Chỉ số | 2026-11-21 | 2026-11-22 |
|---|---:|---:|
| Tệp | 1191 | 1197 |
| ERROR | 0 | 0 |
| WARNING | 394 | 394 |
| Mục liên kết đơn / nhóm | 375 / 19 | 375 / 19 |
| Đích riêng trong các mục đơn | 267 | 267 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1197 | 648 | 232 | 34 | 283 |

## Kết quả

Bộ kiểm tra báo 394 WARNING về liên kết không tìm thấy: 375 mục đơn và 19 mục nhóm. Mỗi nhóm đại diện nhiều liên kết; 394 không phải tổng số liên kết. Số 267 chỉ tính đích riêng từ các mục đơn. Các đích được báo nhiều nhất: `[[game-theory]]` (10), `[[confirmation-bias]]` (8), `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]` và `[[decision-making]]` (mỗi đích 5). Kiểm tra ngữ cảnh trước khi sửa; một số có thể là tham chiếu đến nội dung chưa biên soạn.

## 20 vấn đề ưu tiên

Các mục dưới đây là WARNING — Markdown. Hiện trạng: bộ kiểm tra không tìm thấy đích. Mong đợi: đích tồn tại hoặc liên kết trỏ đúng tệp. Đề xuất: kiểm tra ngữ cảnh, tạo nội dung hoặc sửa đích phù hợp; không xóa hàng loạt.

1. `wiki/concepts/activation-energy.md`: `[[breaking-point]]`.
2. `wiki/concepts/activation-energy.md`: `[[inertia]]`.
3. `wiki/concepts/activation-energy.md`: `[[momentum]]`.
4. `wiki/concepts/agent-backtesting.md`: `[[quantitative-finance]]`.
5. `wiki/concepts/agent-backtesting.md`: `[[reinforcement-learning-environments]]`.
6. `wiki/concepts/agent-sandbox-runtimes.md`: `[[prompt-injection]]`.
7. `wiki/concepts/ai-agent-tool-orchestration.md`: `[[agent-capability-discovery]]`.
8. `wiki/concepts/ai-agent-tool-orchestration.md`: `[[mcp-protocol]]`.
9. `wiki/concepts/ai-alignment.md`: `[[interpretability]]`.
10. `wiki/concepts/ai-alignment.md`: `[[reinforcement-learning]]`.
11. `wiki/concepts/ai-alignment.md`: `[[rlhf]]`.
12. `wiki/concepts/ai-dependency.md`: `[[attention-economy]]`.
13. `wiki/concepts/ai-dependency.md`: `[[automation-paradox]]`.
14. `wiki/concepts/ai-dependency.md`: `[[digital-minimalism]]`.
15. `wiki/concepts/ai-impression-of-work.md`: `[[ai-hype-vs-reality]]`.
16. `wiki/concepts/ai-legal-personhood.md`: `[[dao-legal-structure]]`.
17. `wiki/concepts/ai-safety-monitoring.md`: `[[ai-control]]`.
18. `wiki/concepts/ai-safety-monitoring.md`: `[[alignment-evaluation]]`.
19. `wiki/concepts/ai-safety-monitoring.md`: `[[capability-evaluation]]`.
20. `wiki/concepts/ai-text-watermarking.md`: `[[llm-output-detection]]`.

Danh sách giới hạn 20 mục; tổng 394 phản ánh toàn bộ đầu ra của bộ kiểm tra.

## Giới hạn kiểm tra

1. Báo cáo 2026-11-20 ghi nhận `validate.py` không phát hiện thứ tự phần bị đảo; không thể xác nhận quy tắc thứ tự phần đã được đáp ứng.
2. Script không kiểm tra đầy đủ mọi quy tắc đặc tả, gồm nhiều H1, kiểu danh sách, một số kiểu trường và sự tồn tại của các đích chứa `/`. Vì vậy 0 ERROR không chứng minh không có lỗi định dạng.
3. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
4. Liên kết trong khối mã có thể bị kiểm tra như liên kết thật; cần xác minh trước khi sửa.

## Escalations

- Giới hạn công cụ và tồn đọng liên kết đã được báo trước; không có bằng chứng chúng đã được xử lý.
- Bộ đếm các mục chờ cũ có trạng thái không nhất quán, cần đối soát riêng.

## Verification

- Đã đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md`; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Đã đối chiếu báo cáo đã duyệt 2026-11-21 và trạng thái Git. Không suy luận thành phần cảnh báo không đổi chỉ từ số tổng.
- Không sửa tệp nội dung wiki. Topic được kiểm tra theo quy tắc nhẹ của script.
