# Format Validation — 2026-11-19

**Status:** approved
**Approved by:** Julius
**Issues found:** 394
**Created:** 2026-11-19 23:15:23 +0700
**Validator:** format-validator
**Files checked:** 1173 (638 concepts, 225 sources, 34 indexes, 276 topics)
**ERRORs**: 0
**WARNINGS**: 394
**INFOS:** 0
**Total issues**: 394
Files checked: 1173
Total issues: 394

Δ from 2026-11-07 10:22:07 run (pending — lần gần nhất): 396 → 394 mục; 2 ERROR về `sub_tags` không còn; 394 WARNING không đổi về số lượng. Số tệp 1172 → 1173. Báo cáo trước không liệt kê đầy đủ tập liên kết nên không thể kết luận thành phần cảnh báo không đổi. Hai tệp trước đây bị báo lỗi hiện dùng các tag Pool B hợp lệ; không suy đoán tác nhân sửa.

---

| Files checked | Concepts | Sources | Indexes | Topics |
|---|---|---|---|---|
| 1173 | 638 | 225 | 34 | 276 |

## Tóm tắt phát hiện

Bộ kiểm tra ghi 394 WARNING: 375 mục liên kết đơn và 19 mục nhóm liên kết không tìm thấy. Đây là số mục báo cáo, không phải số liên kết hỏng thực tế; mỗi mục nhóm đại diện nhiều liên kết. Trình phân tích ghi 267 đích riêng biệt từ các mục liên kết đơn; không khẳng định con số này bao gồm mọi đích trong 19 nhóm. Một liên kết không tìm thấy có thể là tham chiếu tới nội dung chưa biên soạn, nhưng cần kiểm tra trước khi kết luận hoặc sửa.

Các đích xuất hiện nhiều nhất trong các mục đơn: `[[game-theory]]` 10, `[[confirmation-bias]]` 8; `[[deep-work]]`, `[[ai-coding-agents]]`, `[[career-design]]`, `[[decision-making]]` mỗi đích 5.

## Vấn đề ưu tiên

Các mục sau đều **WARNING — Markdown**. Hiện trạng: đích wikilink không được bộ kiểm tra tìm thấy. Mong đợi: đích tồn tại hoặc liên kết được sửa thành đích đúng. Đề xuất: đối chiếu ngữ cảnh và tạo nội dung hoặc sửa liên kết khi thích hợp; không xóa hàng loạt.

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

Danh sách giới hạn 20 mục; tổng 394 là toàn bộ đầu ra, không phải toàn bộ số liên kết riêng lẻ.

## Giới hạn kiểm tra

1. `validate.py` dòng 229–233 và 375–379 xây dựng thứ tự phần từ danh sách chuẩn thay vì thứ tự thực tế; do đó không phát hiện được phần bị đảo thứ tự. Không thể xác nhận tuân thủ quy tắc thứ tự phần.
2. Script không thực hiện đầy đủ các quy tắc trong đặc tả, gồm nhiều H1, kiểu danh sách, và một số kiểm tra kiểu trường. Nó cũng bỏ qua đích wikilink chứa `/` khi kiểm tra tồn tại. Vì vậy 0 ERROR chỉ là kết quả của script, không phải chứng nhận không có lỗi.
3. Đối với `original` không tìm thấy, script báo WARNING dù `format-spec.md` §3.2 quy định ERROR; lượt này không có cảnh báo loại đó.
4. Đích liên kết trong khối mã vẫn được quét bởi kiểm tra liên kết hỏng; một số kết quả có thể là ví dụ, cần xác minh từng mục trước khi sửa.

## Escalations

- **Sai lệch công cụ:** Sửa bộ kiểm tra theo các giới hạn trên trong một tác vụ riêng; không thay đổi nội dung wiki trong lượt kiểm tra này.
- **Trạng thái đợt trước:** Báo cáo 11-07 vẫn pending. Hai ERROR cụ thể trong báo cáo đó không còn ở trạng thái tệp hiện tại; không tự động thay đổi trạng thái phê duyệt.
- **Sổ phê duyệt:** bộ đếm chờ hiện có ghi chú không khớp số mục; không tự xác nhận tổng số khi chưa đối soát từng trạng thái.

## Verification

- Đã đọc `wiki/meta/format-spec.md`, `wiki/meta/index-spec.md` và `TAGS.md`.
- Chạy `validate.py` trên tập tệp được script chọn; 0 lỗi đọc. Đã chạy `parse_issues.py` để tổng hợp.
- Đã đối chiếu hai tệp bị báo ERROR ngày 11-07 và báo cáo gốc. Script quét 276 topic theo quy tắc nhẹ, không phải kiểm tra đầy đủ như concept/source.
- Không sửa tệp nội dung wiki. Báo cáo chỉ phản ánh các quy tắc được script thực thi; các thiếu sót nêu riêng ở trên.
