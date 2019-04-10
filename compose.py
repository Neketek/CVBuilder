from jinja2 import Environment, select_autoescape, FileSystemLoader
import os
import yaml

DATA_DIR = "./data"
LOC_DIR = "./loc"
DEFAULT_LOC = "en.yml"

input_prompt = "Select data file:\n"
input_filenames = None
for dirpath, dirnames, filenames in os.walk(DATA_DIR):
    i = 1
    input_filenames = filenames
    for filename in filenames:
        input_prompt += "{}) {}\n".format(i, filename)
        i += 1
    break
while True:
    try:
        selected = int(input(input_prompt))
        data_filename = input_filenames[selected-1]
    except (IndexError, ValueError):
        continue
    break

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html"])
)


main = env.get_template("body.html")


def sort_skills(item):
    return "{}{}".format(item['value'], item["label"])


with open(os.path.join(DATA_DIR, data_filename), "r") as datastream:
    data = yaml.load(datastream)['cv']

locale_filename = "{}.yml".format(data.get("loc", "en"))

try:
    with open(os.path.join(LOC_DIR, locale_filename), "r") as loc:
        data['loc'] = yaml.load(loc)['loc']
except FileNotFoundError:
    with open(os.path.join(LOC_DIR, DEFAULT_LOC)) as loc:
        data['loc'] = yaml.load(loc)['loc']


if data.get("sort") and data.get("sort").get("skills"):
    data["skills"]["general"].sort(key=sort_skills, reverse=True)
    data["skills"]["technical"].sort(key=sort_skills, reverse=True)


with open("build/index.html", "w") as f:
    f.write(main.render(**data))

print("Template rendered successfuly")
