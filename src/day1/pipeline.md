
# How Search Works

At a high level, search follows a pipeline:

```mermaid
graph LR
    A[Query] --> B[Tokenization]
    B --> C[Index Lookup]
    C --> D[Matching]
    D --> E[Ranking]
