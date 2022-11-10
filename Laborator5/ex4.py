# Write a function that receives a variable number of arguments and keyword
# arguments. The function returns a list containing only the arguments which
# are dictionaries, containing minimum 2 keys and at least one string key with
# minimum 3 characters.
# Example:
# my_function(
#  {1: 2, 3: 4, 5: 6},
#  {'a': 5, 'b': 7, 'c': 'e'},
#  {2: 3},
#  [1, 2, 3],
#  {'abc': 4, 'def': 5},
#  3764,
#  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
#  test={1: 1, 'test': True}
# )
# will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]


def has_ch(dictionary):
    for k in dictionary.keys():
        if isinstance(k, str) and len(k) >= 3:
            return True
    return False


def verify_conditions(lst):
    return [element for element in lst if isinstance(element, dict) and
            len(element.keys()) >= 2 and has_ch(element)]


def my_function(*args, **kwargs):
    return verify_conditions(args) + verify_conditions(kwargs.values())


print(my_function({1: 2, 3: 4, 5: 6},
                  {'a': 5, 'b': 7, 'c': 'e'},
                  {2: 3},
                  [1, 2, 3],
                  {'abc': 4, 'def': 5},
                  3764,
                  dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
                  test={1: 1, 'test': True}))
