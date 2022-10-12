# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated
# by only ONE space. For example: "I have Python exam" has 4 words.


def count_words(given_string):

    count = given_string.count(' ') + 1
    print(count)


in_string = str(input("Give string: "))
count_words(in_string)



