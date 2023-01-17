def get_diff_tree(first_source, second_source):
    diff_tree = []

    first_keys = set(first_source)
    second_keys = set(second_source)

    all_keys = sorted(first_keys | second_keys)
    added = second_keys - first_keys
    removed = first_keys - second_keys

    for key in all_keys:
        if isinstance(first_source.get(key), dict) \
                and isinstance(second_source.get(key), dict):
            diff_tree.append({
                'name': key,
                'status': 'nested',
                'children': get_diff_tree(first_source.get(key),
                                          second_source.get(key))
            })

        elif key in added:
            diff_tree.append({
                'name': key,
                'status': 'added',
                'value': second_source.get(key),
            })

        elif key in removed:
            diff_tree.append({
                'name': key,
                'status': 'removed',
                'value': first_source.get(key),

            })

        elif first_source.get(key) == second_source.get(key):
            diff_tree.append({
                'name': key,
                'status': 'unmodified',
                'value': first_source.get(key),
            })

        else:
            diff_tree.append({
                'name': key,
                'status': 'modified',
                'value': first_source.get(key),
                'new_value': second_source.get(key),
            })

    return diff_tree
