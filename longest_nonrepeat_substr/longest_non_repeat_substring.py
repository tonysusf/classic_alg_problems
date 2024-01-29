# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_non_repeat_substring_len(s: str):
    left = 0
    lookup = {} # dict for char to index
    max_len = 0
    for i in range(len(s)):
        if s[i] in lookup and lookup[s[i]] >= left:
            left = lookup[s[i]] + 1 # index of 1st char non-repating
        lookup[s[i]] = i
        max_len = max(max_len, i - left + 1)
    return max_len


assert(longest_non_repeat_substring_len('abcabcbb') == 3)
assert(longest_non_repeat_substring_len('bbbbb') == 1)
assert(longest_non_repeat_substring_len('pwwkew') == 3)
assert(longest_non_repeat_substring_len('') == 0)
assert(longest_non_repeat_substring_len('a') == 1)
assert(longest_non_repeat_substring_len('ab') == 2)
assert(longest_non_repeat_substring_len('abba') == 2) # check dict index vs left case
