# Output Validation — 2026-11-19

**Status:** approved
**Approved by:** Julius
**Issues found:** 4 (0 ERROR, 4 WARNING, 0 INFO)
**Created:** 2026-11-19 23:00:26 +0700
**Validator:** output-validator

## Phạm vi và giới hạn

- Quét tự động 863 tệp: 225 sources và 638 concepts. Không có tệp mang ngày biên soạn hoặc cập nhật 2026-11-19.
- Đọc chi tiết 5 tệp ngày 2026-11-07 vì báo cáo trước chỉ đề xuất kiểm tra chúng, chưa xác nhận đã kiểm tra. Đối chiếu với `raw/articles/2026-11-04_cognitive-offloading-learning-ai.md`. Hai tệp khác có thời gian sửa sau báo cáo trước được đọc lại; ngày frontmatter của chúng không thay đổi.
- Các chỉ số quét là phép kiểm cơ học, không phải kiểm chứng đầy đủ tính chính xác, mạch lạc hoặc chất lượng tiếng Việt của toàn bộ 863 tệp. Không kiểm chứng độc lập bài báo gốc trên mạng hoặc các nghiên cứu nền.
- Quét bốn mẫu lỗi mất chữ i: không có kết quả. Công cụ quét báo 117 định nghĩa một câu và 77 concept có ít hơn 5 ý; đây là chỉ số tồn đọng theo heuristic, chưa kiểm chứng từng tệp và không cộng thành số lỗi mới.

## Issue 1: Chưa nêu rõ cấp học trong mô tả nghiên cứu

**File:** `wiki/sources/src_cognitive-offloading-learning-ai.md:24,31`; `wiki/concepts/cognitive-offloading.md:24`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Ba vị trí ghi học sinh trung học mà không nêu rõ cấp; bản raw ghi rõ middle schoolers, tức học sinh trung học cơ sở.
**Evidence:** Source và concept ghi “học sinh trung học Brazil”; raw dòng 74 ghi “Brazilian middle schoolers”. Cụm tiếng Việt “trung học” có thể bao gồm cả hai cấp, nên cần làm rõ thành trung học cơ sở thay vì suy diễn cấp phổ thông.
**Suggested fix:** Ghi rõ “học sinh trung học cơ sở Brazil” ở cả ba vị trí, đối chiếu nghiên cứu gốc nếu có thể.

## Issue 2: Gán kết quả của một nghiên cứu cho cả tổng quan

**File:** `wiki/sources/src_cognitive-offloading-learning-ai.md:24,32`; `wiki/concepts/cognitive-offloading.md:26`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Cách viết gộp kết quả giảm khả năng nhớ và hoạt động não vào kết luận của toàn bộ tổng quan, trong khi nguồn chỉ nêu một nghiên cứu cụ thể. Phát biểu về tác hại của chatbot cũng mạnh hơn mức thận trọng trong nguồn.
**Evidence:** Source dòng 32 viết “Tổng quan 800+ bài báo, lọc còn 20 nghiên cứu causal chất lượng cao: chatbot đa dụng ... làm giảm recall và giảm hoạt động não”; raw dòng 86 ghi “There was one study”, còn dòng 88 nói điểm thi “had the potential to decrease”.
**Suggested fix:** Tách rõ phát hiện của một nghiên cứu khỏi nhận định của tổng quan; giữ ngôn ngữ về khả năng, không khẳng định mọi chatbot đều gây kết quả đó.

## Issue 3: Thổi phồng độ chắc chắn về scaffolding

**File:** `wiki/sources/src_cognitive-offloading-learning-ai.md:35`; `wiki/concepts/scaffolded-learning-tools.md:16,20,24`
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Bài viết mô tả tác hại với công cụ có hỗ trợ tư duy là chưa rõ; các tệp suy diễn thành giảm rõ tác hại hoặc khẳng định công cụ bảo vệ kết quả học tập và cảm xúc.
**Evidence:** Source ghi “scaffolding ... giảm rõ tác hại”; concept ghi “chính mức scaffolding quyết định AI giúp hay hại việc học”. Raw dòng 92 ghi “the detrimental effects of cognitive offloading were not as clear”; dòng 34 ghi “likely”.
**Suggested fix:** Ghi đây là tín hiệu ban đầu chưa chắc chắn, phân biệt giả thuyết thiết kế với hiệu quả đã được chứng minh.

## Issue 4: Khẳng định tuyệt đối về đo lường chuyển giao

**File:** `wiki/concepts/transfer-of-learning.md:25`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Khẳng định không thể đo transfer bằng điểm số tức thời quá rộng: bài kiểm tra trong ngữ cảnh mới vẫn có thể dùng điểm để đánh giá chuyển giao. Kết quả có công cụ ở bài ban đầu không tự chứng minh năng lực tự thân.
**Evidence:** “Transfer không đo được bằng điểm số tức thời”; raw dòng 42 định nghĩa transfer là khả năng áp dụng kiến thức vào ngữ cảnh mới, không phủ nhận dùng điểm số.
**Suggested fix:** Nêu điểm ở tác vụ ban đầu, nhất là khi còn công cụ, không đủ để xác lập transfer; đánh giá riêng trên tác vụ mới và nêu điều kiện sử dụng công cụ.

## Ghi chú hàng đợi

Trước lần này `_action-required.md` ghi 53 báo cáo chờ, nhưng có 60 tiêu đề cấp ba trong mục Pending Reports. Một mục không có trường trạng thái; con số tiêu đề không tự chứng minh cả 60 báo cáo thực sự còn chờ. Cần đối soát trạng thái trước khi điều chỉnh lịch sử.
