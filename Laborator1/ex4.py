# Write a script that converts a string of characters written in
# UpperCamelCase into lowercase_with_underscores.

def create_new_format(given_string):
    new_string = given_string[0].lower()
    for i in range(1, len(given_string)):
        if given_string[i].isupper():
            new_string = new_string + '_'
        new_string = new_string + given_string[i].lower()
    return new_string


input_string = input("Give string: ")
print(create_new_format(input_string))
