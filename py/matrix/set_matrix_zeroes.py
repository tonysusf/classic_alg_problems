# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix):
    print('input', matrix)
    set_first_col_zero = False
    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            set_first_col_zero = True
        for col in range(1, len(matrix[0])):
            if matrix[row][col]  == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if set_first_col_zero:
        for row in range(len(matrix)):
            matrix[row][0] = 0
    print('output', matrix)


def _to_str(l):
    for row in l:
        row.sort()
        for i in range(len(row)):
            row[i] = str(row[i])
    l = [','.join(k) for k in l]
    l.sort()
    out = '|'.join(l)
    return out

matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes(matrix)
assert _to_str(matrix) == _to_str([[1, 0, 1],[0, 0, 0],[1, 0, 1]])