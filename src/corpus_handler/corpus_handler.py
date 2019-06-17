from src.file_handler import file_handler
from src.text_handler import pre_processing


def generate_corpus(docs):
    print("LOG: Generetating Corpus")
    corpus = []
    for doc in docs:
        words = pre_processing.pre_process(doc)
        string = " ".join([word for word in words])
        corpus.append(string)
    return corpus

def read_corpus(directory):
    pass



def generate_bag_of_words(docs):
    bag_of_words = []
    for doc in docs:
        words = pre_processing.text_to_words(doc, pre_process=True)
        bag_of_words.append(words)
    return bag_of_words