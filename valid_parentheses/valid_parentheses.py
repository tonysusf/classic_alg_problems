# https://leetcode.com/problems/valid-parentheses/description/


def valid_parentheses(input_str):
    print("input_str is", input_str)
    stack = []
    lookup = {
        ')': '(',
        ']': '[',
        '}': '{',
    }
    for chr in input_str:
        if chr in '([{':
            stack.append(chr)
        else:
            if not stack: # stack empty nothing to match
                return False
            t = stack.pop()
            # print('look for', t)
            if lookup[chr] != t:
                return False
    if stack: # something left in stack still
        return False
    return True


assert(valid_parentheses('()') == True)

assert(valid_parentheses('(') == False)

assert(valid_parentheses('([])') == True)

assert(valid_parentheses(')') == False)

assert(valid_parentheses('([{}])') == True)

assert(valid_parentheses('(}') == False)
