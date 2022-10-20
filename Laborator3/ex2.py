# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters
# in the character string and the values are the number of occurrences of that character in the given text.
#
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .


def char_occurrences(phrase):
    occurrences = {}
    for ch in phrase:
        if ch in occurrences:
            occurrences[ch] = occurrences.get(ch) + 1
        else:
            occurrences[ch] = 1
    return occurrences


input_string = str(input("Give string: "))
print(char_occurrences(input_string))
