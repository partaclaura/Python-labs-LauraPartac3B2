"""
Write a function that extracts the words from a given text
as a parameter. A word is defined as a sequence of
alpha-numeric characters.
"""

import re


def split_words(given_text):
    return re.split(r"\s+['-]\s*|['-]\s+|[^0-9a-zA-Z-']+", given_text)


input_text = input("Give text: ")
print(split_words(input_text))
