---
type: raw
source_type: paper
source_url: https://arxiv.org/abs/2505.0xxxxx
date_ingested: 2026-05-27
tags: [ai, agents, research]
status: unprocessed
---

# Research Report: Language Models Need Sleep

**Authors:** Sangyun Lee (CMU), Sean McLeish (UMD), Tom Goldstein (UMD), Giulia Fanti (CMU)  
**Source:** Research Report / arXiv  
**Ingested:** 2026-05-27

---

## Original Content

### 1. Authors and Institution(s)

* Sangyun Lee: Carnegie Mellon University
* Sean McLeish: University of Maryland
* Tom Goldstein: University of Maryland
* Giulia Fanti: Carnegie Mellon University

### 2. How This Work Fits into the Broader Research Landscape

The development of large language models (LLMs) has largely been driven by the Transformer architecture, which relies on a self-attention mechanism to process context. While effective, the attention mechanism scales quadratically with context length, leading to significant computational and memory costs, particularly for long-horizon tasks. This issue manifests as a linearly growing key-value (KV) cache.

Recent advancements have introduced efficient sequence models, such as State-Space Models (SSMs), which utilize fixed-size fast weight memories. These models aim to mitigate the scaling problems of attention by providing a more memory-efficient alternative. Hybrid architectures, combining attention for high-fidelity access to recent tokens and fast-weight memory for compressed information beyond the active context window, have become common in large-scale models.

However, the authors identify a distinction between scalable memory and scalable reasoning. Prior research has shown that while fast-weight memories can support long-range recall, it is not clear if they can support deep computation over tokens once they are no longer in the KV cache. The paper observes that existing SSM-attention hybrid models exhibit degraded performance as the required reasoning depth increases, even when the amount of information to store remains constant. This suggests that the bottleneck is not merely memory capacity but the computational capacity available to transform evicted context into a usable internal state.

This work draws inspiration from biological memory consolidation processes, particularly the role of hippocampal replay during sleep in transferring short-term memories into long-term cortical synaptic weights. In machine learning, related approaches include context compression (condensing long contexts into shorter representations), context distillation (training models to distill context into weights), and test-time training (performing gradient updates on parameters during inference). Additionally, depth-recurrent or looped neural networks have been explored to increase model expressivity and solve sequential reasoning tasks by scaling computation at prediction time.

The novel contribution of this paper is the application of recurrence to the *memory consolidation* phase, rather than solely to the prediction phase. It proposes an "LLM sleep" mechanism where iterative, learned updates to fast weights occur offline, allowing deep computation over evicted context without increasing the latency of wake-time prediction. This distinguishes it from prior work that typically focuses on single-pass updates or recurrent passes during inference.

### 3. Key Objectives and Motivation

The primary objective of this research is to enhance the deep reasoning capabilities of large language models over long contexts, particularly when information has been evicted from the active attention window, without increasing the computational latency during the model's prediction phase.

The motivation stems from several observations:

1. **Limitations of Current LLM Architectures for Long Contexts:** Transformer-based LLMs, despite their effectiveness, incur quadratic computational costs with increasing context length due to the attention mechanism and linear memory growth for the KV cache. This makes them inefficient for tasks requiring very long contexts.
2. **Incompleteness of Existing Memory Solutions:** While hybrid models that combine attention with State-Space Models (SSMs) offer improved memory scalability by using fixed-size fast weight memories, the authors found these models still struggle with tasks demanding deep reasoning over information that has been evicted from the active context. This suggests that simply storing or recalling information is insufficient if the model cannot adequately process and transform that information into a useful, consolidated internal state for future complex queries.
3. **The "Computation for Consolidation" Bottleneck:** The authors' experiments indicate that even with sufficient memory capacity, the performance of hybrid models degrades as the required reasoning depth increases. This points to a bottleneck in the *amount of computation* available for organizing and processing evicted context into a representation that supports deep reasoning. This transformation itself is considered a non-trivial computational task.
4. **Biological Inspiration for Memory Consolidation:** The concept of "sleep" in LLMs is directly inspired by biological processes, specifically how animals consolidate short-term hippocampal memories into long-term cortical synaptic weights during sleep through hippocampal replay. This offline process allows for deep memory organization without interfering with an animal's ability to respond to external stimuli during wakefulness. The authors analogize this to an LLM performing intensive memory updates without receiving new input tokens, justifying the computational cost by the long-term cognitive benefits.
5. **Leveraging Recurrence for Weight Updates:** Drawing from prior work on depth-recurrent neural networks, which can outperform fixed-depth models on sequential reasoning, the authors propose that recurrence can be applied not just for prediction but also for memory consolidation. Similar to how iterative algorithms like gradient descent improve through multiple updates, applying multiple recurrent passes during fast weight formation could provide the model with more steps to transform transient context into robust representations, suitable for later single-pass inference.

In essence, the research aims to introduce a mechanism that explicitly allocates dedicated, iterative computation for consolidating context into fast weights during an "offline" phase, thereby enabling deeper reasoning capabilities without compromising the speed of "wake-time" predictions.

### 4. Methodology and Approach

The core of the proposed methodology is the "LLM Sleep" mechanism, which is integrated into existing SSM-attention hybrid large language models. This mechanism introduces an offline recurrent phase for memory consolidation.

**Architecture and Mechanism:**
The method is built upon hybrid sequence models that interleave attention blocks ($B_{attn}$) with State-Space Model (SSM) blocks ($B_{ssm}$). SSM blocks maintain a fixed-size fast-weight state ($S_t$), enabling more memory-efficient context storage compared to the quadratically scaling KV cache of attention. The paper specifically mentions using Gated Delta Networks (GDNs) for SSMs, which incorporate a delta-rule correction for weight updates.

The LLM Sleep process involves the following stages:

1. **Consolidation Phase (Sleep):**
 * This phase is triggered when the model's context window becomes full, or at a predefined eviction boundary (e.g., every $L$ tokens).
 * Before the attention KV cache is cleared, the model performs $N$ recurrent forward passes over the accumulated context within the current window.
 * During these passes, the fast weights ($S$) within the SSM blocks are iteratively updated. The update rule used (e.g., the Hebbian-like outer-product rule from Mamba2-style SSMs: $S_t = \alpha_t S_{t-1} + \beta_t v_t k_t^\top$) allows for selective writing, overwriting, and forgetting of information.
 * No external input tokens are processed during this phase, similar to biological sleep. The computation is solely focused on refining the internal fast-weight memory based on the current context.
 * The recurrence is applied over a stack of blocks. For example, if looping over all D blocks, the architecture would look like: `Embed → [B_attn_0 → B_ssm_1 → · · · → B_attn_{D-1}] ×N → OutProj`.
 * After $N$ passes, the refined fast weights are retained. The feature vectors (h) resulting from these recurrent passes are discarded, and only the updated fast weights ($S$) persist.

2. **Context Eviction:**
 * Following the consolidation phase, the attention KV cache is cleared. This hard eviction strategy forces the model to rely on its consolidated fast weights for information from previously processed contexts.

3. **Prediction Phase (Wake):**
 * The model resumes processing new input tokens.
 * For each answer token, prediction is made using a *single standard forward pass*. This maintains low prediction-time latency, as all the intensive computation for memory consolidation has been shifted to the offline "sleep" phase.

**Training Procedure:**
The model is trained end-to-end to minimize prediction error. Backpropagation occurs through the entire computational graph, encompassing both the recurrent consolidation phase and the single-pass prediction phase. The gradient flow is crucial, as it propagates through the recursively refined fast weights ($S$). The training procedure involves iterating through token chunks: for consolidation chunks, $N$ recurrent passes update $h$ and $S$; for prediction chunks, one pass computes the loss using masked cross-entropy.

**Evaluation Tasks:**
To assess the efficacy of LLM sleep, the authors conducted experiments on a range of tasks designed to stress-test reasoning capabilities:

1. **Controlled Synthetic Tasks:**
 * **Rule 110 Cellular Automaton:** A 1D binary cellular automaton where the model must predict the first bit of a state after $t$ transitions. The parameter $t$ directly controls the required reasoning depth. Hard eviction (L=24) ensures the model encodes each state into fast weights before its context is cleared.
 * **Depo (Multi-hop Knowledge Retrieval):** A task requiring the model to answer $k$-hop queries on a shuffled directed cycle graph. The parameter $k$ determines the reasoning depth. Each cycle is fragmented across multiple cache windows (L=75), demanding robust context compression and multi-hop retrieval from fast weights.

2. **Realistic Math Reasoning Task:**
 * **GSM-Infinite:** A procedurally generated math reasoning benchmark similar to GSM8K. It controls problem length via distractors and reasoning difficulty by varying the number of arithmetic operations ($op$). The question is placed before the context, and Chain-of-Thought traces are excluded, forcing direct reasoning. The context window size (L=2000) is smaller than problem length (2000-3300 tokens), necessitating consolidation of context.

**Model Implementations and Training Details:**
* Experiments utilized a 4-layer GDN-attention hybrid model for synthetic tasks, and pre-trained LLMs for GSM-Infinite: Jet-Nemotron 2B (an SSM-attention hybrid) and Ouro 1.4B (a depth-recurrent attention-only model augmented with Jet layers for fast-weight memory).
* The Muon optimizer was used with AdamW, and the Muon learning rate was tuned on the $N=1$ baseline and then applied to looped models.
* Batch sizes were adjusted per task, and random seeds were fixed for consistent comparisons.
* **Eviction Strategies:** Both *hard eviction* (KV cache completely cleared) and *sliding-window eviction* (most recent L-1 tokens retained) were tested. For sliding-window eviction, an SSM-only warm-up stage was employed.
* **Training Throughput Analysis:** Examined the impact of recurrence on throughput, noting that while training becomes sequential across context windows, it can be efficient when window size is large, though recurrent depth linearly increases cost.

### 5. Main Findings and Results

The experiments consistently demonstrated that increasing the duration of the "sleep" phase (by increasing the number of recurrent passes, $N$) improved the models' ability to perform deep reasoning over evicted context, across various tasks and model architectures.

1. **Baseline Performance Degradation (Cellular Automaton):**
 * On the Rule 110 cellular automaton task, a vanilla 4-layer GDN-attention hybrid model (with $N=1$, i.e., "no loop") showed a rapid decline in accuracy as the rollout step $t$ (reasoning depth) increased. For $t=32$, this baseline model remained close to random guessing (approximately 10% accuracy) even after 5 billion training tokens. This finding supported the hypothesis that fixed-depth models struggle with deep sequential computation required for memory consolidation.

2. **Improved Performance on Cellular Automaton with LLM Sleep:**
 * When the LLM sleep mechanism was introduced for $t=32$, increasing $N$ directly correlated with improved performance. "2 loops" achieved around 20% accuracy, while "3 loops" and "4 loops" surpassed 30% accuracy within the same training token budget. This indicated that additional consolidation-time computation enabled the model to better encode and process complex state evolutions.

3. **Enhanced Multi-hop Reasoning on Depo Task:**
 * On the Depo multi-hop knowledge retrieval task, increasing $N$ accelerated learning, particularly for queries requiring more hops ($k=4, 8, 16$).
 * The 1-loop model made minimal progress on 4-hop and more challenging queries. The 2-loop model showed similar limitations for 8-hop and beyond.
 * Only the 4-loop model began to show improvements on the most difficult 16-hop task within the training budget. These results suggested that more sleep-time computation was crucial for organizing fragmented graph information into a representation capable of supporting deeper multi-hop traversal.

4. **Benefits for Realistic Math Reasoning on GSM-Infinite (Pre-trained LLMs):**
 * **Jet-Nemotron 2B:** For problems requiring more arithmetic operations ($op$), which demand deeper reasoning, increasing $N$ led to noticeable accuracy gains. For 6-operation problems, 6 loops improved accuracy from 0.742 to 0.812. For 8-operation problems, it improved from 0.351 to 0.388.
 * **Ouro 1.4B (augmented with Jet layers):** The improvements were even more pronounced for Ouro. For 6-operation problems, 4 loops increased accuracy from 0.419 to 0.615 (a 47% relative improvement). For 8-operation problems, 4 loops improved accuracy from 0.210 to 0.272 (a 30% relative improvement). The authors suggested that Ouro's pre-training as a depth-recurrent model might contribute to these larger gaps.
 * These findings indicated that sleep-time computation can effectively support multi-step reasoning in a realistic math context, even when applied to pre-trained LLMs.

5. **Effectiveness with Sliding-Window Eviction:**
 * When evaluating GSM-Infinite with a sliding-window eviction strategy (L=512) and fine-tuning Ouro 1.4B, increasing $N$ continued to improve accuracy across all operation counts.
 * The 1-loop baseline performed poorly on two-operation problems (0.596 accuracy). However, with 4 loops, accuracy significantly improved to 0.905 (a 52% relative improvement). Similar gains were observed for 4, 6, and 8-operation problems.
 * This demonstrated that longer sleep duration helps not only with multi-step reasoning but also with compressing and retrieving relevant context when the active attention window is considerably smaller than the sequence length. A warm-up phase with hard eviction for SSM layers was found to be important for models to learn fast-weight refinement.

6. **Training Throughput Analysis:**
 * The study showed that while training with LLM sleep is recurrent across context windows, this serial dependency does not necessarily hinder wall-clock training time if the window size $L$ is large enough to keep the GPU saturated.
 * The training cost was found to scale approximately linearly with $N$, reflecting the additional computational passes.

Overall, the results consistently supported the central claim that an offline, sleep-like recurrence mechanism can effectively organize evicted context into fast weights, enabling models to perform deeper reasoning without increasing prediction-phase latency. The largest gains were observed on problem instances requiring the most extensive reasoning.

### 6. Significance and Potential Impact

This research presents a significant contribution to the field of large language models by addressing a critical limitation: the ability to perform deep reasoning over long contexts, especially when contextual information has moved beyond the active attention window. The proposed "LLM Sleep" mechanism offers a principled approach to overcoming this challenge.

**Key Significance:**

1. **Enhanced Reasoning Capabilities for Long Contexts:** The work demonstrates that models can improve their capacity for deep sequential computation and multi-step reasoning by iteratively consolidating information into fixed-size fast weights during an offline "sleep" phase. This is particularly relevant for tasks requiring complex inferences over extended inputs where the full context cannot always reside in the attention cache.
2. **Preservation of Prediction Latency:** A notable advantage of this approach is that the computationally intensive consolidation process is shifted to an offline phase. This ensures that during "wake-time" inference, predictions can still be made with a single forward pass, maintaining low latency—a crucial factor for real-world applications of LLMs.
3. **Distinguishing Memory Capacity from Reasoning Capacity:** The research highlights a conceptual distinction between simply having the memory capacity to store information (e.g., in fast weights) and possessing the computational capacity to *transform* that information into a useful, consolidated state that supports complex reasoning. This reframes a key challenge in LLM development, suggesting that computational allocation for memory processing is as important as memory size.
4. **Biologically Inspired Paradigm:** The inspiration drawn from biological memory consolidation during sleep introduces a novel and potentially fruitful paradigm for designing and training LLMs. This cross-disciplinary approach may open new avenues for research into more sophisticated and biologically plausible memory systems in artificial intelligence.
5. **Applicability to Hybrid Architectures:** The method is shown to be effective when integrated with existing SSM-attention hybrid models and even adapted to depth-recurrent architectures, suggesting its broad applicability across the evolving landscape of efficient LLM designs. Its success on both synthetic and a more realistic math reasoning benchmark (GSM-Infinite) indicates its potential for practical relevance.
6. **Insights into Scaling Laws:** The analysis of training throughput, while indicating a linear increase in cost with recurrent depth, also suggests that the serial nature of processing across context windows may not be a prohibitive bottleneck when window sizes are sufficiently large. This provides practical considerations for scaling and deployment.

**Potential Impact:**

* **More Capable LLMs for Complex Tasks:** This research could lead to LLMs that are more proficient at tasks requiring deep understanding and multi-step reasoning over long documents, codebases, or complex conversational histories, without sacrificing inference speed. This has implications for scientific discovery, advanced problem-solving, and enhanced human-AI collaboration.
* **Foundation for Future Memory Systems:** The "LLM Sleep" mechanism could serve as a foundational component for developing more dynamic and adaptive memory management systems in AI, where models can strategically allocate computational resources to consolidate and organize knowledge over time.
* **Reduced Inference Costs for Deep Reasoning:** By front-loading the computational burden of memory consolidation, the method could enable the deployment of LLMs with deep reasoning capabilities in latency-sensitive applications where a single forward pass is required.

**Limitations and Future Work:**
The authors acknowledge limitations, primarily concerning the training cost and stability associated with deeper recurrent passes. These are active research areas in depth-recurrent models, with potential solutions including implicit gradients and truncated backpropagation through time. While the study is primarily methodological and evaluated on modest-scale pretrained models, its findings lay groundwork for further investigation into larger models and broader real-world applications. The core idea supports the "serial scaling hypothesis," suggesting that tasks inherently sequential in nature might benefit from sequential computation, offering a counterpoint to purely parallel approaches.
