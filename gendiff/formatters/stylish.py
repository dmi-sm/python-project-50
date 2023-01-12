def get_stylish(diff_list, depth=0):
    result = '{\n'
    indent = '  '

    for _ in range(depth):
        indent += '    '

    for node in diff_list:
        name = node.get('name')
        status = node.get('status')
        value = node.get('value', '')

        if status == 'nested':
            value = get_stylish(node.get('children'), depth + 1)
            result += f"{indent}  {name}: {value}\n"
        elif status == 'unmodified':
            value = get_string(value, indent)
            result += f"{indent}  {name}: {value}\n"
        elif status == 'added':
            value = get_string(value, indent)
            result += f"{indent}+ {name}: {value}\n"
        elif status == 'removed':
            value = get_string(value, indent)
            result += f"{indent}- {name}: {value}\n"
        else:
            value = get_string(value, indent)
            result += f"{indent}- {name}: {value}\n"
            value = get_string(node.get('new_value'), indent)
            result += f"{indent}+ {name}: {value}\n"

    result += indent[:-2] + '}'
    return result


def get_string(object, indent):
    if isinstance(object, dict):
        indent += '    '
        result = '{\n'
        for key in object.keys():
            value = get_string(object.get(key), indent)
            result += f'{indent}  {key}: {value}\n'
        result += indent[:-2] + '}'
    elif object is None:
        result = 'null'
    elif isinstance(object, bool):
        result = str(object).lower()
    else:
        result = str(object)
    return result
