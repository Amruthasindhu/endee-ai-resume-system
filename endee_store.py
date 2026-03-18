import numpy as np

class EndeeStore:
    def __init__(self):
        self.texts = []
        self.embeddings = []

    def add(self, texts, embeddings):
        for t, e in zip(texts, embeddings):
            self.texts.append(t)
            self.embeddings.append(np.array(e))

    def search(self, query_embedding, top_k=5):
        query_vec = np.array(query_embedding)
        similarities = []

        for i, emb in enumerate(self.embeddings):
            # Cosine similarity
            score = np.dot(query_vec, emb) / (np.linalg.norm(query_vec) * np.linalg.norm(emb) + 1e-10)
            similarities.append((score, self.texts[i]))

        similarities.sort(reverse=True)
        return [text for _, text in similarities[:top_k]]

    def clear(self):
        self.texts = []
        self.embeddings = []
