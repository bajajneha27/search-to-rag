
# Where Search Breaks

So far, we’ve seen search on small data.
Real systems operate at massive scale.

---

## Challenges

- Billions of documents
- Very low latency (milliseconds)
- Constant updates
- Fault tolerance

---

## High-Level Architecture

```mermaid
graph LR
    A[User Query] --> B[Frontend]
    B --> C[Query Processor]
    C --> D[Shard 1]
    C --> E[Shard 2]
    C --> F[Shard N]
    D --> G[Results]
    E --> G
    F --> G
    G --> H[Merge & Rank]
    H --> I[Response]

### Speaker Notes

- Say: "Same logic, just many machines"
- Point at shards and say: "These run in parallel"
- Emphasize latency: "milliseconds"
- Avoid deep distributed system details