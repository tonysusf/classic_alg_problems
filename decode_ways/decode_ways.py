# https://leetcode.com/problems/decode-ways/

# '12': dp [1], [1, 2]
# '226': dp [1], [1, 2, 3]


def num_decodings(s):
    if not s or s[0] == '0': return 0
    b1 = b2 = 1
    for i in range(1, len(s)):
        current = b1 if s[i] != '0' else 0
        if 10 <= int(s[i - 1: i + 1]) <= 26:
            current += b2
        b1, b2 = current, b1
    return b1

assert num_decodings('1') == 1

assert num_decodings('10') == 1

assert num_decodings('12') == 2

assert num_decodings('102') == 1

assert num_decodings('226') == 3

assert num_decodings('09') == 0

assert num_decodings('206') == 1

assert num_decodings('7906') == 0

assert num_decodings('') == 0