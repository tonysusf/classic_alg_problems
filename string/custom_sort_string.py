# https://leetcode.com/problems/custom-sort-string/

from collections import defaultdict

def custom_sort_string(order, s):
    count = defaultdict(int)
    for char in s:
        count[char] += 1

    result = []
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]

    for char, count in count.items():
        result.append(char * count)
    return ''.join(result)


order = "cba"
s = "abcd"
assert custom_sort_string(order, s) == 'cbad'


order = "cbafg"
s = "abcd"
assert custom_sort_string(order, s) == 'cbad'

