# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# return the valid string after removals. no need to count how many being removed.

def min_remove_to_make_valid(s):
    chars = list(s)
    stack = []

    for i, char in enumerate(chars):
        if char == "(":
            stack.append(i)

        elif char == ")":
            if stack:
                stack.pop()
            else:
                chars[i] = ""

    for i in stack:
        chars[i] = ""

    out = "".join(chars)
    print('output is', out)
    return out

assert min_remove_to_make_valid('lee(t(c)o)de)') == 'lee(t(c)o)de'

assert min_remove_to_make_valid('a)b(c)d') == 'ab(c)d'

assert min_remove_to_make_valid('))((') == ''