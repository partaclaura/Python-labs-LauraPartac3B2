"""
Verify using a regular expression whether a string is a valid CNP.
"""

import re


def find_matches(text):
    reg = "[1-8]\\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\\d|3[0-1])(0[1-9]|1[0-9]|2[0-9]|3[0-9]|4[0-6]|5[1-2])(001|[1-9][" \
          "1-9][0-9])\\d"
    if len(text) < 13:
        return False
    if re.match(reg, text):
        return True
    return False


input_text = str(input("Give CNP: "))
print(find_matches(input_text))
