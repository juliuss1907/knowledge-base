# Output Validation — 2026-07-26

**Status:** applied
**Applied by:** fix-agent
**Applied at:** 2026-07-26 14:08
**Approved by:** Julius
**Issues found:** 2 (1 ERROR, 0 WARNING, 1 INFO)
**Created:** 2026-07-26 11:31
**Validator:** output-validator

---

## Issue 1: Dropped-i typos (variant 5) — systemic in new batch

**Severity:** ERROR
**Dimension:** Vietnamese quality
**Files affected:** 6/8 new files (75%), ~10 instances

**Evidence:**

| File | Line | Instance | Should be |
|---|---|---|---|
| `src_introducing-backsearch-gr-inc.md` | 24 | "một thờ điểm" | "một thời điểm" |
| `src_introducing-backsearch-gr-inc.md` | 29 | "tại thờ điểm" | "tại thời điểm" |
| `src_monid-ai-agent-tool-platform.md` | 34 | "cho ngườ dùng" | "cho người dùng" |
| `agent-backtesting.md` | 30 | "tại thờ điểm" | "tại thời điểm" |
| `frozen-corpus-search.md` | 16 | "một thờ điểm" | "một thời điểm" |
| `pay-per-call-pricing.md` | 16 | "ngườ dùng" | "người dùng" |
| `pay-per-call-pricing.md` | 16 | "thay v thanh toán" | "thay vì thanh toán" |
| `point-in-time-data.md` | 16 | "một thờ điểm" | "một thời điểm" |
| `point-in-time-data.md` | 22 | "một thờ điểm" | "một thời điểm" |
| `point-in-time-data.md` | 23 | "qua thờ gian" | "qua thời gian" |

**Pattern:** 75% of today's batch affected — this is the 5th manifestation of the Compile Agent's "ời → ờ" tokenization defect. Quick-scan does not yet detect variant 5, so the validator must run manual grep.

**Suggested fix (Kara):**
```bash
for f in wiki/sources/src_introducing-backsearch-gr-inc.md \
         wiki/sources/src_monid-ai-agent-tool-platform.md \
         wiki/concepts/agent-backtesting.md \
         wiki/concepts/frozen-corpus-search.md \
         wiki/concepts/pay-per-call-pricing.md \
         wiki/concepts/point-in-time-data.md; do
  sed -i 's/thờ điểm/thời điểm/g; s/thờ gian/thời gian/g; s/ngườ dùng/người dùng/g; s/thay v /thay vì /g' "$f"
done
```

**[SYSTEMATIC ISSUE]** — All five dropped-i/ời variants trace to the same Compile Agent prompt defect. Recommend adding variant 5 detection to `quick-scan.sh` and reviewing Compile Agent prompt for the underlying tokenization issue.

---

## Issue 2: "thay v" truncation — word fragment

**Severity:** INFO
**Dimension:** Vietnamese quality
**File:** `wiki/concepts/pay-per-call-pricing.md`, line 16
**Evidence:** "thay v thanh toán" → "thay vì thanh toán"
**Note:** The word "vì" is truncated to "v" — this is a distinct error from dropped-i (the entire word is missing, not just the trailing 'i'). Co-occurs with "ngườ dùng" on the same line. The sed fix above covers this.

---

## ✅ Passing — New files (8)

| File | Definition | Key ideas | Sources | Overall |
|---|---|---|---|---|
| `src_introducing-backsearch-gr-inc.md` | ✅ | ✅ 7 items | ✅ Concepts ref'd | Good |
| `src_monid-ai-agent-tool-platform.md` | ✅ | ✅ 7 items | ✅ Concepts ref'd | Good |
| `agent-backtesting.md` | ✅ 2 câu | ✅ 6 items | ✅ Backlinked | Good |
| `ai-agent-tool-orchestration.md` | ✅ 2 câu | ✅ 5 items | ✅ Backlinked | Good |
| `frozen-corpus-search.md` | ✅ 2 câu | ✅ 6 items | ✅ Backlinked | Good |
| `pay-per-call-pricing.md` | ✅ 2 câu | ✅ 6 items | ✅ Backlinked | Good |
| `point-in-time-data.md` | ✅ 2 câu | ✅ 5 items | ✅ Backlinked | Good |
| `unified-api-gateway.md` | ✅ 2 câu | ✅ 6 items | ✅ Backlinked | Good |

**Structural quality:** All 8 files meet minimum content depth requirements. Definitions are 2 sentences, Key ideas are 5-7 items, Sources sections are populated with backlinks. Vietnamese quality is good aside from the dropped-i typos documented above.

---

## Systemic overview

| Metric | Count |
|---|---|
| Total files checked | 627 (155 sources + 472 concepts) |
| New files today | 8 (2 sources + 6 concepts) |
| 1-sentence definitions | 470 (legacy, systemic) |
| Too few key points (<5) | 86 (legacy, systemic) |
| Empty Key ideas | 9 (not in today's batch) |
| Draft concepts | 303 (legacy) |
| Truncated files | 0 |

---

## Verdict

**REVISE** — 1 ERROR (dropped-i typos in 6 new files) + 1 INFO (word fragment). No structural issues.

Fix list ready for Kara. Dropped-i typos are mechanical (sed fix), not content problems. After fixing, all 8 files qualify for review/promotion.
