# Write a functions that determine the most common
# letter in a string. For example if the string is
# "an apple is not a tomato", then the most common
# character is "a" (4 times). Only letters (A-Z or a-z)
# are to be considered. Casing should not be considered
# "A" and "a" represent the same character.

# UNDONE: "a" and "A" are the same letter

def most_common_letter(string1):
    d = {}
    for ch in string1:
        if ch in d:
            d[ch] = d[ch] + 1
        else:
            d[ch] = 1
    max_ap = 0
    max_ch = '\0'
    for ch in d:
        if d[ch] > max_ap:
            max_ap = d[ch]
            max_ch = ch
    return max_ch


input_string1 = str(input("Give the first string: "))

print(most_common_letter(input_string1))

