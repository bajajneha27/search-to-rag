# Day 2 — The RAG Solution

## Demo
Search: "device for presentations"

Keyword search fails → why?

---

## Embeddings
```mermaid
graph TD
    A["wireless mouse"] --> B["vector"]
    C["bluetooth pointer"] --> D["vector"]

    B --> E["close"]
    D --> E
