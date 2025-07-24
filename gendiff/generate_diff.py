from parser import read_diff


def sorted_diff(arg1, arg2):
    result = []
    for key in sorted(arg1 | arg2):
        if key not in arg2:
            result.append({'key': key, 'status': 'delete', 'value': arg1[key]})
        elif key not in arg1:
            result.append({'key': key, 'status': 'add', 'value': arg2[key]})
        elif key in arg1 and key in arg2:
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
    return result


def is_bool(arg):
    if arg is False or arg is True:
        return str(arg).lower()
    else:
        return arg
    

def stylish_format(diff):
    lines = []
    for item in diff:
        status = item['status']
        key = item['key']
        if status == 'unchange':
            lines.append(f'  {key}: {is_bool(item['value'])}')
        elif status == 'add':
            lines.append(f'+ {key}: {is_bool(item['value'])}')
        elif status == 'delete':
            lines.append(f'- {key}: {is_bool(item['value'])}')
        elif status == 'change':
            lines.append(f'- {key}: {is_bool(item['old_value'])}')
            lines.append(f'+ {key}: {is_bool(item['new_value'])}')
    return "{\n  " + "\n  ".join(lines) + "\n}"


def generate_diff(file1, file2):
    read_file1 = read_diff(file1)
    read_file2 = read_diff(file2)
    sort_diff = sorted_diff(read_file1, read_file2)
    return stylish_format(sort_diff)


