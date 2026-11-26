# Output Validation — 2026-11-25

**Status:** approved
**Approved by:** Julius
**Issues found:** 3 (0 ERROR, 3 WARNING, 0 INFO)
**Created:** 2026-11-25 23:00 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Đã quét cơ học 881 tệp: 233 sources và 648 concepts. Kiểm tra nội dung chi tiết 4 tệp mới hoặc cập nhật sau báo cáo ngày 2026-11-24: 1 source và 3 concepts.
- Đã đối chiếu bài nguồn mới với bản raw tại `raw/articles/2026-04-09_what-becomes-valuable-when-intelligence-is-cheap.md`. Bài gốc là bài luận dự báo; đối chiếu thể hiện đúng quan điểm tác giả không chứng minh các dự báo là sự thật. Chưa kiểm chứng độc lập toàn bộ các nguồn cũ và toàn bộ nội dung của 881 tệp.
- Bốn tệp đều có đủ liên kết nguồn trong thân so với frontmatter; các wikilink nội dung của bốn tệp có đích đúng tên. Source có 4 câu tóm tắt và 9 ý chính; ba concept có ít nhất 5 ý chính.
- Quét bổ sung bốn nhóm lỗi mất chữ i không phân biệt hoa thường: chỉ thấy một lỗi cũ tại `wiki/concepts/internal-locus-of-control.md:16`, đã báo ngày 11-23. Không tính lại vào 3 vấn đề dưới đây. Các nhóm lỗi của quick-scan không có kết quả.
- Không sửa, di chuyển hoặc xóa tệp nội dung. Các khuyến nghị chờ phê duyệt.

---

## Issue 1: Khái quát tuyệt đối về cách hình thành taste

**File:** `wiki/concepts/taste-judgment.md:15,19-20,23`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Định nghĩa và các ý chính khẳng định tuyệt đối taste không ai dạy được, chỉ hình thành bằng immersion và chỉ người có taste mới biết chọn output. Đây là những khẳng định rộng, thiếu giới hạn và bằng chứng tương ứng. Bài nguồn mới trình bày dự báo về sự khan hiếm của taste, không chứng minh các khẳng định tuyệt đối này.
**Evidence:** “thứ không ai dạy được mà chỉ đến từ việc tiêu thụ hàng trăm, hàng nghìn sản phẩm”; “taste chỉ hình thành qua immersion”; “chỉ người có taste mới biết output nào đáng giữ”.
**Suggested fix:** Nêu đây là một quan điểm hoặc giả thuyết có điều kiện, bổ sung nguồn cho những khẳng định có thể kiểm chứng và phân biệt rèn luyện qua trải nghiệm với việc không thể được hướng dẫn.

---

## Issue 2: Dự báo về lợi thế con người được trình bày như kết luận chắc chắn

**File:** `wiki/concepts/human-premium.md:15,19,23-25`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Concept khẳng định lợi thế cạnh tranh bền vững và giá trị bền vững chỉ đến từ một cách tiếp cận, trong khi nguồn mới đưa ra nhận định và dự báo về lợi thế tương đối, không chứng minh tính bền vững hay tính độc quyền của chúng.
**Evidence:** “lợi thế cạnh tranh bền vững khi technical skills ngày càng bị AI san bằng”; “Real, durable value chỉ đến từ việc tập trung vào những vấn đề thực sự ambitious”.
**Suggested fix:** Gắn các dự báo với tác giả hoặc nguồn cụ thể, bỏ các từ tuyệt đối không được chứng minh và nêu điều kiện hoặc giới hạn của lợi thế được đề xuất.

---

## Issue 3: Giới hạn AI và chuyển dịch công việc bị khẳng định không có điều kiện

**File:** `wiki/concepts/human-judgment-ai.md:19-22,26`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Các câu phân biệt trách nhiệm con người và khả năng của AI bị diễn đạt thành các mệnh đề tuyệt đối. Ý mới tại dòng 26 cũng trình bày kịch bản AI đảm nhiệm toàn bộ chu trình như bối cảnh xác định, trong khi raw dòng 72 là dự báo của tác giả. Cần phân biệt lựa chọn quản trị, giới hạn kỹ thuật hiện tại và dự báo.
**Evidence:** “AI không thể quyết định \"điều gì là quan trọng\"”; “AI không nhận thức được quyền lực và niềm tin trong hệ thống”; “Khi AI đảm nhận toàn bộ chu trình tạo dịch vụ”.
**Suggested fix:** Quy định rõ các quyết định về giá trị và trách nhiệm nên do con người nắm giữ; mô tả giới hạn AI theo phạm vi và bằng chứng; gắn kịch bản chuyển dịch với tác giả như một dự báo.
