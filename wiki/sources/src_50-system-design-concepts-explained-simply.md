---
type: source
original: "[[2026-09-17_50-system-design-concepts-explained-simply]]"
main_tag: tech
sub_tags: [tutorial, research]
topic: system-design-concepts-2026
date_compiled: 2026-09-18
url: https://designgurus.substack.com/p/50-system-design-concepts-explained
author: Design Gurus
---

# 50 System Design Concepts Explained Simply [2026 Edition]

## Metadata

- **Author:** Design Gurus
- **Published:** 2026-09-17
- **Source:** designgurus.substack.com
- **URL:** https://designgurus.substack.com/p/50-system-design-concepts-explained
- **Type:** Article

## Summary

Bài viết hướng dẫn 50 khái niệm system design, mỗi khái niệm được giải thích từ first principles — tại sao nó tồn tại, giải quyết vấn đề gì, và trade-off在哪里. 2026 edition bổ sung các khái niệm AI infrastructure (embeddings, RAG) vào vocabulary chuẩn của system design, phản ánh thực tế rằng các concept này đã trở nên phổ biến trong interviews và design reviews. Bài viết chia thành 5 nhóm: infrastructure, data/storage, distributed systems, messaging, và reliability/modern — mỗi nhóm đều giải thích từ base concepts đến advanced patterns.

## Key points

- **Scalability**: Property của entire system, không phải single component — bottleneck luôn nằm ở least scalable part
- **Vertical vs Horizontal scaling**: Vertical có ceiling + single point of failure; horizontal cần stateless servers
- **Load balancer**: Distributes requests + health checks — automatic rerouting làm fleet resilient
- **Latency vs Throughput**: Hai metric riêng biệt — system có thể nhanh cho individual request nhưng slow total capacity, và ngược lại
- **CDN**: Global cache servers giảm latency cho static content; trade-off là stale cache
- **API Gateway**: Single entry point cho cross-cutting concerns (auth, rate limiting, SSL, routing)
- **SQL vs NoSQL**: SQL cho structured relational data + transactions; NoSQL cho scale/flexibility — most common mistake là chọn vì "sounds modern"
- **ACID guarantees**: Atomicity, Consistency, Isolation, Durability — required cho financial transactions
- **Sharding**: Splits data across databases; hardest part là choosing shard key distribution
- **Replication + Replication Lag**: Leader-follower pattern; lag window cần deliberate handling
- **Cache patterns**: Cache-aside (default, lazy), Write-through (consistent but slow writes), Write-behind (fast but data loss risk)
- **CAP Theorem**: Consistency vs Availability during partition — real choice per data type
- **Strong vs Eventual Consistency**: Strong cho bank balances; eventual cho like counts
- **Consensus (Raft/Paxos)**: Majority agreement prevents split-brain; expensive due to network round trips
- **Idempotency + Idempotency Keys**: Safe retry mechanism — critical cho payment APIs
- **Saga Pattern**: Alternative to 2PC — compensating actions cho distributed transactions
- **Consistent Hashing + Virtual Nodes**: Minimizes reshuffling when nodes change
- **Event Sourcing**: State as sequence of events, not current values — enables time-travel queries
- **Message Queue + Pub/Sub**: Decouples producers from consumers; fan-out cho multiple subscribers
- **Backpressure**: Consumer signals producer to slow down — prevents unbounded queue growth
- **WebSocket vs SSE**: WebSocket cho bidirectional real-time; SSE cho one-way server push (simpler, built-in reconnection)
- **Circuit Breaker**: Three states (closed/open/half-open) prevents cascade failure
- **Rate Limiting + Token Bucket**: Enforces fair usage, prevents abuse
- **Load Shedding**: Partial availability > total failure — shed lower-priority work first
- **Bloom Filter**: Probabilistic membership — definitively says "not in set" but only "might be in set"
- **Embeddings**: Numerical representation of semantic meaning — foundation of modern AI-powered search
- **RAG**: Retrieval-Augmented Generation — two-phase pipeline (ingestion + query) grounding LLM in external knowledge

## Concepts referenced

- [[rag-retrieval-augmented-generation]]
- [[system-map]]
- [[systems-thinking]]
- [[design-systems]]
