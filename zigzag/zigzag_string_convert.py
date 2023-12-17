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
    zz_len = num_of_rows * 2 - 2 # num of chars of each zigzag
    num_of_zz = math.ceil(len(input_str) / zz_len) # num of zigzags
    results = []
    for row in range(num_of_rows): # row by row scan
        l = []
        for zz_idx in range(num_of_zz): # scan each zigzag for the row
            idx1 = zz_idx * zz_len + row
            if(idx1 < len(input_str)):
                l.append(input_str[idx1])
            idx2 = (zz_idx+1) * zz_len - row 
            if 0 < row < num_of_rows - 1 and idx2 < len(input_str):
                l.append(input_str[idx2])
        tmp_line = ''.join(l)
        results.append(tmp_line)
    return ''.join(results)

assert zigzag_convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert zigzag_convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
assert zigzag_convert('A', 1) == 'A'
assert zigzag_convert('AB', 2) == 'AB'
assert zigzag_convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
