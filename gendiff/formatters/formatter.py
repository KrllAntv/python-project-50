from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format


def format(diff, format):
    if format == 'plain':
        return plain_format(diff)
    elif format == 'json':
        return json_format(diff)
    elif format == 'stylish':
        return stylish_format(diff)