"""
Write a function that, for a text given as a parameter,
censures words that begin and end with vowels. Censorship
means replacing characters from odd positions with *.
"""

import re


def censor(word):
    new_word = ''
    for i in range(len(word)):
        if i % 2 == 0:
            new_word += '*'
        else:
            new_word += word[i]
    return new_word


def verify_text(text):
    text = re.split(r"\s+['-]\s*|['-]\s+|[^0-9a-zA-Z-']+", text)
    verified = ""
    for word in text:
        if re.match("^[aeiouAEIOU]\\w*[aeiouAEIOU]$", word):
            verified += censor(word)
        else:
            verified += word
        verified += " "

    return verified[:-1]


input_text = input("Give text: ")
print(verify_text(input_text))
