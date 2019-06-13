import os
import custom_pre_processing

root_dir = "../datasets/bbc-raw/"
new_dir = "../datasets/bbc-new/"

dirs = ["business", "entertainment", "politics", "sport", "tech"]

for dir in dirs:
    relative_dir = root_dir + dir
    files = [f for f in os.listdir(relative_dir) if os.path.isfile(os.path.join(relative_dir, f))]
    
    for file in files:
        file_path = relative_dir + "/" + file
        
        f = open(file_path, "r")
        content = f.read()
        f.close()
        words = custom_pre_processing.pre_process(content)
        new_string = " ".join([word for word in words])
        new_file = new_dir + dir + "/" + file
        
        print(new_file)
        f = open(new_file, "w")
        f.write(new_string)
        f.close()
