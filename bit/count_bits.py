# https://leetcode.com/problems/counting-bits/


def count_bits(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        # i & (i-1) drops the right-most 1 from a given i
        # index 0 got no 1s
        result[i] = result[i & (i - 1)] + 1
    return result


assert count_bits(2) == [0,1,1]

assert count_bits(5) == [0,1,1,2,1,2]

