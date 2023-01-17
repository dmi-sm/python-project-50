def get_plain(tree, path=''):
    result = []

    for node in tree:
        name = node.get('name')
        status = node.get('status')
        value = get_string(node.get('value'))
        path_view = path + name

        if status == 'nested':
            result.append(get_plain(node.get('children'), path_view + '.'))
        if status == 'modified':
            result.append(
                f"Property '{path_view}' was updated. From {value}"
                f" to {get_string(node.get('new_value'))}"
            )
        if status == 'added':
            result.append(
                f"Property '{path_view}' was added with value:"
                f" {value}"
            )
        if status == 'removed':
            result.append(f"Property '{path_view}' was removed")
    return '\n'.join(result)


def get_string(object):
    if isinstance(object, dict):
        return '[complex value]'
    if isinstance(object, bool):
        return str(object).lower()
    if isinstance(object, int):
        return object
    if object is None:
        return 'null'
    return f"'{object}'"
