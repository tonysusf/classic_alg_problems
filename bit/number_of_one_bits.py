# https://leetcode.com/problems/number-of-1-bits/


def num_of_one_bits(n):
    print(f"{n} = {n:b}")
    c = 0
    while n>0:
        if n & 1 == 1:
            c += 1
        n = n >> 1
    return c

def hamming_weight(n):
    print(f"{n} = {n:b}")
    count = 0
    while n:
        n &= n-1
        count += 1
    return count

n = 0b00000000000000000000000000001011
assert num_of_one_bits(n) == 3
assert hamming_weight(n) == 3

n = 0b00000000000000000000000010000000
assert num_of_one_bits(n) == 1
assert hamming_weight(n) == 1

n = 0b11111111111111111111111111111101
assert num_of_one_bits(n) == 31
assert hamming_weight(n) == 31

# 0 has no 1 bits
assert num_of_one_bits(0) == 0

# 1 = 1
assert num_of_one_bits(1) == 1

# 2 = 10
assert num_of_one_bits(2) == 1

# 3 = 11
assert num_of_one_bits(3) == 2

# 7 = 111
assert num_of_one_bits(7) == 3

# 8 = 1000
assert num_of_one_bits(8) == 1

# 13 = 1101
assert num_of_one_bits(13) == 3

# 15 = 1111
assert num_of_one_bits(15) == 4

# 16 = 10000
assert num_of_one_bits(16) == 1

# 255 = 11111111
assert num_of_one_bits(255) == 8

