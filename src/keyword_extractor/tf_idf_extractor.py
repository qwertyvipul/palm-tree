import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from src.corpus_handler import corpus_handler

def extract_tf_idf(corpus):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names()
    matrix = X.todense()
    return features, matrix.view(type=np.ndarray)