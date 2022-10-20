# Write a function that receives a number x, default value equal to 1, a list of strings,
# and a boolean flag set to True. For each string, generate a list containing the characters
# that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain
# characters that have the ASCII code not divisible by x.


def ascii_divisible(lst, x = 1, flg = True):
    list_of_lists = []
    for lst_string in lst:
        char_list = []
        for c in lst_string:
            if flg and ord(c) % x == 0:
                char_list.append(c)
            elif flg is False and ord(c) % x != 0:
                char_list.append(c)
        list_of_lists.append(char_list)
    return list_of_lists


input_list = input("Give list of strings: ")
given_list = list(map(str, input_list.strip().split()))
input_x = int(input("Give x: "))
input_flag = str(input("Set flag to true(t) or false(f)?[t/f]: "))
f = True
if input_flag == "f":
    f = False
print(ascii_divisible(given_list, input_x, f))
