# Write a script that receives two strings and prints the number of
# occurrences of the first string in the second

def check_for_occurrences(string1, string2):
    # n_of_occurrences = 0
    if len(string1) > len(string2):
        return 0
    return string2.count(string1)


input_string1 = str(input("Give the first string: "))
input_string2 = str(input("Give the second string: "))

print("Number of occurrences: ", check_for_occurrences(input_string1, input_string2))

