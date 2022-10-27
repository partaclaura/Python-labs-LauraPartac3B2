#  Compare two dictionaries without using the operator "=="
#  returning True or False. (Attention, dictionaries must be
#  recursively covered because they can contain other containers,
#  such as dictionaries, lists, sets, etc.)

def compare(value1, value2):
    if isinstance(value1, dict) and isinstance(value2, dict):
        if value1.keys() != value2.keys():
            return False
        else:
            for k in value1.keys():
                if not compare(value1[k], value2[k]):
                    return False
            return True
    elif isinstance(value1, list) and isinstance(value2, list):
        if len(value1) != len(value2):
            return False
        else:
            for i in range(len(value1)):
                if not compare(value1[i], value2[i]):
                    return False
            return True
    else:
        if value1 != value2:
            return False
        else:
            return True


dict1 = {'a': [0, 1, 2], 'b': 12, 'c': {'1': 3, '2': 4}}
dict2 = {'a': [0, 1, 2], 'b': 12, 'c': {'1': 3, '2': 4}}

print(compare(dict1, dict2))
