import json
from pathlib import Path
import re


def write_replaced_line(line_to_write: str):
    return line_to_write.replace("\t", "").replace("\n", "").replace(", () => {}", "").replace(" () => {}", "")\
        .replace(", () => {", "").replace("() => {", "").replace("it(", "").replace("it.skip(", "")\
        .replace("describe(", "").replace("describe.skip(", "")


def get_tests():
    tests = {}
    describe_on_next_line = False
    it_block_on_next_line = False
    tagsOnNextLine = False
    current_describe = ""
    currentItBlock = ""
    describeReg = "describe.*\((.*),"
    itBlockReg = "it.*\((.*),"
    testPath = "../../code/cy_tests/cypress/integration"
    result = list(Path(testPath).rglob("*.test.js"))

    for filePath in result:
        file_name = filePath.as_posix().replace(testPath, "")

        if not filePath.is_file():
            continue

        with open(filePath, "r") as f:
            file_lines = f.readlines()
            tests[file_name] = {}
            for line in file_lines:

                line_replace = line.replace("\n", "").replace("\t", "")
                if line_replace == "\t" or line_replace == "\n" or line_replace == "" or line_replace == "{" or line_replace == "}":
                    continue

                if tagsOnNextLine and describe_on_next_line:
                    if "it(" in line or "it.skip(" in line:
                        describe_on_next_line = False
                        tagsOnNextLine = False
                    else:
                        if "tags:" in line and "it('" not in line or "it.skip('" not in line:
                            current_describe += " " + write_replaced_line(line)
                            tests[file_name][current_describe] = []
                        describe_on_next_line = False
                        tagsOnNextLine = False
                        continue

                elif describe_on_next_line:
                    current_describe = write_replaced_line(line)

                    if "tags:" not in line:
                        tagsOnNextLine = True
                        continue

                    tests[file_name][current_describe] = []
                    describe_on_next_line = False
                    continue

                elif "describe(" in line or "describe.skip(" in line:
                    current_describe = write_replaced_line(line)
                    if not re.search(describeReg, line):
                        describe_on_next_line = True
                        continue

                    if ".skip(" in line:
                        current_describe = "Skipped: " + current_describe

                    if "() => {" not in line and "tags:" not in line:
                        tagsOnNextLine = True
                        describe_on_next_line = True


                    tests[file_name][current_describe] = []

                if tagsOnNextLine and it_block_on_next_line:
                    currentItBlock += " " + write_replaced_line(line)
                    tests[file_name][current_describe].append(currentItBlock)
                    it_block_on_next_line = False
                    tagsOnNextLine = False
                    continue

                elif it_block_on_next_line:
                    currentItBlock = write_replaced_line(line)
                    if "tags:" not in line:
                        tagsOnNextLine = True
                        continue

                    tests[file_name][current_describe].append(currentItBlock)
                    it_block_on_next_line = False
                    continue

                elif "\tit(" in line or "\tit.skip(" in line:
                    currentItBlock = write_replaced_line(line)
                    if not re.search(itBlockReg, line):
                        it_block_on_next_line = True
                        continue

                    if ".skip(" in line:
                        currentItBlock = "Skipped: " + currentItBlock

                    # print("It Block was on same line")
                    # print(f"Write to: {current_describe}")
                    # print(itBlockFind)
                    tests[file_name][current_describe].append([write_replaced_line(currentItBlock)])

    numberOfTest = 0
    numberOfFiles = 0
    skippedDescribes = 0
    skippedTests = 0
    for testfile in tests:
        print(f"\nFile: {testfile}")
        for suite in tests[testfile]:
            if "Skipped:" in suite:
                skippedDescribes += 1
            print(f"Describe: {suite}")
            if len(tests[testfile][suite]) > 0:
                for test in tests[testfile][suite]:
                    if type(test) is list:
                        for single_test in test:
                            if "Skipped:" in single_test:
                                skippedTests += 1
                            else:
                                numberOfTest += 1
                            print(f"Test: {single_test}")
                        continue
                    if "Skipped:" in test:
                        skippedTests += 1
                    else:
                        numberOfTest += 1
                    print(f"Test: {test}")
            else:
                print("Tests: Contains Only Skipped Tests")
    print("\n\n")
    print(f"Currently Skipped Describes: {skippedDescribes}")
    print(f"Currently Running Tests: {numberOfTest}")
    print(f"Currently Skipped Tests: {skippedTests}")
    with open("../test_file_output.txt", "w") as testFileOutput:
        testFileOutput.write(json.dumps(tests))


get_tests()
# print(tests)
