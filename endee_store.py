import numpy as np

class EndeeStore:
    def __init__(self):
        self.texts = []
        self.embeddings = []

    def add(self, texts, embeddings):
        for t, e in zip(texts, embeddings):
            self.texts.append(t)
            self.embeddings.append(e)

    def search(self, query_embedding, top_k=3):
        similarities = []

        for i, emb in enumerate(self.embeddings):
            score = np.dot(query_embedding, emb)
            similarities.append((score, self.texts[i]))

        similarities.sort(reverse=True)

        return [text for _, text in similarities[:top_k]]