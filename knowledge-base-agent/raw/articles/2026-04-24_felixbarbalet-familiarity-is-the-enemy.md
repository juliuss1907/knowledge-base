---
type: raw
source_type: article
source_url: https://felixbarbalet.com/familiarity-is-the-enemy/
date_ingested: 2026-04-24
tags: [#research, #business]
status: processed
processed_date: 2026-04-25
---
# Familiarity is the Enemy — Felix Barbalet

## Tóm tắt

Bài luận dài 25 phút của Felix Barbalet (24/04/2026) — giải thích tại sao enterprise knowledge systems đã thất bại suốt 60 năm và đề xuất giải pháp thay thế.

## Chủ đề chính

**Core argument:** Enterprise software buyers chọn **familiar** thay vì **correct** — đây là lý do hệ thống quản lý tri thức enterprise thất bại suốt 4 thập kỷ.

**Quote nổi bật:**
> "Software is sold on the perception of safety by people who are rewarded for choosing safe options and penalised for choosing ones that turn out badly, regardless of whether those options actually were safer."

## 5 cách familiarity phá hủy enterprise intelligence

**1. The familiar vendor**
- SharePoint có 200M users nhưng được mô tả là "where documents come to die"
- HP mua Autonomy $11.1B sau 6 tiếng phone calls, sau đó viết off $8.8B
- Product không quyết định sale — familiarity của vendor mới là yếu tố

**2. The familiar language and architecture**
- Enterprise chọn Java/.NET/SAP không phải vì đúng tool mà vì dễ bảo vệ trong hiring committee
- Clojure bị reject vì "unfamiliar" dù Rich Hickey đúng về mặt kỹ thuật
- Thu nhập Clojure developers: họ tự filter — người muốn viết Clojure thường giỏi hơn

**3. The familiar buyer motion**
- Enterprise software không bán theo outcomes — bán license để shift implementation risk sang buyer
- Akerlof's "market for lemons" (1970 Nobel): vendor với best lemon-market signals thắng, không phải vendor với best product
- Procurement officers chọn "industry standard" để bảo vệ career risk — dù sản phẩm thường fail

**4. The familiar failure**
- Cyc (1984): $200M, 2,000 person-years, 30M assertions → thất bại hoàn toàn
- XCON (1980): 6,200 rules, 40-50% churn/year → retired 1990s
- Expert systems era: MYCIN, CADUCEUS, PROSPECTOR — technical success nhưng commercially never deployed
- 1997: 84% knowledge-management programs produced no significant impact
- **Root cause:** Knowledge encoded outlives its relevance faster than experts can update it

**5. The familiar AI stack (RAG)**
- 2023: Retrieval Augmented Generation được ca ngợi là definitive answer
- June 2024: Stanford benchmark — RAG systems kém expert humans đáng kể
- LLM "trains on CONVINCINGNESS rather than CORRECTNESS" (Doug Lenat, 2023)
- Đây là same failure mode viết lại bằng ngôn ngữ mới

## Rich Hickey's Simple vs Easy

- **Simple** = objective (không intertwined)
- **Easy** = relative (familiar = what your team already knows)

Enterprise đã confuse simple với easy suốt 40 năm — mua accidental complexity wholesale.

## Điểm mới

Khi code được viết bởi agents, familiar-language argument yếu nhất từ trước đến giờ — LLM không quan tâm codebase là Java hay Clojure.

## Nguồn

https://felixbarbalet.com/familiarity-is-the-enemy/