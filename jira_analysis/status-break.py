from re import findall, search
data_file_name = "../data2.txt"
replaced_file = "../replaced.txt"
replace_text_1 = "<"
matched_file = "../types.txt"
reg_expression = 'data-descriptor-title=\".*\"'

with open(data_file_name, "r") as f:
    with open(replaced_file, "w") as new_file:
        new_file.write(f.read().replace(replace_text_1, "\n" + replace_text_1))

with open(replaced_file, "r") as nf:
    nl = nf.read().split("\n")
    status_array = []

    for line in nl:
        # print(line)
        searching = search(reg_expression, line)
        if searching:
            status_array.append(findall(reg_expression, line))


with open(matched_file, "w") as match_file:
    # print(status_array)
    for line in status_array:
        match_file.write(str(line).replace('[', '\n['))

with open(matched_file, "r") as match_file:
    print(match_file.read())
    #
    # print(status_array)
