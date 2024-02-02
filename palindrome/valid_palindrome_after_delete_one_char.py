# https://leetcode.com/problems/valid-palindrome-ii/


def valid_palindrome(s):
    def is_palindrome_substr(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    i = 0
    k = len(s) - 1
    while i < k:
        if s[i] != s[k]:
            return is_palindrome_substr(s, i, k-1) or is_palindrome_substr(s, i+1, k)
        i += 1
        k -= 1
    return True

assert valid_palindrome('aba') == True

assert valid_palindrome('abca') == True

assert valid_palindrome('abc') == False
