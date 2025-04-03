import nltk
import numpy as np
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device="cpu")


class HumanToneSimilarity:
    @staticmethod
    def _get_antonym_penalty(text1: str, text2: str) -> float:
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())

        antonym_count = 0
        total_words = len(words1.union(words2))

        for word in words1:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    if lemma.antonyms() and lemma.antonyms()[0].name() in words2:
                        antonym_count += 1

        penalty = antonym_count / total_words if total_words > 0 else 0
        return max(0, 1 - (penalty * 2.0)) 

    @staticmethod
    def _get_jaccard_similarity(text1: str, text2: str) -> float:
        stop_words = set(stopwords.words("english"))
        words1 = {word for word in word_tokenize(text1.lower()) if word.isalnum() and word not in stop_words}
        words2 = {word for word in word_tokenize(text2.lower()) if word.isalnum() and word not in stop_words}

        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))

        return intersection / union if union > 0 else 0

    @staticmethod
    def get_similarity(text1: str, text2: str) -> float:
        embedding1 = model.encode(text1, normalize_embeddings=True)
        embedding2 = model.encode(text2, normalize_embeddings=True)

        cosine_sim = util.cos_sim(embedding1, embedding2).item()

        jaccard_sim = HumanToneSimilarity._get_jaccard_similarity(text1, text2)

        antonym_penalty = HumanToneSimilarity._get_antonym_penalty(text1, text2)

        final_score = (0.90 * cosine_sim) + (0.10 * jaccard_sim)
        final_score *= antonym_penalty 

        return max(0, min(1, final_score)) 

    @staticmethod
    def analyze_similarity(text1: str, text2: str) -> str:
        similarity_score = HumanToneSimilarity.get_similarity(text1, text2)

        if similarity_score > 0.9:
            reason = "✅ (Highly similar, meaning retained)"
        elif similarity_score > 0.7:
            reason = "✅ (Very similar meaning)"
        elif similarity_score > 0.4:
            reason = "⚠️ (Somewhat similar but could be better)"
        else:
            reason = "❌ (Opposite meaning, should be near 0)"  

        return f"Similarity Score: {similarity_score:.4f} {reason}"


if __name__ == "__main__":
    test_cases = [
        ("The quick brown fox jumps over the lazy dog.", "A fast brown animal leaps over a sleepy canine."),
        ("I love programming in Python!", "Python programming is something I enjoy."),
        ("This movie was fantastic!", "The film was absolutely terrible."),
        ("The sun is shining brightly.", "It's a very sunny day."),
    ]

    print("\n--- HumanTone Similarity Tests ---")
    for t1, t2 in test_cases:
        print(f"Text 1: {t1}")
        print(f"Text 2: {t2}")
        print(HumanToneSimilarity.analyze_similarity(t1, t2))
        print()
