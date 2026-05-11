# Output Validator — Validation Criteria

Detailed quality rubrics for the 4 validation dimensions: Factual Accuracy, Completeness, Coherence, and Vietnamese Quality.

---

## Overview

Each dimension has specific criteria with severity levels (ERROR/WARNING/INFO). This document serves as the ground truth for Output Validator's quality checks.

**Scope:** Content quality only. Structural format checks (frontmatter, sections, markdown syntax) are handled by Format Validator per `wiki/meta/format-spec.md`.

---

## Dimension 1: Factual Accuracy

### Definition

Content claims are verifiable, technically correct, and consistent with cited sources.

### Criteria

#### 1.1 Source Citations (Concepts only)

**ERROR:**
- Factual claim with no source cited
- Citation to non-existent source file
- Claim contradicts cited source

**WARNING:**
- Vague citation (e.g., "according to research" without specific source)
- Citation format incorrect (not using wikilink)

**INFO:**
- Could benefit from additional source citation
- Source citation could be more specific

**Examples:**

```markdown
❌ ERROR:
"RAG improves accuracy by 40%"
→ No source cited for specific statistic

✅ CORRECT:
"RAG improves accuracy by 40% (Source: [[src_rag-benchmark-2026]])"

⚠️ WARNING:
"According to studies, RAG improves accuracy"
→ Vague citation, which studies?

✅ CORRECT:
"According to [[src_anthropic-rag-study]], RAG improves accuracy"
```

#### 1.2 Technical Term Usage

**ERROR:**
- Technical term used with wrong meaning
- Term definition contradicts standard definition
- Mixing up similar terms (e.g., "embedding" vs "fine-tuning")

**WARNING:**
- Technical term used without definition on first mention
- Inconsistent terminology (switching between synonyms)

**INFO:**
- Could add clarification for complex term
- Could link to concept file for term

**Technical terms dictionary:**

| Term | Correct usage | Common mistakes |
|---|---|---|
| RAG | Retrieval-Augmented Generation | Not "Retrieval and Generation" |
| Embedding | Vector representation of text | Not "encoding" or "vectorization" |
| Fine-tuning | Training on specific dataset | Not "customization" or "optimization" |
| Prompt injection | Security attack via prompt | Not "prompt hacking" |
| Context window | Token limit for input | Not "memory limit" |
| LLM | Large Language Model | Not "AI model" (too generic) |
| Agent | Autonomous AI system | Not "bot" or "assistant" |

**Examples:**

```markdown
❌ ERROR:
"We use embeddings to fine-tune the model"
→ Embeddings are not used for fine-tuning

✅ CORRECT:
"We use embeddings for semantic search, then fine-tune the model on domain data"

⚠️ WARNING:
"The model uses RAG to retrieve information"
→ First mention without definition

✅ CORRECT:
"The model uses RAG (Retrieval-Augmented Generation) to retrieve information"
```

#### 1.3 Contradictions with Sources

**ERROR:**
- Concept file claims opposite of what source says
- Dates/numbers differ from source
- Key facts misrepresented

**WARNING:**
- Interpretation differs from source (but not contradictory)
- Emphasis differs from source

**INFO:**
- Could note nuance from source
- Could acknowledge alternative interpretation

**Check method:**
```python
# For concepts with multiple sources
for source in concept['sources']:
    source_content = read_file(source)
    
    # Use LLM to check contradiction
    prompt = f"""
    Does this concept contradict its source?
    
    Concept: {concept['body']}
    Source: {source_content}
    
    Output: "OK" or describe contradiction
    """
```

#### 1.4 Dates and Numbers

**ERROR:**
- Number with wrong unit (e.g., "10 GB RAM" when source says "10 MB")
- Statistic without source
- Impossible number (e.g., "150% of users")

**WARNING:**
- Number seems unreasonable (e.g., "1000% improvement")
- Date seems unlikely (e.g., future date for past event)

**INFO:**
- Could add date context (e.g., "as of 2026")
- Could specify number precision (e.g., "approximately 40%")

**Validation rules:**

```python
# Number validation
number_pattern = r'\b(\d+(?:\.\d+)?)\s*(%|GB|MB|KB|USD|VND)\b'

for match in re.finditer(number_pattern, text):
    value, unit = match.groups()
    
    # Check reasonable ranges
    if unit == '%' and float(value) > 100:
        → WARNING: Percentage over 100%
    
    if unit == 'GB' and float(value) > 1000:
        → WARNING: Unusually large GB value
```

---

## Dimension 2: Completeness

### Definition

All required content present with sufficient detail and appropriate length.

**Note:** Section structure (presence, order) is validated by Format Validator. This dimension checks content depth within those sections.

### Criteria

#### 2.1 Definition Length (Concepts only)

**ERROR:**
- Definition missing or empty
- Definition <1 sentence

**WARNING:**
- Definition 1 sentence (need 2-3)
- Definition >3 sentences (too long)

**INFO:**
- Definition exactly 2-3 sentences but could be clearer
- Definition could include more context

**Validation:**

```python
if file['type'] == 'concept':
    definition = extract_section(file, '## Definition')
    
    sentences = re.split(r'[.!?]+', definition.strip())
    sentence_count = len([s for s in sentences if s.strip()])
    
    if sentence_count == 0:
        → ERROR: Definition missing or empty
    
    if sentence_count < 2:
        → WARNING: Definition too short ({sentence_count} sentence, need 2-3)
    
    if sentence_count > 3:
        → INFO: Definition too long ({sentence_count} sentences, prefer 2-3)
```

#### 2.2 Summary Length (Sources only)

**ERROR:**
- Summary missing
- Summary <1 sentence

**WARNING:**
- Summary 1-2 sentences (need 3-5)
- Summary >5 sentences (too long)

**INFO:**
- Summary exactly 3-5 sentences but could be more concise
- Summary could include more key takeaways

**Validation:**

```python
if file['type'] == 'source':
    summary = extract_section(file, '## Summary')

    sentences = re.split(r'[.!?]+', summary.strip())
    sentence_count = len([s for s in sentences if s.strip()])

    if sentence_count == 0:
        → ERROR: Summary missing or empty

    if sentence_count < 3:
        → WARNING: Summary too short ({sentence_count} sentences, need 3-5)

    if sentence_count > 5:
        → INFO: Summary too long ({sentence_count} sentences, prefer 3-5)
```

#### 2.3 Key Points/Ideas Count

**ERROR:**
- Key points/ideas section empty
- No bullet points found

**WARNING:**
- <5 key points (need 5-10)
- >10 key points (too many)

**INFO:**
- Key points at boundary (exactly 5 or 10)
- Key points could be more specific

**Validation:**

```python
# For concepts: "## Key ideas"
# For sources: "## Key points"
section_name = 'Key ideas' if file['type'] == 'concept' else 'Key points'
key_content = extract_section(file, f'## {section_name}')

# Count bullet points
points = re.findall(r'^- ', key_content, re.MULTILINE)
point_count = len(points)

if point_count == 0:
    → ERROR: No key points/ideas found

if point_count < 5:
    → WARNING: Too few items ({point_count}, need 5-10)

if point_count > 10:
    → INFO: Too many items ({point_count}, prefer 5-10)
```

#### 2.4 Content Depth

**ERROR:**
- Section present but only placeholder text (e.g., "[To be filled]")
- Section has title but no content

**WARNING:**
- Section content too shallow (e.g., single sentence when paragraph expected)
- Key ideas list has <3 items

**INFO:**
- Section could benefit from more examples
- Section could include more detail

**Depth heuristics:**

```python
def check_content_depth(section_text):
    # Check for placeholders
    placeholders = ['[to be filled]', '[tbd]', '[todo]', '(empty)']
    if any(p in section_text.lower() for p in placeholders):
        → ERROR: Placeholder text found
    
    # Check word count
    word_count = len(section_text.split())
    
    if word_count < 20:
        → WARNING: Section too short ({word_count} words)
    
    if word_count < 50:
        → INFO: Section could be more detailed ({word_count} words)
```

---

## Dimension 3: Coherence

### Definition

Logical flow between sections, clear arguments, no internal contradictions, smooth transitions.

### Criteria

#### 3.1 Logical Flow

**ERROR:**
- Argument jumps to conclusion without support
- Major logical gap in reasoning
- Definition contradicts key ideas

**WARNING:**
- Weak connection between sections
- Argument could be clearer
- Some logical steps missing

**INFO:**
- Flow is acceptable but could be smoother
- Could add transitional phrases

**Check method:**

```python
# Use LLM to assess logical flow
prompt = f"""
Assess the logical flow of this content:

{file['body']}

Check:
1. Does the definition align with key ideas?
2. Are arguments well-supported?
3. Are there logical gaps?

Output: "OK" or list issues
"""

result = llm_call(prompt, model='claude-3-5-sonnet')
```

#### 3.2 Internal Contradictions

**ERROR:**
- Direct contradiction (e.g., "X is true" then "X is false")
- Contradictory claims about same fact
- Definition contradicts key ideas

**WARNING:**
- Apparent contradiction that might be contextual
- Inconsistent terminology (same concept, different names)

**INFO:**
- Could clarify potential ambiguity
- Could note exception or special case

**Detection:**

```python
# Extract all claims
claims = extract_claims(file['body'])

# Check each pair for contradiction
for i, claim1 in enumerate(claims):
    for claim2 in claims[i+1:]:
        # Use LLM to check contradiction
        prompt = f"""
        Do these two claims contradict each other?
        
        Claim 1: {claim1}
        Claim 2: {claim2}
        
        Output: "OK" or explain contradiction
        """
        
        result = llm_call(prompt)
        if result != "OK":
            → ERROR: Internal contradiction
```

#### 3.3 Argument Support

**ERROR:**
- Claim made without any support or evidence
- Conclusion doesn't follow from premises
- Circular reasoning

**WARNING:**
- Weak support for claim
- Could use more evidence
- Argument relies on assumption

**INFO:**
- Argument is sound but could be stronger
- Could add example to illustrate

**Examples:**

```markdown
❌ ERROR:
"RAG is the best approach for all use cases"
→ Absolute claim without support

✅ CORRECT:
"RAG is effective for knowledge-intensive tasks (Source: [[src_rag-study]]), though other approaches may be better for creative tasks"

⚠️ WARNING:
"Most developers prefer Claude Code"
→ Vague claim, needs data

✅ CORRECT:
"In a 2026 survey of 1000 developers, 65% preferred Claude Code (Source: [[src_dev-survey-2026]])"
```

#### 3.4 Definition Quality (Concepts only)

**ERROR:**
- Definition is circular (defines term using itself)
- Definition is too vague to be useful
- Definition contradicts standard usage

**WARNING:**
- Definition could be more precise
- Definition assumes prior knowledge

**INFO:**
- Definition is acceptable but could be clearer
- Could add example to illustrate

**Examples:**

```markdown
❌ ERROR (circular):
"Claude Code is a code tool that helps with coding"
→ Defines "code" using "code"

✅ CORRECT:
"Claude Code is an AI-assisted development workflow where Claude autonomously implements features given high-level specifications"

⚠️ WARNING (vague):
"RAG is a technique for improving AI"
→ Too vague, what kind of technique?

✅ CORRECT:
"RAG (Retrieval-Augmented Generation) is a technique that enhances LLM responses by retrieving relevant documents before generation"
```

---

## Dimension 4: Vietnamese Quality

### Definition

For Vietnamese content: correct grammar, natural phrasing, no machine translation artifacts, technical terms preserved in English.

**Note:** This dimension only applies to files with Vietnamese content. English-only files skip this check.

### Criteria

#### 4.1 Grammar

**ERROR:**
- Subject-verb disagreement
- Wrong tense
- Sentence fragment

**WARNING:**
- Awkward phrasing
- Overly complex sentence structure
- Minor grammar issue

**INFO:**
- Grammar correct but could be more natural
- Could simplify sentence

**Common Vietnamese grammar issues:**

| Issue | Example (Wrong) | Correct |
|---|---|---|
| Tense | "Năm 2025, mô hình sẽ ra mắt" (but 2025 passed) | "Năm 2025, mô hình đã ra mắt" |
| Double passive | "Được được huấn luyện" | "Được huấn luyện" |
| Redundant words | "Rất là tốt" | "Rất tốt" |

**Check method:**

```python
# Use Vietnamese language model
prompt = f"""
Kiểm tra ngữ pháp tiếng Việt:

{text}

Tìm lỗi:
1. Chủ ngữ - động từ
2. Thì
3. Cấu trúc câu

Output: Danh sách lỗi hoặc "OK"
"""

result = llm_call(prompt, model='gemini-2.0-flash')
```

#### 4.2 Spelling

**ERROR:**
- Misspelled Vietnamese word
- Wrong diacritic marks

**WARNING:**
- Inconsistent spelling (e.g., "hoá" vs "hóa")
- Typo that doesn't change meaning

**INFO:**
- Spelling correct but could use more common variant

**Common spelling issues:**

| Wrong | Correct |
|---|---|
| hoc | học |
| nang cao | nâng cao |
| du lieu | dữ liệu |
| thuat toan | thuật toán |

#### 4.3 Machine Translation Artifacts

**ERROR:**
- Obvious machine translation (unnatural phrasing)
- Word-for-word translation from English

**WARNING:**
- Slightly unnatural phrasing
- Calque from English

**INFO:**
- Phrasing is acceptable but could be more idiomatic

**Common MT artifacts:**

```markdown
❌ ERROR (MT artifact):
"Mô hình ngôn ngữ lớn là một loại của trí tuệ nhân tạo"
→ Word-for-word from "Large language model is a type of artificial intelligence"

✅ CORRECT (natural Vietnamese):
"Mô hình ngôn ngữ lớn là một dạng trí tuệ nhân tạo"

❌ ERROR (double passive):
"Được được sử dụng rộng rãi"

✅ CORRECT:
"Được sử dụng rộng rãi"

❌ ERROR (double preposition):
"Về về vấn đề này"

✅ CORRECT:
"Về vấn đề này"
```

**Detection patterns:**

```python
mt_patterns = [
    r'\b(?:được|bị)\s+(?:được|bị)\b',  # Double passive
    r'\b(?:của|về)\s+(?:của|về)\b',    # Double preposition
    r'\b(?:rất|quá)\s+(?:rất|quá)\b',  # Double intensifier
    r'\bmột loại của\b',                # Calque "a type of"
]

for pattern in mt_patterns:
    if re.search(pattern, text):
        → WARNING: Possible MT artifact
```

#### 4.4 Technical Term Preservation

**ERROR:**
- Technical term translated to Vietnamese when should stay English
- English term used inconsistently (sometimes translated, sometimes not)

**WARNING:**
- Technical term translated but meaning preserved
- Could add English term in parentheses

**INFO:**
- Term usage is acceptable
- Could standardize terminology

**Technical terms that should stay in English:**

| Term (English) | ❌ Don't translate to | ✅ Use in Vietnamese |
|---|---|---|
| embedding | nhúng, vector hóa | embedding |
| fine-tuning | tinh chỉnh | fine-tuning |
| prompt injection | tiêm prompt | prompt injection |
| RAG | Tạo tăng cường truy xuất | RAG |
| LLM | Mô hình ngôn ngữ lớn | LLM (có thể giải thích lần đầu) |
| token | mã thông báo | token |
| context window | cửa sổ ngữ cảnh | context window |

**Acceptable pattern:**

```markdown
✅ CORRECT:
"RAG (Retrieval-Augmented Generation) là kỹ thuật..."
→ English term + Vietnamese explanation

✅ CORRECT:
"Kỹ thuật embedding giúp..."
→ English term used naturally in Vietnamese sentence

❌ ERROR:
"Kỹ thuật nhúng giúp..."
→ "embedding" translated to "nhúng"
```

---

## Severity Assignment Logic

### Priority order

When multiple issues found in same file:

1. **ERROR** — Must fix before file is usable
2. **WARNING** — Should fix for quality
3. **INFO** — Nice to fix, suggestions

### Escalation rules

- 3+ ERRORs in one file → Consider moving to `wiki/drafts/`
- 5+ WARNINGs in one file → Flag for systematic issue
- 10+ INFOs in one file → Likely over-reporting, review criteria

### Aggregation

When reporting to Julius:
- Group issues by file
- Sort by severity within file
- Limit to top 20 issues total (daily validation)

---

## Validation State Tracking

### Last validation timestamp

Store in `.hermes/MEMORY.md`:

```markdown
## Last validation state

- Date: 2026-05-09 22:00:00
- Files validated: 205
- File hashes: {file_path: hash, ...}
```

### Skip unchanged files

```python
last_state = load_last_validation_state()

for file in existing_files:
    current_hash = hash_file(file)
    
    if current_hash == last_state.get(file):
        # File unchanged since last validation
        skip_validation(file)
    else:
        # File changed, validate
        validate(file)
        last_state[file] = current_hash

save_validation_state(last_state)
```

---

## Related Documentation

- [SKILL.md](SKILL.md) — Output Validator overview
- [workflow.md](workflow.md) — Step-by-step validation process
- [examples.md](examples.md) — Sample reports and issues
- [wiki/meta/format-spec.md](../../wiki/meta/format-spec.md) — Structural format rules (validated by Format Validator)

---

**End of validation-criteria.md**
