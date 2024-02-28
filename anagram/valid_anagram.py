# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

assert is_anagram('anagram', 'nagaram') == True

assert is_anagram('rat', 'cat') == False
