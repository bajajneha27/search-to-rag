
# Demo

Let’s revisit a query:

"device for presentations"

Traditional search relies on Lexical Overlap (TF-IDF, BM25). While fast, it suffers from two major flaws:

- **The Synonym Problem**: Searching "feline" won't find a document containing only the word "cat."

- **Polysemy**: The word "bank" means something different in "river bank" vs. "investment bank."

Semantic Search shifts the focus from matching **words** to matching **meaning** (intent and context).

```python
from sentence_transformers import SentenceTransformer, util
import torch

# 1. Initialize the Open-Source Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Our "Database" (The Corpus)
catalog = [
    "Oak wood dining table with 6 chairs",
    "Memory foam queen mattress with cooling gel",
    "Ergonomic office chair with lumbar support",
    "Modern velvet sofa in midnight blue",
    "Folding metal desk for small spaces"
]

# 3. Create the Embeddings
catalog_embeddings = model.encode(catalog, convert_to_tensor=True)

# 4. User Search
query = "something comfortable to sleep on"
query_embedding = model.encode(query, convert_to_tensor=True)

# 5. Compute Similarity (using top_k=2)
# This returns the scores and the index positions of the matches
hits = util.semantic_search(query_embedding, catalog_embeddings, top_k=2)

print("Search Results:")
for hit in hits[0]:
    print(f"- {catalog[hit['corpus_id']]} (Score: {hit['score']:.4f})")
```

