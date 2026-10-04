---
type: source
original: "[[2026-10-01_gemini-4-argon-explained-in-5min]]"
main_tag: ai
sub_tags: [news, research, strategy]
topic: gemini-4-argon
date_compiled: 2026-10-02
url: https://youtu.be/1ZbNgx6Gscw
author: Caleb Writes Code
---

# Gemini 4 Argon explained in 5min

## Metadata

- **Author:** Caleb Writes Code
- **Published:** 2026-10-01
- **Source:** youtube.com
- **URL:** https://youtu.be/1ZbNgx6Gscw
- **Type:** video
- **Duration:** 4:56
- **Transcript language:** en (bản dịch tiếng Việt)

## Summary

Google cuối cùng tung ra một flagship model sau 7 tháng chờ đợi — Gemini 4 Argon — sau khi liên tục phát hành các model dạng flash không giành được thị phần. Điểm nổi bật nhất là kết quả coding benchmark: 77,9% trên Deep SWE, đứng trên mọi model hiện có, nhưng video cảnh báo mạnh về độ tin cậy của con số này vì toàn bộ 113 task và lời giải của benchmark đã công khai từ tháng 5, khiến các lab có thể học và nhắm vào benchmark trong post-training; Epoch cũng đã phát hiện 23 task bị lỗi. Lợi thế giá không dịch được thành lợi thế thị trường: dù Argon rẻ hơn Anthropic và OpenAI về cost of intelligence, nó vẫn nằm dưới Pareto Frontier vì cả model adoption và harness adoption đều thua — Codex có 5 triệu weekly active users so với 2,4 triệu của anti-gravity. Chiến lược của Google là không chơi cuộc đua trợ giá subscription như OpenAI và Anthropic, mà dồn compute vào API channel đang thu doanh thu lớn (22 tỷ token/phút, hơn 11 quadrillion token/năm) và chấp nhận rằng sẽ phải giải bài toán supply constraint. Điểm đáng chú ý nhất về kỹ thuật là output token mở rộng từ 64.000 lên 1 triệu — một cam kết lớn về khả năng duy trì coherence trong autoregressive generation, mở đường cho các task dài hạn như code migration và nghiên cứu kéo dài.

## Key points

- **Gemini 4 Argon** là flagship model mới của Google sau khoảng 7 tháng kể từ lúc công bố; trước đó Google phát hành nhiều model dạng flash nhưng chúng khó giành được market adoption vì cạnh tranh với flagship model khác và open model giá rẻ từ Trung Quốc
- Kết quả benchmark sơ bộ rất mạnh, nổi bật nhất ở coding: **77,9% trên Deep SWE**, cao hơn mọi model hiện có
- **Benchmark contamination là rủi ro lớn:** toàn bộ 113 task cùng lời giải của Deep SWE được công khai từ tháng 5, nên lab có thể nghiên cứu và nhắm benchmark trong post-training rồi công bố model
- **Epoch đã tìm ra 23 task bị lỗi** trong bộ benchmark này — cơ sở để giữ "healthy skepticism" về mọi con số do lab tự báo cáo
- Đa số benchmark mà Google báo cáo đều là public benchmark → **lab ra model càng muộn càng có lợi thế nhẹ** vì có thể đưa chúng vào post-training
- **Benchmark saturate nhanh hơn trước**, buộc phải refresh thường xuyên hơn → người dùng phải tự gánh phần lớn gánh nặng theo dõi tiến bộ khoa học thật của AI
- **Model mạnh ≠ adoption:** dù Argon mạnh, Google vẫn chưa giải được bài toán làm anti-gravity thành lựa chọn cạnh tranh cho developer
- **Codex 5 triệu weekly active users vs anti-gravity 2,4 triệu** — hơn gấp đôi; phần lớn developer vẫn dùng Claude Code, Codex hoặc open harness
- **Cost of intelligence rẻ hơn không đủ:** Argon undercut cả Anthropic và OpenAI về giá, nhưng chỉ cho tới khi discount tạm thời kết thúc và giá tăng gấp đôi
- **Argon nằm dưới Pareto Frontier** — Anthropic và OpenAI vẫn dẫn đầu ở cả hai trục: harness adoption và model adoption
- **Áp lực IPO đổi chiến lược:** OpenAI và Anthropic có động lực lớn để trợ giá model thông qua subscription nhằm tăng user, còn Google đã là công ty đại chúng và phải cẩn thận phân bổ compute để tạo giá trị trong ecosystem của mình
- **Rollout theo segment:** Argon dành cho Ultra subscription users và paid API users — nơi doanh thu lớn đã được thu, thay vì đốt compute để đua subscription
- **Quy mô API của Google:** trong call Q2 earnings, Google cho biết API xử lý **22 tỷ token/phút**, tăng 6 tỷ so với quý trước — hơn **11 quadrillion token/năm** chỉ riêng kênh API; cộng thêm các kênh phân phối khác mới hiện rõ ý nghĩa thực sự của tuyên bố "supply constrained"
- **OpenAI và Anthropic sớm phải giải bài toán scaling** vừa duy trì biên lợi nhuận khỏe, vừa không chỉ dựa vào trợ giá subscription để giành user
- **Output token mở rộng từ 64.000 lên 1 triệu** — bước nhảy lớn bất thường với Google vì duy trì coherence khi autoregressive generation kéo dài càng khó
- **Vấn đề compounding error:** mỗi token có 99% độ tin cậy thì chuỗi 100 bước độc lập chỉ còn khoảng **37% khả năng mọi bước đúng** (đây là lý thuyết, giả định lỗi độc lập)
- **Yann LeCun** đã chỉ trích autoregressive model chính vì cơ chế sinh token liên tiếp làm lỗi tích luỹ trên quỹ đạo dài, chứ đừng nói tới 1 triệu token của Argon
- Việc Google dám mở rộng sản phẩm thương mại lên 1 triệu output token **mở đường cho long-horizon task** như code migration và research task chạy dài

## Concepts referenced

- [[gemini-4-argon]]
- [[benchmark-contamination]]
- [[model-vs-harness-adoption]]
- [[autoregressive-error-compounding]]
- [[ai-evals]]
- [[ai-lab-business-model]]

## Original excerpts

> "Scoring 77.9% on Deep SWE, which would put Gemini 4 Argon above every other model we currently have. But it's always good to have some healthy skepticism here."

> "Recently Epoch found issues on [Deep SWE], finding 23 tasks that are flawed. And looking back to when the benchmark was actually released back in May, the entire 113 tasks and their solutions are made public, which means labs that have access to these could easily study them during post training and benchmark their models around public benchmarks."

> "As users, all of this makes it really difficult to track real progress in AI since so many public benchmarks can be contaminated pretty fast."

> "The cost benefit that we find here doesn't actually translate in Pareto Frontier. As you can see, Argon falls below the Pareto Frontier, showing you that Anthropic and OpenAI still leads ahead in both the harness and model adoption."

> "On a recent Google's Q2 earning call, they said that their API is processing 22 billion tokens per minute, which is 6 billion more than the previous quarter. That's more than 11 quadrillion tokens per year in just API channel alone."

> "If you can imagine each token that's 99% reliable, chaining 100 independent steps together would leave about 37% chance of every step being correct."

## Notes
