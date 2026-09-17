---
type: article
title: "50 System Design Concepts Explained Simply [2026 Edition]"
url: https://designgurus.substack.com/p/50-system-design-concepts-explained
author: Design Gurus
date_ingested: 2026-09-17
status: unprocessed
source: designgurus.substack.com
---

Source: Web Fetch
---
https://substackcdn.com/image/fetch/$s_!k35M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31463d2a-93f5-4e57-8e6c-c85481faa0bc_1536x1024.png

- Why simple explanations matter
- Core infrastructure concepts
- Data and storage concepts
- Distributed systems concepts
- Reliability and modern concepts
There is a specific kind of embarrassment that hits engineers in design reviews and interviews.
Someone mentions a concept they recognize but cannot quite define, and rather than asking, they nod along and hope the conversation moves on before they are asked to explain it. Every engineer has been there.
The word is familiar but the understanding underneath it is thin.
System design has more of these moments than almost any other technical domain.
The vocabulary is rich, the concepts are abstract, and most of them are rarely explained from scratch because everyone in the room is assumed to already know them.
The result is a field full of engineers who use words like idempotency and backpressure and consistent hashing correctly in sentences but would struggle to explain from first principles why these things exist and what problem they solve.
This guide covers fifty system design concepts, each explained simply enough to actually understand rather than just recognize.
Not dictionary definitions. Real explanations that tell you what the concept is, why it exists, what problem it solves, and where the trade-off lives.
The kind of explanation that lets you use the concept correctly in your next design review rather than just identifying it when someone else uses it.
The 2026 edition covers the foundational concepts that have been important for years alongside the newer ones, specifically around AI systems and modern infrastructure, that have become part of standard system design vocabulary in the last few years.
Scalability is the ability of a system to handle growth without breaking. Growth can mean more users, more data, more requests, or more geographic reach.
A scalable system expands its capacity to meet that growth while keeping performance acceptable.
The important thing to understand about scalability is that it is not a property of any single component. It is a property of the entire system, and the system is only as scalable as its least scalable part. You can scale your application servers to handle ten times the traffic and the bottleneck simply moves to the database.
True scalability requires every layer to be able to grow.
Vertical scaling means making one machine more powerful. When the system needs more capacity, you upgrade the server with more CPU, more memory, or faster storage. The application does not change and the architecture does not change. You just get a bigger machine.
Vertical scaling is simple and works well until it does not.
The problem is that single machines have a maximum size, and a single machine is a single point of failure.
There is no redundancy. When it goes down, everything goes down with it.
https://substackcdn.com/image/fetch/$s_!oL5G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe4efd77-a416-4bc2-957a-704e29a7ec28_1200x750.jpeg
Horizontal scaling means adding more machines instead of making one bigger.
When the system needs more capacity, you run more copies of it across more servers. No ceiling, and the failure of one machine reduces capacity slightly rather than causing a total outage.
Horizontal scaling requires the servers to be stateless, meaning they hold no information between requests that is specific to a particular user.
If a server holds state, requests must return to the same server, which breaks the flexibility that makes horizontal scaling work.
A load balancer sits in front of a group of servers and distributes incoming requests across them. Every request goes to the load balancer first.
https://substackcdn.com/image/fetch/$s_!wKsb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd3e0243-a537-4d7e-95e2-56caa1ff0d98_1448x1086.png
The balancer picks a server, forwards the request, and returns the response.
From the outside, it looks like one server. On the inside, many servers are sharing the work.
A load balancer also checks the health of servers behind it and stops sending traffic to ones that are failing. This automatic detection and rerouting is what makes a fleet of servers resilient to individual failures.
Latency is the time between sending a request and receiving a response. It is the delay a single user experiences. Low latency feels instant. High latency feels sluggish.
Latency has multiple sources that stack together: the time for the request to travel over the network, the time the server spends processing it, and the time the database spends answering the query. Reducing latency means identifying which of these dominates and optimizing that specific part.
https://substackcdn.com/image/fetch/$s_!2Yir!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F66c74354-8651-46dc-bd81-b4ac4f4daeb2_1200x750.jpeg
Throughput is how much work a system completes in a given period, usually measured in requests per second. It describes the system’s total capacity for work rather than the speed of any individual request.
Latency and throughput are related but different.
A system can be fast for individual requests but slow in total if it can only handle one at a time.
A system can be slow for individual requests but high throughput if it processes many in parallel. Designing for one does not automatically give you the other.
A CDN is a network of servers distributed globally that cache copies of static content and serve them to users from the nearest location. Instead of every user fetching an image from a server on a different continent, they fetch it from a server in their city.
https://substackcdn.com/image/fetch/$s_!1_54!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F19113e00-60dc-4efb-8a0a-3b52e1f9191c_1536x1024.png
CDNs reduce latency for content that does not change per user, such as images, videos, and scripts, and they offload an enormous amount of traffic from the origin server.
The trade-off is that cached content can become stale if it changes and the cache is not invalidated quickly.
DNS translates human-readable domain names like example.com into IP addresses that computers use to find each other. It is the internet’s directory service.
DNS matters in system design because it can be used for traffic routing, directing users to different servers based on their geographic location or on the health of the servers.
DNS-based routing is simple but slow to respond to changes because DNS records are cached by clients and intermediate resolvers.
An API gateway is a single entry point that sits in front of multiple backend services and handles cross-cutting concerns like authentication, rate limiting, SSL termination, and request routing in one place.
https://substackcdn.com/image/fetch/$s_!RRcr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F78296589-b3c6-451b-99ac-41c5d5585d27_1448x1086.png
Without a gateway, every service must implement authentication and rate limiting independently.
With a gateway, these concerns are centralized and every service behind it gets them for free.
The trade-off is that the gateway becomes a critical component that must be highly available and must not become a bottleneck.
A reverse proxy receives requests on behalf of one or more servers and forwards them. It sits between the client and the server, and the client does not know or need to know which actual server is handling the request.
Reverse proxies handle caching, compression, SSL, and load balancing. They are closely related to load balancers but broader in purpose.
https://substackcdn.com/image/fetch/$s_!Acsj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85c249eb-3561-48e7-9348-f5d8a53308b5_1536x880.png
A load balancer is a type of reverse proxy specialized for traffic distribution, while a reverse proxy can do many other things as well.
A database is a system for storing, organizing, and retrieving data that persists beyond the life of a single request or process.
Without a database, any data created during a request disappears when the request ends.
Databases come in many types optimized for different data shapes and access patterns.
The choice of database is one of the most consequential decisions in a system design because it is hard to change later and everything else in the system depends on it.
A SQL database, also called a relational database, stores data in tables with rows and columns and enforces relationships between them using foreign keys. It uses a structured query language for all data operations and provides ACID guarantees: atomicity, consistency, isolation, and durability.
https://substackcdn.com/image/fetch/$s_!8WO9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe73a416a-f004-4828-a86d-2a83bb7b5554_1536x1024.png
SQL databases are the right choice when data is structured and relational, when the system needs transactions, and when query patterns are varied or not fully known in advance.
The main limitation is that scaling writes beyond a single server requires sharding, which adds significant complexity.
NoSQL is a broad category of databases that do not use the relational table model. They include key-value stores, document stores, wide-column stores, and graph databases. Each trades the query flexibility and consistency guarantees of SQL for specific advantages in scale, flexibility, or access pattern optimization.
https://substackcdn.com/image/fetch/$s_!J2-s!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15bf78e0-beee-4c61-ad37-337bbc5f2b61_1448x1086.png
The most common mistake with NoSQL is choosing it because it sounds modern rather than because the data model actually fits. The access patterns determine the right choice, not the technology trend.
ACID stands for Atomicity, Consistency, Isolation, and Durability. It describes the guarantees that a database transaction provides.
Atomicity means all operations in a transaction succeed or all fail together.
Consistency means the database moves from one valid state to another valid state.
Isolation means concurrent transactions do not interfere with each other.
Durability means committed data survives a system crash.
These guarantees are what make relational databases the right choice for financial transactions and other operations where partial completion is worse than total failure.
An index is a separate data structure that the database maintains to make certain queries faster.
Without an index, finding rows that match a condition requires scanning every row in the table.
With an index, the database can jump directly to the matching rows.
The trade-off is that indexes speed up reads but slow down writes. Every insert, update, or delete must update all indexes on the affected table.
A table with ten indexes pays ten times the write cost for index maintenance.
Good indexing means indexing the queries you actually run, not every column.
Sharding splits data across multiple databases so each one holds only a portion.
A shard key determines which database stores each piece of data.
Sharding scales both write throughput and storage capacity because the load is divided across many machines.
https://substackcdn.com/image/fetch/$s_!0NfW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ba0ea2c-f287-4dd4-b49c-ff772999fcdc_1448x1086.png
The hardest part of sharding is choosing the shard key.
A good shard key distributes data and traffic evenly.
A poor one creates hot partitions where one shard receives most of the traffic while others sit idle.
Cross-shard queries are expensive because they must be executed on multiple shards and the results assembled.
Replication keeps copies of data on multiple machines.
The most common pattern is leader-follower, where one primary node handles all writes and replica nodes hold copies that serve reads. This scales read capacity and provides redundancy.
https://substackcdn.com/image/fetch/$s_!KDb1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd86a955-bfd6-44a6-9bd2-e7739a5d98fc_1536x1024.png
The important subtlety is replication lag, the delay between a write on the primary and its appearance on the replicas.
During this window, reads from replicas return stale data. This is usually acceptable but must be handled deliberately when a read must reflect a recent write.
A cache is a fast storage layer that holds copies of frequently accessed data to avoid repeated slow operations.
The most common use is an in-memory cache in front of a database, serving read requests from memory and only going to the database on a miss.
The trade-off is staleness.
The cache holds a copy that can become outdated when the source data changes. Designing the cache means deciding how stale data can be and for how long, which determines the expiry policy and invalidation strategy.
Cache-aside is the most common caching pattern. The application checks the cache first.
On a hit, it returns the cached value.
On a miss, it reads from the database, stores the result in the cache, and returns it. The cache is populated lazily, only as data is requested.
https://substackcdn.com/image/fetch/$s_!OfIo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44c83d70-123c-4e46-b4e5-73bb4b5cbcd3_1536x1024.png
Cache-aside is the right default because it is simple, it naturally populates the cache with the data that is actually accessed, and it degrades gracefully when the cache is unavailable since the application falls back to the database.
Write-through is a caching pattern where every write goes to the cache and the database simultaneously.
The cache is always consistent with the database because every update hits both.
The trade-off is write latency. Every write must complete in both the cache and the database before returning to the caller.
https://substackcdn.com/image/fetch/$s_!wX_k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c9aa4c0-dbee-45ee-9733-578b70033e6f_1448x698.png
Write-through makes sense when read-after-write consistency is critical and the write latency cost is acceptable.
Write-behind is a caching pattern where writes go to the cache immediately and are flushed to the database asynchronously.
Writes feel fast because they complete as soon as the cache acknowledges them.
The risk is data loss.
https://substackcdn.com/image/fetch/$s_!6PGg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7be96ff8-f029-4da3-a43c-a457dfe6fd1a_1536x653.png
If the cache fails before it flushes to the database, the writes are lost.
Write-behind is appropriate for high-write-volume workloads where some data loss is acceptable, like analytics event ingestion.
Consistent hashing is a technique for distributing data across nodes that minimizes reshuffling when nodes are added or removed.
In a standard hash ring, each node is responsible for a range of hash values.
When a node is added or removed, only the keys in the adjacent range need to move.
Without consistent hashing, adding one node to a ten-node cluster might require moving ninety percent of the data.
With consistent hashing, adding the same node requires moving roughly ten percent. This makes it the standard technique for distributed caches and databases where the cluster size changes over time.
Object storage is a system for storing large unstructured files as objects identified by a key. It is infinitely scalable, cheap per gigabyte, and highly durable.
Amazon S3 is the most common example.
Object storage is the right place for images, videos, documents, and backups. It is not a database and should not be used like one. It does not support transactions, complex queries, or low-latency random access to small portions of a file.
Data partitioning is the general practice of dividing data into separate parts for storage or processing.
Sharding is one form of partitioning.
Time-based partitioning, where data for each month goes into a separate table, is another.
https://substackcdn.com/image/fetch/$s_!lPAe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e804db5-bd21-4df1-8ba4-576c0b5b3439_1536x1024.png
Partitioning is done to improve query performance by scanning less data, to manage data lifecycle by archiving or deleting old partitions, and to distribute load across machines.
The partition key determines which partition holds each piece of data and should be chosen based on the dominant query pattern.
Event sourcing stores the state of a system not as the current values but as the sequence of events that produced those values.
Instead of storing that an account balance is one hundred dollars, the system stores all the transactions that led to that balance: deposit two hundred, withdraw fifty, withdraw fifty.
The current state is derived by replaying the events. This provides a complete audit trail, makes it easy to rebuild derived data models, and enables time-travel queries that ask what the state was at any point in the past.
The trade-off is that querying current state requires replaying potentially many events unless a snapshot is maintained.
A distributed system is a system where components run on multiple machines that communicate over a network to achieve a common goal.
Distributed systems are more capable than single-machine systems but introduce a class of problems that do not exist on a single machine: network failures, partial failures, and the challenge of keeping multiple copies of data consistent.
Understanding distributed systems means accepting that the network is unreliable, clocks on different machines disagree, and any component can fail at any time. Designing for these realities is what distributed systems engineering is about.
The CAP theorem states that a distributed system can guarantee at most two of three properties: consistency, availability, and partition tolerance.
https://substackcdn.com/image/fetch/$s_!W9Xg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69d8b304-cd09-4c39-9e78-b5510e4af4d4_1200x750.jpeg
Since network partitions are unavoidable in any real distributed system, partition tolerance is mandatory, which means the real choice during a partition is between consistency and availability.
A system that chooses consistency will reject requests rather than serve stale data during a partition.
A system that chooses availability will continue serving requests but may return stale data. Most systems make this choice per data type: financial records favor consistency, social media counts favor availability.
Strong consistency means every read reflects the most recent write.
No matter which node in a distributed system handles a read, it sees the latest data. Achieving this requires coordination between nodes on every write, which adds latency.
Strong consistency is the right choice when serving stale data would cause a problem: bank balances, inventory levels, and seat availability for high-demand events. The cost is higher latency and reduced availability during failures.
Eventual consistency means replicas will converge to the same state over time but may differ briefly after a write.
A read immediately after a write might return the old value if it goes to a replica that has not yet received the update.
https://substackcdn.com/image/fetch/$s_!arqN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd785d861-31b6-46ec-9bee-9de1ed8b246b_1536x896.png
Eventual consistency is cheaper and more available than strong consistency. It is the right choice when brief staleness is acceptable: like counts, follower counts, and recommendation scores.
The key is being deliberate about which data can tolerate staleness and which cannot.
Consensus is the problem of getting multiple nodes in a distributed system to agree on a single value despite failures. It is the foundation of leader election, distributed locking, and replicated logs.
Algorithms like Raft and Paxos solve the consensus problem. They guarantee that a majority of nodes must agree before a value is committed, which prevents split-brain scenarios where two nodes both believe they are the leader.
Consensus is expensive because it requires multiple network round trips, so it is used only where agreement truly must be guaranteed.
Leader election is the process by which distributed nodes agree on which one is responsible for coordinating work.
The leader handles writes, coordinates distributed operations, or manages resources that should not be duplicated.
Leader election requires consensus to prevent two nodes from both believing they are the leader and accepting conflicting writes.
https://substackcdn.com/image/fetch/$s_!RSs6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F245c0636-bb50-4a7e-b17c-d40ad6285393_1536x858.png
When the leader fails, a new election runs among the remaining nodes.
The window between a leader failing and a new one being elected is a period of reduced capability during which the system cannot perform leader-dependent operations.
An operation is idempotent if performing it multiple times produces the same result as performing it once.
HTTP GET is naturally idempotent because reading the same resource twice leaves it unchanged.
HTTP POST is not naturally idempotent because creating a resource twice creates two resources.
https://substackcdn.com/image/fetch/$s_!M27D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc68734d0-e66a-4a3d-841a-795695357ff4_1448x1086.png
Idempotency matters because distributed systems cannot guarantee that a request is delivered exactly once. A request may be lost, the response may be lost, or the caller may retry without knowing whether the first attempt succeeded.
Idempotent operations are safe to retry.
Non-idempotent operations that are retried can cause duplicates.
An idempotency key is a unique identifier a client attaches to a request so the server can detect and ignore duplicates. The server stores which keys it has processed and returns the original result if the same key arrives again without re-executing the operation.
Idempotency keys are the standard mechanism for making non-idempotent operations safe to retry. Payment APIs use them to prevent double charges when a network failure causes a retry. The key must be generated by the client before the first attempt so it can be sent with every retry.
Two-phase commit is a protocol for making a transaction atomic across multiple databases or services.
https://substackcdn.com/image/fetch/$s_!kvv3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1da5d5f-c018-4202-84a2-c1a530d5aeac_1536x1024.png
In the prepare phase, the coordinator asks all participants whether they can commit.
In the commit phase, if all say yes, the coordinator tells everyone to commit. If any say no, everyone aborts.
The problem with 2PC is that participants hold locks between the two phases.
If the coordinator crashes during this window, participants are blocked waiting indefinitely. This makes 2PC fragile for large distributed systems and is why the Saga pattern is more commonly used.
The Saga pattern is an alternative to distributed transactions for operations that span multiple services. It breaks the operation into a sequence of local transactions, each with a compensating action that undoes it if a later step fails.
If an order placement involves charging payment, reserving inventory, and creating a shipment, the saga runs each step locally.
https://substackcdn.com/image/fetch/$s_!bRkd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcfb43407-f22c-452e-82d3-f286060d01b8_1448x972.png
If the shipment creation fails, the saga runs the compensating actions: release the inventory and refund the payment. The system reaches eventual consistency through compensation rather than atomicity.
A consistent hashing ring arranges hash values in a circle and assigns each node responsibility for a range of values. Data is stored on the first node clockwise from its hash value.
When a node is added or removed, only the keys in the adjacent range move to a different node.
Virtual nodes, where each physical node occupies multiple positions on the ring, improve distribution uniformity and allow gradual capacity changes. This is the standard technique behind distributed caches like Redis Cluster.
Clock skew is the difference in time between clocks on different machines. Even with time synchronization protocols, clocks on different machines drift apart over time and can differ by milliseconds or more.
Clock skew breaks any logic that relies on timestamps from different machines to establish event ordering.
Two events with timestamps five milliseconds apart on different machines might have actually occurred in the opposite order. Distributed systems use logical clocks and vector clocks instead of wall-clock time to establish causal ordering without depending on synchronized clocks.
A vector clock is a mechanism for tracking the causal order of events across distributed nodes without depending on synchronized clocks. Each node maintains a counter, and the vector clock captures which events causally precede which others.
When a message is sent, the sender includes its current vector clock. The receiver updates its own clock by taking the maximum of each position. This allows the system to determine not just when events happened but whether one event could have caused another, which is the information needed to resolve conflicts in eventually consistent systems.
A message queue is a component that holds messages from producers until consumers are ready to process them.
The producer sends a message and moves on without waiting for the consumer to finish. The consumer processes messages at its own pace.
https://substackcdn.com/image/fetch/$s_!D6wt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb06df94b-4b1b-4947-b004-056a6302a8b9_1448x956.png
Message queues decouple producers from consumers in time, which absorbs traffic spikes and allows the two sides to scale independently.
The trade-off is that results are not immediately available since processing happens asynchronously.
Publish-subscribe is a messaging pattern where producers publish messages to a topic and any number of consumers subscribe to receive copies.
Unlike a queue where each message goes to one consumer, pub/sub fans out each message to all subscribers.
https://substackcdn.com/image/fetch/$s_!ei4h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffa687de8-45b2-492c-b98c-8dde047d7076_1448x1005.png
Pub/sub is used when multiple independent parts of the system need to react to the same event.
An order placed event might need to trigger inventory reservation, notification sending, and analytics recording simultaneously.
Pub/sub lets each of these happen without the order service knowing or caring who is listening.
A dead-letter queue holds messages that failed to process after a set number of attempts.
Rather than letting a bad message block the main queue by retrying indefinitely, the queue moves it aside after the retry limit is reached.
https://substackcdn.com/image/fetch/$s_!7bZC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4469d5b4-775d-4526-87aa-1c444bf1e5ae_1448x1086.png
Without a dead-letter queue, one malformed message can stall processing for everything behind it.
With one, the bad message is parked for inspection while the rest of the queue keeps flowing. Monitoring the dead-letter queue is an essential part of operating any message-driven system.
Backpressure is a mechanism where a consumer signals to a producer to slow down when it cannot keep pace.
https://substackcdn.com/image/fetch/$s_!Frhc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdea689a3-88f6-452f-93de-cb9bb5cdb39a_1536x1024.png
Without backpressure, a fast producer and a slow consumer leads to an unbounded queue that grows until memory is exhausted.
Backpressure makes overload visible and manageable rather than letting it accumulate silently. It is implemented through bounded queues that reject new messages when full, forcing the producer to wait or slow down, or through explicit flow control signals from consumer to producer.
A WebSocket is a protocol that establishes a persistent bidirectional connection between a client and a server. Once established, either side can send data at any time without the overhead of opening a new connection for each message.
https://substackcdn.com/image/fetch/$s_!yMxL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e9a411b-e5af-444e-bc2f-8e38340f2890_1536x1024.png
WebSockets are the right choice for real-time features that require low-latency bidirectional communication: chat, live collaboration, multiplayer games, and live trading.
The challenge at scale is that each WebSocket connection is stateful and long-lived, which means horizontal scaling requires a connection registry and a pub/sub backplane to route messages to the right server.
Server-Sent Events is a protocol for streaming one-way updates from a server to a client over a single HTTP connection that stays open. The server can push events to the client at any time, but the client cannot send data back over the same connection.
https://substackcdn.com/image/fetch/$s_!s_iV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feea59e51-28f6-4bd4-8d2a-404c308f4c6f_1536x1024.png
SSE is simpler than WebSockets and includes built-in reconnection, making it the right choice when only the server needs to push data: live notifications, stock prices, AI response streaming, and dashboard updates.
The lack of bidirectionality is a feature rather than a limitation for these use cases.
A circuit breaker monitors calls to a dependency and stops making them when the failure rate exceeds a threshold. It has three states: closed (normal operation), open (dependency failing, all calls rejected immediately), and half-open (testing recovery with a small number of trial calls).
The circuit breaker prevents a failing dependency from dragging down the service that depends on it.
https://substackcdn.com/image/fetch/$s_!n1ig!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F018ae772-a560-45cf-8f6d-6c507e11fe61_1448x1086.png
Without one, a slow or failing database causes the application servers to accumulate waiting requests, eventually exhausting their resources and failing as well.
With one, the application fails fast when the database is unhealthy, freeing its resources and giving the database room to recover.
Rate limiting caps how many requests a client can make in a given period.
When a client exceeds the limit, further requests are rejected with a specific status code until the limit resets.
https://substackcdn.com/image/fetch/$s_!xKNi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F201f077a-7fa6-4b66-8d34-0a47c7804399_1448x933.png
Rate limiting protects services from overload and abuse and ensures fair usage among all clients.
The token bucket algorithm is the most common implementation: each client has a bucket that fills with tokens at a fixed rate and empties as requests are made. This allows short bursts while enforcing a long-term average rate.
Load shedding is the deliberate rejection of excess requests when a system is overloaded.
Rather than trying to serve all requests poorly and collapsing, the system serves what it can handle well and declines the rest with a clear signal to retry later.
Load shedding is the principle that partial availability is better than total failure.
https://substackcdn.com/image/fetch/$s_!djPT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8221803-5f0e-495e-9465-dfc2b090ccfe_1536x1024.png
A system that serves eighty percent of requests successfully is far more useful than one that attempts all requests and fails all of them. Shedding should be prioritized, dropping lower-priority work first to preserve capacity for the most critical operations.
A bloom filter is a space-efficient probabilistic data structure that answers membership queries: is this item in the set?
It can say definitively that an item is not in the set, but it can only say that an item might be in the set, with a tunable false positive rate.
Bloom filters are used when the cost of a false negative (missing a real member) is high but a small rate of false positives is acceptable, and when memory is too limited to store the full set.
https://substackcdn.com/image/fetch/$s_!9eS3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d7b76d3-b0fa-4295-977b-2e8415099b40_1448x1086.png
Databases use them to avoid expensive disk lookups for keys that definitely do not exist.
Web crawlers use them to track which URLs have been visited.
An embedding is a numerical representation of data, typically text or images, as a vector of floating point numbers that captures the semantic meaning of the data. Items with similar meaning have vectors that are close together in the high-dimensional space.
Embeddings are the foundation of modern AI-powered search and retrieval. By converting text to vectors, a system can find documents that are semantically similar to a query even when they share no words in common. This is what powers semantic search, recommendation systems, and retrieval-augmented generation.
RAG is an architecture that improves the answers of a language model by retrieving relevant information from an external knowledge base and providing it as context.
https://substackcdn.com/image/fetch/$s_!co0o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05d9223c-666b-4c3f-bd47-db0065412277_1448x1086.png
Instead of relying solely on what the model learned during training, the system fetches up-to-date or domain-specific information at query time.
The pipeline has two phases.
During ingestion, documents are chunked, converted to embeddings, and stored in a vector database.
During query time, the question is embedded and used to search the vector database for relevant chunks, which are included in the prompt sent to the model. The model generates an answer grounded in the retrieved context rather than hallucinating from general training knowledge.

- Infrastructure concepts like scalability, load balancing, CDN, and API gateway describe how traffic flows through a system, how it is distributed, and how the system grows to handle more of it.
- Data and storage concepts like sharding, replication, indexing, caching patterns, and consistent hashing determine how data is stored, accessed, and kept consistent as the system scales.
- Distributed systems concepts like the CAP theorem, consensus, idempotency, sagas, and clock skew describe the fundamental challenges of running a system across multiple machines and the patterns that address them.
- Messaging concepts like queues, pub/sub, backpressure, and WebSockets describe how components communicate asynchronously and how real-time features are built at scale.
- Reliability and modern concepts like circuit breakers, rate limiting, load shedding, bloom filters, embeddings, and RAG cover how systems stay up under stress and how AI capabilities are integrated into production architectures.
- No concept exists in isolation. Understanding why each one exists, what problem it solves, and what it costs is what turns a vocabulary list into the ability to design systems.
- The 2026 edition reflects the reality that AI infrastructure concepts like embeddings and RAG are now standard system design vocabulary, as common in interviews as caching and sharding were five years ago.
System design has a language, and fluency in that language is what separates engineers who participate fully in design conversations from ones who nod along and hope not to be called on.
These fifty concepts are the vocabulary that covers the vast majority of [system design interviews](https://www.designgurus.io/course/grokking-the-system-design-interview), discussions, and design reviews.
Learn what each one does, why it exists, and what it costs, and you will find that the conversations you once found impenetrable become ones where you have something genuine to say.
