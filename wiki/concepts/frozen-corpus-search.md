---
type: concept
status: draft
main_tag: system
sub_tags: [tools, research]
topic: agent-backtesting
sources:
  - "[[src_introducing-backsearch-gr-inc.md]]"
last_updated: 2026-07-26
---

# Frozen Corpus Search

## Definition

Frozen Corpus Search là kiến trúc search system nơi underlying document collection được đóng băng tại một thời điểm cụ thể, đảm bảo reproducibility và consistency của search results. Mỗi query kết hợp với một temporal cutoff trả về cùng một result set vĩnh viễn, không bị ảnh hưởng bởi new crawls hoặc index updates.

## Key ideas

- **Immutability**: Corpus không thay đổi sau khi được đóng băng — không có new documents, không có updates
- **Temporal gating**: Mọi queries đều yêu cầu explicit as_of date parameter
- **Crawl-date filtering**: Documents được filtered dựa trên crawl timestamp, không phải self-reported publish date
- **Reproducible results**: Cùng query + as_of = cùng results, forever
- **No hindsight leakage**: Impossible cho "future" information leak vào historical queries
- **Archive-based retrieval**: Nội dung được lấy từ historical snapshots, không phải live web

## Applications

- **Agent evaluation**: Testing forecasting agents trên historical data
- **Academic research**: Reproducible information retrieval studies
- **Legal discovery**: Point-in-time document collection
- **Compliance auditing**: Proving what information was available when

## Technical implementation

- Index partitioned by crawl_date
- Fetch endpoint retrieves from archived snapshots
- 404 returned nếu không có capture on or before cutoff date

## Related concepts

- [[point-in-time-data]]
- [[agent-backtesting]]
- [[web-archiving]]
- [[temporal-databases]]

## Sources

- [[src_introducing-backsearch-gr-inc.md]] — BackSearch implements frozen corpus cho news domains December 2025 - July 2026

## Notes

