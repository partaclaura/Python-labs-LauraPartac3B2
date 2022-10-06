# Print the greatest common divisor of multiple numbers read from the console

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def compute_array_gcd(numbers, index):
    if index == len(numbers) - 1: #reached the last element of the array
        return numbers[index]
    a = numbers[index] #takes the numer stored at the currently reached index of the array
    b = compute_array_gcd(numbers, index + 1) #takes the computed gcd of the next pair of numbers (a, b)
    return gcd(a, b) # computes the gcd for this pair


numbers = [int(numbers) for numbers in input("Give multiple numbers: ").split()]
print("The gcd of the given numbers is ", compute_array_gcd(numbers, 0))

