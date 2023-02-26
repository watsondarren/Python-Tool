import re

file_path_input = "bdd_input.txt"
file_path_output = "tests_output.js"


def login(url_to_use: str = ""):
    return f"cy.login({{url: '{url_to_use}'}});"


def write_suite(name: str = "", desired_tags=[], tests_to_write: str = ""):
    tags_to_use = []
    if len(desired_tags) > 0:
        for tag in desired_tags:
            tags_to_use.append(tag)
    return f"describe('{name}', {{tags: {desired_tags}}}, () => {{\n{tests_to_write}\n}});\n\n"


def write_test(name: str = "", desired_tags=[], steps_to_write: str = ""):
    tags_to_use = []
    if len(desired_tags) > 0:
        for tag in desired_tags:
            tags_to_use.append(tag)
    return f"it('{name}', {{tags:{desired_tags}}}, () => {{\n{steps_to_write}}});\n\n"


def write_before(step_to_write: list):
    thing_to_write = ""
    for step in step_to_write:
        thing_to_write += f"{str(step)}\n"
    return f"beforeEach(() = {{\n{thing_to_write}\n}});\n\n"


with open(file_path_input, "r") as file_to_read:
    file_lines = file_to_read.readlines()
    file_to_write = {}
    current_suite = ""
    current_scenario = ""
    step_number = 1

    for line in file_lines:
        print(f"LINE: {line}")
        line = line.replace("\n", "")
        if line == '':
            continue
        if "suite:" in line:
            current_suite = line.replace("suite: ", "")
            file_to_write[current_suite] = {"before": "", "after": "", "scenarios": {}, "tags": []}
        elif "before:" in line:
            if "login" in line.replace("before: ", ""):
                find_url = re.findall("url:\"(.*)\"", line)
                file_to_write[current_suite]["before"] = write_before([login(find_url[0])])
        elif "scenario:" in line:
            step_number = 1
            current_scenario = line.replace("scenario: ", "")
            file_to_write[current_suite]["scenarios"][current_scenario] = {"tags": [], "steps": ""}
            print(f"CURRENT SCENARIO: {current_suite}")
        elif "suite_tags:" in line:
            tags = line.replace("suite_tags: ", "").split(" ",)
            file_to_write[current_suite]["tags"] = tags
        elif "scenario_tags:" in line:
            tags = line.replace("scenario_tags: ", "").split(" ",)
            file_to_write[current_suite]["scenarios"][current_scenario]["tags"] = tags
        elif "step:" in line:
            joined_line = line.replace("step: ", "")
            file_to_write[current_suite]["scenarios"][current_scenario]["steps"] += f"// Step {step_number} {joined_line}\n\n"
            step_number += 1
        else:
            file_to_write[current_suite]["scenarios"][current_scenario]["steps"] += f"// Step {step_number} {line}\n\n"
            step_number += 1

construct_file = ""
for suite in file_to_write:
    scenarios_to_write = ""
    before_text = ""

    for scenario in file_to_write[suite]["scenarios"]:
        scenario_tags = file_to_write[suite]["scenarios"][scenario]["tags"]
        steps_to_use = file_to_write[suite]["scenarios"][scenario]["steps"]
        scenarios_to_write += write_test(scenario, scenario_tags, steps_to_use)

    if file_to_write[suite]["before"]:
        before_text = file_to_write[suite]["before"]
    suite_tags = file_to_write[suite]["tags"]
    construct_file += write_suite(suite, suite_tags, before_text + scenarios_to_write)

with open(file_path_output, "w") as file_for_output:
    file_for_output.writelines(construct_file)
