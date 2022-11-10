# Using functions, anonymous functions, list comprehensions and filter,
# implement three methods to generate a list with all the vowels in a
# given string.
# For the string "Programming in Python is fun" the list returned will
# be ['o', 'a', 'i', 'i', 'o', 'i', 'u'].


def v_1(string):
    return [ch for ch in string if ch in "aeiouAEIOU"]


def v_2(string):
    vowels = filter(lambda ch: ch in "aeiouAEIOU", string)
    return list(vowels)


def v_3(string):
    vowels = []
    for ch in string:
        if ch in "aeiouAEIOU":
            vowels.append(ch)
    return vowels


given_string = "Programming in Python is fun"
print(v_1(given_string))
print(v_2(given_string))
print(v_3(given_string))
