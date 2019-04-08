from jinja2 import Environment, select_autoescape, FileSystemLoader
import yaml


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html"])
)


main = env.get_template("body.html")

with open("data.yml", "r") as datastream:
    data = yaml.load(datastream)['cv']

with open("loc/{}.yml".format(data.get("loc", "en")), "r") as loc:
    data['loc'] = yaml.load(loc)['loc']

with open("build/index.html", "w") as f:
    f.write(main.render(**data))
