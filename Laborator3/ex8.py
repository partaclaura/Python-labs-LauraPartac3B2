# Write a function that receives a single dict parameter named mapping.
# This dictionary always contains a string key "start". Starting with
# the value of this key you must obtain a list of objects by iterating
# over mapping in the following way: the value of the current key is
# the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects
# obtained as previously described.

def loop(dictionary):
    previous = "start"
    current = dictionary["start"]
    stop = False
    result = []
    while stop is False:
        if previous == current:
            stop = True
        else:
            result.append(current)
            previous = current
            current = dictionary[current]
    return result


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
