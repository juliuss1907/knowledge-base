---
type: concept
status: draft
tags: [#crypto, #finance]
---

# Morpho

## Mô tả
Morpho là một giao thức cho vay phi tập trung (DeFi lending protocol) được thiết kế để tối ưu hóa hiệu quả vốn và quản lý rủi ro thông qua kiến trúc phân lớp. Thay vì sử dụng một bể thanh khoản chung (pooled liquidity) như Aave hay Compound, Morpho cung cấp một hệ thống linh hoạt hơn bao gồm:

1. **Morpho Markets:** Các thị trường cho vay tách biệt (isolated markets) cho phép tùy chỉnh tài sản thế chấp, oracle và lãi suất. Thiết kế này giúp cô lập rủi ro, đảm bảo rằng sự cố tại một thị trường không gây sụp đổ toàn bộ giao thức.
2. **Morpho Vaults:** Các kho lưu trữ tuân theo chuẩn ERC-4626, cho phép người dùng gửi tài sản để nhận lợi nhuận. Các "curators" (chuyên gia rủi ro) sẽ điều phối vốn từ các Vault này vào các Market phù hợp để tối ưu hóa yield.

Nhờ tính tương thích cao (composable) và thiết kế an toàn, Morpho đang trở thành lớp hạ tầng (infrastructure layer) cho lending trong DeFi, thu hút sự quan tâm từ cả các tổ chức TradFi (như Apollo Global Management) và các tổ chức cốt lõi của Ethereum.

**Cập nhật 2026:**
- Quy mô cho vay active đạt ~$3.85B.
- Optics đối với các tổ chức rất tốt.
- Tuy nhiên, hiện tại **$0 doanh thu cho người nắm giữ token**, do giao thức tắt fee switch để tập trung vào giai đoạn tăng trưởng.

## Liên quan
- [[DeFi Lending]]
- [[ERC-4626]]
- [[Isolated Markets]]
- [[Real World Assets (RWA)]]

## Nguồn tham khảo
- [Morpho — DeFi Lending Juggernaut](wiki/sources/src_morpho-defi-lending.md)
