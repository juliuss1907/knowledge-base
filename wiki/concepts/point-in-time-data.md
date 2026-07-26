---
type: concept
status: draft
main_tag: system
sub_tags: [research, tools]
topic: agent-backtesting
sources:
  - "[[src_introducing-backsearch-gr-inc.md]]"
last_updated: 2026-07-26
---

# Point-in-Time Data

## Definition

Point-in-Time Data là data representation cho thấy state của information tại một thờ điểm cụ thể trong quá khứ, không bị contaminate bởi subsequent updates hoặc revisions. Trong AI/ML, điều này critical cho việc đánh giá models trên historical scenarios mà không gặp phải look-ahead bias.

## Key ideas

- **Temporal accuracy**: Data reflects exactly what was known at the specified time
- **No retroactive changes**: Historical records không bị overwrite bởi subsequent corrections
- **As-of semantics**: Queries trả về view của data tại một thờ điểm cụ thể
- **Audit trail**: Có thể trace lại data evolution qua thờ gian
- **Elimination of hindsight bias**: Prevents using information that wasn't available at decision time

## Contrast with live systems

| Point-in-Time | Live Systems |
|---------------|--------------|
| Fixed snapshot | Continuously updated |
| Reproducible | Results change over time |
| Historical accuracy | Current accuracy |
| Prevents data leakage | Risk of hindsight contamination |

## Use cases

- **Financial backtesting**: Simulating trades với information available at that time
- **Agent evaluation**: Testing AI agents on historical scenarios
- **Regulatory compliance**: Proving decision-making process was appropriate given available info
- **Academic research**: Reproducible studies với fixed dataset

## Related concepts

- [[frozen-corpus-search]]
- [[agent-backtesting]]
- [[temporal-versioning]]
- [[bimodal-data]]

## Sources

- [[src_introducing-backsearch-gr-inc.md]] — BackSearch cung cấp point-in-time web access cho agent evaluation

## Notes

