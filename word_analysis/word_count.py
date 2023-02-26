from word_analysis.process_lines import process_lines, get_file_lines, split_each_line_by, get_words_with_word_count, \
    write_results_to_file

filePath = "../things_to_count.txt"
write_path = "../wordCountResults.txt"

lines = process_lines(get_file_lines(filePath))

split_lines = split_each_line_by(lines, " ")

finalCount = get_words_with_word_count(split_lines)
finalCount = sorted(finalCount.items(), key=lambda item: item[1])


def format_word_count(counts):
    final_lines = ["Words Count\n"]
    for count in counts:
        final_lines.append(f"{count[0]} {count[1]}\n")
    return final_lines


write_results_to_file(write_path, format_word_count(finalCount))
