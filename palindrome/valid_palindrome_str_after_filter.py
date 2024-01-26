# https://leetcode.com/problems/valid-palindrome/

def is_palindrome(s):
    l = [c.lower() for c in s if c.isalnum()]
    return l == l[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True

assert is_palindrome('race a car') == False

assert is_palindrome(' ') == True
