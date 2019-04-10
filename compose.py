from jinja2 import Environment, select_autoescape, FileSystemLoader
import os
import yaml
import pdfkit


HTML_IN_FILE = os.path.realpath("./build/index.html")
PDF_OUT_FILE = os.path.realpath("./cv.pdf")
DATA_DIR = os.path.abspath("./data")
LOC_DIR = os.path.abspath("./loc")
PHOTO_DIR = os.path.abspath("./data/photo")
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
if len(input_filenames) == 1:
    data_filename = input_filenames[0]
elif len(input_filenames) == 0:
    exit("CV data dir has no files!")
else:
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
    data = yaml.safe_load(datastream)['cv']

locale_filename = "{}.yml".format(data.get("loc", "en"))

try:
    with open(os.path.join(LOC_DIR, locale_filename), "r") as loc:
        data['loc'] = yaml.safe_load(loc, )['loc']
except FileNotFoundError:
    with open(os.path.join(LOC_DIR, DEFAULT_LOC)) as loc:
        data['loc'] = yaml.safe_load(loc)['loc']

if data.get('photo'):
    data['photo'] = os.path.join(PHOTO_DIR, data['photo'])
input_prompt
if data.get("sort") and data.get("sort").get("skills"):
    data["skills"]["general"].sort(key=sort_skills, reverse=True)
    data["skills"]["technical"].sort(key=sort_skills, reverse=True)


with open("build/index.html", "w") as f:
    f.write(main.render(**data))

options = {
    'page-width': '26cm',
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'encoding': "UTF-8",
    'no-outline': None
}


options['page-height'] = "{}cm".format(
    int(input("Enter page height in cm:\n"))
)

pdfkit.from_file(HTML_IN_FILE, PDF_OUT_FILE, options=options)

print("Template rendered successfuly")
