def get_plain(tree, path=''):
    result = []

    for node in tree:
        name = node.get('name')
        status = node.get('status')
        value = get_string(node.get('value', ''))
        path_view = path + name

        if status == 'nested':
            result.append(get_plain(node.get('children'), path_view + '.'))
        if status == 'modified':
            result.append(f"Property '{path_view}' was updated. From {value} to {get_string(node.get('new_value'))}")
        if status == 'added':
            result.append(f"Property '{path_view}' was added with value: {value}")
        if status == 'removed':
            result.append(f"Property '{path_view}' was removed")
    return '\n'.join(result)


def get_string(object):
    if isinstance(object, dict):
        return '[complex value]'
    elif object is None:
        return 'null'
    elif isinstance(object, bool):
        return 'true' if object else 'false'
    else:
        return f"'{object}'"
