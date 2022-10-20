# Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.
#
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2
# lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.


def x_appear(lists, x):
    d = {}
    for lst in lists:
        for element in lst:
            if element in d:
                d[element] = d.get(element) + 1
            else:
                d[element] = 1
    result = []
    for e in d.keys():
        if d.get(e) == x:
            result.append(e)
    return result


input_n = int(input("Give n (the number of lists): "))
list_of_lists = []
for i in range(input_n):
    in_list = input("Give list: ")
    new_list = list(map(str, in_list.strip().split()))
    list_of_lists.append(new_list)

input_x = int(input("Give x: "))
print("Resulted list: ", x_appear(list_of_lists, input_x))
