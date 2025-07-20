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

#def is_bool(arg):
    #if 'False' in arg or 'True' in arg:
     #   return str(arg).lower()
    #else:
     #   return arg
    
def stylish_format(diff):
    lines= []
    for item in diff:
        status = diff['status']
        key = diff['key']
        if status == 'unchange':
            lines.append(f' {key}: {item['value']}')
        elif status == 'add':
            lines.append(f'+ {key}: {item['value']}')
        elif status == 'delete':
            lines.append(f'- {key}: {item['value']}')
        elif status == 'change':
            lines.append(f'- {key}: {item['old_value']}')
            lines.append(f'+ {key}: {item['new_value']}')
        return "{\n  " + "\n  ".join(lines) + "\n}"

def read_diff(file):
    if file.endswith('.json'):
        return json.load(open(file))
    else:
        raise ValueError('Unsupported format')


