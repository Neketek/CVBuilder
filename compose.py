#!/usr/bin/env python3
from jinja2 import Environment, select_autoescape, FileSystemLoader
from argparse import ArgumentParser
import os
import yaml
import pdfkit
import subprocess


arg_parser = ArgumentParser()

arg_parser.add_argument(
    dest="data",
    help="CV data file name"
)
arg_parser.add_argument(
    "--width",
    dest="width",
    help="Page width in cm",
    default=21,
    type=float
)
arg_parser.add_argument(
    "--height",
    dest="height",
    help="Page height in cm",
    default=29.7,
    type=float
)
arg_parser.add_argument(
    "--template",
    dest="template",
    help="Template to use",
    default="default"
)

args = arg_parser.parse_args()


DIR_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_FOLDER = os.path.join(DIR_PATH, "templates", args.template)
STYLES_FILE = os.path.join(TEMPLATES_FOLDER, "styles.scss")
HTML_IN_FILE = os.path.join(TEMPLATES_FOLDER, "build/index.html")
CSS_IN_FILE = os.path.join(TEMPLATES_FOLDER, "build/index.css")
LOC_DIR = os.path.join(TEMPLATES_FOLDER, "loc")
PDF_OUT_FILE = os.path.join(DIR_PATH, "cv.pdf")
DATA_DIR = os.path.join(DIR_PATH, "data")
PHOTO_DIR = os.path.join(DIR_PATH, "data/photo")

DEFAULT_LOC = "en.yml"

data_filename = "{}.yml".format(args.data)

with open(os.path.join(DATA_DIR, data_filename), "r") as datastream:
    data = yaml.safe_load(datastream)['cv']

locale_filename = "{}.yml".format(data.get("loc", "en"))

try:
    with open(os.path.join(LOC_DIR, locale_filename), "r") as loc:
        data['loc'] = yaml.safe_load(loc, )['loc']
except FileNotFoundError:
    with open(os.path.join(LOC_DIR, DEFAULT_LOC)) as loc:
        data['loc'] = yaml.safe_load(loc)['loc']


def sort_skills(item):
    return "{}{}".format(item['value'], item["label"])


if data.get('photo'):
    data['photo'] = os.path.join(PHOTO_DIR, data['photo'])

if data.get("sort") and data.get("sort").get("skills"):
    data["skills"]["general"].sort(key=sort_skills, reverse=True)
    data["skills"]["technical"].sort(key=sort_skills, reverse=True)


env = Environment(
    loader=FileSystemLoader(TEMPLATES_FOLDER),
    autoescape=select_autoescape(["html"])
)

main = env.get_template("body.html")

with open(HTML_IN_FILE, "w") as f:
    f.write(main.render(**data))

subprocess.call(["npx", "node-sass", STYLES_FILE, CSS_IN_FILE])
subprocess.call(["npx", "postcss", CSS_IN_FILE, "-u", "autoprefixer", "-r"])

options = {
    'page-width': "{}cm".format(args.width),
    'page-height': "{}cm".format(args.height),
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'encoding': "UTF-8",
}

pdfkit.from_file(HTML_IN_FILE, PDF_OUT_FILE, options=options)

print("Template rendered successfuly")
