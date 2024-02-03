# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


def min_add_to_make_valid(s):
    l = 0 # open count to be matched
    r = 0 # close count to be matched
    for char in s:
        if char == '(':
            l += 1
        elif char == ')' and l > 0:
            l -= 1
        else: # char is ')' without open ones
            r += 1
    return l + r


assert min_add_to_make_valid('())') == 1

assert min_add_to_make_valid('(((') == 3

assert min_add_to_make_valid('()))((') == 4

assert min_add_to_make_valid(')())') == 2