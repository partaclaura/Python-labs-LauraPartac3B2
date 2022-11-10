from math import sqrt


def check_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def process_item(x):
    number = x + 1
    found = False
    while not found:
        if check_prime(number):
            return number
        number += 1


if __name__ == '__main__':
    input_number = int(input("Give number: "))
    print("The least prime number greater the given number: ", process_item(input_number))

