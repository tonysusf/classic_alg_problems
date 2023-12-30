# https://leetcode.com/problems/number-of-1-bits/


def num_of_one_bits(n):
    c = 0
    while n>0:
        if n & 1 == 1:
            c += 1
        n = n >> 1
    return c

n = 0b00000000000000000000000000001011
assert num_of_one_bits(n) == 3

n = 0b00000000000000000000000010000000
assert num_of_one_bits(n) == 1

n = 0b11111111111111111111111111111101
assert num_of_one_bits(n) == 31
