import json

def _sorted_diff(arg1, arg2):
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

def _is_bool(arg):
    if 'False' in arg or 'True' in arg:
        return str(arg).lower()
    else:
        return arg
    
def stylish_format(arg):
    if arg['status'] == 'add':
        return f' + {arg['key']}: {arg['value']}'
    elif arg['status'] == 'delete':
        return f' - {arg['key']}: {arg['value']}'
    elif arg['status'] == 'unchange':
        return f'   {arg['key']}: {arg['value']}'
    else:   
        return (f' - {arg['key']}: {arg['old_value']}\n'
            f' + {arg['key']}: {arg['new_value']}')
    
def _read_diff(file):
    if file.endswith('.json'):
        return json.load(open(file))
    else:
        raise ValueError('Unsupported format')

def check_diff(file1, file2):
    result1 = _sorted_diff(_read_diff(file1), _read_diff(file2))
    format = '\n'.join(map(stylish_format, result1))
    return f'{'{'}\n{_is_bool(format)} \n{'}'}'
