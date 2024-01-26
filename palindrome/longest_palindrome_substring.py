# https://leetcode.com/problems/longest-palindromic-substring/

def max_len_expand(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def find_longest_palindrome(s):
    p1 = p2 = 0 # index for 1st and last char in palindrome
    for i in range(len(s)):
        max_len = max_len_expand(i, i, s) # 'maban'
        if p2 - p1 + 1 < max_len:
            p1 = i - max_len // 2
            p2 = i + max_len // 2

        max_len = max_len_expand(i, i + 1, s) # 'maan', 'mabba'
        if p2 - p1 + 1 < max_len:
            p1 = i - max_len // 2 + 1
            p2 = i + max_len // 2

    return s[p1: p2+1]


assert find_longest_palindrome('babad') == 'bab'

assert find_longest_palindrome('cbbd') == 'bb'

assert find_longest_palindrome('a') == 'a'

assert find_longest_palindrome('aacabdkacaa') == 'aca' # this case for LCA
