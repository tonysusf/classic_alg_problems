# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_col = any(matrix[r][0] == 0 for r in range(m))
    first_row = any(matrix[0][c] == 0 for c in range(n))
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][c] == 0:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(1, m):
        for c in range(1, n):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if first_row:
        for c in range(n): matrix[0][c] = 0
    if first_col:
        for r in range(m): matrix[r][0] = 0


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

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes(matrix)
assert _to_str(matrix) == _to_str([[0,0,0,0],[0,4,5,0],[0,3,1,0]])
