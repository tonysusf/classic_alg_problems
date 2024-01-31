# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#   1 2 3      7 4 1  (clockwise)
#   4 5 6  =>  8 5 2
#   7 8 9      9 6 3
#

# Algorithm: for a given row, col
# (1) swap, opposite new col
# (2) no swap, opposite both
# (3) swap, opposite new row
# swap is mirror by diagonal; opposite is mirror horizontally or vertically

def rotate_2d(m):
    n = len(matrix)
    def opposite(x): # 1 -> 1; 0 -> 2; 2->0
        return n - x -1
    for row in range(n//2 + n%2): # 2
        for col in range(n//2): # 1
            r1, c1 = col, opposite(row)
            r2, c2 = opposite(row), opposite(col)
            r3, c3 = opposite(col), row

            tmp = matrix[row][col]
            matrix[row][col] = matrix[r3][c3]
            matrix[r3][c3] = matrix[r2][c2]
            matrix[r2][c2] = matrix[r1][c1]
            matrix[r1][c1] = tmp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [[7,4,1],[8,5,2],[9,6,3]]
rotate_2d(matrix)
assert matrix == expected


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
rotate_2d(matrix)
assert matrix == expected
