import custom_pre_processing
import tf_idf_extractor
import numpy as np
import pandas as pd

def get_thesaurus(docs, is_corpus = False):
    print("LOG: Generetating Thesaurus")
    corpus = docs
    if not is_corpus:
        corpus = custom_pre_processing.generate_corpus(docs)

    features, matrix = tf_idf_extractor.generate_tf_idf_matrix(corpus)
    
    td_matrix = matrix.transpose()
    thesaurus_matrix = np.matmul(td_matrix, td_matrix.transpose())
    
    # Create Ralation List
    relation_list = []
    for row in range(0, len(features)):
        for col in range(row, len(features)):
            if thesaurus_matrix[row][col] == 0 or row == col:
                continue
            relation_list.append([features[row], features[col], thesaurus_matrix[row][col]])
    
    df = pd.DataFrame(relation_list, columns = ["word-1", "word-2", "score"])
    df = df.sort_values("score", ascending = False)
    return df

"""
docs = [
        "Both cat and dogs are animals",
        "I love animals but not cats",
        "steve jobs was the founder of apple",
        "jobs made back to the apple after getting fired",
        "car has brakes and gear",
        "brakes of the car failed"
]

corpus = custom_pre_processing.generate_corpus(docs)
features, matrix = tf_idf_extractor.generate_tf_idf_matrix(corpus)

td_matrix = matrix.transpose()
thesaurus_matrix = np.matmul(td_matrix, td_matrix.transpose())

# Create Ralation List
relation_list = []
for row in range(0, len(features)):
    for col in range(row, len(features)):
        relation_list.append([features[row], features[col], thesaurus_matrix[row][col]])

df = pd.DataFrame(relation_list, columns = ["word-1", "word-2", "score"])
df = df.sort_values("score")
"""