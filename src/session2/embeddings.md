
# Words to Meaning: Embeddings

At the heart of AI search is the transformation of unstructured text into high-dimensional numerical vectors.

An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

---

Embeddings are commonly used for:

- **Search** (where results are ranked by relevance to a query string)
- **Clustering** (where text strings are grouped by similarity)
- **Recommendations** (where items with related text strings are recommended)
- **Anomaly detection** (where outliers with little relatedness are identified)
- **Diversity measurement** (where similarity distributions are analyzed)
- **Classification** (where text strings are classified by their most similar label)

---

## Generating Embeddings

```python
from sentence_transformers import SentenceTransformer

# 1. Load a pre-trained model (all-MiniLM-L6-v2 is fast and efficient)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define our "documents"
sentences = [
    "High-precision wireless gaming mouse with RGB",
    "Ergonomic vertical mouse for wrist pain relief",
    "Travel-friendly Bluetooth mouse with silent clicks"
]

# 3. Encode the sentences into vectors
embeddings = model.encode(sentences)

# 4. Check the shape (Dimension of this specific model is 384)
print(f"Embedding shape: {embeddings.shape}")
# Result: (3, 384)
```

---

## The Mathematical Distance

To determine "relevance," we calculate the distance between the query vector (\\(q\\)) and document vectors (\\(d\\)).

- **Cosine Similarity**: Measures the angle between vectors.

<center>
\\(\text{sim}(q, d) = \frac{q \cdot d}{\|q\| \|d\|}\\)
</center>

- **Euclidean Distance (\\(L2\\))**: Measures the straight-line distance.