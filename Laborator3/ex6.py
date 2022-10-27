# Write a function that receives as a parameter a list and returns a
# tuple (a, b), representing the number of unique elements in the list,
# and b representing the number of duplicate elements in the list
# (use sets to achieve this objective).

def get_tuple(lst):
    s = set(lst)
    count_unique = 0
    count_duplicate = 0
    for nr in s:
        if lst.count(nr) > 1:
            count_duplicate += 1
        else:
            count_unique += 1
    return tuple([count_unique, count_duplicate])


whatever_list = ["4", "5", "4", "7"]
print(get_tuple(whatever_list))
