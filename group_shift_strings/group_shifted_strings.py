# https://leetcode.com/problems/group-shifted-strings/

from collections import defaultdict

def group_strings(sstrings):
    def get_shift_key(s):
        l = []
        for i in range(1, len(s)):
            l.append((ord(s[i]) - ord(s[i-1])) % 26)
        return tuple(l)

    data = defaultdict(list)
    for s in strings:
        data[get_shift_key(s)].append(s)

    return list(data.values())

def _2d_list_to_set(l):
    tmp_set = set()
    for row in l:
        tmp_str = '-'.join([str(x) for x in row])
        tmp_set.add(tmp_str)
    return tmp_set

strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
expected = [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
assert _2d_list_to_set(group_strings(strings)) == _2d_list_to_set(expected)

strings = ['a']
expected = [['a']]
assert group_strings(strings) == expected
