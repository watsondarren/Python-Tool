from json import load

output_file_path = "../test_file_output.txt"


def print_test_results(results_to_print):
    for tests in results_to_print:
        if type(tests) is list:
            for test in tests:
                print(f"Test: {test}")
        else:
            print(f"Test: {tests}")


def print_tests_in_dict(file_data: dict):
    for file_path in file_data:
        print(f"\nFile Path: {file_path}")
        for describe in file_data[file_path]:
            print(f"Describe: {describe}")
            print_test_results(file_data[file_path][describe])


def get_test_from_file(file_name):
    results_to_print = {}
    with open(output_file_path, "r") as file_to_read:
        loaded_file = load(file_to_read)

        for file_path in loaded_file:
            if file_name in file_path:
                results_to_print[file_name] = {}
                for describe in loaded_file[file_path]:
                    results_to_print[file_name][describe] = []
                    for tests in loaded_file[file_path][describe]:
                        if type(tests) is list:
                            for test in tests:
                                results_to_print[file_name][describe].append(test)
                        elif type(tests) is str:
                            results_to_print[file_name][describe].append(test)
    print_tests_in_dict(results_to_print)


def get_tests_with_tag(tag):
    test_count = 0
    results_to_print = {}
    with open(output_file_path, "r") as file_to_read:
        loaded_file = load(file_to_read)

        for file_name in loaded_file:
            for describe in loaded_file[file_name]:
                if tag in describe:
                    if file_name in results_to_print:
                        results_to_print[file_name][describe] = []
                    else:
                        results_to_print[file_name] = {}
                        results_to_print[file_name][describe] = []
                    for tests in loaded_file[file_name][describe]:
                        if type(tests) is list:
                            for test in tests:
                                test_count += 1
                                results_to_print[file_name][describe].append(test)
                        else:
                            test_count += 1
                            results_to_print[file_name][describe].append(tests)
                else:
                    tagged_tests = []
                    for tests in loaded_file[file_name][describe]:
                        if type(tests) is list:
                            for test in tests:
                                if tag in test:
                                    test_count += 1
                                    tagged_tests.append(test)
                        else:
                            if tag in test:
                                test_count += 1
                                tagged_tests.append(test)
                        if len(tagged_tests) > 0:
                            results_to_print[file_name] = {}
                            results_to_print[file_name][describe] = []
                            results_to_print[file_name][describe].append(tagged_tests)
    print_tests_in_dict(results_to_print)
    print(f"Total Tests: {test_count}")



# search_for_test("/all_messages", ["@nightly"])

# get_test_from_file("")
get_tests_with_tag("@engagement")