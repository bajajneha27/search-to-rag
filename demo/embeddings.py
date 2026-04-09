from sentence_transformers import SentenceTransformer

# 1. Load a pre-trained model (all-MiniLM-L6-v2 is fast and efficient)
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Define our "documents"
sentences = [
    "The cat sits outside", 
    "A man is playing guitar", 
    "The feline is resting outdoors"
]

# 3. Encode the sentences into vectors
embeddings = model.encode(sentences)

# 4. Check the shape (Dimension of this specific model is 384)
print(f"Embedding shape: {embeddings.shape}")