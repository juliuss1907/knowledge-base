# Output Validator — Examples

Sample validation reports and common quality issues with fixes.

---

## Overview

This document provides real-world examples of Output Validator reports and demonstrates how to fix common content quality issues across the 4 validation dimensions.

---

## Example 1: Complete Validation Report

### Sample report structure

```markdown
# Output Validation — 2026-05-09

**Status:** pending
**Issues found:** 8 (3 ERROR, 4 WARNING, 1 INFO)
**Created:** 2026-05-09 22:00:15
**Validator:** output-validator

**Files checked:** 127 (12 new, 115 existing)

---

## Issue 1: Definition too short

**File:** wiki/concepts/rag-system.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** Definition too short (1 sentence, need 2-3)
**Evidence:**
```
RAG is a technique for improving LLM responses.
```
**Suggested fix:** Expand definition to 2-3 sentences

---

## Issue 2: Claim without source citation

**File:** wiki/concepts/rag-system.md
**Severity:** WARNING
**Dimension:** Factual
**Issue:** Claim without source citation
**Evidence:**
```
RAG improves accuracy by 40% in knowledge-intensive tasks.
```
**Suggested fix:** Add source citation: (Source: [[src_name]])

---

## Issue 3: Technical term used incorrectly

**File:** wiki/concepts/embedding-search.md
**Severity:** ERROR
**Dimension:** Factual
**Issue:** Technical term "embedding" used incorrectly
**Evidence:**
```
We use embeddings to fine-tune the model for better performance.
```
**Suggested fix:** Review definition of "embedding" and correct usage. Embeddings are for semantic search, not fine-tuning.

---

## Issue 4: Too few key ideas

**File:** wiki/concepts/prompt-engineering.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Too few key ideas (3, need 5-10)
**Evidence:**
```
- Clear instructions improve results
- Examples help the model understand
- Iteration is important
```
**Suggested fix:** Add more key ideas (target 5-10)

---

## Issue 5: Internal contradiction

**File:** wiki/concepts/context-window.md
**Severity:** ERROR
**Dimension:** Coherence
**Issue:** Internal contradiction detected
**Evidence:**
```
Claim 1: Claude has a 200K token context window.
Claim 2: The maximum context is 100K tokens for Claude.
```
**Suggested fix:** Resolve contradiction or clarify context (different Claude versions?)

---

## Issue 6: Machine translation artifact

**File:** wiki/sources/src_anthropic-rag.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Possible machine translation artifact
**Evidence:**
```
Mô hình ngôn ngữ lớn là một loại của trí tuệ nhân tạo
```
**Suggested fix:** Rephrase more naturally: "Mô hình ngôn ngữ lớn là một dạng trí tuệ nhân tạo"

---

## Issue 7: Technical term translated

**File:** wiki/sources/src_openai-embeddings.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Technical term translated: "nhúng" should be "embedding"
**Evidence:**
```
Kỹ thuật nhúng giúp tìm kiếm ngữ nghĩa
```
**Suggested fix:** Use English term "embedding" instead

---

## Issue 8: Summary could be more concise

**File:** wiki/sources/src_llm-security.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Summary too long (6 sentences, prefer 3-5)
**Evidence:**
```
Bài viết này thảo luận về các vấn đề bảo mật trong LLM. Tác giả đề cập đến prompt injection...
```
**Suggested fix:** Condense summary to 3-5 sentences
```

---

## Example 2: Factual Accuracy Issues

### Issue 2.1: Missing source citation

**Before (ERROR):**
```markdown
## Key ideas

- RAG improves accuracy by 40% in knowledge-intensive tasks
- Vector databases enable fast semantic search
- Embedding models convert text to numerical representations
```

**After (FIXED):**
```markdown
## Key ideas

- RAG improves accuracy by 40% in knowledge-intensive tasks (Source: [[src_anthropic-rag-study]])
- Vector databases enable fast semantic search
- Embedding models convert text to numerical representations
```

---

### Issue 2.2: Technical term misuse

**Before (ERROR):**
```markdown
## Definition

Embedding is a technique for fine-tuning language models to improve their performance on specific tasks.
```

**After (FIXED):**
```markdown
## Definition

Embedding is a technique for converting text into dense vector representations that capture semantic meaning. These vectors enable semantic search and similarity comparison.
```

---

### Issue 2.3: Contradiction with source

**Before (ERROR):**

**Concept file says:**
```markdown
Claude Code can autonomously refactor legacy codebases without human supervision.
```

**Source file says:**
```markdown
Claude Code works best with clear specifications. Complex refactoring requires human oversight and iterative review.
```

**After (FIXED):**
```markdown
Claude Code can implement refactoring tasks when given clear specifications, but complex legacy refactoring requires human oversight and iterative review (Source: [[src_anthropic-claude-code]]).
```

---

### Issue 2.4: Unreasonable number

**Before (WARNING):**
```markdown
RAG systems can improve accuracy by 500% compared to baseline LLMs.
```

**After (FIXED):**
```markdown
RAG systems can improve accuracy by 40-60% compared to baseline LLMs in knowledge-intensive tasks (Source: [[src_rag-benchmark-2026]]).
```

---

## Example 3: Completeness Issues

### Issue 3.1: Definition too short

**Before (ERROR):**
```markdown
## Definition

RAG is a technique for improving LLM responses.
```

**After (FIXED):**
```markdown
## Definition

RAG (Retrieval-Augmented Generation) is a technique that enhances LLM responses by retrieving relevant documents before generation. The retrieved context provides factual grounding and reduces hallucinations.
```

---

### Issue 3.2: Too few key ideas

**Before (WARNING):**
```markdown
## Key ideas

- RAG improves accuracy
- Uses vector search
- Reduces hallucinations
```

**After (FIXED):**
```markdown
## Key ideas

- RAG improves accuracy by providing factual context from retrieved documents
- Uses vector search to find semantically similar content
- Reduces hallucinations by grounding responses in real data
- Requires high-quality document corpus for best results
- Embedding quality directly impacts retrieval accuracy
- Can be combined with fine-tuning for domain-specific tasks
- Trade-off between retrieval speed and accuracy
```

---

### Issue 3.3: Summary too short

**Before (WARNING):**
```markdown
## Summary

Bài viết giới thiệu RAG. RAG cải thiện độ chính xác của LLM.
```

**After (FIXED):**
```markdown
## Summary

Bài viết giới thiệu RAG (Retrieval-Augmented Generation), kỹ thuật cải thiện độ chính xác của LLM bằng cách truy xuất tài liệu liên quan trước khi sinh câu trả lời. Tác giả phân tích workflow của RAG: embedding documents, vector search, và context injection. Kết quả thử nghiệm cho thấy RAG cải thiện accuracy 40-60% trên các task knowledge-intensive so với baseline LLM.
```

---

### Issue 3.4: Placeholder content

**Before (ERROR):**
```markdown
## Key ideas

- [To be filled]
- [TBD]
```

**After (FIXED):**
```markdown
## Key ideas

- Claude Code enables AI-assisted development workflows
- Developer focuses on system design, Claude implements features
- Requires clear specifications for accurate implementation
- Best for greenfield projects and well-defined tasks
- Iterative review process ensures quality
```

---

## Example 4: Coherence Issues

### Issue 4.1: Circular definition

**Before (ERROR):**
```markdown
## Definition

Claude Code is a code tool that helps developers write code more efficiently using code assistance.
```

**After (FIXED):**
```markdown
## Definition

Claude Code is an AI-assisted development workflow where Claude autonomously implements features given high-level specifications. The developer focuses on system design and decision-making rather than writing code.
```

---

### Issue 4.2: Internal contradiction

**Before (ERROR):**
```markdown
## Definition

RAG always improves LLM accuracy by retrieving relevant context.

## Key ideas

- RAG may reduce accuracy if retrieved documents are irrelevant or outdated
- Document quality is critical for RAG effectiveness
```

**After (FIXED):**
```markdown
## Definition

RAG improves LLM accuracy by retrieving relevant context before generation. Effectiveness depends on document quality and retrieval accuracy.

## Key ideas

- RAG improves accuracy when retrieved documents are relevant and high-quality
- Irrelevant or outdated documents can reduce accuracy
- Document quality is critical for RAG effectiveness
```

---

### Issue 4.3: Unsupported claim

**Before (ERROR):**
```markdown
## Key ideas

- RAG is the best approach for all AI applications
- Every company should implement RAG immediately
```

**After (FIXED):**
```markdown
## Key ideas

- RAG is effective for knowledge-intensive tasks requiring factual accuracy (Source: [[src_rag-study]])
- Best suited for applications with large document corpora
- May not be necessary for creative or generative tasks
- Implementation requires infrastructure for vector search and embedding
```

---

### Issue 4.4: Weak logical flow

**Before (WARNING):**
```markdown
## Definition

Embedding converts text to vectors.

## Key ideas

- Vector databases store embeddings
- Semantic search uses cosine similarity
- RAG retrieves documents
```

**After (FIXED):**
```markdown
## Definition

Embedding converts text into dense vector representations that capture semantic meaning. These vectors enable semantic search and similarity comparison.

## Key ideas

- Embedding models (e.g., text-embedding-3) convert text to high-dimensional vectors
- Vector databases (e.g., Pinecone, Weaviate) store and index embeddings efficiently
- Semantic search uses cosine similarity to find related content
- RAG systems use embeddings to retrieve relevant documents before generation
- Embedding quality directly impacts downstream task performance
```

---

## Example 5: Vietnamese Quality Issues

### Issue 5.1: Grammar error (tense)

**Before (ERROR):**
```markdown
Năm 2025, Claude Code sẽ ra mắt với nhiều tính năng mới.
```

**After (FIXED):**
```markdown
Năm 2025, Claude Code đã ra mắt với nhiều tính năng mới.
```

---

### Issue 5.2: Machine translation artifact

**Before (ERROR):**
```markdown
Mô hình ngôn ngữ lớn là một loại của trí tuệ nhân tạo được được sử dụng rộng rãi.
```

**After (FIXED):**
```markdown
Mô hình ngôn ngữ lớn là một dạng trí tuệ nhân tạo được sử dụng rộng rãi.
```

---

### Issue 5.3: Technical term translated

**Before (WARNING):**
```markdown
Kỹ thuật nhúng giúp chuyển đổi văn bản thành vector để tìm kiếm ngữ nghĩa.
```

**After (FIXED):**
```markdown
Kỹ thuật embedding giúp chuyển đổi văn bản thành vector để tìm kiếm ngữ nghĩa.
```

---

### Issue 5.4: Awkward phrasing

**Before (WARNING):**
```markdown
RAG là một kỹ thuật mà nó cải thiện độ chính xác của LLM bằng cách mà truy xuất tài liệu.
```

**After (FIXED):**
```markdown
RAG là kỹ thuật cải thiện độ chính xác của LLM bằng cách truy xuất tài liệu liên quan.
```

---

## Example 6: Multi-Dimension Issues

### Complex case: Multiple issues in one file

**Before (3 ERROR, 2 WARNING):**

```markdown
---
type: concept
status: draft
main_tag: ai
sub_tags: [tools]
topic: rag
sources:
  - [[wiki/sources/src_rag-intro]]
last_updated: 2026-05-09
---

# RAG

## Definition

RAG is a technique.

## Key ideas

- Improves accuracy
- Uses vectors
- [TBD]

## Related concepts

- [[embedding]]
- [[llm]]

## Sources

- [[wiki/sources/src_rag-intro]]
```

**Issues found:**
1. ERROR (Completeness): Definition too short (1 sentence, need 2-3)
2. ERROR (Completeness): Placeholder content in key ideas
3. WARNING (Completeness): Too few key ideas (2 real items, need 5-10)
4. WARNING (Factual): Vague claim "Improves accuracy" without source
5. WARNING (Coherence): Definition too vague to be useful

---

**After (FIXED):**

```markdown
---
type: concept
status: reviewed
main_tag: ai
sub_tags: [tools, research]
topic: rag-system
sources:
  - [[wiki/sources/src_rag-intro]]
  - [[wiki/sources/src_anthropic-rag-study]]
last_updated: 2026-05-09
---

# RAG (Retrieval-Augmented Generation)

## Definition

RAG (Retrieval-Augmented Generation) is a technique that enhances LLM responses by retrieving relevant documents before generation. The retrieved context provides factual grounding and reduces hallucinations.

## Key ideas

- RAG improves accuracy by 40-60% in knowledge-intensive tasks (Source: [[src_anthropic-rag-study]])
- Uses vector embeddings to find semantically similar documents
- Reduces hallucinations by grounding responses in real data
- Requires high-quality document corpus for best results
- Embedding quality directly impacts retrieval accuracy
- Can be combined with fine-tuning for domain-specific tasks
- Trade-off between retrieval speed and accuracy

## Related concepts

- [[embedding]]
- [[vector-database]]
- [[semantic-search]]
- [[llm]]

## Sources

- [[wiki/sources/src_rag-intro]]
- [[wiki/sources/src_anthropic-rag-study]]
```

---

## Example 7: Edge Cases

### Case 7.1: English content (skip Vietnamese check)

**File:** wiki/concepts/claude-code.md (English only)

**Validation:**
- ✅ Factual accuracy: checked
- ✅ Completeness: checked
- ✅ Coherence: checked
- ⏭️ Vietnamese quality: skipped (English content)

---

### Case 7.2: Mixed language content

**File:** wiki/sources/src_anthropic-claude.md (English + Vietnamese)

**Validation:**
- Check Vietnamese sections only for Vietnamese quality
- Technical terms in English sections: no translation check
- Technical terms in Vietnamese sections: check preservation

---

### Case 7.3: Concept with no sources yet

**File:** wiki/concepts/new-concept.md

**Issue:**
```markdown
sources: []
```

**Validation:**
- WARNING (Completeness): Sources array is empty
- Suggested fix: Add at least one source file

---

## Example 8: Systematic Issues

### Pattern: Multiple files with same issue

**Detected pattern:**
```
15 files have definitions <2 sentences
Likely cause: Compile Agent prompt needs tuning
```

**Report includes:**
```markdown
[SYSTEMATIC ISSUE]
Pattern: 15 concept files have definitions <2 sentences
Files affected: rag-system.md, embedding.md, vector-db.md, ...
Likely cause: Compile Agent prompt needs tuning
Recommendation: Review compile-agent/SKILL.md definition generation
```

---

## Example 9: Report Actions

### Julius approves report

**Telegram command:**
```
approve output
```

**Result:**
- Report status: pending → approved
- Entry moves to "Recently Applied" in _action-required.md
- Fix Agent can now apply fixes

---

### Julius rejects report

**Telegram command:**
```
reject output
```

**Result:**
- Report status: pending → rejected
- Entry removed from _action-required.md
- Report archived to wiki/reviews/archive/

---

### Julius requests details

**Telegram command:**
```
show output
```

**Result:**
- Full report sent to Telegram
- Or link to wiki/reviews/2026-05-09_output-report.md

---

## Related Documentation

- [SKILL.md](SKILL.md) — Output Validator overview
- [workflow.md](workflow.md) — Step-by-step validation process
- [validation-criteria.md](validation-criteria.md) — Detailed quality rubrics

---

**End of examples.md**
