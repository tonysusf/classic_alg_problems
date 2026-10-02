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

def spiral_matrix_traverse_v2(matrix):
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    result = []

    while top <= bottom and left <= right:
        for c in range(left,right+1):
            result.append(matrix[top][c])
        top += 1
        for r in range(top,bottom+1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right,left-1,-1):
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom,top-1,-1):
                result.append(matrix[r][left])
            left += 1
    return result


assert spiral_matrix_traverse([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert spiral_matrix_traverse_v2([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]

assert spiral_matrix_traverse([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert spiral_matrix_traverse_v2([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
