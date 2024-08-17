from os import makedirs, path


def create_file(file_path, list_of_content):
    makedirs(path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding="utf8") as f:
        f.writelines(list_of_content)
