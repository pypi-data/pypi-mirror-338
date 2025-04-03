import nltk
import numpy as np
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

# Ensure required NLTK resources are available
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("stopwords")

# Load the high-accuracy sentence similarity model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device="cpu")


class HumanToneSimilarity:
    """
    HumanTone similarity class that provides an accurate similarity score
    between two sentences while considering antonyms, word overlap, and semantics.
    """

    @staticmethod
    def _get_antonym_penalty(text1: str, text2: str) -> float:
        """
        Identifies antonyms between words in two sentences and applies a penalty.
        """
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
        return max(0, 1 - (penalty * 2.0))  # Stronger penalty for antonyms

    @staticmethod
    def _get_jaccard_similarity(text1: str, text2: str) -> float:
        """
        Computes Jaccard Similarity with stopword removal and tokenization.
        """
        stop_words = set(stopwords.words("english"))
        words1 = {word for word in word_tokenize(text1.lower()) if word.isalnum() and word not in stop_words}
        words2 = {word for word in word_tokenize(text2.lower()) if word.isalnum() and word not in stop_words}

        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))

        return intersection / union if union > 0 else 0

    @staticmethod
    def get_similarity(text1: str, text2: str) -> float:
        """
        Computes similarity using cosine similarity & Jaccard similarity.
        Applies antonym penalty for better accuracy.
        """
        # Encode text with normalization
        embedding1 = model.encode(text1, normalize_embeddings=True)
        embedding2 = model.encode(text2, normalize_embeddings=True)

        # Compute cosine similarity (semantic meaning)
        cosine_sim = util.cos_sim(embedding1, embedding2).item()

        # Compute Jaccard similarity (word overlap)
        jaccard_sim = HumanToneSimilarity._get_jaccard_similarity(text1, text2)

        # Apply antonym penalty
        antonym_penalty = HumanToneSimilarity._get_antonym_penalty(text1, text2)

        # Final similarity score: 90% Cosine + 10% Jaccard, with antonym adjustment
        final_score = (0.90 * cosine_sim) + (0.10 * jaccard_sim)
        final_score *= antonym_penalty  # Reduce score if antonyms exist

        return max(0, min(1, final_score))  # Ensure score is between 0-1

    @staticmethod
    def analyze_similarity(text1: str, text2: str) -> str:
        """
        Provides a similarity score with an explanation.
        """
        similarity_score = HumanToneSimilarity.get_similarity(text1, text2)

        # Categorize similarity
        if similarity_score > 0.9:
            reason = "✅ (Highly similar, meaning retained)"
        elif similarity_score > 0.7:
            reason = "✅ (Very similar meaning)"
        elif similarity_score > 0.4:
            reason = "⚠️ (Somewhat similar but could be better)"
        else:
            reason = "❌ (Opposite meaning, should be near 0)"  # Cross emoji for opposite meanings

        return f"Similarity Score: {similarity_score:.4f} {reason}"


# Example usage inside HumanTone
if __name__ == "__main__":
    # Example test cases
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
