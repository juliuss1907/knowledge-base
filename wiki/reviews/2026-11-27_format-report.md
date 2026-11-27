# Format Validation — 2026-11-27

**Status:** pending
**Issues found:** 394
**Created:** 2026-11-27 23:15:45 +0700
**Validator:** format-validator
**Files checked:** 1202 (649 concepts, 234 sources, 34 indexes, 285 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1202
Total issues: 394

Δ from 2026-11-26 23:15:34 (pending — lượt trước): tăng 3 tệp; số phát hiện không đổi. Git ghi nhận thêm một concept, một source và một topic. Không có đầu ra chi tiết lượt trước để kết luận toàn bộ thành phần cảnh báo không đổi.

| Chỉ số | 2026-11-26 | 2026-11-27 | Chênh lệch |
|---|---:|---:|---:|
| Tệp kiểm tra | 1199 | 1202 | +3 |
| ERROR | 0 | 0 | 0 |
| WARNING | 394 | 394 | 0 |
| Liên kết đơn / nhóm | 375 / 19 | 375 / 19 | 0 / 0 |
| Đích riêng trong mục đơn | 267 | 267 | 0 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1202 | 649 | 234 | 34 | 285 |

## Kết quả

Bộ kiểm tra báo 394 WARNING: 375 mục liên kết đơn và 19 mục nhóm. Mỗi nhóm có thể chứa nhiều liên kết, nên 394 không phải tổng số liên kết. Có 267 đích riêng trong các mục đơn; con số này không bao gồm các đích chỉ xuất hiện trong nhóm. `[[game-theory]]` xuất hiện 10 lần, `[[confirmation-bias]]` 8 lần; `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]`, `[[decision-making]]` mỗi đích 5 lần trong các mục đơn. Một số có thể là tham chiếu tới nội dung chưa biên soạn.

## 20 vấn đề ưu tiên

Các mục dưới đây đều là WARNING, loại Markdown: bộ kiểm tra không tìm thấy đích. Cần kiểm tra ngữ cảnh và sự tồn tại của đích, sau đó biên soạn nội dung hoặc sửa liên kết phù hợp; không xóa hàng loạt.

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

Danh sách giới hạn 20 mục; tổng 394 phản ánh toàn bộ đầu ra bộ kiểm tra.

## Giới hạn kiểm tra

1. Bộ kiểm tra chưa bao phủ đầy đủ kiểu danh sách, một số kiểu trường và đích chứa `/`. Vì vậy 0 ERROR không chứng minh mọi tệp tuân thủ đặc tả.
2. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
3. Kiểm tra đích có thể tính liên kết trong khối mã; cần xác minh từng trường hợp trước khi sửa. Danh sách tag trong script là cố định, không tự đồng bộ `TAGS.md`.
4. Phạm vi index dựa trên danh sách đường dẫn cố định. Topic được kiểm tra theo quy tắc nhẹ.

## Escalations

Tồn đọng liên kết và giới hạn bộ kiểm tra đã được báo trước. Các mục chờ cũ trong `_action-required.md` có trạng thái không nhất quán, cần đối soát riêng.

## Verification

- Đã đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md`; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Đã đối chiếu báo cáo trước, lịch sử Git và tệp chưa theo dõi. Ba tệp mới được Git ghi nhận là `wiki/concepts/agent-native-operations.md`, `wiki/sources/src_how-21-people-built-100m-agent-company.md`, `wiki/topic/agent-native-operations.md`.
- Không sửa nội dung wiki. Không ghi `MEMORY.md` vì vùng ghi được phép chỉ là `wiki/reviews/`.
