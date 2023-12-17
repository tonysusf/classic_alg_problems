# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_non_repeat_substring_len(s: str):
    print('s is', s)
    l = 0 # left pointer
    lookup = {} # dict for char to index
    max_len = 0
    for i in range(len(s)):
        c = s[i]
        if c in lookup and lookup[c] >= l:
            l = lookup[c] + 1 # point l to be after the duplicate, +1 so no duplicate
        lookup[c] = i # save the current char with index
        max_len = max(max_len, i - l + 1)
    return max_len


assert(longest_non_repeat_substring_len('abcabcbb') == 3)
assert(longest_non_repeat_substring_len('bbbbb') == 1)
assert(longest_non_repeat_substring_len('pwwkew') == 3)
assert(longest_non_repeat_substring_len('') == 0)
assert(longest_non_repeat_substring_len('a') == 1)
assert(longest_non_repeat_substring_len('ab') == 2)
