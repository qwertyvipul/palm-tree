import custom_pre_processing
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_tf_idf_matrix(corpus):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    features = vectorizer.get_feature_names()
    matrix = X.todense()
    return features, matrix.view(type = np.ndarray)

# features, matrix = generate_tf_idf_matrix(corpus)
