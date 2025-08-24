def json_value(arg):
    if isinstance(arg, dict):
        res = []
        for k, v in arg.items():
            res.append(f'"{k}": {json_value(v)}')
        return '{' + ','.join(res) + '}'
    elif isinstance(arg, bool):
        return str(arg).lower()
    elif arg is None:
        return 'null'
    elif isinstance(arg, str):
        return f'"{arg}"'
    else:
        return str(arg)


def json_format(arg):
    result = []
    for item in arg:
        if item['status'] == 'nested':
            val = json_format(item['value'])
            result.append(
                f'"{item['key']}": ' + '{' + 
                f'"status": "{item['status']}", "value": {val}' + '}'
            )
        elif item['status'] == 'change':
            old_val = json_value(item['old_value'])
            new_val = json_value(item['new_value'])
            result.append(
                f'"{item['key']}": ' + '{' 
                f'"status": "{item['status']}",'
                f'"old_value": {old_val}, "new_value": {new_val}' + '}'
            )
        else:
            val = json_value(item['value'])
            result.append(
                f'"{item['key']}": ' + '{'
                f'"status": "{item['status']}", "value": {val}' + '}'
            )
    return '{' + ','.join(result) + '}'