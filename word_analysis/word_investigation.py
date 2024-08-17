from word_analysis.process_lines import process_lines, return_lines_with_word
from read_from_file.read_from_file import read_file
from write_to_file.create_file import create_file

file_location = "../things_to_count.txt"
write_file = "../lines_with_word.txt"
word_to_look_for = "integrations"

lines = process_lines(read_file(file_location))

found_lines = return_lines_with_word(lines, word_to_look_for)

create_file(write_file, found_lines)
