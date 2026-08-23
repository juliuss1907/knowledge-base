# Output Validation — 2026-08-22

**Status:** approved
**Approved by:** Julius
**Issues found:** 8 (1 ERROR, 4 WARNING, 3 INFO)
**Created:** 2026-08-22 23:00:29
**Validator:** output-validator

---

**Files checked:** 174 sources + 525 concepts
**New files:** 21 (5 sources + 16 concepts) — compiled 2026-08-22

**New files validated in detail:**
- Sources: src_3-ways-to-get-rich, src_neuroscience-of-perfect-skill-acquisition, src_once-you-understand-neuroplasticity, src_principles-of-better-decisions, src_the-art-of-strategic-thinking
- Concepts: career-compounding, compounding-effect, costly-signal, deliberate-practice, first-principles-thinking, focus, identity-transformation, incentives-mental-model, inversion, leverage, neuroplasticity, opportunity-cost, probabilistic-thinking, second-order-thinking, skill-acquisition-framework, strategic-thinking

**Overall:** Batch chất lượng cao. Factual accuracy tốt — các citation kiểm tra được đều đúng (Ericsson/Krampe/Tesch-Römer 1993; Spence 1973; Crawford & Sobel 1982; Bayes essay 1763; Jacobi "man muss immer umkehren"; Berkshire ~20%/năm; số liệu diabetes 0.93%→7.4% theo Farnam Street). Không có mâu thuẫn nội bộ, không file truncated, cấu trúc section đầy đủ. Vietnamese tự nhiên. Vấn đề chính: 2 typo "Ngườii" trong file mới (quick-scan KHÔNG bắt được vì regex case-sensitive — "Ngườii" viết hoa N), 1 typo "bậce", 1 source link sai slug sẽ không bao giờ resolve, và kho typo carry-over từ các batch cũ chưa được Fix Agent dọn sạch.

**Dropped-i manual grep (bắt buộc):** 0 matches cho cả 3 sub-patterns (ngườ / thờ-compound / thay v + lờ) — sạch.

**Ghi chú quick-scan false positives:** "Empty Key ideas: 9" phần lớn là false positive — 8/9 file dùng numbered list hoặc bảng (google-project-oxygen.md có đủ 8 behaviors dạng numbered list; six-stage-research-pipeline.md dùng bảng Stage/Tool), chỉ đếm được `-` bullets. Nội dung thực tế đầy đủ. Không cần fix.

---

## Issue 1: Typo "Ngườii" ×2 trong file mới — variant 2 (double-i)

**File:** wiki/concepts/second-order-thinking.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Hai instance typo double-i "Ngườii" (viết hoa N) — variant 2 của Compile Agent defect. Đáng chú ý: quick-scan.sh báo "double-i (new: 0)" vì regex `ngườii|đờii|...` case-sensitive, không match "Ngườii" viết hoa đầu câu. Đây là lỗ hổng detection của quick-scan, không phải file sạch.
**Evidence:** Line 30: `- Ngườii nghĩ cấp hai hỏi: "Và sau đó thì sao?" (And then what?) — xem xét hậu quả kéo dài nhiều năm`; Line 44: `- Ngườii nghĩ ở cấp độ cao hơn chơi trò chơi dài hơn, nhìn xa hơn, chuẩn bị tốt hơn`
**Suggested fix:** `s/Ngườii/Người/g` cả 2 dòng.

---

## Issue 2: Typo "bậce" → "bậc"

**File:** wiki/sources/src_the-art-of-strategic-thinking.md
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Trong Summary, "bậce chiến lược gia" sai chính tả — đúng là "bậc".
**Evidence:** Line 24: `Bài viết phân tích 9 precepts của Miyamoto Musashi về bậce chiến lược gia, phân biệt generalist – specialist – master/strategist`
**Suggested fix:** `s/về bậce chiến lược gia/về bậc chiến lược gia/`.

---

## Issue 3: Source link sai slug — không bao giờ resolve

**File:** wiki/concepts/incentives-mental-model.md
**Severity:** ERROR
**Dimension:** Completeness / Factual (source verifiability)
**Issue:** Frontmatter (line 8) và section Sources (line 41) trỏ đến `[[src_the-power-of-incentives-hidden-forces-shape-behavior]]` — slug này KHÔNG tồn tại. File thật là `wiki/sources/src_incentives-hidden-forces.md` (đã tồn tại từ 06-29). Đây không phải forward-reference (target không "chưa compile" mà là "sai tên") — link sẽ không bao giờ resolve, nguồn của concept không verify được.
**Evidence:** Line 8: `  - "[[src_the-power-of-incentives-hidden-forces-shape-behavior]]"`; Line 41: `- [[src_the-power-of-incentives-hidden-forces-shape-behavior]]`
**Suggested fix:** Thay cả 2 chỗ bằng `[[src_incentives-hidden-forces]]`.

---

## Issue 4: [SYSTEMIC — carry-over] Double-i typos còn sót 18 file cũ (~26 instances)

**File:** 18 files (chi tiết bên dưới)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Kho typo double-i (ờii/ớii/ỏii) từ các batch 06-23 → 08-01 vẫn còn sau đợt "fix" 08-06 (đợt đó chỉ xử lý 5 file). 0/19 file bị ảnh hưởng là file mới hôm nay — toàn bộ carry-over. Không phải lỗi mới của Compile Agent; là backlog Fix Agent chưa dọn xong.
**Evidence (top files theo số instance):** src_lam-the-nao-e-ra-quyet-inh-khi-con-thankvn.md (3), src_never-enough-ronacher.md (2), type-1-vs-type-2-decisions.md (2), streak-psychology.md (2), never-enough-culture.md (2), decision-cost-analysis.md (2), colin-powell-40-70-rule.md (2 — gồm "tớii"→"tới" và "thờii"), optionality-principle.md (2 — gồm "giỏii"), cùng 11 file khác 1 instance each (attention-economy-vs-knowledge-economy, completion-motivation, increasing-surface-area-luck, src_gamification-app-truth, src_nha-bao-lam-gi, src_this-will-help-you-figure-out-what-you-want, work-life-balance, small-bets-strategy, protoge-effect, moores-law-economics).
**Suggested fix:** Chạy sed fix double-i (đã có trong SKILL.md production lessons) trên 18 file; thêm "Ngườii" viết hoa vào pattern.

---

## Issue 5: [SYSTEMIC — carry-over] Capital-I typos 14 file cũ (~18 instances)

**File:** 14 files (chi tiết bên dưới)
**Severity:** WARNING
**Dimension:** Vietnamese
**Issue:** Variant 4 (chữ I hoa sau nguyên âm có dấu) vẫn còn trong 14 file cũ — 18 instances (ơI ×9, ờI ×7, khác). Toàn bộ carry-over, 0 file mới hôm nay.
**Evidence (top files):** dopamine-prediction-gap.md (3), src_reward-hacking-writeup.md (2), ai-safety-monitoring.md (2), ai-alignment.md (2), cùng 10 file khác 1 instance each (reward-seeking, reward-hacking, psychic-entropy, outcome-independence, machine-economy, hedonic-adaptation, autonomous-agents, apparent-success-seeking, agentic-commerce, src_is-there-anything-left-build-crypto-wintermute).
**Suggested fix:** Chạy sed comprehensive capital-I (42 cặp ký tự, có sẵn trong SKILL.md) trên 14 file.

---

## Issue 6: Forward-reference wikilinks từ file mới — 17 unique targets

**File:** 16 concept/source mới hôm nay
**Severity:** INFO
**Dimension:** Completeness
**Issue:** Các file mới link đến 17 concept chưa compile: decision-making (×3 files), game-theory, bayesian-thinking, cognitive-biases, deep-work, fat-tailed-curves, first-order-thinking, five-whys, premeditatio-malorum, reinforcement-schedules, saying-no, scarcity-mental-model, socratic-questioning, stoicism, time-blocking, trade-offs-mental-model, uncertainty. Đây là forward-references hợp lệ, thuộc pool ~393 WARNING broken-wikilink mà Format Validator đang track — sẽ tự resolve khi Compile Agent xử lý raw tương ứng.
**Evidence:** Ví dụ: second-order-thinking.md → [[first-order-thinking]], [[decision-making]]; probabilistic-thinking.md → [[bayesian-thinking]], [[fat-tailed-curves]], [[cognitive-biases]], [[uncertainty]]; inversion.md → [[stoicism]], [[premeditatio-malorum]]; focus.md → [[deep-work]], [[saying-no]], [[time-blocking]].
**Suggested fix:** None required. 5 link `[[2026-08-*_*]]` trong frontmatter `original:` là by-design (trỏ raw), đã verify raw tồn tại trong `raw/posts/` và `raw/articles/`.

---

## Issue 7: Duplicate sub_tag trong frontmatter

**File:** wiki/concepts/compounding-effect.md
**Severity:** INFO
**Dimension:** Completeness (frontmatter hygiene)
**Issue:** `sub_tags: [opinion, opinion]` — tag "opinion" bị lặp 2 lần.
**Evidence:** Line 5: `sub_tags: [opinion, opinion]`
**Suggested fix:** Sửa thành `sub_tags: [opinion]`.

---

## Issue 8: Source paywalled — compile từ preview (đã disclose đúng)

**File:** wiki/sources/src_neuroscience-of-perfect-skill-acquisition.md
**Severity:** INFO
**Dimension:** Factual (transparency)
**Issue:** Bài gốc paywalled, nội dung compile từ free preview — phần thân bài (motor learning research chi tiết) chưa được capture. File đã disclose rõ trong Metadata (dòng ⚠️ Lưu ý) và 2 concept consuming nó (career-compounding.md, skill-acquisition-framework.md) cũng ghi chú "(paywalled, compile từ preview)" ở Sources. Xử lý đúng quy trình — không phải lỗi, chỉ ghi nhận để Julius biết nguồn này incomplete theo thiết kế.
**Evidence:** Line 20: `- **⚠️ Lưu ý:** Bài gốc PAYWALLED — chỉ có free preview. Nội dung dưới đây compile từ phần preview; phần thân bài (chi tiết motor learning research) chưa được capture.`
**Suggested fix:** None. Nếu sau này có quyền truy cập full bài, re-capture để bổ sung phần motor learning.

---

## Summary

| Severity | Count |
|---|---|
| ERROR | 1 (source link sai slug) |
| WARNING | 4 (2 typo file mới + 2 nhóm carry-over systemic) |
| INFO | 3 |

**Factual accuracy:** Pass — các claim kiểm chứng được đều đúng, citation chính xác.
**Completeness:** Pass — đủ sections, definitions 2+ câu, key ideas 5+ (trừ false positive của quick-scan, xem ghi chú đầu báo cáo).
**Coherence:** Pass — không mâu thuẫn, flow logic.
**Vietnamese:** 3 typo nhỏ (Ngườii ×2, bậce ×1) + kho carry-over.

**Action cần Fix Agent:**
1. Fix Issue 3 (ERROR) — ưu tiên cao, sửa link trong incentives-mental-model.md
2. Fix Issue 1, 2 — sed 2 dòng
3. Fix Issue 4, 5 — quét sed carry-over 18 + 14 file (backlog cũ, gộp 1 lần)
4. Issue 7 — 1 dòng frontmatter
