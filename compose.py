from jinja2 import Environment, select_autoescape, FileSystemLoader


env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html"])
)


main = env.get_template("body.html")

data = dict(
    name=dict(
        first="Nikita",
        last="Balakin"
    ),
    profession="Web developer",
    info=[
        dict(label="Address", value="Kyiv, Ukraine"),
        dict(label="Date/Place of birth", value="1994-12-29/Ukraine"),
        dict(label="Nationality", value="Ukrainian")
    ],
    links=[
        dict(label="Skype", value=""),
        dict(label="Telegram", value=""),
        dict(label="Linkedin", value="")
    ],
    skills=[
        dict(label="Python", value=6),
        dict(label="Javascript", value=6),
        dict(label="HTML/CSS", value=6),
        dict(label="SQL", value=6)
    ]
)

with open("index.html", "w") as f:
    f.write(main.render(**data))
