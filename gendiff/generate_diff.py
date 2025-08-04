from gendiff.parser import read_diff


def sorted_diff(arg1, arg2):
    result = []
    soer = sorted(arg1 | arg2)
    for key in soer:
            if key in arg1 and key in arg2:
                if isinstance(arg1[key], dict) and isinstance(arg2[key], dict):
                    result.append({'key': key, 'status': 'nested', 'value': sorted_diff(arg1[key], arg2[key])})
                    continue
                if arg1[key] == arg2[key]:
                    result.append(
                        {
                            'key': key,
                            'status': 'unchange',
                            'value': arg1[key],
                        }
                    )
                else: 
                    result.append(
                        {
                            'key': key, 
                            'status': 'change',
                            'old_value': arg1[key], 
                            'new_value': arg2[key],
                        }
                    )        
            elif key not in arg2:
                    result.append({'key': key, 'status': 'delete', 'value': arg1[key]})
            elif key not in arg1:
                    result.append({'key': key, 'status': 'add', 'value': arg2[key]})
    return result


def is_bool(arg):
    if arg is False or arg is True:
        return str(arg).lower()
    else:
        return str(arg)
    

def stylish_format(diff):
    SIGN = {'add': '+', 'delete': '-', 'unchange': ' ', 'old_value': '-', 'new_value': '+', 'nested': ' '}
    lvl = 1
    char = ' '
    count = 2
    lines = '{\n'
    for item in diff:
        lvl += 1
        if item['status'] == 'nested' and isinstance(item['value'], list):
            lines += f'{char*count*(lvl)}{SIGN[item['status']]} {item['key']}: {stylish_format(item['value'])}' + '\n'
        elif item['status'] == 'change':
            lines += f'{char*count*(lvl)}{SIGN['old_value']} {item['key']}: {item['old_value']}' + '\n'
            lines += f'{char*count*(lvl)}{SIGN['new_value']} {item['key']}: {item['new_value']}' + '\n'
        else:
            lines += f'{char*count*(lvl)}{SIGN[item['status']]} {item['key']}: {item['value']}' + '\n'
    lvl -= 1
    lines += f'{char*count*(lvl-1)}' + '\n}'
    return lines


def generate_diff(file1, file2):
    read_file1 = read_diff(file1)
    read_file2 = read_diff(file2)
    sort_diff = sorted_diff(read_file1, read_file2)
    return stylish_format(sort_diff)


print(generate_diff('tests/test_data/test_file1.json', 'tests/test_data/test_file2.json'))


