---
type: source
original: "[[2026-07-25_introducing-backsearch-gr-inc.md]]"
main_tag: ai
sub_tags: [tools, research]
topic: agent-backtesting
date_compiled: 2026-07-26
url: https://www.gr.inc/releases/introducing-backsearch
author: General Reasoning (GR.inc)
---

# Introducing BackSearch

## Metadata

- **Author:** General Reasoning (GR.inc)
- **Published:** 2026-07-24
- **Source:** gr.inc
- **URL:** https://www.gr.inc/releases/introducing-backsearch
- **Type:** article

## Summary

BackSearch là giải pháp cho phép backtest AI agents trên web archive đóng băng tại một thời điểm cụ thể. Thay vì sử dụng live search APIs có thể gây data leakage (kết quả được rank với hindsight knowledge), BackSearch cung cấp hai endpoints — search và fetch — đều yêu cầu `as_of` date parameter. Corpus được đóng băng, đảm bảo reproducibility: cùng một query với cùng `as_of` sẽ trả về kết quả giống hệt mãi mãi. Hiện tại hỗ trợ news domains từ December 2025 đến July 2026.

## Key points

- BackSearch giải quyết vấn đề "data leakage" trong agent evaluation khi dùng live search APIs
- Hai endpoints chính: `/v1/search` (tìm kiếm với as_of filter) và `/v1/fetch` (lấy content tại thời điểm cụ thể)
- `as_of` gates trên `crawl_date`, không phải article's published date — điều này đảm bảo không có content nào post-cutoff leaked vào
- Use cases chính: forecasting evaluation, quantitative finance backtesting, RL environment training
- Pricing: $10 per 1,000 searches, $2 per 1,000 fetches — pay-as-you-go, chỉ tính tiền successful requests
- Tích hợp với OpenReward environments qua built-in toolset `web_search` và `web_fetch`
- Hiện tại chỉ hỗ trợ news domains, dự định mở rộng coverage và backdated period

## Concepts referenced

- [[agent-backtesting]]
- [[frozen-corpus-search]]
- [[point-in-time-data]]

## Original excerpts

> "The one thing worth internalising: as_of gates on crawl_date, not on the article's own stated publish date."

> "The corpus never moves, so the same query with the same as_of returns the same results forever."
