from setuptools import setup, find_packages

setup(
    name="HumanTone",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
    "transformers",
    "textblob",
    "nltk",
    "sentence-transformers",
    "pyttsx3",
    "torch",
    "scipy",
    "pandas"
    ],
    description="""HumanTone is a powerful and intuitive Natural Language Processing (NLP) library designed to enhance human-like text processing and interaction. It integrates advanced sentiment analysis, intelligent text paraphrasing, semantic similarity detection, and natural speech synthesis, making it an all-in-one solution for text-based AI applications.
Key Features:
✅ Sentiment Analysis – Accurately determines the emotional tone of a given text (Positive, Negative, Neutral) with confidence scores.
✅ Paraphrasing – Generates high-quality paraphrases while maintaining semantic meaning, improving text diversity and readability.
✅ Text Similarity Detection – Compares sentences for semantic similarity, aiding in duplicate detection, question-answering, and recommendation systems.
✅ Speech Synthesis – Converts text into natural-sounding speech using text-to-speech (TTS) technology.

HumanTone is ideal for chatbots, content generation, virtual assistants, and AI-driven conversations, helping developers create more natural and engaging user experiences. Designed for ease of use, it ensures seamless integration into Python projects.""",
    author="Vansh Gautam",
    author_email="vanshgautam2005@gmail.com",
    github="Private",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
