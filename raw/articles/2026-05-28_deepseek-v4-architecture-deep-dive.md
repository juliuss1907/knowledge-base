---
type: raw
source_type: article
source_url: https://boringbot.substack.com/p/deepseek-v4-architecture-deep-dive
date_ingested: 2026-05-28
tags: [ai, research, tech]
status: processed
compiled_at: 2026-05-29
compiled_to: "[[src_deepseek-v4-architecture]]"
---

# DeepSeek V4 Architecture Deep Dive

**Author:** Hamza Farooq (UCLA, MAVEN, Traversaal.ai)  
**Source:** Substack — Boring Bot  
**Date:** 2026-05-13  
**URL:** https://boringbot.substack.com/p/deepseek-v4-architecture-deep-dive

---

## Summary

Phân tích kiến trúc DeepSeek V4 Pro (1.6T tham số) và V4 Flash (284B), so sánh với V3, Claude Opus, OpenAI. Tập trung vào architectural innovations: CSA/HCA hybrid attention, FP4 Lightning Indexer, MCHC — những thứ quyết định production deployment, không chỉ benchmark.

## Core Argument

Việc chọn giữa V4 Pro và V4 Flash không đơn thuần là đánh đổi throughput vs. capability. Hai biến thể có attention topology khác nhau, KV cache pressure profile khác nhau, memory access patterns khác nhau — với cascading effects lên GPU memory budgeting, batching strategy, và multi-agent serving infrastructure.

## Key Points

### 1. V3 → V4: Khoảng cách lớn hơn vẻ bề ngoài

| Thông số | V3 | V4 Pro | V4 Flash |
|----------|-----|--------|----------|
| **Tổng tham số** | 671B | 1.6T | 284B |
| **Activated/token** | ~37B (5.5%) | ~49B (3.1%) | ~13B (4.6%) |
| **Context window** | 128K | 1M tokens | 1M tokens |
| **Attention** | MLA (single-mechanism) | CSA + HCA hybrid | CSA + HCA hybrid |
| **Optimizer** | AdamW | Muon (32T+ tokens) | Muon |
| **Precision** | FP8 | FP8/FP4 (QAT) | FP8/FP4 |

**So sánh activation ratio:** Mixtral 8×22B ~28%, V4 Pro ~3.1% → sparsity cực kỳ mạnh mẽ, chỉ khả thi nhờ routing và expert specialization được engineering ở mức rất cao.

> "V4 Flash KHÔNG phải là phiên bản distilled hay compressed của V4 Pro. Nó được thiết kế độc lập — MoE config riêng, interleaving ratio riêng, expert routing parameters riêng."

### 2. CSA + HCA: Hybrid Attention — Innovation Cốt Lõi

Đây là điểm khác biệt lớn nhất về kiến trúc.

**Compressed Sparse Attention (CSA)**
- Nén local context ~4× trước khi compute attention
- Không giống sliding window attention (bỏ qua token) — CSA **nén token**
- Complexity: thay vì O(n·w), CSA giảm effective dimensionality của compressed context
- Kết hợp với **FP4 Lightning Indexer**: scoring + top-k block selection

**Heavily Compressed Attention (HCA)**
- Nén ~128× dọc theo sequence dimension
- Sau khi nén, sequence đủ ngắn → dense attention trở lại (bỏ sparse selection)
- Xử lý global attention trên 1M token mà không cần quadratic attention

**Interleaving Pattern (tỷ lệ luân phiên)**
- V4 Pro: ~3:1 CSA-to-HCA (HCA tập trung ở 2/3 cuối network)
- V4 Flash: ~4:1 CSA-to-HCA (ít HCA hơn → latency thấp hơn)

> "CSA + HCA không chỉ giảm cache size — nó thay đổi những gì model tính toán. Đây là genuine structural differentiator, không phải quantization shortcut."

**So sánh với GQA (Grouped Query Attention) của Claude/OpenAI:**
- GQA tối ưu trong fixed computational graph — giảm memory cost nhưng vẫn O(n²)
- CSA + HCA **thay đổi computation**: CSA thay thế full local attention, HCA thay thế full-sequence global attention

**Kết quả:** Ở 1M token context, V4 Pro chỉ dùng ~27% FLOPs và ~10% KV cache so với V3.2.

### 3. MoE: Mixture-of-Experts

**Routing Innovations**
- V3 đã có auxiliary-loss-free load balancing
- V4 thêm **adaptive routing temperature** — tự động điều chỉnh độ sharpness của routing distribution dựa trên token-level uncertainty
- **Shared experts** — một pool nhỏ nhận routing probability mass từ mọi token (đảm bảo universal language capability không bị mất khi specialized experts phân hóa)

**Manifold-Constrained Hyper-Connections (MCHC)**
Đây là thành phần ít được thảo luận nhất nhưng cực kỳ quan trọng.

- **Standard residual connections:** mỗi sublayer output cộng vào residual stream với uniform weight
- **MCHC:** parameterize connectivity giữa các sublayer → model học input-dependent weighting
- **Manifold constraint:** ép các learned connectivity weights vào lower-dimensional manifold → ngăn expert connectivity patterns drift vào vùng không ổn định

> "Hệ quả: models với MCHC có output variance thấp hơn trên các input tương tự — tức behavior production predictable hơn. Trong agentic deployments với hàng chục model calls cho một task, variance accumulation là meaningful quality degradation mechanism."

### 4. Lightning Indexer + Compressed KV Blocks

**Vấn đề:** KV cache ở 1M tokens = hàng trăm GB mỗi request.

**Giải pháp của V4 — ba lớp:**
1. **CSA compression** ~4× dọc sequence dimension
2. **HCA compression** ~128×
3. **FP4 Lightning Indexer** — scoring network chạy ở FP4, chọn top-k compressed blocks cho sparse attention

**Economic profile:**
- Capital cost cao (multi-node GPU) nhưng per-token compute cost thấp
- Lý tưởng cho high-throughput, long-session workloads
- KHÔNG lý tưởng cho low-throughput workloads ngắn (không amortize được fixed cost)

**KV Cache trong Multi-Agent Deployments**

> "Đây là lợi thế mà hầu như không phân tích nào đề cập."

- **Naive full KV caching:** Mỗi agent trong multi-agent architecture giữ KV cache riêng → memory footprint × số agent
- **V4:** shared compressed KV giữa các agents — multiple agents access cùng document có thể share compressed block representation + Lightning Indexer scoring infrastructure. Memory footprint scale với compressed block pool size + per-agent indexer state — không scale với document length × agent count.

> "Với 10-agent architecture xử lý 1M-token document, đây là khác biệt giữa feasible memory budget và infeasible."

### 5. Benchmark Results

| Benchmark | V4 Pro | Claude Opus | OpenAI | V4 Flash |
|-----------|--------|-------------|--------|----------|
| MATH-500 | ~96.2 | ~94 | ~95 | ~87 |
| MMLU-Pro | ~87 | ~89 | ~88 | ~77 |
| HumanEval | ~92 | ~91 | ~93 | ~83 |
| RULER (128K) | ~95 | ~87 | ~90 | ~88 |
| Long-ROPE (1M) | ~89 | N/A (200K max) | N/A | ~79 |

**Điểm mạnh nhất của V4 Pro:**
- Long-context benchmarks — gap với V3 tăng theo context length
- Ở 1M tokens, V4 Pro không có đối thủ closed-source (Claude Opus max 200K)
- **Auditability:** có thể kiểm tra tại sao performance degrade giữ ở context length cụ thể

### 6. Practitioner Guidance

**Khi nào chọn V4 Pro?**
- Workload >200K tokens (documents, codebases, legal corpora, long-horizon agentic sessions)
- Yêu cầu: tối thiểu 3 H200 nodes (BF16) hoặc 2 nodes (FP8)
- Expert parallelism yêu cầu NVLink fabric
- Break-even: >500M tokens/tháng → open-weights rẻ hơn API

**Khi nào chọn V4 Flash?**
- GPU memory là binding constraint
- Tail latency SLAs khắt khe
- Single/dual-node deployments (vừa 8-GPU H200 node với FP8/FP4)
- Workload 32K-200K token (extraction, summarization — không multi-hop reasoning)

**Data Sovereignty**

> "Claude Opus và OpenAI xử lý data trên infrastructure của họ. V4 deployed trên infrastructure của bạn — mọi token ở lại trong security perimeter của bạn. Trong regulated industries, open-weights có thể là con đường compliance duy nhất."

**Fine-tuning Lưu ý**
- MCHC manifold constraints có implications cho PEFT
- Standard LoRA có thể không tôn trọng manifold geometry → giảm inference consistency
- Dùng MCHC-aware fine-tuning guidelines từ DeepSeek

## Kết luận

> "Câu hỏi 'open-weights có đạt frontier quality không' đã được giải quyết. V4 Pro's benchmark parity với Claude Opus xác nhận điều đó."

Khoảng cách practitioner trong coverage hiện tại không phải thiếu dữ liệu — technical report của DeepSeek công bố nhiều architectural detail hơn bất kỳ model frontier nào. Khoảng cách là analytical: hầu như không phân tích nào kết nối CSA/HCA interleaving ratios với serving latency profiles, Lightning Indexer với multi-agent KV cache dynamics, hay MCHC với fine-tuning stability.

> "Những kết nối này quyết định liệu quyết định chọn architecture ở cấp độ model có tạo ra production infrastructure hoạt động như kỳ vọng — hay cần re-engineering tốn kém 6 tháng sau deployment."

---

*Source: Boring Bot (Substack)*
