"""
Write a function that recursively scrolls a directory and displays those
files whose name matches a regular expression given as a parameter or
contains a string that matches the same expression. Files that satisfy
both conditions will be prefixed with ">>"
"""

import re
import os


def search_in_content(file):
    with open(file, "r") as fd:
        return str(fd.read())


def find_matches(reg, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            found = 0
            if re.match(reg, file):
                found += 1
            if re.match(reg, search_in_content(os.path.join(root, file))):
                found += 1
            if found == 2:
                print(">>", file)
            elif found == 1:
                print(file)


input_regex = input("Give regex expr: ")
directory = input("Give directory path: ")
find_matches(input_regex, directory)
