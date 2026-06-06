# https://leetcode.com/problems/climbing-stairs/solution/


def climb_stairs(n):
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

assert climb_stairs(1) == 1
assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(4) == 5