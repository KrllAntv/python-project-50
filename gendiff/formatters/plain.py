def _value(arg):
    if isinstance(arg, dict):
        return '[complex value]'
    elif isinstance(arg, bool):
        return str(arg).lower()
    elif arg is None:
        return 'null'
    else:
        return f"'{str(arg)}'"


def plain_format(arg, path=''):
    res = []
    for item in arg:
        if item['status'] == 'add':
            res.append(
                f"Property '{path}{item['key']}' "
                f"was added with value: {_value(item['value'])}"
            )
        elif item['status'] == 'delete':
            res.append(f"Property '{path}{item['key']}' was removed")
        elif item['status'] == 'change':
            res.append(
                f"Property '{path}{item['key']}' was updated. "
                f"From {_value(item['old_value'])} "
                f"to {_value(item['new_value'])}"
            )
        elif item['status'] == 'nested':
            res.append(plain_format(item['value'], path + f'{item['key']}.'))
    return '\n'.join(res)