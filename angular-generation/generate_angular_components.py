from read_from_file.read_from_file import read_file
from create_angular_files import create_all_angular_files

fl = read_file("text_to_parse")
current_tag = ''
list_of_tags = []
current_group = []
for line in fl:
    list_of_words = line.replace("</", " </").replace(">", "> ").replace("\n","").replace("\t", "").split(" ")

    if current_tag:
        current_group.append(line)
    for word in list_of_words:
        modified_word = word.replace("<", "").replace(">", "")
        naked_word = modified_word.replace("/", "")
        if not current_tag and word != "" and "<" in word and "<!" not in word and naked_word and naked_word != "h2" and naked_word != "h3":
            list_of_tags.append(naked_word)
            current_group.append(line)
            current_tag = naked_word
        elif modified_word == "/" + current_tag:
            if list_of_tags.count(naked_word) == 1:
                create_all_angular_files(naked_word, current_group)
            else:
                name = naked_word + str(list_of_tags.count(naked_word))
                create_all_angular_files(name, current_group)
            current_group = []
            current_tag = ''
