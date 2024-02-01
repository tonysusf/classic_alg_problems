# https://leetcode.com/problems/add-strings


def add_strings(num1, num2):
    l = []
    carry = 0
    p1 = len(num1) - 1
    p2 = len(num2) - 1
    while p1 >= 0 or p2 >= 0:
        current = 0
        x1 = int(num1[p1]) if p1 >= 0 else 0
        x2 = int(num2[p2]) if p2 >= 0 else 0
        current = x1 + x2 + carry
        current, carry = current % 10, current // 10
        l.append(str(current))
        p1 -= 1
        p2 -= 1
    if carry:
        l.append(str(carry))
    l = l[::-1]
    return ''.join(l)

assert add_strings('11', '123') == '134'
assert add_strings('1', '1') == '2'
assert add_strings('456', '1') == '457'
assert add_strings('9', '99') == '108'
assert add_strings('9', '0') == '9'
assert add_strings('0', '0') == '0'