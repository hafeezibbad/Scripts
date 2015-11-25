#!/usr/bin/python
__author__ = 'eb'
x = {'a': 1, 'b': 2}
y = {'a': 3, 'c': 4}
z = {'c': 6, 'b': 3}

def merge_dict(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)

    return result

def combine_dicts(*args):
    result = {}
    for dictionary in args:
        for key in dictionary:
            if key not in result:
                result[key] = [dictionary[key]]
            else:
                result[key].append(dictionary[key])

    return result

# print merge_dict(x, y)
print combine_dicts(x, y, z)
