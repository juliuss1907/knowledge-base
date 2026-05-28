---
type: raw
source_type: article
source_url: https://ryanswright.substack.com/p/a-setup-is-not-an-edge
date_ingested: 2026-05-28
tags: [economic, opinion]
status: unprocessed
---

# A setup is not an edge

**Author:** Ryan Wright  
**Source:** Substack — Ryan Wright  
**Date:** 2026-05-01  
**URL:** https://ryanswright.substack.com/p/a-setup-is-not-an-edge

---

## Summary

Most retail traders are taught to memorize patterns. Professional trading starts when you realize the setup is only a trigger inside a state.

## Core Argument

Retail traders bị dạy cách memorize patterns, nhưng professional trading bắt đầu khi nhận ra **setup chỉ là trigger bên trong một state** — không phải là edge hoàn chỉnh.

## Key Points

### 1. Ảo tưởng retail vs. Công việc thực sự

**Ảo tưởng (The Fantasy):**
- Trading có thể học như một hệ thống — tìm setup, thuộc rule, chờ tín hiệu, đặt stop/take profit, lặp lại mỗi sáng → có thu nhập thứ hai thoát khỏi 9-to-5.
- YouTube tràn ngập "chiến lược duy nhất bạn cần", "setup in tiền", "chỉ báo không thể thua" — tất cả đều bán cùng một lời hứa: Học cái này rồi in tiền.

**Thực tế (The Reality):**
- Trading là trò chơi ra quyết định lặp lại dưới sự bất định (repeated decision game under uncertainty).
- Một quyết định tốt có thể thua lỗ. Một quyết định tệ có thể có lời. PnL không phải là điểm số sạch.

Tác giả phân biệt:
- **Kẻ lừa đảo** có chủ ý
- **Người sống sót** — từng có lợi nhuận trong một môi trường nhất định, lẫn lộn kết quả với sự hiểu biết, rồi bắt đầu bán "hệ thống" của mình như chân lý vĩnh cửu.

> "A system is easier to market than judgment. A setup is easier to sell than state-conditioned decision-making."

Vấn đề không phải là technical analysis — mà là **giả vờ technical analysis đã ra quyết định thay bạn**. Một breakout có thể có ý nghĩa, nhưng nó không tự quyết định bạn có nên trade hay không.

### 2. Trading là một trò chơi quyết định

**Cốt lõi: Policy (π)** — quy tắc hành động.

```
π(s_t) = a_t
```

Với trạng thái này, chọn hành động này.

| Policy | Mô tả |
|--------|-------|
| π* (Pi-Star) | Policy tối ưu lý thuyết — chọn hành động có xác suất tốt nhất từ mỗi trạng thái. Vẫn có thể thua lỗ (vì không biết tương lai). |
| π̂ (Pi-Hat) | Policy thực tế bạn đang có — xấp xỉ tốt nhất hiện tại, xây từ bằng chứng, kinh nghiệm, mô hình, sai lầm và sẹo. |

**Vòng lặp quyết định:**
```
s_t → a_t → r(t+1) → s(t+1)
```

- **State (s_t):** Bạn đang ở trạng thái nào?
- **Action (a_t):** Bạn có thể làm gì từ đây?
- **Reward (r(t+1)):** Điều gì xảy ra sau khi hành động?
- **Next state (s(t+1)):** Hành động này đã làm gì với tài khoản, exposure, risk budget, cảm xúc và cơ hội tương lai?

**Điểm mấu chốt:** Feedback trong trading KHÔNG sạch — r(t+1) ≠ chất lượng quyết định. Một trade thua lỗ nhưng tuân theo một policy tốt trong môi trường nhiễu không tự động là sai lầm.

### 3. State (Trạng thái) — Cao hơn nhiều chiều so với bạn nghĩ

> "A trading state is not one variable. It is a bundle of conditions."

**State không chỉ là price.** Nó bao gồm:
- Volatility, liquidity, trend, time of day
- Catalyst structure, correlations, order flow
- Current positions, drawdown, risk limits, margin usage, spread, regime
- **Và bạn** — giấc ngủ 4 tiếng, đang âm trong năm, còn bực vì trade trước — đó cũng là một phần của state.

> "Same chart, different operator, different distribution."

**Sai lầm retail:** Thu gọn state thành một thứ visible duy nhất: chart pattern.

### 4. Action space — Lớn hơn "Mua/Bán"

**Action không chỉ là buy hay sell:**
- Enter, exit, hold, reduce, add, hedge, wait, scratch
- Lower size, change markets, stop trading
- Hoặc đơn giản: **không làm gì** vì state không đáng để mạo hiểm vốn

Một trader có thể đoán đúng hướng nhưng vẫn sai vì: sai size, sai vị trí, sai stop, sai time horizon, sai liquidity, sai risk profile.

### 5. Edge sống ở đâu?

> "Expected value lives in the state-action pair."

```
Q(s, a) = E[R | s, a]
```

**Edge KHÔNG sống trong pattern.** Nó sống trong cặp **trạng thái-hành động**.

Một breakout có thể là:
- Continuation trong state này
- Exhaustion trong state khác
- Noise trong state thứ ba
- Món quà cho người đã long sẵn trong state thứ tư

> "Buy the breakout" isn't good or bad by itself. **Buy WHICH breakout?**

Tác giả chỉ ra: **Outcome worship** là cái bẫy — học ngược bằng cách nhìn kết quả rồi kết luận setup "có hiệu quả" hay không. Một trade xanh không có nghĩa quyết định đúng.

### 6. Setup: Triệu chứng, không phải chẩn đoán

> "A setup is closer to a symptom than a diagnosis. A fever is real... but no serious doctor treats the number on the thermometer as the whole diagnosis."

**Chuỗi logic:**
```
setup ⊂ s_t ⇒ P(R|s_t, a_t) ⇒ E[R|s_t, a_t]
```

- Setup là một phần của state
- State quyết định distribution
- Distribution quyết định expectancy

**Hai câu đều dùng chữ "breakout" — nhưng trade lại khác hoàn toàn:**

> "This is a breakout after compression, with expanding volatility, strong participation... buying the first pullback may have positive expectancy."

> "This is a breakout after exhaustion, into poor liquidity, with no room left in the payoff... **the correct action is no trade.**"

### 7. Tại sao Market KHÔNG giống Roulette

| Trò chơi | Đặc điểm |
|----------|---------|
| **Roulette** | Edge cố định. Xác suất không đổi. Casino luôn thắng về dài hạn. |
| **Blackjack** | Policy bắt đầu có ảnh hưởng. Đếm bài tốt có thể tạo lợi thế. |
| **Poker** | Thông tin bất hoàn hảo, đối thủ thích nghi, ẩn state — gần với trading nhất. |
| **Trading** | **Edge động (dynamic)** — không cố định theo thời gian. Thay đổi theo regime, liquidity, positioning, volatility, participant behavior. |

> "The same action can have positive expected value in one state and negative expected value in another. The same setup can work beautifully for months, then stop working right when the trader has the most confidence in it."

**Hệ quả:** Một trader không thể có π* (policy hoàn hảo). Công việc là cải thiện π̂ (policy hiện tại) — nhưng ngay cả khi cải thiện, vẫn chưa chắc có positive EV.

> "Better than before isn't the same as good."

### 8. Kết luận & Link Part 2

**Chẩn đoán của Ryan Wright:**
1. Setups không phải là edges
2. Edges phụ thuộc vào state
3. State thay đổi
4. Feedback thì nhiễu
5. Quyết định tốt vẫn có thể thua
6. Pattern tồn tại ngay cả khi điều kiện làm nó hiệu quả đã biến mất

**Đó là cách trader bị mắc bẫy.** Họ cứ click vào chart pattern quen thuộc trong khi distribution bên dưới nó đã thay đổi.

**Câu hỏi lớn cho Part 2:** Nếu system không phải là công việc thực sự, thì cái gì thay thế nó? Làm sao để size? Khi nào ngồi ngoài? Discretion thực sự nghĩa là gì? Và làm sao để thị trường không dạy bạn bài học sai lầm trong lúc đang trả tiền cho bạn?

## Original Excerpts

> "If you're looking for the system that will make you consistently profitable, you're operating inside the retail fantasy of trading."

> "The fantasy is that trading can be learned as a system: find the setup, memorize the rules, wait for the signal, place the stop here, take profit there, then repeat the process every morning until you've built a second income and a way out of your 9-to-5."

> "That is not how the job works."

> "The problem isn't technical analysis. The problem is pretending technical analysis has already made the decision."

> "A chart pattern with an entry rule doesn't tell you what state the market is in, whether the trade is worth taking, how much risk it deserves, what liquidity it requires, what costs it has to overcome, what account condition it fits or when the exact same pattern should be left alone."

> "Without those answers, you don't have a strategy. You have a thing to click when the chart looks familiar."

> "Trading isn't a puzzle that resolves once you collect the final piece. It's a repeated decision game under uncertainty."

> "The real job is less marketable than the fantasy."

> "Stop asking whether the setup appeared. Start asking whether the action made sense from the state."

> "Professional trading isn't the search for a magic pattern. It's the process of making better state-conditioned decisions under uncertainty, with risk, sizing, liquidity, cost, drawdown, objective, and future opportunity all included in the decision."

---

*Part 1 of a two-part series on what professional trading actually is.*
