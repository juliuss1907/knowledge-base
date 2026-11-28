# Format Validation — 2026-11-28

**Status:** pending
**Issues found:** 394
**Created:** 2026-11-28 23:15:38 +0700
**Validator:** format-validator
**Files checked:** 1202 (649 concepts, 234 sources, 34 indexes, 285 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1202
Total issues: 394

Δ from 2026-11-27 23:15:45 (pending — lượt trước): số tệp, số phát hiện, cơ cấu nhóm và số đích riêng trong mục đơn không đổi. Không có đầu ra chi tiết của lượt trước để khẳng định thành phần từng cảnh báo không đổi. Có commit tác động phạm vi kiểm tra; không kết luận không có chỉnh sửa.

| Chỉ số | 2026-11-27 | 2026-11-28 | Chênh lệch |
|---|---:|---:|---:|
| Tệp kiểm tra | 1202 | 1202 | 0 |
| ERROR | 0 | 0 | 0 |
| WARNING | 394 | 394 | 0 |
| Liên kết đơn / nhóm | 375 / 19 | 375 / 19 | 0 / 0 |
| Đích riêng trong mục đơn | 267 | 267 | 0 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1202 | 649 | 234 | 34 | 285 |

## Kết quả

Bộ kiểm tra báo 394 WARNING: 375 mục liên kết đơn và 19 mục nhóm. Mỗi nhóm có thể chứa nhiều liên kết; 394 không phải tổng số liên kết. Có 267 đích riêng trong các mục đơn, không bao gồm đích chỉ xuất hiện trong nhóm. `[[game-theory]]` xuất hiện trong 10 mục đơn, `[[confirmation-bias]]` trong 8; `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]` và `[[decision-making]]` mỗi đích 5 mục đơn. Một số liên kết có thể trỏ tới nội dung chưa biên soạn.

## 20 vấn đề ưu tiên

Mỗi mục là WARNING về liên kết mà bộ kiểm tra không tìm thấy đích. Kiểm tra ngữ cảnh và xác nhận đích thực sự thiếu trước khi biên soạn hoặc sửa; không xóa hàng loạt.

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

Danh sách giới hạn 20 mục; tổng 394 phản ánh toàn bộ đầu ra bộ kiểm tra. Đầu ra đầy đủ: `wiki/reviews/.format-validation-current.txt`.

## Giới hạn kiểm tra

1. Script chưa bao phủ đầy đủ kiểu danh sách, một số kiểu trường, thứ tự phần và đích chứa `/`. Không thể coi 0 ERROR là chứng nhận tuân thủ đầy đủ.
2. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
3. Kiểm tra đích có thể tính liên kết trong khối mã; cần xác minh từng trường hợp. Danh sách tag trong script cố định, không tự đồng bộ `TAGS.md`.
4. Phạm vi index dựa trên danh sách đường dẫn cố định. Topic được kiểm tra theo quy tắc nhẹ.

## Escalations

Tồn đọng liên kết và giới hạn bộ kiểm tra đã được báo trước. Các mục chờ cũ trong `_action-required.md` có trạng thái không nhất quán, cần đối soát riêng.

## Verification

- Đã đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md`; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Đã đối chiếu báo cáo trước, lịch sử Git và trạng thái các tệp nội dung. Lượt trước vẫn pending; không suy diễn nguyên nhân từ tổng không đổi.
- Không sửa nội dung wiki. Không ghi `MEMORY.md` vì phạm vi ghi cho phép chỉ là `wiki/reviews/`.
