# https://leetcode.com/problems/simplify-path/


def simplify_path(path):
    stack = []
    l = path.split('/')
    for k in l:
        if k == '.' or not k:
            continue
        elif k == '..':
            if stack: stack.pop()
        else:
            stack.append(k)
    return '/' + '/'.join(stack)

assert simplify_path('/home/') == '/home'

assert simplify_path('/../') == '/'

assert simplify_path('/home//foo') == '/home/foo'

assert simplify_path('/home/./xyz') == '/home/xyz'