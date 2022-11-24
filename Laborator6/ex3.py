"""
Write a function that receives as a parameter a string
of text characters and a list of regular expressions
and returns a list of strings that match on at least
one regular expression given as a parameter.
"""

import re


def find_matches(regex_list, texts):
    strings = []
    for reg in regex_list:
        for text in texts:
            if re.match(reg, text):
                strings += re.findall(reg, text)
    return strings


input_text = [str_in for str_in in input("Give string list: ").split()]
input_regex = [expr for expr in input("Give list of regex expressions:").split()]
print(find_matches(input_regex, input_text))
