from word_analysis.process_lines import process_lines, return_lines_with_word, get_file_lines, write_results_to_file

file_location = "../things_to_count.txt"
write_file = "../lines_with_word.txt"
word_to_look_for = "integrations"

lines = process_lines(get_file_lines(file_location))

found_lines = return_lines_with_word(lines, word_to_look_for)

write_results_to_file(write_file, found_lines)