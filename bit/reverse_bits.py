# https://leetcode.com/problems/reverse-bits/

def reverse_bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= (n & 1)
        n >>= 1
    return result


n = 0b00000010100101000001111010011100
assert reverse_bits(n) == 0b00111001011110000010100101000000

n = 0b11111111111111111111111111111101
assert reverse_bits(n) == 0b10111111111111111111111111111111

