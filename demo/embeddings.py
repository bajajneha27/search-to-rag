from sentence_transformers import SentenceTransformer, util

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

# 5. Define a user search query
query = "A portable mouse that doesn't make noise"
query_embedding = model.encode(query)

# 3. Find the best match using Cosine Similarity
hits = util.semantic_search(query_embedding, embeddings, top_k=1)

print(f"Top result: {sentences[hits[0][0]['corpus_id']]}")