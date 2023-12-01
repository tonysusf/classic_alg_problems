# https://leetcode.com/problems/palindrome-number/description/

def is_palindrome(x: int):
    print('x is', x)
    if x < 0:
        raise ValueError('Must be positive')
    l = []
    while x > 0:
        l.append(x % 10)
        x = x // 10
    for i in range(len(l)):
        if l[i] != l[-i-1]:
            return False
    return True


assert(is_palindrome(121) == True)
assert(is_palindrome(112) == False)
assert(is_palindrome(1) == True)
assert(is_palindrome(0) == True)
assert(is_palindrome(1221) == True)