#  Write a function that receives as parameter a list of numbers (integers)
#  and will return a tuple with 2 elements. The first element of the tuple will
#  be the number of palindrome numbers found in the list and the second element
#  will be the greatest palindrome number.

def is_palindrome(n):
    half = 0
    while n:
        half = half * 10 + n % 10
        n //= 10
        if n == half or n // 10 == half:
            return True
    return False


def palindromes_in_list(lst):
    count_palindromes = 0
    max_palindrome = 0
    result = tuple()
    for element in lst:
        if is_palindrome(element):
            count_palindromes += 1
            if element > max_palindrome:
                max_palindrome = element
    result = (count_palindromes, max_palindrome)
    return result


given_input = input("Give list of numbers: ")
list_input = list(map(int, given_input.strip().split()))
print(palindromes_in_list(list_input))

