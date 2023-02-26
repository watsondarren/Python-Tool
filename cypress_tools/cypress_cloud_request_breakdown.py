import json

data_file_name = "../cypresstests.json"

with open(data_file_name) as f:
    tests_ran = []
    test_data = {}
    data_loaded = json.load(f)
    for result in data_loaded["data"]["testResults"]:
        if result["__typename"] == "TestResult":
            test_name = ""
            for name in result["titleParts"]:
                test_name = test_name + name + " > "
            tests_ran.append(test_name[:-3])
    for test in tests_ran:
        print(test)
