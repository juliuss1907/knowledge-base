---
type: concept
status: draft
main_tag: ai
sub_tags: [strategy, research]
topic: open-models-us-china
sources:
  - "[[src_atom-project-american-truly-open-models]]"
  - "[[src_gemini-4-argon-explained-in-5min]]"
last_updated: 2026-10-02
---

# Compute Concentration Frontier

## Definition

Ràng buộc kỹ thuật rằng muốn dẫn đầu open model development, một lab cần cụm compute **tập trung** cỡ 10.000+ GPU thế hệ H100 — không thể chia nhỏ ngân sách thành nhiều dự án rải rác. Điểm tương phản là quy mô *lab*: nên có **nhiều lab**, mỗi lab một cụm đủ lớn.

## Key ideas

- **Ngưỡng 10.000+ GPU** là entry point cho rapid iteration *song song với* large-scale training — cho phép train nhiều biến thể cùng lúc thay vì chờ mỗi run kết thúc
- **Chia nhỏ ngân sách sẽ thất bại:** "Splitting such an investment in AI training into smaller, widespread projects will not be sufficient to build leading models due to a lack of compute concentration"
- **Quy mô model dẫn dắt 2025:** 100–600+ tỷ tham số, kiến trúc **mixture of experts (MoE)** — mọi open model tiên phong Mỹ và Trung Quốc đều dùng dải này để cạnh tranh intelligence benchmark với closed model
- **Team nhỏ, compute lớn:** model top thường train bằng 50 đến vài trăm người — ràng buộc là capital + compute, không phải headcount
- **Chi phí train bị truyền thông sai lệch:** con số $5M cho DeepSeek V3 từng được nêu rộng rãi, nhóm tác giả chính DeepSeek đã thừa nhận con số đó không phản ánh chi phí thực tế phát triển model
- **"Nhiều lab" có ba lý do riêng:** (1) de-risk tiến độ trong nhiệm vụ khẩn cấp, (2) tạo artifact đa dạng hơn, (3) các nhóm nghiên cứu học từ nhau mà không phải gộp thành tổ chức quá lớn làm chậm tiến bộ
- **Cần phân bố kích thước, không chỉ một model đỉnh:** từ chạy trên iPhone tới model phục vụ công trình trí tuệ khó nhất. Chỉ task khó nhất mới cần model lớn nhất; với task còn lại cần biết **kích thước model tối thiểu** để giải
- **Cách phân bổ nguồn lực:** cần huy động cả private companies, philanthropic institutions, government agencies — nhưng giải pháp ecosystem-wide kiểu NAIRR không thay thế được **cược tập trung** mà Trung Quốc đang dùng
- **Chỉ thị quan trọng bằng lượng compute:** công thức là đưa compute và talent tới nơi *với điều kiện phát hành model mở* — nếu không có chỉ thị, cùng lượng đó sinh ra closed model
- **Bài toán institutional:** khác với phòng thí nghiệm công ty tư nhân, chương trình công phải cân bằng giữa tốc độ (6–12 tháng) và tính bền vững của hệ sinh thái nghiên cứu
- **"Supply constrained" là hệ quả của phân phối tích tụ:** API của Google xử lý 22 tỷ token/phút — hơn 11 quadrillion token/năm chỉ riêng kênh API — và Google sở hữu thêm nhiều kênh phân phối khác, nên ràng buộc của họ là **cấp tải trong hệ sinh thái của chính mình**, không chỉ là số GPU dùng để train
- **Compute không nên chảy vào nơi không thu doanh thu:** open model giá rẻ từ Trung Quốc đẩy các flash model của Google vào thế khó giành adoption, vì compute được dồn vào phân phối rộng mà không gắn được doanh thu tương ứng
- **Lợi thế compute chỉ thành lợi thế khi đi kèm adoption:** Gemini 4 Argon rẻ hơn và mạnh hơn nhưng vẫn nằm dưới Pareto Frontier — xem [[model-vs-harness-adoption]]

## Related concepts

- [[open-model-ecosystem-race]]
- [[open-weight-vs-open-source]]
- [[mixture-of-experts-moe]]
- [[industrial-scale]]
- [[institutional-capacity]]
- [[infrastructure-capex-cycle]]
- [[model-vs-harness-adoption]]

## Sources

- [[src_atom-project-american-truly-open-models]] — Nathan Lambert, The ATOM Project
- [[src_gemini-4-argon-explained-in-5min]]

## Notes
