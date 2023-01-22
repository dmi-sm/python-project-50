def get_stylish(tree, depth=0):  # noqa c901
    result = '{\n'
    indent = '  '
    indent += '    ' * depth

    for node in tree:
        name = node.get('name')
        status = node.get('status')
        value = node.get('value')

        if status == 'nested':
            value = get_stylish(node.get('children'), depth + 1)
            result += f"{indent}  {name}: {value}\n"
        if status == 'unmodified':
            value = get_string(value, indent)
            result += f"{indent}  {name}: {value}\n"
        if status == 'added':
            value = get_string(value, indent)
            result += f"{indent}+ {name}: {value}\n"
        if status == 'removed':
            value = get_string(value, indent)
            result += f"{indent}- {name}: {value}\n"
        if status == 'modified':
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
        return result
    if isinstance(object, bool):
        return str(object).lower()
    if object is None:
        return 'null'
    return str(object)
