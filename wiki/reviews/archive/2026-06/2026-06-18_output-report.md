# Output Validation — 2026-06-18

**Status:** approved
**Approved by:** Julius
**Issues found:** 4
**Created:** 2026-06-18 22:00:00
**Validator:** output-validator

**Files checked:** 392 (92 sources + 300 concepts; 5 new since last run)
**New files (compiled today):** 5 (1 source + 4 concepts)

---

## Issue 1: File truncated — Missing required sections

**File:** wiki/concepts/infrastructure-capex-cycle.md
**Severity:** ERROR
**Dimension:** Completeness
**Issue:** File is truncated/incomplete. The Key ideas section's last bullet cuts off mid-sentence at `- **Commoditization risk`. Missing both required sections: `## Related concepts` and `## Sources`. The file has only 25 lines total; a typical concept file has 35-40 lines.

**Evidence:**
```
Line 25: - **Strategic relationships**: Special relationships với chip manufacturers và energy providers là competitive advantage
Line 26: - **Commoditization risk
(end of file — no Related concepts, no Sources)
```

**Suggested fix:** Re-compile this concept. The Compile Agent output was likely interrupted or truncated. Run compile-agent again for `src_l1-blockchain-ai-lab-comparison.md` to regenerate `infrastructure-capex-cycle.md`.

---

## Issue 2: Definition too short (1 sentence, need 2-3)

**File:** wiki/concepts/altcoin-frenzy-pattern.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition section contains only 1 sentence. The recommended range for concept definitions is 2-3 sentences.

**Evidence:**
```
Pattern thị trường xảy ra khi một category đã được de-risk bởi existence proof của category kings (first movers), dẫn đến làn sóng new entrants raise capital ở định giá cao dựa trên whitepapers, research, hoặc promises của differentiation trong tương lai.
```

**Suggested fix:** Expand definition to 2-3 sentences. E.g., add a sentence about the outcome distribution: "Hầu hết các alt-entrants thất bại, một số ít breakout thành tier 2, và rất ít durable trong dài hạn."

---

## Issue 3: Definition too short (1 sentence, need 2-3)

**File:** wiki/concepts/category-kings-dynamics.md
**Severity:** WARNING
**Dimension:** Completeness
**Issue:** Definition section contains only 1 sentence. The recommended range for concept definitions is 2-3 sentences.

**Evidence:**
```
Hiện tượng first movers trong một category mới accrue outsized value một cách nhanh chóng, tạo ra "prize" legible cho các competitors sau, đồng thời liên tục nâng cao table stakes cho new entrants thông qua ecosystem development.
```

**Suggested fix:** Expand definition to 2-3 sentences. E.g., add a sentence clarifying what makes category kings defensible: "Lợi thế này đến từ ecosystem moat (SDKs, integrations, partnerships) và immaculate conception — founding stories độc nhất không thể replicate."

---

## Issue 4: Definition at minimum threshold (2 sentences, could expand)

**File:** wiki/concepts/ai-lab-crypto-analogy.md
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Definition section has exactly 2 sentences, meeting the minimum requirement but at the boundary. Could benefit from a third sentence to more fully define the concept.

**Evidence:**
```
Pattern so sánh cấu trúc và động lực ngành AI labs với chu kỳ L1 blockchain (2017-2021). Theo đó, các AI labs lớn tương ứng với các L1 blockchain: OpenAI = Bitcoin (first mover), Anthropic = Ethereum (credible alternative), và các lab mới = altcoins (high-risk, high-valuation entrants).
```

**Suggested fix:** Add a third sentence explaining what this analogy predicts. E.g.: "Dựa trên lịch sử L1, analogy này dự đoán đa số AI alt-labs sẽ thất bại, với chỉ một số ít breakout."

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 |
| WARNING | 2 |
| INFO | 1 |

**Systemic issues (previously flagged, not re-reported):**
- "ngưởi" typo: Still present in 10 files from 2026-06-17 batch (report pending, not yet approved/fixed). Not re-flagging — no new evidence.
- `status: draft`: All 4 new concepts carry `draft` status. This is consistent with the ~160 draft concepts pattern flagged in 2026-06-14 and 2026-06-17. Julius marked this as "Not Approved In This Pass." Not re-flagging.

**Individual issues:**
1. ERROR: `infrastructure-capex-cycle.md` truncated — missing 2 required sections
2-3. WARNING: Two concepts with 1-sentence definitions
4. INFO: One concept with 2-sentence definition (minimum threshold)

**Backlinks health:**
- All 4 concepts referenced by today's source exist (all compiled today).
- One wikilink in `ai-lab-crypto-analogy.md` → `[[ai-infrastructure-bubble]]` exists ✓
- No new broken wikilinks detected in today's batch.

**Overall assessment:** Today's batch is small (5 files from 1 source) and well-compiled aside from one truncated file. The source file (`src_l1-blockchain-ai-lab-comparison.md`) is complete and well-structured. Three of four concepts are complete; one (`infrastructure-capex-cycle.md`) was cut off mid-generation. Vietnamese quality is good — no "ngưởi" typo in today's batch (the Compile Agent appears to have been fixed). The mix of Vietnamese content with English technical terms is appropriate and natural.

**1 ERROR — `infrastructure-capex-cycle.md` should be blocked from referencing until re-compiled.**
