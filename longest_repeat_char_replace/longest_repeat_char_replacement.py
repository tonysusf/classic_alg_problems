# https://leetcode.com/problems/longest-repeating-character-replacement/
# You are given a string s and an integer k. You can choose any character of the string and
# change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing
# the above operations.

from collections import defaultdict


# sliding window, window keep increasing or stay the same len. O(n)
def repeating_char_replacement_optimal(s, k):
    left = 0
    count = defaultdict(int)
    maxf = 0
    result = 0
    for i in range(len(s)):
        count[s[i]] += 1
        maxf = max(maxf, count[s[i]])
        # right increased by 1, if not valid, then increse left by 1
        # so total len same
        if (i - left + 1 - maxf) > k: # not valid then move left pointer
            count[s[left]] -= 1
            left += 1
        result = i - left + 1 # the window will increase or stay the same
    return result


# O(n * 26)
def repeating_char_replacement_easy(s, k):
    left = 0
    count = defaultdict(int)
    maxf = 0
    result = 0
    for i in range(len(s)):
        count[s[i]] += 1
        while (i - left + 1 - max(count.values())) > k: # not valid then move left pointer
            count[s[left]] -= 1
            left += 1
        result = max(result, i - left + 1)
    return result



assert repeating_char_replacement_optimal('ABAB', 2) == 4
assert repeating_char_replacement_optimal('AABABBA', 1) == 4
assert repeating_char_replacement_optimal('A', 2) == 1
assert repeating_char_replacement_optimal('ABAC', 2) == 4
assert repeating_char_replacement_optimal('AAABABBAXYZ', 1) == 5


assert repeating_char_replacement_easy('ABAB', 2) == 4
assert repeating_char_replacement_easy('AABABBA', 1) == 4
assert repeating_char_replacement_easy('A', 2) == 1
assert repeating_char_replacement_easy('ABAC', 2) == 4
assert repeating_char_replacement_easy('AAABABBAXYZ', 1) == 5
