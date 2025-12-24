import numpy as np


class SemanticSimilarity:
    def __init__(self):
        self.model = None
        self.util = None

    def _load(self):
        if self.model is None:
            from sentence_transformers import SentenceTransformer, util
            self.model = SentenceTransformer("all-MiniLM-L6-v2")
            self.util = util

    def compute(self, sentences: list[str], corpus: list[str]) -> np.ndarray:
        if not sentences or not corpus:
            return np.zeros((len(sentences), len(corpus)))

        self._load()

        s_emb = self.model.encode(sentences, convert_to_tensor=True)
        c_emb = self.model.encode(corpus, convert_to_tensor=True)

        scores = self.util.cos_sim(s_emb, c_emb)
        return scores.cpu().numpy()

