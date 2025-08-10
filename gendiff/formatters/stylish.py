def is_bool(arg):
    if arg is False or arg is True:
        return str(arg).lower()
    elif arg is None:
        return 'null'
    else:
        return str(arg)
    

def stylish_format(data, repl=' ', space_count=4, _lvl=1):
    SIGN = {
        'add': '+', 'delete': '-', 
        'unchange': ' ', 'old_value': '-', 
        'new_value': '+', 'nested': ' ',
    }
    res = '{\n'
    indent = repl * ((space_count * _lvl) - 2)
    for item in data:
        if isinstance(item.get('value'), list):
            value = stylish_format(item['value'], repl, space_count, _lvl + 1)
            res += f'{indent}{SIGN[item['status']]} {item['key']}: {value}'
        elif isinstance(item.get('value'), dict):
            chang_dict = [
                {
                    'key': k, 'status': 'unchange', 'value': v
                }
            for k, v in item['value'].items()]
            value = stylish_format(chang_dict, repl, space_count, _lvl + 1)
            res += f'{indent}{SIGN[item['status']]} {item['key']}: {value}'
        else:
            res += f'{indent}{SIGN[item['status']]} {item['key']}: '
            res += f'{is_bool(item['value'])}' + '\n'
    res += f'{repl * space_count * (_lvl - 1)}' + '}\n'
    return res