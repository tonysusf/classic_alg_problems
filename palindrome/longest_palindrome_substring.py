# https://leetcode.com/problems/longest-palindromic-substring/


def expand_from_center(left, right, s):
    # 'aba' -> len is 3, l=1 r=1 -> l=0 r=2 -> ret 1
    # 'abba' -> len is 4, l=1, r=2 -> l=0, r=3 -> ret 2
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def find_longest_palindrome(s):
    ans = [0, 0] # left and right index
    for i in range(len(s)):
        odd_len = expand_from_center(i, i, s) # aba
        if odd_len > ans[1] - ans[0] + 1:
            dist = odd_len // 2
            ans = [i - dist, i + dist]

        even_len = expand_from_center(i, i + 1, s) # abba
        if even_len > ans[1] - ans[0] + 1:
            dist = (even_len // 2) - 1
            ans = [i - dist, i + 1 + dist]

    return s[ans[0]: ans[1] + 1]


assert find_longest_palindrome('babad') == 'bab'

assert find_longest_palindrome('cbbd') == 'bb'

assert find_longest_palindrome('a') == 'a'

assert find_longest_palindrome('aacabdkacaa') == 'aca' # this case for LCA
