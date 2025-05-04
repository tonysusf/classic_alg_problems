# https://leetcode.com/problems/counting-bits/

# Brian Kernighan’s algorithm
def count_bits(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        # i & (i-1) drops the right-most 1 from a given i
        # index 0 got no 1s
        result[i] = result[i & (i - 1)] + 1
    return result


def count_bits_v2(n):
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + (i & 1)
    return res


assert count_bits(2) == [0,1,1]

assert count_bits(5) == [0,1,1,2,1,2]

