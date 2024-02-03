# https://leetcode.com/problems/toeplitz-matrix/description/

def is_toeplitz_matrix(m):
    for row in range(1, len(m)):
        for col in range(1, len(m[0])):
            if m[row][col] != m[row-1][col-1]:
                return False
    return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
assert is_toeplitz_matrix(matrix) == True

matrix = [[1,2],[2,2]]
assert is_toeplitz_matrix(matrix) == False
