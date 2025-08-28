import json


def json_format(arg):
    return json.dumps(arg, indent=4, separators=(',', ':'))