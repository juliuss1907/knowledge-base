---
type: raw
source_type: video
source_url: https://www.youtube.com/watch?v=ow1we5PzK-o
date_ingested: 2026-05-22
main_tag: ai
sub_tags: [tools, automation]
topic: factory-missions-architecture
status: processed
compiled_at: 2026-05-23
compiled_to: [[src_luke-alvoeiro-multi-agent-architecture-factory.md]]
---

# The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory

## Metadata

- **Speaker:** Luke Alvoeiro (Factory)
- **Source:** YouTube
- **URL:** https://www.youtube.com/watch?v=ow1we5PzK-o
- **Date Ingested:** 2026-05-22

## Executive Summary

Tài liệu này trình bày về "Missions", một kiến trúc đa tác vụ (multi-agent) tiên tiến được phát triển bởi Factory nhằm mang lại khả năng tự trị hoàn toàn cho vòng đời phát triển phần mềm (SDLC). 

**Nút thắt cổ chai cốt lõi:** Không nằm ở trí tuệ mà là **sự chú ý của con người**. Các kỹ sư giỏi nhất cũng chỉ có thể xử lý một vài tác vụ cùng lúc do nhu cầu giám sát và đánh giá liên tục.

**Giải pháp:** Hệ thống "Missions" chuyển đổi từ việc con người trực tiếp thực hiện sang việc con người quyết định **cái gì** cần xây dựng, để hệ thống tự tìm ra cách **làm thế nào**.

## Kiến trúc Ba Vai Trò Cốt Lõi

1. **Điều phối viên (Orchestrator)** — Lập kế hoạch
   - Đóng vai trò như một đối tác tư duy (sounding board)
   - Đặt ra các câu hỏi chiến lược để làm rõ yêu cầu chưa rõ ràng
   - Tạo ra kế hoạch bao gồm các tính năng, cột mốc và **Hợp đồng xác thực (Validation Contract)**
   - Định nghĩa "hoàn thành" trước khi bất kỳ dòng mã nào được viết

2. **Người thực hiện (Worker)** — Thực thi
   - Xử lý việc triển khai thực tế
   - Mỗi Worker bắt đầu với một ngữ cảnh sạch, không bị tích tụ "hành lý" từ các phiên trước
   - Thực hiện cam kết (commit) qua Git, cho phép Worker tiếp theo kế thừa mã nguồn sạch

3. **Người xác thực (Validator)** — Kiểm tra
   - **Xác thực rà soát (Scrutiny Validator):** Kiểm tra truyền thống (lint, type check, tests) và đánh giá mã nguồn
   - **Xác thực thử nghiệm người dùng (User Testing Validator):** Hoạt động như kỹ sư QA, tương tác qua giao diện để đảm bảo luồng chức năng
   - **Tính đối kháng:** Các Validator chưa bao giờ nhìn thấy mã nguồn trước đó, đảm bảo tính khách quan

## Phân Loại Các Khung Làm Việc Đa Tác Vụ (Multi-Agent Taxonomy)

5 mô hình giao tiếp cơ bản giữa các tác vụ:

1. **Ủy quyền (Delegation):** Tác vụ cha tạo tác vụ con xử lý vấn đề cụ thể — hình thức đơn giản và phổ biến nhất
2. **Người tạo - Người xác thực (Creator-Verifier):** Một tác vụ thực hiện, một tác vụ kiểm tra — loại bỏ "định kiến về chi phí"
3. **Giao tiếp trực tiếp (Direct Communication):** Các tác vụ nhắn tin trực tiếp — khó thực hiện do trạng thái dễ phân mảnh
4. **Thương lượng (Negotiation):** Tương tác qua tài nguyên chung — hiệu quả khi đạt trao đổi cùng có lợi
5. **Phát sóng (Broadcast):** Một tác vụ gửi thông tin đến tất cả — yếu tố then chốt duy trì tính nhất quán

## Nguyên Tắc Vận Hành Quan Trọng

- **Hợp đồng xác thực (Validation Contract):** Được viết **trước** khi triển khai — định nghĩa rõ ràng "hoàn thành" là gì
- **Quy trình bàn giao (Handoff) có cấu trúc:** Duy trì ngữ cảnh giữa các tác vụ
- **Chiến lược thực thi tuần tự:** Giảm thiểu xung đột giữa các tác vụ

## Kết Quả Thực Tế

- Hệ thống có thể chạy liên tục lên đến **16 ngày** (tiềm năng lên đến 30 ngày)
- Tạo ra mã nguồn sạch với độ bao phủ kiểm thử cao

## Related Content

- Google Docs note chi tiết: https://docs.google.com/document/d/e/2PACX-1vQTt9ppCFv0Mb97gbUIF4hbdmLWaktb4NqNwNT985kmlGbKlBcEq8CGZ92PtvJWHDOYbvHp922lOkQB/pub
- Edit link: https://docs.google.com/document/d/1PeFfkdS-ss6gxHFspLYDZOlloVsS22azx6r03ji63kU/edit?usp=sharing
