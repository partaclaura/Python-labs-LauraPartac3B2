# Write a function that receives a list of numbers and returns a
# list of the prime numbers found in it.

from math import sqrt


def check_prime(number):
    if number == 1 or number == 0:
        return False
    else:
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
    return True


def extract_primes(number_list):
    primes = []
    for n in number_list:
        if check_prime(n):
            primes.append(n)
    return primes


given_input = input("Give a list of numbers (separated by space): ")
input_list = list(map(int, given_input.strip().split()))
print("List of prime numbers found: ", extract_primes(input_list))
