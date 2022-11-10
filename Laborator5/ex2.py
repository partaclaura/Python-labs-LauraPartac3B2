# Create a function and an anonymous function that receive a variable
# number of arguments. Both will return the sum of the values of the
# keyword arguments.
# Example:
# For the call my_function(1, 2, c=3, d=4) the returned value will be 7.
from functools import reduce

def my_function(*args, **kwargs):
    suma = 0
    for nr in kwargs.values():
        suma += nr
    return suma


def my_other_function(*args, **kwargs):
    return reduce(lambda a, b: a + b, kwargs.values())


print(my_function(1, 2, c=3, d=4))
s = my_other_function(1, 2, c=3, d=4)
print(s)
