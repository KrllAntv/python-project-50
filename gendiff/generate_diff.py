from gendiff.formatters.formatter import format
from gendiff.parser import read_diff


def sorted_diff(arg1, arg2):
    result = []
    for key in sorted(arg1 | arg2):
        if key in arg1 and key in arg2:
            if isinstance(arg1[key], dict) and isinstance(arg2[key], dict):
                result.append(
                    {
                        "key": key, 
                        "status": "nested",
                        "value": sorted_diff(arg1[key], arg2[key])
                    }
                )
                continue
            if arg1[key] == arg2[key]:
                result.append(
                    {
                        "key": key,
                        "status": "unchange",
                        "value": arg1[key],
                    }
                )
            else: 
                result.append(
                    {
                        "key": key, 
                        "status": "change",
                        "old_value": arg1[key],
                        "new_value": arg2[key],
                    }
                )
        elif key not in arg2:
            result.append(
                {
                    "key": key, 
                    "status": "delete", 
                    "value": arg1[key],
                }
            )
        elif key not in arg1:
            result.append(
                {
                    "key": key, 
                    "status": "add", 
                    "value": arg2[key],
                }
            )
    return result


def generate_diff(file1, file2, format_name):
    read_file1 = read_diff(file1)
    read_file2 = read_diff(file2)
    sort_diff = sorted_diff(read_file1, read_file2)
    return format(sort_diff, format_name)
