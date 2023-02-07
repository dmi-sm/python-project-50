import os
import json
import yaml


def get_content(file):
    file_path, format = os.path.splitext(file)
    with open(file_path + format) as content:
        data = content.read()
        return parse(format, data)


def parse(format, data):
    if format == '.json':
        return json.loads(data)
    if format == '.yaml' or format == '.yml':
        return yaml.load(data, Loader=yaml.SafeLoader)
    raise Exception('Comparison is available only for json and yaml files')
