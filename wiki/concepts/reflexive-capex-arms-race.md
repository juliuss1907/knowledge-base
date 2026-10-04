---
type: concept
status: draft
main_tag: economic
sub_tags: [opinion, strategy]
topic: ai-credit-cycle
sources:
  - "[[src_the-second-derivative-why-no-one]]"
last_updated: 2026-09-30
---

# Reflexive Capex Arms Race

## Definition

Vòng lặp tự củng cố trong đó capex của hyperscaler tạo ra chính nhu cầu mà nó tuyên bố đang phục vụ, được duy trì bởi một Nash equilibrium **có điều kiện**: chi tiêu chỉ là chiến lược thống trị khi thị trường còn thưởng cho dollar chi tiêu tiếp theo. Điểm đảo chiều xảy ra khi thị trường bắt đầu thưởng cho việc *cắt* — và vì là coordination equilibrium, sự đảo không diễn ra dần dần.

## Key ideas

- **"Hyperscaler capex không chủ yếu là phản ứng với AI demand — ở mức độ đáng kể, nó *là* demand."** Doanh thu lab phần lớn là chi tiêu hyperscaler tái tuần hoàn; doanh thu Nvidia là capex hyperscaler; doanh thu neocloud là capex hyperscaler, đòn bẩy
- Bỏ chi tiêu ra thì nhu cầu hữu cơ, độc lập capex chỉ là một phần nhỏ của con số headline → tỷ lệ tăng trưởng quan trọng nhất trong hệ thống là **S″ của hyperscaler capex**
- Take-or-pay **không phải ràng buộc thụ động**: để justify gigawatt tiếp theo, hyperscaler cần backlog gigawatt tiếp theo → đẩy tenant commit xa hơn. $2.1T backlog không phải giới hạn sẵn có của cuộc đua, nó là **giấy vết của chính cuộc đua** ("the race writes the loan book")
- **Equilibrium có điều kiện**: trong boom regime, chi tiêu là hành động thống trị vì không chi là chấp nhận thua tương lai; leo thang chỉ bền vì thị trường hoan tán. Ai cũng chi vì mọi CFO khác đang chi và multiple thưởng kẻ chi
- **Keynesian beauty contest có chip**: "Bạn không chi vì bạn nghĩ compute đáng bao nhiêu — bạn chi vì bạn nghĩ thị trường sẽ thưởng cho việc được thấy là đã chi"
- Morgan Stanley mô tả capex 2027 nhảy 30% trong một quý như hành vi của một cuộc đấu giá — đúng frame, vì giá trong đấu giá do bidder lạc quan nhất ấn định và hành động bid tự nó là tín hiệu
- **Reflexive flip**: khi hyperscaler đầu tiên công bố cắt capex và multiple *tăng* thay vì giảm, mọi payoff viết lại — chi tiêu chuyển từ thống trị sang bị phạt một mình, cắt chuyển từ đầu hàng sang được định giá lại. Người đầu tiên được thưởng khi cắt cho mọi CFO khác cả cái cover lẫn động lực đi theo
- **Đây là lý do 2000 ≠ 2008**: equity multiple là vốn kiên nhẫn, có thể mark down rồi nắm giữ; credit structure thì snap
- **Điều đau nhất của cú flip là tác động lên các contract**: trong boom regime take-or-pay là asset cho mọi bên (forward demand, bankable backlog, collateral); sau repricing, **cùng contract đó là liability cho tất cả đồng thời**
- Hệ quả thay thế: không phải default gọn gàng mà là **thương lượng** — cắt volume, kéo dài lịch, restructure contract; contract không biến mất, chúng reprice, bắt đầu từ borrower cần vòng tiếp theo nhất
- **Ai chớp trước không phải balance sheet yếu nhất** mà là bên có thông tin tốt nhất + uy tín reframe + dư địa balance sheet để được thưởng thay vì bị phạt
- Bốn trường hợp: Meta (Zuckerberg dual-class, từng chạy đúng playbook này và được thưởng gấp 3; monetization capex yếu nhất vì không có public cloud để bán → spend khó bảo vệ nhất, dễ cắt nhất; chỉ chưa cắt vì chờ thị trường báo an toàn); Google (không thể — TPU lợi thế chi phí cấu trúc, backlog cloud >$460B, hưởng lợi khi đối thủ rút); Oracle (không thể — ~86% sales vào capex, stress lộ ra như một **credit event**); Amazon (bị ép từ hướng khác — FCF đã âm dưới build; thị trường vốn cuối cùng sẽ bỏ phiếu)
- **Leverage là biến số cận biên**: IG leverage ~1.8x gross debt, gấp đôi trong một năm, cao hơn cả ngành năng lượng — và con số đó không đếm hơn trăm tỷ đậu ngoài balance sheet
- **Gigawatt biên là dòng chi tiêu discretionary đầu tiên bị cắt** — cũng là thứ dễ cắt nhất để bảo vệ leverage
- **Rủi ro tương quan = 1 trước khi được kiểm tra**: Oracle >50% OpenAI, CoreWeave ~2/3 sau khi truy vết, SoftBank gần như toàn bộ qua Stargate. Giống 2008, hàng nghìn exposure "độc lập thống kê" hoá ra phụ thuộc một biến macro duy nhất — ở đây là *OpenAI có clear được mark kế tiếp hay không*

## Related concepts

- [[reflexivity-soros]]
- [[nash-equilibrium]]
- [[ai-infrastructure-bubble]]
- [[ai-capex-as-credit-cycle]]
- [[second-derivative-thinking]]
- [[infrastructure-capex-cycle]]
- [[repeated-games]]
- [[iterated-game-theory]]

## Sources

- [[src_the-second-derivative-why-no-one]] — Groundbreaker, "The Second Derivative: Why No One Understands the AI Boom"

## Notes
