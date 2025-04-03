from setuptools import setup, find_packages
import os
import shutil
import requests
import tempfile

MODEL_FILES = [
    "https://github.com/RezaGooner/PerSent/raw/main/PerSent/model/classifier.joblib",
    "https://github.com/RezaGooner/PerSent/raw/main/PerSent/model/weighted_sentiment_model.joblib",
    "https://github.com/RezaGooner/PerSent/raw/main/PerSent/model/word2vec.model",
]

def download_models():
    try:
        print("Downloading model files...")
        install_dir = os.path.dirname(os.path.abspath(__file__))
        target_dir = os.path.join(install_dir, "PerSent", "model")
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        for url in MODEL_FILES:
            file_name = os.path.basename(url)
            target_path = os.path.join(target_dir, file_name)
            
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(target_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded: {file_name}")
        
        print("All model files downloaded successfully.")
    except Exception as e:
        print(f"Error downloading models: {e}")

download_models()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PerSent",
    version="0.299.299",
    author="RezaGooner",
    author_email="RezaAsadiProgrammer@Gmail.com",
    description="Persian Sentiment Analysis Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RezaGooner/PerSent",
    packages=find_packages(),
    package_data={
        'PerSent': ['CommentAnalyzer.py', 'SentimentAnalyzer.py', 'model/*'],
    },
    include_package_data=True,
    install_requires=[
        'hazm>=0.7.0',
        'gensim>=4.0.0',
        'scikit-learn>=1.0.0',
        'pandas>=1.3.0',
        'tqdm>=4.62.0',
        'joblib>=1.1.0',
        'requests>=2.26.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    keywords='persian sentiment analysis nlp',
)
