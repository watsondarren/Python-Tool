ignoreWords = ["to", "the", "and", "a", "is", "as", "In", "in", "for", "on", "see", "of", "tab", "not", "this", "are",
               "that", "or", "", "all", "when", "was", "they", "but", "can", "you", "has", "there", "from", "&", "-",
               "we", "be", "it", "if", "i", "their", "with", "an", "have"]


def process_lines(fl: str):
    temp_lines = []
    for line in fl:
        line = line.replace("\n", "").replace(",", " ").replace("\t", "").lower()
        if line == " ":
            continue
        elif line == "":
            continue
        else:
            temp_lines.append(line)
    return temp_lines


def return_lines_with_word(lines: list, word_or_phrase: str):
    temp_lines = []
    for line in lines:
        if word_or_phrase in line:
            temp_lines.append(line + "\n")
    return temp_lines


def get_file_lines(file_path: str):
    with open(file_path, "r") as f:
        return f.readlines()


def split_each_line_by(lines: list, delineator: str):
    separated = []
    for line in lines:
        for split_item in line.split(delineator):
            separated.append(split_item)
    return separated


def get_words_with_word_count(lines: list, word_length_to_ignore: int = 0):
    final_count = {}
    for word in lines:
        word = word.lower()
        word = word.replace(":", "")
        if word in ignoreWords:
            continue
        if "*" in word:
            continue
        #     If you wish to only look at counts higher than a certain amount that goes here
        if len(word) < word_length_to_ignore:
            continue
        if word[0] == "+":
            word = word.replace("+", "\\")
        if word in final_count:
            final_count[word] += 1
        else:
            final_count[word] = 1
    return final_count


def ignore_word_count(words_with_count: list, count_to_ignore: int):
    word_count_to_use = {}
    for count in words_with_count:
        if count[1] < count_to_ignore:
            continue
        word_count_to_use[count[0]] = count[1]
    return word_count_to_use


def write_results_to_file(file_name: str, list_of_results_to_write: list):
    with open(file_name, "w") as file_to_write_to:
        for line in list_of_results_to_write:
            file_to_write_to.writelines(line)

