import numpy as np
import pandas as pd
from src.keyword_extractor import tf_idf_extractor

def extract_thesaurus(corpus):
    features, matrix = tf_idf_extractor.extract_tf_idf(corpus)
    td_matrix = matrix.transpose()
    thesaurus_matrix = np.matmul(td_matrix, td_matrix.transpose())
    return features, thesaurus_matrix

def get_thesaurus_relation_list(corpus):
    features, thesaurus_matrix = extract_thesaurus(corpus)
    relation_list = []
    for row in range(0, len(features)):
        for col in range(0, row):
            if thesaurus_matrix[row][col] == 0:
                continue
            relation_list.append([features[row], features[col], thesaurus_matrix[row][col]])

    return relation_list

def get_thesaurus_relation_df(corpus):
    features, thesaurus_matrix = extract_thesaurus(corpus)
    relation_list = []
    for row in range(0, len(features)):
        for col in range(0, row):
            if thesaurus_matrix[row][col] == 0:
                continue
            relation_list.append([features[row], features[col], thesaurus_matrix[row][col]])

    df = pd.DataFrame(relation_list, columns=["word-1", "word-2", "score"])
    df = df.sort_values("score", ascending=False)
    return df

"""
corpus = [
        "cat and dogs are animals",
        "i love animals but not cats",
        "steve jobs was the founder of apple",
        "jobs made back to the apple after getting fired",
        "car has brakes and gear",
        "brakes of the car failed"
]

print(get_thesaurus_relation_df(corpus))
"""