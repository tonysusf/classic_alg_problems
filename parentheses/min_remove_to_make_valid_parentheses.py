# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

def min_remove_to_make_valid(s):
    # remove invalid close parentheses
    tmp_list = []
    open_balance = 0
    open_count = 0
    for c in s:
        if c == "(":
            open_balance += 1
            open_count += 1
        if c == ")":
            if open_balance == 0:
                continue
            open_balance -= 1
        tmp_list.append(c)
    open_used = open_count - open_balance

    # remove unused open parentheses from the right side
    result = []
    for c in tmp_list:
        if c == "(":
            if open_used <= 0:
                continue
            open_used -= 1
        result.append(c)

    return "".join(result)

assert min_remove_to_make_valid('lee(t(c)o)de)') == 'lee(t(c)o)de'

assert min_remove_to_make_valid('a)b(c)d') == 'ab(c)d'

assert min_remove_to_make_valid('))((') == ''