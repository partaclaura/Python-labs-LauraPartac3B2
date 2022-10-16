# Write a function that receives as parameters two lists a and b and
# returns: (a intersected with b, a reunited with b, a - b, b - a)


def a_minus_b(a, b):
    return [element for element in a if element not in b]


def reunion(a, b):
    a_or_b = []
    for element in b:
        if element not in a:
            a_or_b.append(element)
    for element in a:
        if element not in a_or_b:
            a_or_b.append(element)
    return a_or_b


def intersection(a, b):
    return [element for element in a if element in b]


given_input_a = input("Give list A (separated by space): ")
input_a = list(map(int, given_input_a.strip().split()))
given_input_b = input("Give list B (separated by space): ")
input_b = list(map(int, given_input_b.strip().split()))
print("A intersected with B: ", intersection(input_a, input_b))
print("A reunited with B: ", reunion(input_a, input_b))
print("A-B: ", a_minus_b(input_a, input_b))
print("B-A: ", a_minus_b(input_b, input_a))
