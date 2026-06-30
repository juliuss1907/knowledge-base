---
type: source
original: "[[2026-05-27_lee-et-al_llm-need-sleep-consolidation]]"
main_tag: ai
sub_tags: [research, tools]
topic: llm-memory-consolidation
date_compiled: 2026-05-28
url: https://arxiv.org/abs/2505.0xxxxx
author: Sangyun Lee, Sean McLeish, Tom Goldstein, Giulia Fanti
---

# Language Models Need Sleep

## Metadata

- **Authors:** Sangyun Lee (CMU), Sean McLeish (UMD), Tom Goldstein (UMD), Giulia Fanti (CMU)
- **Institution:** Carnegie Mellon University, University of Maryland
- **Source:** arXiv / Research Report
- **Date compiled:** 2026-05-28
- **Original:** [[2026-05-27_llm-need-sleep-consolidation]]

## Summary

Research paper proposing "LLM Sleep" — a mechanism inspired by biological memory consolidation during sleep. The approach applies recurrence to the memory consolidation phase (not just prediction) in SSM-attention hybrid models. During "sleep," the model performs N recurrent forward passes over evicted context to iteratively update fast weights, enabling deep reasoning without increasing wake-time prediction latency. Experiments on Rule 110 Cellular Automaton, Depo multi-hop retrieval, and GSM-Infinite show that increasing sleep duration (more recurrent passes) significantly improves deep reasoning capabilities over long contexts.

## Key points

- **Problem:** Transformer attention scales quadratically with context length; SSM hybrids struggle with deep reasoning over evicted context despite having memory capacity
- **Insight:** Bottleneck is not memory capacity but computational capacity for transforming evicted context into usable internal state
- **Biological inspiration:** Hippocampal replay during sleep transfers short-term memories to long-term cortical synaptic weights offline
- **Mechanism:** N recurrent passes during consolidation phase update fast weights (S) before KV cache eviction; prediction uses single forward pass
- **Key result:** More sleep loops (N) → better deep reasoning; 4-loop model showed 30%+ accuracy on Rule 110 t=32 vs 10% baseline
- **GSM-Infinite results:** 4 loops improved Ouro 1.4B accuracy 47% relative (0.419→0.615) on 6-op problems
- **Trade-off:** Linear training cost increase with N, but prediction latency unchanged
- **Eviction strategies:** Hard eviction (full clear) and sliding-window tested; warm-up important for sliding-window

## Concepts referenced

- [[llm-sleep]]
- [[memory-consolidation-offline]]
- [[state-space-models-ssm]]
- [[fast-weights]]
- [[gated-delta-networks]]
- [[kv-cache-eviction]]
- [[hippocampal-replay]]

## Original excerpts

> "The novel contribution of this paper is the application of recurrence to the memory consolidation phase, rather than solely to the prediction phase."

> "The concept of 'sleep' in LLMs is directly inspired by biological processes, specifically how animals consolidate short-term hippocampal memories into long-term cortical synaptic weights during sleep through hippocampal replay."

> "For 6-operation problems, 6 loops improved accuracy from 0.742 to 0.812. For 8-operation problems, it improved from 0.351 to 0.388."
