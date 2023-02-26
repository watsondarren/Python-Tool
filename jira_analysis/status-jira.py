import json

data_file_name = "../status.json"

with open(data_file_name) as f:
    status_name = []
    status_data = json.load(f)
    for status in status_data:
        status_name.append(status["name"])
        # print(status["name"])
    for status in status_name:
        print(status + ": %d" % status_name.count(status))
