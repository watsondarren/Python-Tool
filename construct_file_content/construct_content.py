def construct_content(file_content, word_to_look_for, replace_with):
    print(file_content)
    new_file_content = []
    for line in file_content:
        if word_to_look_for in line:
            new_file_content.append(line.replace(word_to_look_for, replace_with))
        else:
            new_file_content.append(line)
    return new_file_content
