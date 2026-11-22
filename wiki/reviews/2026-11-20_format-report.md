# Format Validation — 2026-11-20

**Status:** approved
**Approved by:** Julius
**Issues found:** 394
**Created:** 2026-11-20 23:15:36 +0700
**Validator:** format-validator
**Files checked:** 1173 (638 concepts, 225 sources, 34 indexes, 276 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1173
Total issues: 394

Δ from 2026-11-19 23:15:23 run (approved): tổng số mục, phân loại mức độ, số tệp, số nhóm và số đích trong các mục đơn không đổi. Báo cáo trước không lưu toàn bộ kết quả, nên không thể xác nhận thành phần cảnh báo hoàn toàn giống nhau.

| Chỉ số | 2026-11-19 | 2026-11-20 |
|---|---:|---:|
| Tệp | 1173 | 1173 |
| ERROR | 0 | 0 |
| WARNING | 394 | 394 |
| Mục liên kết đơn / nhóm | 375 / 19 | 375 / 19 |
| Đích riêng trong các mục đơn | 267 | 267 |

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1173 | 638 | 225 | 34 | 276 |

## Kết quả

Bộ kiểm tra báo 394 WARNING về liên kết không tìm thấy: 375 mục đơn và 19 mục nhóm. Đây là số mục, không phải tổng số liên kết: mỗi nhóm đại diện nhiều liên kết. Con số 267 chỉ tính đích riêng từ các mục đơn. Các đích được báo nhiều nhất là `[[game-theory]]` (10), `[[confirmation-bias]]` (8), `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]` và `[[decision-making]]` (mỗi đích 5). Một số có thể là tham chiếu tới nội dung chưa biên soạn; cần xác minh trước khi sửa.

## 20 vấn đề ưu tiên

Mỗi mục dưới đây là **WARNING — Markdown**. Hiện trạng: bộ kiểm tra không tìm thấy đích. Mong đợi: đích tồn tại hoặc liên kết trỏ đúng tệp. Đề xuất: kiểm tra ngữ cảnh, sau đó tạo nội dung hoặc sửa đích phù hợp; không xóa hàng loạt.

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

Danh sách được giới hạn 20 mục; tổng 394 phản ánh toàn bộ đầu ra của bộ kiểm tra.

## Giới hạn kiểm tra

1. `validate.py` dòng 229–233 tạo thứ tự phần từ danh sách chuẩn thay vì thứ tự thực tế; không phát hiện được phần bị đảo. Không thể xác nhận quy tắc thứ tự phần đã được đáp ứng.
2. Script không kiểm tra đầy đủ mọi quy tắc đặc tả, gồm nhiều H1, kiểu danh sách, một số kiểu trường và sự tồn tại của các đích chứa `/`. Vì vậy 0 ERROR không chứng minh không có lỗi định dạng.
3. Script phân loại `original` không tìm thấy là WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
4. Liên kết trong khối mã vẫn có thể bị kiểm tra như liên kết thật; cần xác minh từng trường hợp trước khi sửa.

## Escalations

- Giới hạn công cụ và tồn đọng liên kết đã được nêu trong báo cáo 2026-11-19; lượt này không có bằng chứng mới để khẳng định đã xử lý.
- Commit gần nhất được kiểm tra là `c1688317`, ngày 2026-11-17 10:07:51 +0700; không thể dùng riêng lịch sử Git để kết luận không có thay đổi sau lần chạy trước.
- Bộ đếm báo cáo chờ có ghi chú cần đối soát; không tự suy đoán số lượng.

## Verification

- Đã đọc `wiki/meta/format-spec.md`, `wiki/meta/index-spec.md`; chạy `validate.py` và `parse_issues.py`. Bộ kiểm tra báo 0 lỗi đọc.
- Đã đối chiếu báo cáo đã duyệt 2026-11-19; chưa có dữ liệu đầy đủ để khẳng định thành phần 394 cảnh báo không đổi.
- Đã kiểm tra trạng thái Git; nhiều tệp tag và topic có thay đổi chưa cam kết. Không suy luận rằng tầng wiki bất biến chỉ từ lịch sử Git.
- Không sửa các tệp nội dung wiki. Kiểm tra topic theo quy tắc nhẹ của script.
