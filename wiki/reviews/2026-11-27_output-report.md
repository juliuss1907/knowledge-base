# Output Validation — 2026-11-27

**Status:** pending
**Issues found:** 3 (0 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-11-27 23:00 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét cơ học 883 tệp: 234 nguồn và 649 khái niệm. Đọc chi tiết 4 tệp có ngày biên soạn hoặc cập nhật 2026-11-27: 1 nguồn và 3 khái niệm. Ngày cập nhật không chứng minh cả 4 tệp đều mới tạo.
- Đối chiếu nguồn video và khái niệm agent-native với bản chép lời tại `raw/videos/2026-11-25_how-21-people-built-100m-agent-company.md`; đối chiếu nhận định về Price's Law với `wiki/sources/src_cach-thoat-khoi-prices-law.md`. Bản chép lời là nguồn cho phát biểu của diễn giả, không phải xác minh độc lập doanh thu hay hiệu quả công ty. Không kiểm chứng chi tiết bốn chiều cho 879 tệp còn lại.
- Hai liên kết `[[incentive-alignment]]` và `[[principal-agent-problem]]` tại `skin-in-the-game.md:34-35` chưa có đích khái niệm hoặc nguồn đúng tên; tìm tên tương ứng trong raw không thấy. Đây là liên kết cần đối soát cùng tồn đọng của Format Validator, không khẳng định phát sinh hôm nay. Có thể biên soạn khi có nguồn phù hợp hoặc bỏ liên kết sau khi duyệt.
- Không phát hiện mẫu mất chữ i trong bốn nhóm kiểm tra bổ sung, không phân biệt hoa thường. Quick-scan báo 117 định nghĩa một câu và 77 khái niệm ít ý theo heuristic; chưa xác minh từng trường hợp.
- Không sửa tệp nội dung. Các vấn đề sau được phát hiện trong tệp cập nhật, không khẳng định đều mới phát sinh hôm nay.

---

## Issue 1: Định nghĩa vòng phản hồi thiếu điều kiện quay lại điểm xuất phát

**File:** `wiki/concepts/feedback-loop.md:18`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Đầu ra của một phần làm đầu vào cho phần khác mới mô tả quan hệ nhân quả, chưa đủ để tạo vòng phản hồi. Định nghĩa không nêu tác động quay trở lại biến hoặc phần ban đầu.
**Evidence:** “output của một phần trở thành input của phần khác, tạo thành chuỗi ảnh hưởng qua lại.”
**Suggested fix:** Nêu rõ chuỗi tác động khép kín quay lại ảnh hưởng biến ban đầu; phân biệt vòng cân bằng và vòng khuếch đại theo tác động phản hồi.

---

## Issue 2: Quy tắc một tuần và giải thích Price's Law bị khái quát quá mức

**File:** `wiki/concepts/feedback-loop.md:32`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Tệp trình bày ngưỡng một tuần và lý do nhóm √n đạt năng suất cao như nguyên tắc chung. Nguồn được dẫn là lời khuyên cụ thể của Markus, không chứng minh ngưỡng đó đúng cho mọi loại vòng phản hồi hoặc mọi nhóm theo Price's Law.
**Evidence:** “Nhóm √n không giỏi hơn ở lần thử đầu — họ thử-sai-sửa nhanh hơn. Nguyên tắc: nếu feedback loop > 1 tuần, nó quá chậm”. Nguồn `src_cach-thoat-khoi-prices-law.md:23,28` quy thuộc chiến lược này cho Markus.
**Suggested fix:** Quy thuộc quy tắc cho Markus như một kinh nghiệm thực hành trong bối cảnh nguồn; bỏ hoặc bổ sung bằng chứng độc lập cho khẳng định so sánh toàn bộ nhóm √n.

---

## Issue 3: Mức tự động hóa hỗ trợ vượt quá bằng chứng trong bản chép lời

**File:** `wiki/concepts/agent-native-operations.md:23`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Câu này gợi ý toàn bộ chuỗi, kể cả liên hệ và bồi hoàn, có thể được tự động hóa. Bản chép lời nói lỗi được sửa bằng agent và đội gửi email, tặng credits, tra log và liên hệ chủ động; không xác định mỗi bước sau đều do agent tự động thực hiện.
**Evidence:** “Vòng lặp support có thể được tự động hóa từ phát hiện lỗi, sửa lỗi, xác định người dùng bị ảnh hưởng đến liên hệ chủ động và bồi hoàn.” Raw dòng 55: “we will fix it, of course, with the agent” và “We'll send an email to the person, we give them free credits”.
**Suggested fix:** Mô tả agent hỗ trợ sửa lỗi và đội thực hiện các bước còn lại; nếu muốn khẳng định toàn chuỗi tự động, bổ sung nguồn chứng minh từng bước.
