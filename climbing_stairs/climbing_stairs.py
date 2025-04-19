# https://leetcode.com/problems/climbing-stairs/solution/


def climb_stairs(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    a = 1
    b = 2
    for i in range(n-2): # fibonacci 
        c = a + b
        a, b = b, c
    return b

assert climb_stairs(1) == 1
assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(4) == 5