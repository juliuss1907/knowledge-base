---
type: concept
status: draft
main_tag: tech
sub_tags: [tutorial, research]
topic: system-design-concepts-2026
sources:
  - "[[src_50-system-design-concepts-explained-simply]]"
last_updated: 2026-09-18
---

# System Design Concepts 2026

## Definition

Bộ 50 khái niệm system design từ first principles, bao gồm cả traditional infrastructure và các khái niệm AI mới được thêm vào năm 2026. Phản ánh thực tế rằng embeddings và RAG đã trở thành vocabulary chuẩn trong system design interviews và reviews.

## Key ideas

- **Scalability là system-level property**: Không nằm ở single component — bottleneck luôn là least scalable part, mọi layers đều cần scale được
- **Vertical vs Horizontal**: Vertical có ceiling + SPOF; horizontal cần stateless + load balancer — redundancy thay vì power
- **Latency vs Throughput**: Hai metric riêng biệt — system nhanh individual nhưng slow capacity, và ngược lại, không tự động cho nhau
- **Data layer choices**: SQL cho transactions + relational; NoSQL cho scale/flexibility; shard key selection là hardest part của sharding
- **Cache patterns**: Cache-aside (lazy, default, graceful degradation); Write-through (consistent but slow); Write-behind (fast but data loss risk)
- **CAP Theorem thực tế**: Partition tolerance mandatory; real choice là consistency vs availability per data type — financial records ≠ social counts
- **Consensus cost**: Raft/Paxos cần multiple network round trips — expensive, used only where agreement truly required
- **Idempotency**: Critical cho distributed systems — request có thể lost, response lost, caller retry — idempotent operations safe to retry
- **Messaging decoupling**: Message queue absorbs traffic spikes; Pub/sub fan-out cho multiple subscribers; backpressure prevents unbounded growth
- **Real-time protocols**: WebSocket cho bidirectional; SSE cho one-way push — SSE simpler, built-in reconnection, sufficient cho most cases
- **Resilience patterns**: Circuit breaker (prevent cascade failure); Rate limiting (fair usage); Load shedding (partial availability > total failure)
- **Probabilistic structures**: Bloom filter — definitively says "not in set" but probabilistic "might be" — useful cho avoiding expensive lookups
- **AI infra vocabulary**: Embeddings (semantic vectors) và RAG (two-phase retrieval + generation) — now standard system design concepts, not just ML topics
- **Event sourcing**: State as event sequence, not current values — enables time-travel queries, complete audit trail, easy derived data rebuild

## Related concepts

- [[rag-retrieval-augmented-generation]]
- [[system-map]]
- [[systems-thinking]]
- [[design-systems]]

## Sources

- "[[src_50-system-design-concepts-explained-simply]]"
