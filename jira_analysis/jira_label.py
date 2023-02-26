data_file_name = "../jira_label.txt"
replaced_file = "../replaced-label.txt"

with open(data_file_name, "r") as f:
    with open(replaced_file, "w") as new_file:
        new_file.write(f.read().replace(",", "\n").replace("\"", ""))
