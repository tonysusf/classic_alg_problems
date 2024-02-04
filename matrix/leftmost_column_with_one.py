# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/


class BinaryMatrix(object):
    def __init__(self, m):
        self.m = m

    def get(self, row, col):
        return self.m[row][col]

    def dimensions(self) :
        return (len(self.m), len(self.m[0]))


def left_most_column_with_one(binary_matrix):
    num_of_rows, num_of_cols = binary_matrix.dimensions()
    row = 0
    col = num_of_cols - 1

    # go down and left
    while row < num_of_rows and col >= 0:
        if binary_matrix.get(row, col) == 0:
            row += 1 # 1 found on current row, go to next row
        else:
            col -= 1 # try find 1 on current row
    return col+1 if col != num_of_cols-1 else -1

m = BinaryMatrix([[0,0],[1,1]])
assert left_most_column_with_one(m) == 0

m = BinaryMatrix([[0,0],[0,1]])
assert left_most_column_with_one(m) == 1

m = BinaryMatrix([[0,0],[0,0]])
assert left_most_column_with_one(m) == -1