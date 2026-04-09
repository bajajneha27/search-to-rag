
# Retrieval-Augmented Generation

Foundation models have broad knowledge, but can lack depth in specialized domains. This limitation can result in responses that are incomplete or irrelevant. This behavior is known as “hallucination.”

Retrieval-augmented generation, or RAG, is a technique that uses authoritative, external data to improve the accuracy, relevancy, and usefulness of a model’s output.

---

- **User Query**: "How do I fix a leaky pipe?
- **Retrieve**: Convert query to vector $\rightarrow$ Find top 3 relevant chunks in the Vector DB.
- **Augment**: Feed the retrieved text + the original query into an LLM.
- **Generate**: The LLM provides a grounded, conversational answer.

![alt text](rag.png)