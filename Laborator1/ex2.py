# Write a script that calculates how many vowels are in a string

def check_for_vowels(given_string):
    n_of_vowels = 0
    for ch in given_string:
        if ch in "aeiou":
            n_of_vowels = n_of_vowels + 1
    return n_of_vowels


input_string = str(input("Give string: "))
print("Number of vowels in given string: ", check_for_vowels(input_string))

