# https://leetcode.com/problems/fibonacci-number/

def fib(n):
    if n == 0: return 0
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    return b

assert fib(0) == 0
assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
