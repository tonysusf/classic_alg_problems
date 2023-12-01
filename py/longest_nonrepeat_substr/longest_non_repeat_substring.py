# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_non_repeat_substring_len(s: str):
    print('s is', s)
    l = r = 0 # left and right pointer for sliding window
    lookup = {} # dict for char to index
    max_len = 0
    for i in range(len(s)):
        k = s[i]
        r += 1
        if k in lookup and lookup[k] >= l:
            l = lookup[k] + 1
        lookup[k] = i
        max_len = max(max_len, r - l)
    return max_len


assert(longest_non_repeat_substring_len('abcabcbb') == 3)
assert(longest_non_repeat_substring_len('bbbbb') == 1)
assert(longest_non_repeat_substring_len('pwwkew') == 3)
