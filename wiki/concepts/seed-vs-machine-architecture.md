---
type: concept
status: draft
main_tag: ai
sub_tags: [system, vibecode]
topic: ai-architecture
sources:
  - "[[src_the-seed-and-the-machine]]"
last_updated: 2026-06-17
---

# Seed vs Machine Architecture

## Definition

Phân biệt hai cách xây dựng AI system: Machine (assemble từ components hoàn thành - obsolete khi ship) vs Seed (compact core + growth rules - compound qua thời gian). 95% công ty deploy AI không có ROI vì assemble machines, 5% plant seeds.

## Key ideas

- **Machine**: assembled from finished parts, complete structure, degrades as world drifts from baked-in assumptions
- **Seed**: compact core + growth rules (introspect-generate-verify), environment finishes it, same seed in different places → different trees
- 3 layers chuyển dịch: software (integration code → model writes), data (schema → semantic graph), org (conway's law reverse)
- **Swap test**: nếu replace model tomorrow, phần nào giữ nguyên? Seed giữ growth rules, semantic layer, verifier. Machine giữ almost nothing
- Seed có 3 phần: core (ổn định, slow change), growth rules (heart of seed), environment (soil - data estate + domain meaning)
- Semantic layer là moat thực sự - model và database rented, không phải asset
- Ora example: knowledge of no particular database, reads schema, builds map, indexes real values, correction loop
- Cost của loop: phải quên để tiếp tục grow - creative destruction của memory

## Related concepts

- [[loop-native-factory]]
- [[semantic-layer-moat]]
- [[swap-test]]
- [[ora-system]]

## Sources

- [[src_the-seed-and-the-machine]]

## Notes
