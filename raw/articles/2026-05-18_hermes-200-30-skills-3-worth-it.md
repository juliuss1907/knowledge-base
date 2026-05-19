---
type: raw
source_type: article
source_url: https://defi0xjeff.substack.com/p/hermes-200-and-30-skills-later-here
date_ingested: 2026-05-18
status: processed
compiled_at: 2026-05-19
compiled_to: [[wiki/sources/src_hermes-200-30-skills-3-worth-it]]
---

# Hermes, $200 and 30 Skills Later — Here Are the 3 Skills That're Worth It

**Tác giả:** defi0xjeff  
**Nguồn:** Substack — defi0xjeff  
**Ngày đăng:** 2026-05-18

---

## Tóm tắt

Sau $200 và 30 skills, tác giả chia sẻ 3 skills đáng giá nhất từ Hermes — cùng những bài học đắt giá về token management và tránh lãng phí.

## Self-Learning + Self-Remembering

Hermes tự động:
- Học về user: preference, workflows, cách làm việc
- Tổng hợp và tạo skills proactively (không cần user làm gì)
- Memory config + external memory provider giúp retain context, search knowledge base

**Cảnh báo:** Số lượng skills và cron jobs có thể expand nhanh → mess khi change config/setup.

## Bài học đắt giá ($150-200 wasted)

Tác giả tốn $150-200 tokens trong 2 tuần để debug, test skills, đảm bảo setup đúng.

## 3 Skills Đáng Giá

### Skill 1: X Account Tracking (Cron Job)

**Setup:**
- Theo dõi X accounts cung cấp insights về macro, geopolitics, tech, AI
- X API (bảo mật hơn Bird CLI)

**Bài học đắt giá:**
- **Bird CLI mistake:** Có permission write → Hermes hallucinate, post random things
- **Fix:** Delete Bird CLI, dùng official X API ($0.5/ngày nhưng yên tâm hơn)

**Output:** Daily morning report (ví dụ: Kobeissi cho geopolitics & macro real-time)

### Skill 2: X Bookmark Prioritization

**Vấn đề:** 10-20 bookmarks/ngày nhưng chỉ revisit 1-2, còn lại stale.

**Solution:**
- Hermes nhìn vào bookmarks
- Pick 15 và rank theo priority (preference/investments/interests)
- Summarize và propose next steps

**Blocker:** X API v2 không đọc được X articles → dùng Browser Harness

**Workflow hiện tại:**
1. X API → fetch bookmarks list (tweet text + linked URLs)
2. Browser → navigate to article URL → extract full text
3. LLM → summarize mỗi article
4. Output → daily report + store insights in wiki

### Skill 3: Reflect (External Memory)

**"Reflect":** Hermes synthesize thông tin quá khứ, kết nối relationships, detect patterns, cung cấp actionable analysis.

**External Memory Provider:** Hindsight (#1 recall accuracy, especially long-horizon, multi-session, large-scale)

**Output:** Top 5 Daily insights — highlight signals và giải thích tại sao quan trọng cho user.

## Tips & Tools

| Tool | Mô tả |
|------|-------|
| **last30dayskill** | Lấy 30 ngày activity trên X, Tiktok, IG, Reddit (No API needed) |
| **Coingecko & Defillama** | Bread-and-butter real-time market data |
| **delegate task** | Long-running tasks |
| **Opencode Go** | Best subscription để bắt đầu — $5/tháng đầu, inference credits đủ setup |

**Cảnh báo:**
- **Đừng link Hindsight to OpenRouter + Claude Sonnet 4.6** → Burn $50+ tokens trong 1 ngày
- **Bird CLI:** Chỉ enable read function, remove write function
- **Browser Harness:** Practice extreme caution — dùng isolated/fresh browser, không share sensitive credentials

## Next Workflows

**Pre-call context:**
- Plug vào social media, past transcripts & notes
- Inform latest status 30-60 phút trước call

**Prediction markets:**
- Low risk, consistently compounding strategies
- Better R/R cho DeFi lending positions

## Token Management

**Thách thức:** Balance productivity boost + learning vs inference cost + time fixing bugs.

**Quan điểm:**
- Không chắc GPT5.4 hay Opus 4.7 worth it với giá hiện tại
- Open models work well, subscriptions tốt
- Claude expensive nhưng great cho one-off tasks → downgrade to $20 package

---

## Bài viết liên quan

- 3 Things I learnt after 3 weeks of using Hermes as a personal analyst
- Inference is the New Oil - The Economics of AI
- Machine-to-Vendors Economy 2030
- Bittensor Subnets vs Virtuals Agents
