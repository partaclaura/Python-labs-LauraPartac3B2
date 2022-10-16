# Write a function to return a list of the first n numbers
# in the Fibonacci string.

def first_n_fibonacci(n):
    if n < 0:
        return []
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        n_fib = first_n_fibonacci(n-1)
        n_fib.append(n_fib[-1] + n_fib[-2])
        return n_fib


n_input = int(input("Give n: "))
print("The first ", n_input, "numbers in the Fibonacci sequence: ", first_n_fibonacci(n_input)[1:])
