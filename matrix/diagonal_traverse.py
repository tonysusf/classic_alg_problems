# https://leetcode.com/problems/diagonal-traverse/

def find_diagonal_order(m):
    if not m or not m[0]: return []
    num_of_rows, num_of_cols = len(m), len(m[0])
    row = col = 0
    up = True
    result = []
    while row < num_of_rows and col < num_of_cols:
        result.append(m[row][col])

        tmp_row = row + (-1 if up else 1)
        tmp_col = col + (1 if up else -1)

        if not(0 <= tmp_row < num_of_rows) or not(0 <= tmp_col < num_of_cols):
            if up:
                tmp_row = row + (1 if col == num_of_cols - 1 else 0)
                tmp_col = col + (1 if col < num_of_cols - 1 else 0)
            else:
                tmp_row = row + (1 if row < num_of_rows - 1 else 0)
                tmp_col = col + (1 if row == num_of_rows - 1 else 0)
            up = not up

        row, col = tmp_row, tmp_col

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [1,2,4,7,5,3,6,8,9]
assert find_diagonal_order(matrix) == expected


matrix = [[1,2],[3,4]]
expected =[1,2,3,4]
assert find_diagonal_order(matrix) == expected
