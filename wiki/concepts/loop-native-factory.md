---
type: concept
status: draft
main_tag: ai
sub_tags: [vibecode, system]
topic: ai-engineering
sources:
  - "[[src_loop-native-factory]]"
  - "[[src_the-seed-and-the-machine]]"
last_updated: 2026-06-17
---

# Loop Native Factory

## Definition

Mô hình nhà máy sản xuất phần mềm mới nơi đơn vị sản xuất không còn là developer viết code mà là "loop" - một model chạy trong harness với tools, context, policy cho đến khi verifier kết thúc công việc.

## Key ideas

- Lịch sử: 1970s software factory (Hitachi) chuẩn hóa process → 2001 Agile → 2009 DevOps → 2016 SRE → 2019 Platform Engineering → 2026 Loop Native
- Loop = model + harness + tools + context + policy + verifier
- 3 planes: inner loop (IDE, human-agent collab), outer loop (CI/CD, multi-agent review), governance plane (policy, evals, telemetry)
- 3 thay đổi khi loop thành đơn vị nguyên tử: (1) production không deterministic, (2) marginal cost of generation collapse, (3) scaffolding bị model absorb mỗi release
- Cognition pattern: single-threaded writes, multi-agent intelligence around writer
- Claude Code: 1.6% AI decision logic, 98.4% operational infrastructure
- Bottleneck mới: không phải viết code mà là alignment - biết code nào cần viết và tại sao
- 5 layers of alignment: ontological, teleological, behavioral, temporal, reflexive

## Related concepts

- [[agent-harness]]
- [[alignment-engineering]]
- [[three-plane-architecture]]
- [[seed-vs-machine-architecture]]

## Sources

- [[src_loop-native-factory]]
- [[src_the-seed-and-the-machine]]

## Notes
