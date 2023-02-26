import json

data_file_name = "../label.json"

with open(data_file_name) as f:
    data_name = []
    data = json.load(f)
    for i in data:
        print(i)
