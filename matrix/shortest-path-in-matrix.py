# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque

def shortest_path_matrix(m):
    n = len(m)
    if m[0][0] != 0 or m[n-1][n-1] != 0: return -1

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    queue = deque([(0, 0, 1)])  # tuple as row, col, path len

    while queue:
        row, col, path_len = queue.popleft()
        if row == n-1 and col == n-1:
            return path_len
        for dr, dc in directions:
            tmp_row, tmp_col = row + dr, col + dc
            if 0 <= tmp_row < n and 0 <= tmp_col < n and m[tmp_row][tmp_col] == 0:
                m[tmp_row][tmp_col] = 1  # mark as visited!
                queue.append((tmp_row, tmp_col, path_len+1))
    return -1


grid = [[0,0,0],[1,1,0],[1,1,0]]
assert shortest_path_matrix(grid) == 4

grid = [[1,0,0],[1,1,0],[1,1,0]]
assert shortest_path_matrix(grid) == -1
