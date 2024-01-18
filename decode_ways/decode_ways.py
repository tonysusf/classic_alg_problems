# https://leetcode.com/problems/decode-ways/

# '12': dp [1], [1, 2]
# '226': dp [1], [1, 2, 3]


def num_decodings(s):
    if s[0] == '0': return 0
    back2 = 1
    back1 = 1
    for i in range(1, len(s)):
        current = 0
        if s[i] != '0':
            current += back1
        two_digit = int(s[i - 1: i + 1])
        if 10 <= two_digit <= 26:
            current += back2
        back1, back2 = current, back1
    return back1

assert num_decodings('12') == 2

assert num_decodings('226') == 3

assert num_decodings('09') == 0

assert num_decodings('206') == 1

assert num_decodings('7906') == 0