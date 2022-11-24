"""
Write a function that receives as a parameter
a regex string, a text string and a whole number x,
and returns those long-length x substrings that
match the regular expression.
"""

import re


def find_matches(regex_string, text, x):
    result = []
    for substring in re.findall(regex_string, text):
        if len(substring) == x:
            result.append(substring)
    return result


input_text = input("Give text: ")
input_regex = input("Give regex:")
input_x = int(input("Give x: "))
print(find_matches(input_regex, input_text, input_x))
