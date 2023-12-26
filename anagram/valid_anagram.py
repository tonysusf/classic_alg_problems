# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

def is_anagram(s, t):
    c1 = Counter(s)
    c2 = Counter(t)
    return c1 == c2

assert is_anagram('anagram', 'nagaram') == True

assert is_anagram('rat', 'cat') == False
