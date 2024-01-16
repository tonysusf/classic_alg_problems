# https://leetcode.com/problems/spiral-matrix/
# traverse the matrix in spiral way

def spiral_matrix_traverse(matrix):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    row = col = 0
    result = [matrix[0][0]]
    matrix[0][0] = None
    total = len(matrix) * len(matrix[0])
    while len(result) < total:
        while True:
            next_row = row + dirs[current_dir][0]
            next_col = col + dirs[current_dir][1]

            if not (0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0])):
                break
            if matrix[next_row][next_col] == None:
                break

            row, col = next_row, next_col
            result.append(matrix[row][col])
            matrix[row][col] = None

        current_dir = (current_dir + 1) % 4
    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]
assert spiral_matrix_traverse(matrix) == [1,2,3,6,9,8,7,4,5]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
assert spiral_matrix_traverse(matrix) == [1,2,3,4,8,12,11,10,9,5,6,7]
