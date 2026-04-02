---
layout: default
---

# Day 1 — The Retrieval Problem

## 🔥 Demo

Search:
- wireless mouse
- wirless mause

Why does this fail?

---

## ⚙️ How Search Works

```mermaid
graph LR
    A[Query] --> B[Tokenization]
    B --> C[Inverted Index]
    C --> D[Matching]
    D --> E[Ranking]
