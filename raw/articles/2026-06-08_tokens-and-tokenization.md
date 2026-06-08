---
type: raw
source_type: article
source_url: https://bearisland.dev/posts/tokens-and-tokenization/
date_ingested: 2026-06-08
tags: []
status: unprocessed
---

# Tokens and Tokenization

Source: [Bear Island](https://bearisland.dev/posts/tokens-and-tokenization/)

---

Ask GPT-4 how many r's are in "strawberry" and it will confidently say two. The right answer is three. This isn't because the model can't count. It's because it never sees the letters at all.

Every Large Language Model (LLM) starts with the same operation: text comes in, gets chopped into chunks called tokens, and those chunks become integer IDs that index into an embedding matrix. The chunks aren't characters and they aren't words. They're something more specific, and the specificity matters more than most people realize.

## What a "token" really is

Most people first meet the word "token" through prices and limits: "1,500 tokens used", "the context window is 128K tokens". Those numbers are real, but they hide what a token actually is.

A token is the **smallest unit of input a specific model can perceive**. Each model has its own fixed list of tokens, called its vocabulary, decided once at training time. GPT-4's vocabulary isn't Claude's. Claude's isn't Llama's.

When you send text to a model, the text gets chopped into pieces from that model's vocabulary, and each piece is swapped for an integer ID. Only those IDs ever reach the model. The model never sees text. It sees a sequence of integer indices into its own private alphabet.

So tokens aren't "roughly like words" or "kind of like characters". They're the **atoms of perception for one specific model**, and they're the only language that model speaks. Two models fed the same English sentence will produce two different integer sequences, often of different lengths.

Example: "I love strawberry milkshakes!"
- **GPT-4:** 9 tokens (I · love · str aw berry · milk sh akes !)
- **Llama 3:** 7 tokens (I · love · straw berry · milk shakes !)

The same sentence is nine tokens to GPT-4 and seven tokens to Llama 3. Not because Llama is smarter or the sentence changed, but because the two models have different vocabularies. To GPT-4, the token "·straw" doesn't exist as a single chunk, so "strawberry" splits across three pieces. Llama 3's vocabulary happens to include "·straw", so it gets through in two.

## BPE, the algorithm

BPE (Byte Pair Encoding) is an algorithm for deciding which subword chunks deserve to be tokens, given a corpus and a target vocabulary size. It starts small and grows the vocabulary one merge at a time, always merging the most frequent adjacent pair in the corpus.

**The algorithm:**

1. Initialize the vocabulary as every distinct character in the corpus.
2. Scan the corpus and count every adjacent pair of tokens.
3. Take the most frequent pair, merge it into a new token, and add it to the vocabulary.
4. Repeat steps 2 and 3 until the vocabulary has V entries.

That's it. No clever scoring, no neural network. The "merge" in step 3 doesn't do anything sophisticated. It just declares: from now on, whenever you see t followed by h in this corpus, treat them as one symbol called th.

Two details matter:
- The originals don't disappear: when t and h get merged into th, all three are now in the vocabulary.
- Pairs get re-counted after each merge: once th is a token, the next iteration might find that th + e is the new top pair → merge → the.

## Byte-level BPE

The problem with character-level BPE: any rare Unicode codepoint the corpus didn't include is still out-of-vocabulary at the character level.

**GPT-2 introduced a fix:** start with bytes instead of characters. There are exactly 256 possible byte values, so:
- The initial vocabulary is fixed at 256, regardless of corpus.
- Every byte is in the vocabulary, by definition.
- Any text representable on a computer is, by definition, a byte sequence.
- **Out-of-vocabulary is eliminated by construction.**

**The UTF-8 wrinkle:** Most modern text is encoded as UTF-8, where each Unicode character becomes 1 to 4 bytes:
- ASCII (A): 1 byte
- European scripts (é): 2 bytes
- Asian scripts (中): 3 bytes
- Emoji (🍓): 4 bytes

**The cost:** non-ASCII text uses more tokens when the training corpus underrepresents the script. A Chinese sentence run through an English-heavy model decomposes into byte-level chunks rather than character-shaped tokens. Same string, more tokens. This is why API pricing tends to hit Chinese, Arabic, and Hindi harder than English.

## Vocabulary size as a design knob

Vocabulary size V is a hyperparameter set before training. The obvious instinct is that bigger should be better, since common substrings collapse into single tokens and text compresses into shorter sequences. So why do real models stop at 32K to 256K?

**The short answer:** V controls three different costs at once and only one benefit, and the cost quickly becomes severe.

**The benefit: compression.**
- Bigger V means more common substrings get their own token
- A given document encodes into fewer tokens
- Less work per document, more content per budget

**Cost 1: embedding matrices.**
Every token needs its own row in the embedding matrix (V × d). There's also a matching output matrix. So just the vocab tables cost: **2 × V × d** parameters.

With d = 4,096:
| V | Model | Vocab Parameters |
|---|-------|------------------|
| 32,000 | LLaMA 2 | 262 M |
| 128,000 | LLaMA 3 | 1.05 B |
| 256,000 | Gemini | 2.10 B |
| 1,000,000 | hypothetical | 8.19 B |

At V = 1M, you've spent the parameter count of an entire 8B-class model on lookup tables alone.

**Cost 2: rare tokens barely get trained.**
A token's row in the embedding matrix only gets trained on the times that token appears in the data. Real text is brutally skewed (Zipf's law):
- Top 1,000 tokens cover ~80% of all text
- Top 10,000 cover ~95%
- Everything beyond is the long tail

On a 1 trillion-token training corpus:
- V = 32K: even rarest tokens see tens of thousands of updates
- V = 1M: hundreds of thousands of long-tail tokens see only 10 to a few hundred updates each

**Cost 3: each prediction gets expensive.**
Every time the model picks the next token, it produces a probability distribution over all V tokens. The V × d matrix multiplication costs V × d operations. For d = 4,096, the crossover lands near V = 50,000. Beyond it, the prediction is one of the most expensive single operations.

**The central tradeoff:**
```
parameter cost ∝ V
compression gain ∝ log V
```

That gives a clear Pareto frontier. At small V (below 30K), spending a small extra parameter budget yields big compression gains. At large V (above 256K), spending huge extra parameters yields almost nothing.

**Where real models land:**
| Model | V | Comment |
|-------|---|---------|
| LLaMA 1 / LLaMA 2 | 32,000 | English-focused, parameter-efficient |
| GPT-2 | 50,257 | |
| GPT-4 (cl100k_base) | ~100,000 | |
| LLaMA 3 | 128,256 | Jumped specifically for multilingual coverage |
| Gemini | 256,000 | Heavy multilingual |

The dominant pressure pushing V up is **multilingual coverage**. Each new script (Cyrillic, Arabic, Devanagari, CJK) wants its own token budget.

## Variants: BPE, WordPiece, and SentencePiece

**BPE** (covered above): Frequency-based. Merge the most common adjacent pair. Runs on pre-tokenized words (regex-split on whitespace and punctuation first, GPT-style).

**WordPiece**: Google's variant, originally for speech recognition, later adopted by BERT. Similar to BPE but optimizes for likelihood rather than frequency.

**SentencePiece**: Google's library that implements BPE and unigram language modeling. Treats the input as a raw stream of characters with no preprocessing. The space character is just another token. This matters for languages that don't use spaces (Chinese, Japanese, Thai).

## Why "strawberry" has 3 r's

Back to the opening question. GPT-4 says "strawberry" has 2 r's because:

1. It never sees the letters.
2. "strawberry" tokenizes to: ["str", "aw", "berry"]
3. The model sees: token 12345, token 67890, token 11111
4. It learns that "str" and "aw" don't contain "r"
5. It learns that "berry" contains "r" once
6. Total: 1 "r" (in its mind)
7. It rounds up to 2 because "berry" has "rry" which might be two r's

The model never had a chance to count the r's because it never saw them as individual characters. It saw three opaque integer IDs.

## Key takeaways

- **Tokens are model-specific atoms of perception.** Not words, not characters.
- **BPE builds vocabularies by frequency**, merging common pairs iteratively.
- **Byte-level BPE guarantees coverage** for any Unicode text by starting with 256 bytes.
- **Vocabulary size is a tradeoff:** compression vs. parameter cost vs. training quality vs. inference speed.
- **The "strawberry" problem isn't counting failure** — it's a fundamental limitation of tokenization.

---

*A token is the smallest unit of input a specific model can perceive. The model never sees text. It sees a sequence of integer indices into its own private alphabet.*