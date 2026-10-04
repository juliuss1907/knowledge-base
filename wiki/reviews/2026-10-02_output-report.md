# Output Validation — 2026-10-02
- **Status:** APPLIED — Fix Agent (Kara AX400, OpenClaw main) xử lúc 2026-10-03 09:27 +07:00. Đã sửa 4 file: ai-lab-business-model.md (stub bullet + bỏ quotes 3 body wikilink + merge 3 bullet Google → 2 + dịch 4 cụm English lẫn), harness-engineering.md (bỏ quotes 3 body wikilink), ai-evals.md (bỏ .md khỏi 4 wikilink), raw/articles/articles.md (159/0, stale sau compile 08:08). Verify: validate.py 1138 files, ERROR 0, WARNING 402. Issue 1 nói target ai-capex-as-credit-cycle không tồn tại — SAI, file có thật (compile 09-30); stub bullet vẫn là defect thật. Chưa xử: Issue 5 Defect B (cần chốt mức trùng lặp), Issue 4 (2 forward-ref raw=0), Issue 3 tồn dư 19 file + 78/82 wikilink .md. Chi tiết: .openclaw/MEMORY.md 2026-10-03.
**Issues found:** 7 (1 ERROR, 5 WARNING, 1 INFO)
**Created:** 2026-10-02 23:00:50
**Validator:** output-validator
**Files checked:** 833 (217 sources + 616 concepts)
**New files:** 6 genuinely new (1 source + 5 concepts) + 5 existing concepts updated today by Compile Agent

---

## Issue 1: Stub key-idea bullet — content-free redirect

**File:** `wiki/concepts/ai-lab-business-model.md`
**Severity:** ERROR
**Dimension:** Completeness / Coherence
**Issue:** Key ideas contains a bare link bullet with no explanatory text. Every other bullet in the file is a full sentence; this one is a pointer.
**Evidence:** line 38 — `- Xem [[ai-capex-as-credit-cycle]]`
**Context:** Added in today's compile (confirmed in `git diff`: `+ - Xem [[ai-capex-as-credit-cycle]]`). Target resolution: `ai-capex-as-credit-cycle` → **no concept, no source, no raw** (`find raw/ -name '*ai-capex-as-credit-cycle*'` = 0). So the bullet is doubly defective: it carries no content, and its target does not exist.
**Suggested fix:** Expand the bullet to state the claim it is meant to support (the borrower's credit cycle: take-or-pay obligations refinanced by equity, i.e. `OpenAI nợ hàng trăm tỷ USD… mỗi vòng mới phải định giá cao hơn vòng trước` already states it 4 bullets above). Either (a) merge it into that bullet and drop the link, or (b) compile `ai-capex-as-credit-cycle` from a suitable source and keep the link. Do **not** keep a content-free redirect.
**KB-wide note:** this is the only link-only bullet across all 11 files (checked `grep '^- [^[]*\[\['` over every `## Key ideas` range). KB baseline is clean — treat as new defect, not a pattern.

---

## Issue 2: `.md` extension inside wikilinks — `ai-evals.md`

**File:** `wiki/concepts/ai-evals.md`
**Severity:** WARNING
**Dimension:** Coherence (Obsidian graph breakage)
**Issue:** All 4 wikilinks in this file (2 frontmatter, 2 body `## Sources`) carry a `.md` extension, so none of them resolve as Obsidian links.
**Evidence:** frontmatter line 7–8 + body lines 43–44 — `[[src_you-just-hired-a-million-bad-employees-a16z.md]]`, `[[src_gemini-4-argon-explained-in-5min.md]]`
**Root cause — carry-over, not today's defect:** the `.md` suffix on `src_you-just-hired-a-million-bad-employees-a16z.md` is present in `HEAD` (both frontmatter and body). Today's compile **copied the existing defect** when adding the new `src_gemini-4-argon-explained-in-5min` line. Fixing the new line without fixing the old one leaves the file still broken.
**Suggested fix:** Strip `.md` from all 4 links in this file (2 lines of frontmatter, 2 lines of body). See Issue 3 — this is a KB-wide pattern, so handle it as one sweep.
**KB-wide measurement:** `grep -rP '\[\[[^\]]+\.md\]\]' wiki/concepts/ wiki/sources/` = **82 occurrences**. Precedent files: `tokenmaxxing.md`, `external-retrieval-memory.md`, `semiconductor-industry-consolidation.md`.

---

## Issue 3: Quoted wikilinks in body `## Sources` — Obsidian renders them as text

**File:** `wiki/concepts/ai-lab-business-model.md`, `wiki/concepts/harness-engineering.md`
**Severity:** WARNING
**Dimension:** Coherence (Obsidian display)
**Issue:** format-spec §475 is explicit: *"Wikilinks in frontmatter fields (`original`, `sources`) use quoted format `"[[...]]"` for Obsidian compatibility. Wikilinks in body content use bare format `[[...]]`."* These two files put the **quoted** form inside the body `## Sources` list, so Obsidian shows literal quotes instead of a link.
**Evidence:**
- `ai-lab-business-model.md:50-52` — `- "[[src_how-ai-labs-eventually-make-money]]"`, `- "[[src_the-second-derivative-why-no-one]]"`, `- "[[src_gemini-4-argon-explained-in-5min]]"`
- `harness-engineering.md:44-46` — `- "[[src_harness-engineering-ai-coding]]"`, `- "[[src_googletech-behavioral-evals-harness-engineering]]"`, `- "[[src_gemini-4-argon-explained-in-5min]]"`
**Classification per line:**
- `ai-lab-business-model.md:50` — **carry-over**, present in `HEAD`
- `ai-lab-business-model.md:51,52` + all 3 lines of `harness-engineering.md:44,45,46` — **introduced today** (confirmed in `git diff`)
**Suggested fix:** Remove the quotes from the 6 body lines (leave frontmatter quoted). Do **not** touch the 25 KB-wide occurrences this run did not compile — see Info 2 for why that is now a Format Validator matter rather than an Output Validator one.
**KB-wide measurement:** quoted wikilinks inside body `## Sources` = **25 files** (sweep of all 616 concepts). Precedent: `agent-sandbox-runtimes.md`, `behavioral-evals.md`, `cognitive-distortions.md`, `context-engineering.md`.

---

## Issue 4: `agent-harness.md` — 2 broken wikilinks with no resolution path

**File:** `wiki/concepts/agent-harness.md`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Two `## Related concepts` links have no target and no raw material, so there is no natural resolution path. Per skill rules these stay WARNING, not ERROR — but they need an explicit decision, not silent carry-forward.
**Evidence:**
- line 32 — `[[agent-initiated-code-artifacts]]` → no concept, no source, **raw = 0**
- line 34 — `[[multi-agent-systems]]` → no concept, no source, **raw = 0**

Both links pre-date today (present in `HEAD`) — carry-forward. Today added `[[model-vs-harness-adoption]]` and `[[harness-engineering]]`, both of which resolve correctly.
**Suggested fix:** Two acceptable endings, same as other no-source forward-refs: (a) compile the concept when a suitable source arrives, or (b) Fix Agent drops the links. State which; do not auto-drop. Format Validator tracks both targets in its broken-target backlog.
**Note on resolution method:** resolved with **exact-filename tests** (`[ -f wiki/concepts/$t.md ]`), not `find -iname` globs — per the 2026-10-01 lesson, `find -iname` produces false positives that make a broken link look resolved.

---

## Issue 5: [SYSTEMATIC ISSUE] Defect B — source data points replicated across 5 concepts in one batch

**File:** 6 files in today's batch (see table)
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** Compile Agent propagated the same handful of facts from one source into 5 different concepts with near-identical wording. Each repetition is locally fine; collectively it means editing one number requires 5 edits, and the concepts stop carrying information specific to themselves. This is the **2nd occurrence** of Defect B (1st: `ai-engineering-skills.md`, 08-31).

| Fact | Duplicated in | Wording |
|---|---|---|
| Codex 5M vs anti-gravity 2.4M WAU | `agent-harness.md:25`, `harness-engineering.md:30`, `model-vs-harness-adoption.md:21` (+ source `:26,:37`) | near-verbatim, 3/3 |
| Argon below Pareto Frontier | `agent-harness.md:26`, `compute-concentration-frontier.md:49`, `gemini-4-argon.md:24` | near-verbatim, 3/3 |
| 113 Deep SWE tasks public since May + 23 flawed | `ai-evals.md:29,30`, `gemini-4-argon.md:23,24`, `benchmark-contamination.md:19,22` | near-verbatim, 3/3 |
| 22 tỷ token/phút → 11 quadrillion token/năm | `ai-lab-business-model.md:45`, `compute-concentration-frontier.md:47`, `gemini-4-argon.md:29` | near-verbatim, 3/3 |
| 1 triệu output token | `agent-harness.md:27`, `long-context-models.md:43`, `gemini-4-argon.md:31` | near-verbatim, 3/3 |

**Compounding factor:** 4 of the 10 concepts today derive from the **single** source `src_gemini-4-argon-explained-in-5min.md`, and its 19 Key points feed the batch. Every fact above has a natural canonical home:
- Codex/Pareto → `model-vs-harness-adoption.md` (the concept *about* that comparison)
- 113 tasks / 23 flawed → `benchmark-contamination.md`
- 1 triệu token + compounding → `autoregressive-error-compounding.md`
- 22 tỷ token/phút → `compute-concentration-frontier.md`

**Suggested fix:** In each of the 3 satellite concepts, replace the duplicated bullet with a one-line pointer (`xem [[canonical-concept]]`) that states *why the fact matters there*, rather than restating the number. Keep the full number in the canonical concept and in the source. Fix Agent applies; this is a judgment call about how much redundancy a concept should carry, so it needs Julius's call on the tolerance level before a sweep.

---

## Issue 6: [SYSTEMATIC ISSUE] Defect B, second form — same claim twice inside one file

**File:** `wiki/concepts/ai-lab-business-model.md`
**Severity:** WARNING
**Dimension:** Coherence
**Issue:** The Google-rollout argument appears as three separate bullets where one would do, each restating the preceding one.
**Evidence:** lines 43, 44, 45 —
- `:43` "Trợ giá subscription là đòn bẩy tạm thời… Google đã là công ty đại chông nên phải cẩn thận phân bổ compute"
- `:44` "Google chọn rollout theo segment doanh thu: Gemini 4 Argon dành cho Ultra subscription users và paid API users… thay vì đốt compute để đua subscription"
- `:45` "Quy mô API tạo lợi thế cấu trúc: 22 tỷ token/phút… kênh này có thể đang tự tài trợ, khác với mô hình trợ giá subscription"

All three are new today (confirmed in `git diff`). `:44` is the concrete instance of `:43`'s general claim; `:45`'s "khác với mô hình trợ giá subscription" repeats `:43`'s contrast a third time.
**Suggested fix:** Merge `:43` and `:44` into one bullet (general claim + Argon's concrete rollout as the example), keeping `:45` separate for the API scale figure. 3 bullets → 2.

---

## Issue 7: [INFO] `ai-lab-business-model.md` — heavy English mixing in Vietnamese prose

**File:** `wiki/concepts/ai-lab-business-model.md`
**Severity:** INFO
**Dimension:** Vietnamese quality
**Issue:** The file's `## Definition` and Key ideas mix untranslated English into Vietnamese sentences at a density above the rest of the batch. Preserved technical terms (`frontier`, `distillation`, `post-training`) are correct usage; the following are not — they are ordinary English words left in a Vietnamese clause.
**Evidence:**
- `:12` (Definition) — *"Câu hỏi cốt lõi: khi nào labs thực sự bắt đầu **makes money**?"*
- `:17` — *"Thay vì **trying to makes money** từ fares/API, labs nên tìm tài sản appreciates"*
- `:21` — *"**becoming the service**… rather than selling API"*
- `:12` — *"giá trị tạo ra cho users **flowing trực tiếp đến economy** thay vì builder"*

Note `:17` contains a grammar break as well: *"trying to makes money"* is not English and not Vietnamese — it should be *"trying to make money"*. This is a machine-translation artefact, not deliberate term preservation.
**Suggested fix:** Translate to Vietnamese, keeping only the genuinely technical terms in English. Also correct `trying to makes money` → `trying to make money`.
**Batch comparison:** the other 9 new files read as natural Vietnamese. This file is the outlier — likely because it aggregates 3 sources, 2 of them English-language finance writing.
**Cross-check:** dropped-i variant 5 = 0, so this is not the known tokenization defect; it is a separate translation-quality issue.

---

## Carry-forward measurements (all re-verified today, not inherited)

Per the 09-27 lesson, every numeric claim from the previous report's carry-over sections was re-measured against the filesystem before being inherited. Results:

| Claim (source) | Claimed | **Measured 2026-10-02** | Verdict |
|---|---|---|---|
| CJK injection files (10-01 Issue 7) | 9 files | **0** | ✅ **RESOLVED** — cleanup applied 10-02 10:52 per report status header |
| CJK legitimate set | 3 files | **3** (`byte-level-bpe` 中, `hundred-years-humiliation` 百年国耻, `chinese-culture-confucianism` 国家) | ✅ unchanged; `既是` streak = 0 since it was fixed |
| `amygdala-vs-prefrontal-cortex.md:25` CJK | present | **0 matches** | ✅ RESOLVED |
| Raw `status: processed` missing `compiled_to` (09-30 #3) | 3 files | **0** | ✅ RESOLVED — incl. the `compile_to:` misspelling (0 matches) |
| Raw genuine backlog (`status: unprocessed`) | 0 (drained 09-30) | **1** (`raw/articles/2026-05-20_unreasonable-effectiveness-of-html.md`) | ⚠️ **NEW** — 1 file ingested; see below |

**The single CJK injection backlog is closed.** 10 validator runs carried it unresolved; Fix Agent cleared all 9 files in one pass on 10-02. This is the first run in 10 days where no CJK cleanup action is requested.

**New raw backlog — 1 file, INFO only:** `raw/articles/2026-05-20_unreasonable-effectiveness-of-html.md` (`status: unprocessed`). Expected behaviour — Compile Agent runs 08:00, this was ingested later. No action; recorded so the next run can confirm it drained.

---

## Clean this run

- **Dropped-i variant 5 = 0 on all 4 sub-patterns** (`ngườ`, `thờ …`, `thay v `, `chính lờ/bằng lờ`). Clean streak now **12 runs** (08-23 → 10-02). Demotion to weekly has been recommended 3× (08-30, 08-31, 09-01) and remains unconfirmed — keeping daily.
- **Typo variants 1–4 = 0** (`ngưởi`, double-i incl. case-insensitive, `người` spacing merge, capital-I).
- **Source section-name drift: PASS.** `src_gemini-4-argon-explained-in-5min.md` uses `## Key points` (correct for sources), not `## Key ideas`.
- **Defect A (frontmatter sources vs body `## Sources` count): 6/6 PASS.** All 6 multi-source concepts today match exactly — 2/2, 2/2, 3/3, 2/2, 3/3, 2/2. Note this check passes *count-wise* on `ai-evals.md` (2 vs 2) even though both links carry `.md` (Issue 2) — the counts agree, the targets don't.
- **Definitions: all 10 new/updated concepts = 2–3 sentences.** Within spec (2–3).
- **0 truncated files, 0 empty sections, 0 draft-status regressions.**
- **New source's `original:` correctly points to** `raw/videos/2026-10-01_gemini-4-argon-explained-in-5min.md`, which carries `status: processed` + valid `compiled_to` backlink.
- **Content quality is high.** All 10 concepts have 7–19 substantive Key ideas, specific numbers (77,9% Deep SWE, 22 tỷ token/phút, 0,99^100 ≈ 0,366), direct quotes preserved in the source's `## Original excerpts`, and inline `[[wikilink]]` cross-references that resolve. The Argon batch is the best-aggregated compile in weeks: 4 of 10 concepts from one source, all with 3+ sources, zero Defect A failures.
- **Read-only confirmed:** no file under `wiki/sources/`, `wiki/concepts/`, `wiki/drafts/`, `wiki/topic/`, `wiki/tag/`, or `wiki/meta/` was written this run. Writes confined to `wiki/reviews/` + `.hermes/MEMORY.md`.

---

## Corrections to carried-over claims

No claim inherited from the 10-01 report was found wrong. All four numeric carry-overs were re-measured and came back either resolved or unchanged-with-justification. The one item that changed is a count the 10-01 report did not make: the raw backlog went 0 → 1.

---

## Actions needed

1. **Julius — decide redundancy tolerance for Defect B (Issue 5).** 5 concepts carry the same 5 facts in near-verbatim form. Suggested: keep full numbers in the canonical concept + source; satellites get a one-line "why it matters here" pointer. Needs a tolerance call before a sweep, since some redundancy is intentional in a wiki.
2. **`ai-lab-business-model.md` — remove the content-free bullet (Issue 1).** 1 line. Its target `ai-capex-as-credit-cycle` has no concept, no source, no raw — so the link is also unresolvable.
3. **`.md` sweep in `ai-evals.md` (Issue 2).** Strip `.md` from 4 links. KB-wide the pattern spans 82 occurrences — recommend Format Validator own the full sweep rather than Output Validator patching files it did not compile.
4. **Un-quote 6 body wikilinks** in `ai-lab-business-model.md` (3) and `harness-engineering.md` (3). 3 of 6 are today's, 3 are carry-over.
5. **`agent-harness.md` — decide on 2 no-source forward-refs** (`agent-initiated-code-artifacts`, `multi-agent-systems`): compile when a source arrives, or drop.
6. **`ai-lab-business-model.md` — merge 3 overlapping bullets → 2 (Issue 6)** and translate the English-mixing prose (Issue 7, ~5 phrases incl. one grammar break).
7. **No CJK action this run** — backlog closed 10-02. Do not re-raise.
8. **Standing recommendation, unchanged:** review `compile-agent/SKILL.md`. Rationale has shifted — CJK injection was the last active producer and is now fixed, but today's batch surfaced 3 new shape defects (stub bullet, body-quoted wikilinks, cross-concept fact replication). All 5 Vietnamese tokenization variants remain at 0.

---

## Structural integrity

| Check | Result |
|---|---|
| Files checked | 833 (217 sources + 616 concepts) — quick-scan total |
| Genuinely new today | 6 (`??` untracked: 1 source + 5 concepts) |
| Updated today (pre-existing) | 5 concepts (` M`: agent-harness, ai-evals, ai-lab-business-model, harness-engineering, long-context-models) |
| New files vs `find -newer` | Distinguished by `git ls-files --error-unmatch` + `git diff`, not mtime — per the 08-27 lesson, mtime is inflated by fix-apply edits |
| Backup cron | Still down — HEAD `e05f00ab` (`vault backup: 2026-09-24 20:51:08`). 10 days. 17+ `??` files untracked. Not an Output finding; Hygiene owns it. |