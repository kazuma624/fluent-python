import json

JSON = "data/osconfeed.json"


def load():
    with open(JSON) as fp:
        return json.load(fp)
