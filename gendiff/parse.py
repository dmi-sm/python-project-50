import json
import yaml


def get_content(file_path):
    if file_path.endswith('.json'):
        with open(f'{file_path}') as content:
            return json.load(content)
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        with open(f'{file_path}') as content:
            return yaml.safe_load(content)
    raise Exception('Comparison is available only for json and yaml files')
