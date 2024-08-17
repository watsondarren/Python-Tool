import string

from construct_file_content.construct_content import construct_content
from write_to_file.create_file import create_file
from read_from_file.read_from_file import read_file


def create_angular_html_file(file_name, content):
    create_file(f"./angular/{file_name}/{file_name}.component.html", content)


def create_angular_ts_file(file_name):
    content = construct_content(read_file("base_files/base.component.ts"), "[LOWER_NAME]", file_name.lower())
    cap_name = file_name.replace("-", " ")
    cap_name = string.capwords(cap_name).replace(" ", "")
    content = construct_content(content, "[CAP_NAME]", cap_name)
    create_file(f"./angular/{file_name}/{file_name}.component.ts", content)


def create_angular_spec_ts_file(file_name):
    content = construct_content(read_file("base_files/base.component.spec.ts"), "[LOWER_NAME]", file_name.lower())
    cap_name = file_name.replace("-", " ")
    cap_name = string.capwords(cap_name).replace(" ", "")
    content = construct_content(content, "[CAP_NAME]", cap_name)
    create_file(f"./angular/{file_name}/{file_name}.component.spec.ts", content)


def create_angular_css_file(file_name):
    content = ""
    create_file(f"./angular/{file_name}/{file_name}.component.css", content)


def create_all_angular_files(file_name, html_content):
    create_angular_html_file(file_name, html_content)
    create_angular_ts_file(file_name)
    create_angular_spec_ts_file(file_name)
    create_angular_css_file(file_name)