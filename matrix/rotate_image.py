# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
#   1 2 3      7 4 1  (clockwise)
#   4 5 6  =>  8 5 2
#   7 8 9      9 6 3
#

def rotate_2d(m):
    n = len(m[0])
    for col in range(n // 2 + n % 2): # i
        for row in range(n // 2): # j
            # 4 notes: (row to col, col to opposite as row - clockwise)
            # (1) n-row-1, col
            # (2) n-col-1, n-row-1
            # (3) row, n-col-1
            # (4) col, row

            tmp = m[n -row -1][col]

            m[n -row -1][col]       = m[n -col -1][n -row -1]
            m[n -col -1][n -row -1] = m[row]      [n -col -1]
            m[row]      [n -col -1] = m[col]      [row]
            m[col]      [row]       = tmp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [[7,4,1],[8,5,2],[9,6,3]]
rotate_2d(matrix)
assert matrix == expected


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
rotate_2d(matrix)
assert matrix == expected
