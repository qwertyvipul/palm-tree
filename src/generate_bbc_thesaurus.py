import os
import thesaurus_extractor

root_dir = "../datasets/bbc-new/"

dirs = ["business", "entertainment", "politics", "sport", "tech"]

docs = []
for dir in dirs:
    relative_dir = root_dir + dir
    files = [f for f in os.listdir(relative_dir) if os.path.isfile(os.path.join(relative_dir, f))]
    
    for file in files[0:2]:
        file_path = relative_dir + "/" + file
        
        f = open(file_path, "r")
        content = f.read()
        f.close()
        docs.append(content)
        print(len(docs))

bbc_thesaurus = thesaurus_extractor.get_thesaurus(docs, is_corpus = True)