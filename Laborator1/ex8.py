# Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"


def count_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    print(count)


n = int(input("Give number: "))
count_bits(n)



