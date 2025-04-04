from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="HumanTone",
    version="0.1.2",
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
    description="A unique sentiment analysis library with paraphrasing, contextual similarity, and speech output.",
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
