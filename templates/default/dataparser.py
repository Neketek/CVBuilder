def sort_skills(item):
    return "{}{}".format(item['value'], item["label"])


def parse(data):
    if data.get("sort") and data.get("sort").get("skills"):
        data["skills"]["general"].sort(key=sort_skills, reverse=True)
        data["skills"]["technical"].sort(key=sort_skills, reverse=True)
    return data
