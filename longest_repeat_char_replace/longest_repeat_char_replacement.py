# https://leetcode.com/problems/longest-repeating-character-replacement/
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

from collections import defaultdict

def char_replacement(s, k):
    freq = defaultdict(int) # key as char, val as count
    left = max_freq = max_substr_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]]) # max frequency in the sliding window

        if not (right - left +1 - max_freq <= k): # not valid case, then move left pointer
            freq[s[left]] -= 1
            left += 1

        max_substr_len = right - left + 1
    return max_substr_len


s = 'ABAB'
k = 2
assert char_replacement(s, k) == 4


s = 'AABABBA'
k = 1
assert char_replacement(s, k) == 4


s = 'A'
k = 2
assert char_replacement(s, k) == 1


s = 'ABAC'
k = 2
assert char_replacement(s, k) == 4
