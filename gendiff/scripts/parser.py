import json

import yaml


def read_diff(file):
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith('.yaml') or file.endswith('.yml'):
        with open(file, 'r') as f:
            yaml_file = yaml.safe_load(f)
        return yaml_file
    else:
        raise ValueError('Unsupported format')