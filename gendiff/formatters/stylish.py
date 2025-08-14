def is_value(arg):
    if isinstance(arg, dict):
        res = []
        for k, v in arg.items():
            res.append({'key': k, 'status': 'nested', 'value': is_value(v)})
        return res
    elif isinstance(arg, bool):
        return str(arg).lower()
    elif arg is None:
        return 'null'
    else:
        return arg


SIGN = {
    'add': '+', 'delete': '-', 
    'unchange': ' ', 'old_value': '-', 
    'new_value': '+', 'nested': ' ',
}


def stylish_format(data, repl=' ', space_count=4, _lvl=1):
    res = '{\n'
    ind = repl * ((space_count * _lvl) - 2)
    for item in data:
        if isinstance(item.get('value'), list):
            # Рекурсивный обход если ключ value - список
            value = stylish_format(item['value'], repl, space_count, _lvl + 1)
            res += f'{ind}{SIGN[item['status']]} {item['key']}: {value}'
            res += '\n'  
        elif item['status'] == 'change':
            # Вывод словаря со статусом "CHANGE"
            val1 = is_value(item['old_value'])
            val2 = is_value(item['new_value'])
            res += f'{ind}{SIGN['old_value']} {item['key']}: ' 
            res += f'{
                val1 if not isinstance(val1, list)
                else stylish_format(val1, repl, space_count, _lvl + 1)
                }'
            res += '\n'
            res += f'{ind}{SIGN['new_value']} {item['key']}: ' 
            res += f'{
                val2 if not isinstance(val2, list) 
                else stylish_format(val2, repl, space_count, _lvl + 1)}'
            res += '\n'
        else:
            # Вывод остальных словарей
            res += f'{ind}{SIGN[item['status']]} {item['key']}: '
            val = is_value(item['value'])
            res += f'{
                val if not isinstance(val, list) 
                else stylish_format(val, repl, space_count, _lvl + 1)}'
            res += '\n'
    res += f'{repl * space_count * (_lvl - 1)}' + '}'
    return res