import os


def get_dir_files(directory):
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    return files


def get_dir_folders(directory):
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    return folders


def get_file_content(file):
    f = open(file, "r")
    content = f.read()
    f.close()
    return content


def write_file(file, content):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file), exist_ok=True)
    f = open(file, "w")
    f.write(content)
    f.close()


def get_dir_file_contents(directory):
    contents = []
    file_names = get_dir_files(directory)
    for filename in file_names:
        file = directory + filename
        content = get_file_content(file)
        contents.append(content)
    return contents


def get_multiple_file_contents(files):
    contents = []
    for file in files:
        content = get_file_content(file)
        contents.append(content)
    return contents