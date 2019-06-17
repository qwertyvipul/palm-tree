import os
from src.corpus_handler import corpus_handler
from src.file_handler import file_handler
from src.keyword_extractor import tf_idf_extractor
from src.settings import root_dir
from src.text_handler import pre_processing

class BbcProject:
    def __init__(self):
        self.log = False
        self.root_dir = root_dir()
        self.dataset_dir = self.root_dir + "/static/datasets/bbc/raw/"
        self.corpus_dir = self.root_dir + "/static/corpus/bbc/prep/"
        self.tf_idf_dir = self.root_dir + "/static/corpus/bbc/keyword/tf-idf"
        self.dir_names = ["/business/", "/entertainment/", "/politics/", "/sport/", "/tech/"]

    def print_log(self, message):
        if(self.log):
            print(message)

    def generate_corpus(self):
        for dir in self.dir_names:
            self.print_log(dir)
            relative_dir = self.dataset_dir + dir
            files = file_handler.get_dir_files(relative_dir)

            for file in files:
                content = file_handler.get_file_content(relative_dir + file)
                new_content = pre_processing.pre_process(content)
                new_file = self.corpus_dir + dir + file
                file_handler.write_file(new_file, new_content)

    def get_corpus(self):
        corpus = []
        for dir in self.dir_names:
            docs = file_handler.read_some_files(self.corpus_dir + dir)
            for doc in docs:
                corpus.append(doc)
        return corpus

    def generate_tf_idf_corpus(self):
        corpus = self.get_corpus()
        features, matrix = tf_idf_extractor.extract_tf_idf(corpus)

        count = 0
        for dir in self.dir_names:
            self.print_log(dir)
            relative_dir = self.dataset_dir + dir
            files = file_handler.get_dir_files(relative_dir)

            for i in len(files):
                keyword_list = []
                for j in range(0, matrix.shape[1]):
                    if matrix[i][j] == 0:
                        continue

                    keyword = features[j]






        print(len(features))
        print(matrix.shape[0])
        print(matrix.shape[1])

    def generate_thesaurus(self):
        pass