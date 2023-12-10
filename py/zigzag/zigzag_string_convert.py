# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

import math

def zigzag_convert(input_str, num_of_rows):
    if num_of_rows == 1:
        return input_str
    z_len = num_of_rows * 2 - 2 # num of chars of each zigzag
    n = math.ceil(len(input_str) / z_len) # num of zigzags
    result = [[] for k in range(num_of_rows)] # init
    for z_idx in range(n):
        for row in range(num_of_rows):
            idx = z_idx * z_len + row # index in the input string
            if(idx < len(input_str)):
                result[row].append(input_str[idx])
            idx2 = (z_idx+1) * z_len - row
            if row > 0 and row < num_of_rows - 1 and idx2 < len(input_str):
                result[row].append(input_str[idx2])
    return ''.join([''.join(row) for row in result])

assert zigzag_convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert zigzag_convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
assert zigzag_convert('A', 1) == 'A'
assert zigzag_convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
