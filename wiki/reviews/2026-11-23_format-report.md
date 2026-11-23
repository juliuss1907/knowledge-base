# Format Validation — 2026-11-23

**Status:** pending
**Issues found:** 394
**Created:** 2026-11-23 23:16:05 +0700
**Validator:** format-validator
**Files checked:** 1197 (648 concepts, 232 sources, 34 indexes, 283 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1197
Total issues: 394

Δ from 2026-11-22 23:15:35 run (pending): Số tệp, số mục và phân bố mức độ không đổi. Không có đầu ra đầy đủ của lượt trước để xác nhận toàn bộ thành phần cảnh báo không đổi; không suy luận rằng không có sửa chữa.

| Chỉ số | 2026-11-22 | 2026-11-23 |
|---|---:|---:|
| Tệp | 1197 | 1197 |
| ERROR | 0 | 0 |
| WARNING | 394 | 394 |
| Mục liên kết đơn / nhóm | 375 / 19 | 375 / 19 |
| Đích riêng trong các mục đơn | 267 | 267 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1197 | 648 | 232 | 34 | 283 |

## Kết quả

Bộ kiểm tra báo 394 WARNING: 375 mục liên kết đơn và 19 mục nhóm; một nhóm đại diện nhiều liên kết, nên 394 không phải tổng số liên kết. 267 là số đích riêng trong các mục đơn, không bao gồm những đích chỉ xuất hiện trong nhóm. Các đích được báo nhiều nhất trong mục đơn: `[[game-theory]]` (10), `[[confirmation-bias]]` (8), `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]`, `[[decision-making]]` (mỗi đích 5). Cần kiểm tra ngữ cảnh trước khi sửa; một số có thể là tham chiếu đến nội dung chưa biên soạn.

## 20 vấn đề ưu tiên

Các mục dưới đây đều là WARNING, loại Markdown. Hiện trạng: bộ kiểm tra không tìm thấy đích. Mong đợi: đích tồn tại hoặc liên kết trỏ đúng tệp. Đề xuất: kiểm tra ngữ cảnh, tạo nội dung hoặc sửa đích phù hợp; không xóa hàng loạt.

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

1. `validate.py` dòng 230–232 và 376–378 tạo danh sách theo thứ tự đặc tả thay vì thứ tự thực tế: không phát hiện được thứ tự phần bị đảo.
2. Script không kiểm tra đầy đủ mọi quy tắc, gồm nhiều H1, kiểu danh sách, một số kiểu trường và đích chứa `/`. Vì vậy 0 ERROR không chứng minh mọi tệp tuân thủ đặc tả.
3. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
4. Kiểm tra đích liên kết dùng cả nội dung khối mã; cần xác minh từng trường hợp trước khi sửa. Danh sách tag được cố định trong script, không tự đồng bộ `TAGS.md`.

## Escalations

Giới hạn bộ kiểm tra và tồn đọng liên kết đã được báo trước; chưa có bằng chứng các giới hạn đã được xử lý. Bộ đếm các mục chờ cũ có trạng thái không nhất quán, cần đối soát riêng.

## Verification

- Đã đọc `wiki/meta/format-spec.md`, `wiki/meta/index-spec.md` và script; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Báo cáo 2026-11-22 còn pending. Git ghi nhận cập nhật các tệp tag và topic; không dùng số lượng bằng nhau để khẳng định nội dung không đổi.
- Không sửa tệp nội dung wiki. Topic được kiểm tra theo quy tắc nhẹ của script.
