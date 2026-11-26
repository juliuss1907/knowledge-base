# Format Validation — 2026-11-25

**Status:** approved
**Approved by:** Julius
**Issues found:** 394
**Created:** 2026-11-25 23:15:30 +0700
**Validator:** format-validator
**Files checked:** 1199 (648 concepts, 233 sources, 34 indexes, 284 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1199
Total issues: 394

Δ from 2026-11-24 23:15:29 (pending — lượt trước): thêm 2 tệp được kiểm tra, số mục cảnh báo không đổi. Không có đầu ra chi tiết của lượt trước để chứng minh toàn bộ thành phần cảnh báo không đổi.

| Chỉ số | 2026-11-24 | 2026-11-25 | Chênh lệch |
|---|---:|---:|---:|
| Tệp | 1197 | 1199 | +2 |
| ERROR | 0 | 0 | 0 |
| WARNING | 394 | 394 | 0 |
| Mục liên kết đơn / nhóm | 375 / 19 | 375 / 19 | 0 / 0 |
| Đích riêng trong các mục đơn | 267 | 267 | 0 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1199 | 648 | 233 | 34 | 284 |

## Kết quả

Bộ kiểm tra báo 394 WARNING: 375 mục liên kết đơn và 19 mục nhóm. Một nhóm đại diện nhiều liên kết; 394 không phải tổng số liên kết. Có 267 đích riêng trong các mục đơn; số này không bao gồm những đích chỉ xuất hiện trong nhóm. Các đích được báo nhiều nhất: `[[game-theory]]` 10 lần, `[[confirmation-bias]]` 8 lần; `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]` và `[[decision-making]]` mỗi đích 5 lần. Một số có thể là tham chiếu đến nội dung chưa biên soạn.

## 20 vấn đề ưu tiên

Tất cả là WARNING, loại Markdown. Hiện trạng: bộ kiểm tra không tìm thấy đích. Mong đợi: đích tồn tại hoặc liên kết trỏ đúng tệp. Đề xuất: kiểm tra từng ngữ cảnh, tạo nội dung hoặc sửa đích phù hợp; không xóa hàng loạt.

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

1. Bộ kiểm tra không phát hiện đúng thứ tự phần bị đảo; chưa kiểm tra đầy đủ nhiều H1, kiểu danh sách, một số kiểu trường và đích chứa `/`. Do đó 0 ERROR không chứng minh mọi tệp tuân thủ đặc tả.
2. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
3. Kiểm tra đích liên kết dùng cả nội dung khối mã; xác minh từng trường hợp trước khi sửa. Danh sách tag cố định trong script, không tự đồng bộ `TAGS.md`.
4. Phạm vi quét index là danh sách đường dẫn cố định; không khẳng định đã kiểm tra mọi tệp Markdown ngoài các thư mục được quét. Topic được kiểm tra theo quy tắc nhẹ.

## Escalations

Các giới hạn bộ kiểm tra và tồn đọng liên kết đã được báo trước. Bộ đếm các mục chờ cũ có trạng thái không nhất quán, cần đối soát riêng.

## Verification

- Đã đọc `wiki/meta/format-spec.md` và `wiki/meta/index-spec.md`; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Báo cáo 2026-11-24 còn pending. Git ghi nhận thêm `wiki/sources/src_what-becomes-valuable-when-intelligence-is-cheap.md` và `wiki/topic/human-value-ai-abundance.md` sau lượt trước, cùng chỉnh sửa các tệp khác. Số lượng bằng nhau không chứng minh nội dung không đổi.
- Không sửa tệp nội dung wiki. Không ghi `MEMORY.md` vì vùng ghi được phép chỉ là `wiki/reviews/`.
