def read_file(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        return f.readlines()
