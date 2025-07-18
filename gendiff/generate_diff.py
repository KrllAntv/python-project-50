import json

def sorted_diff(arg1, arg2):
    result = []
    for key in sorted(arg1 | arg2):
        if key not in arg2:
            result.append({'key': key, 'status': 'delete', 'value': arg1[key]})
        elif key not in arg1:
            result.append({'key': key, 'status': 'add', 'value': arg2[key]})
        elif key in arg1 and key in arg2:
            if arg1[key] == arg2[key]:
                result.append({'key': key, 'status': 'unchange', 'value': arg1[key]})
            else:
                result.append({'key': key, 'status': 'change', 'old_value': arg1[key], 'new_value': arg2[key]})
    return result

def is_bool(arg):
    if arg is False or arg is True:
        return str(arg).lower()
    else:
        return arg
    
def formater(arg):
    if arg['status'] == 'add':
        return f' + {arg['key']}: {arg['value']}'
    elif arg['status'] == 'delete':
        return f' - {arg['key']}: {arg['value']}'
    elif arg['status'] == 'unchange':
        return f'   {arg['key']}: {arg['value']}'
    else:
        return (f' - {arg['key']}: {arg['old_value']}\n'
            f' + {arg['key']}: {arg['new_value']}')

def check_diff(file1, file2):
    first_file = json.load(open(file1))
    second_file = json.load(open(file2))
    result1 = sorted_diff(first_file, second_file)
    itog = '\n'.join(map(formater, result1))
    return f'{'{'}\n{itog} \n{'}'}'
