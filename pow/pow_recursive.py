# https://leetcode.com/problems/powx-n/

# cases: n > 0, n = 0, n < 0

def my_pow(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n < 0:
        return 1 / my_pow(x, -n)
    if n % 2 == 1:
        return my_pow(x, n-1) * x
    tmp = my_pow(x, n/2)
    return tmp * tmp


assert my_pow(2, 3) == 8

assert my_pow(2, -3) == 1/8

assert my_pow(2, 0) == 1

assert my_pow(2, 4) == 16

assert my_pow(0, 3) == 0

assert my_pow(-3, 2) == 9
