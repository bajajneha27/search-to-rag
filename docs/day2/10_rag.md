
# 10. Retrieval-Augmented Generation

RAG combines retrieval with generation.

---

## Pipeline

```mermaid
graph LR
    A[Query] --> B[Retriever]
    B --> C[Documents]
    C --> D[LLM]
    D --> E[Answer]
