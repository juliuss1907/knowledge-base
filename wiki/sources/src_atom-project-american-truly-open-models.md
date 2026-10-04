---
type: source
original: "[[2025-08-04_atom-project-american-truly-open-models]]"
main_tag: ai
sub_tags: [geopolitics, research, opinion]
topic: open-models-us-china
date_compiled: 2026-09-30
url: https://atomproject.ai/
author: Nathan Lambert
---

# The ATOM Project — American Truly Open Models

## Metadata

- **Author:** Nathan Lambert
- **Published:** 2025-08-04
- **Source:** atomproject.ai
- **URL:** https://atomproject.ai/
- **Type:** website

## Summary

ATOM Project là một lời kêu gọi chính sách từ Nathan Lambert nhằm đảo ngược tình trạng Mỹ mất thế chủ động trong hệ sinh thái open AI models. Luận điểm trung tâm: các lab Mỹ vẫn *có* số model tốt, nhưng phần lớn phát hành model nhỏ với license hạn chế, trong khi Trung Quốc đã có ít nhất 5 phòng thí nghiệm liên tục phát hành model mở ngang hoặc vượt best open model của Mỹ, dẫn tới chiếm đa số top-10 LMArena và >40% model mới trên HuggingFace mỗi tháng. Tác giả gọi đây là việc Mỹ chạy "một vận động viên đơn độc" (Meta) đối đầu "một đội có hệ sinh thái" (Qwen, DeepSeek, Kimi…). Đề xuất cụ thể: Mỹ cần **nhiều** phòng thí nghiệm, mỗi nơi một cụm **10.000+ GPU thế hệ H100**, phát hành trọn bộ open model (weights + training data + checkpoints + code + license permissive), với thời gian thực thi 6–12 tháng chứ không phải nhiều năm.

## Key points

- **Định nghĩa phân loại quan trọng:** *open-weight* (chỉ có weights để inference/finetune) vs *open source* (weights + training data + training code). Bài viết dùng "truly open" theo nghĩa thứ hai
- **Bối cảnh chiến lược:** Mỹ từng là trung tâm open AI research nhờ hợp tác tech company ↔ university; Transformer, ChatGPT, các tiến bộ reasoning/agent đều ra đời từ hệ sinh thái đó. Nay model Mỹ đóng hơn, model Trung Quốc mở hơn
- **Đề xuất cốt lõi:** duy trì **nhiều lab** train open model với **10.000+ GPU leading-edge**; lý do "nhiều lab" là chia nhỏ giảm rủi ro và tạo artifact đa dạng, còn "10.000+ GPU" là vì **compute phải tập trung** — chia nhỏ ngân sách sẽ không đủ
- **Quy mô model dẫn dắt 2025:** 100–600+ tỷ tham số với kiến trúc **mixture of experts (MoE)** — dải kích thước mà mọi open model tiên phong Mỹ và Trung Quốc đều dùng để cạnh tranh benchmark intelligence với closed model
- **Cần cả một *hệ sinh thái* kích thước:** model từ chạy trên iPhone đến model phục vụ công trình tri thức khó nhất. "Chỉ task khó nhất mới cần model lớn nhất" — với phần còn lại cần biết *kích thước model tối thiểu* để giải
- **Rủi ro của đầu tơi lan man:** NAIRR và các giải pháp ecosystem-wide không đủ, vì Trung Quốc thắng bằng **cược tập trung**; cần can thiệp có mục tiêu trong 6–12 tháng
- **Bối cảnh lab Mỹ 2025:** số lượng lab tương đương Trung Quốc (~20 lab), nhưng nhiều lab Mỹ phát hành model *nhỏ hơn* với *license hạn chế hơn*
- **Ai2 (Olmo)** — người dẫn đầu open source thực sự, chủ yếu dense nhỏ, Apache 2.0, Olmo 3 32B Think được coi là reasoning model fully open tốt nhất từng có
- **Nvidia (Nemotron)** — được coi là người dẫn đầu open ở Mỹ sau Llama 4; Nemotron Nano 9B v2 ở phân khúc 9B ngang hoặc vượt model Trung Quốc; license ngày càng mở, đã có thêm data release
- **OpenAI (GPT OSS)** — bước ngoặt lớn: open weights đầu tiên kể từ GPT-2 (gpt-oss-120b), Apache 2.0
- **Meta (Llama)** — "original" nhưng im lặng sau "Llama 4 fiasco"; từng là model định nghĩa của cộng đồng nghiên cứu năm 2023–2024
- **Các lab khác:** IBM Granite (Apache 2.0, hybrid-attention), Liquid AI (license gần Apache nhưng chặn doanh thu ≥$10M/năm), Microsoft Phi (thường MIT), Google Gemma, HuggingFace SmolLM, Moondream (vision, on-device), ServiceNow Apriel (reasoning), Stanford Marin Community Models, Arcee/Datology/Prime Intellect Trinity (MoE), Reflection
- **Cú đánh đuổi kịp về adoption:** mùa hè 2023 Llama 2 có khoảng 500% download của Qwen 1.5 (10M vs 60M với Llama có 4 model, Qwen có 8); tới Qwen 2.5 (2024) khoảng cách thu hẹp còn ~20M download (cả hai vượt 120M)
- **Điểm gãy:** DeepSeek V3 và R1 phát hành frontier model với license permissive; **top 10 open model trên LMArena đều từ tổ chức Trung Quốc**; top 3 open model trên ArtificialAnalysis là Trung Quốc (tại thời điểm 4/8/2025)
- **Derivatives là metric quyết định:** đầu 2024 model Trung Quốc chiếm 10–30% finetune mới trên HuggingFace; nay derivative của Qwen >40% model ngôn ngữ xuất hiện mỗi tháng. Share derivative của Llama rơi từ đỉnh ~50% (cuối 2024) xuống còn 15%
- **Inference share:** sau khi DeepSeek ra mắt, Trung Quốc nắm dẫn đầu token share trên OpenRouter; token share theo quốc gia cũng dẫn đầu (nguồn arXiv:2511.02781)
- **Cơ chế cạnh tranh Meta thua:** Llama thắng nhờ performance + distribution channel sẵn có, *bất chấp* license hạn chế; Qwen và model Trung Quốc dùng license đơn giản rút gọn từ thực hành open-source, gỡ thêm một rào cản uptake
- **Cú sốc Meta:** chỉ có Meta trong 5-6 năm, giờ "sau khi Llama 3 và trước Llama 4, cảnh quan open model thay đổi căn bản" — Meta chạy solo chống lại cả Qwen (family đa kích thước) lẫn DeepSeek (frontier mở)
- **Đánh giá chất lượng deployment:** Qwen 3 effect, DeepSeek dẫn đầu phân khúc kích thước lớn, các nhóm mới của Mỹ vẫn chưa đạt quy mô tải
- **Bối cảnh chính sách:** White House AI Action Plan được xem là inflection point trong nhận thức về open models — innovation và adoption toàn cầu lợi ích vượt rủi ro đo được — nhưng vẫn thiếu artifact và hành động cụ thể
- **Bài toán đo lường:** thiếu adoption gần như không tạo tín hiệu, vì nó đo qua hành vi riêng tư — sentiment này xuất hiện nhiều trong trao đổi thực tế với các công ty muốn build trên open model
- **Phân bổ 3 nguồn lực cần thiết:** private companies, philanthropic institutions, government agencies — với điều kiện "phải hướng tới việc phát hành model mở"

## Concepts referenced

- [[open-weight-vs-open-source]]
- [[open-model-ecosystem-race]]
- [[compute-concentration-frontier]]
- [[mixture-of-experts-moe]]
- [[structural-competition]]
- [[institutional-capacity]]

## Original excerpts

> "America's best AI models have become more closed and restricted, while Chinese models have become more open, capturing substantial market share from businesses and researchers in the U.S. and abroad."

> "Recommendation: To regain global leadership in open source AI, America needs to maintain multiple labs focused on training open models with 10,000+ leading-edge GPUs."

> "We estimate that to lead in open model development, the United States needs to invest in multiple clusters of 10,000+ H100 level GPUs to create an ecosystem of fully open language models."

> "Splitting such an investment in AI training into smaller, widespread projects will not be sufficient to build leading models due to a lack of compute concentration."

> "Closed labs make closed research, and the acceleration of AI was built on open collaboration with world-class American models as the key tool."

> "China today has 5 amazing open labs, a number which is growing, and America has Meta as its open models champion. We are running Meta in a race against 5 other Chinese runners, and then complain when it doesn't win every race every time. Our problem is not Llama 4 being not state-of-the-art; our problem is running a solo athlete against a team built with an ecosystem to support its growth."

> "Meta's share of derivatives with the Llama models has dropped from a peak of nearly 50% in the fall of 2024 down to only 15% today."

> "The benefits of openly sharing a technology accrue to the builder in mindshare and other subtle soft power dynamics seen throughout the history of open source software."

> "Every stakeholder – from tech giants to philanthropies to federal agencies to researchers and engineers – must ask themselves: Are we funding or participating in the future of AI research, or are we ceding it to competitors who understand that open models are the foundation of AI supremacy?"
