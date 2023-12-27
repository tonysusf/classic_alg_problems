# https://leetcode.com/problems/rotate-image/description/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate_2d(matrix):
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp

matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [[7,4,1],[8,5,2],[9,6,3]]
rotate_2d(matrix)
assert matrix == expected

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
rotate_2d(matrix)
assert matrix == expected
