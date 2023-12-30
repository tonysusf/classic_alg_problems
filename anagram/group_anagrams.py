# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

def group_anagrams(strs):
    result = defaultdict(list)
    for s in strs:
        arr = [0] * 26
        for chr in s:
            arr[ord(chr) - ord('a')] += 1
        result[tuple(arr)].append(s)
    return result.values()


def __sort_2d(m):
    for row in m:
        row.sort()


strs = ["eat","tea","tan","ate","nat","bat"]
expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
assert __sort_2d(group_anagrams(strs)) == __sort_2d(expected)


strs = []
expected = []
assert __sort_2d(group_anagrams(strs)) == __sort_2d(expected)


strs = ['a']
expected = [['a']]
assert __sort_2d(group_anagrams(strs)) == __sort_2d(expected)
