# Write a function that extract a number from a text
# (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc"
# the function will extract 123). The function will extract only
# the first number that is found.
import re


def extract_number(given_string):

    found = re.search('\\d*\\d', given_string)
    if found is None:
        print(None)
    else:
        print(found.group())


in_string = str(input("Give string: "))
extract_number(in_string)



