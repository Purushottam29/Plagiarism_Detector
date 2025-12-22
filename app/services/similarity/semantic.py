from sentence_transformers import SentenceTransformer, util
import torch

class SemanticSimilarity:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def compute(self, sentences: list[str], corpus: list[str]):
        s_emb = self.model.encode(sentences, convert_to_tensor=True)
        c_emb = self.model.encode(corpus, convert_to_tensor=True)

        scores = util.cos_sim(s_emb, c_emb)
        return scores.cpu().numpy()

