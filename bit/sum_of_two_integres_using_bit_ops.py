# https://leetcode.com/problems/sum-of-two-integers/


def get_sum(a, b):
    MAX = 0x7FFFFFFF # out of 32 bits 31 of them are 1s.
    mask = 0xFFFFFFFF # 1s in all 32 bit

    while b != 0:
        # xor is sum without carry
        # and with shift is the carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    result = None
    if a <= MAX: # positive
        result = a
    else:
        # negative in binary:
        # https://en.wikipedia.org/wiki/Two%27s_complement
        result = ~(a ^ mask)
    return result


assert get_sum(1, 2) == 3

assert get_sum(2, 3) == 5

assert get_sum(-1, 2) == 1

assert get_sum(-1, -2) == -3