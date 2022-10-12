# Write a function that validates
# if a number is a palindrome

def is_palindrome(n):
    half = 0
    while n:
        half = half * 10 + n % 10
        n //= 10
        if n == half or n // 10 == half:
            return True
    return False


number = int(input("Give number: "))
if is_palindrome(number):
    print("is palindrome")
else:
    print("is not palindrome")
