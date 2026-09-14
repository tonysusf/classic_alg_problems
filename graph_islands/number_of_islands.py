# https://leetcode.com/problems/number-of-islands/

from typing import *
import copy

def num_of_islands(grid):
    count = 0

    def dfs(r, c):
        nonlocal grid
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])): return
        if grid[r][c] == '0': return
        grid[r][c] = '0'
        dfs(r, c-1)
        dfs(r, c+1)
        dfs(r-1, c)
        dfs(r+1, c)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                count += 1
                dfs(row, col)
    print('output is', count)
    return count


def num_of_islands_v2(grid: List[List[str]]) -> int:
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '0':
                continue;
            count += 1
            stack = []
            stack.append((r, c))
            while stack:
                curr = stack.pop()
                for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    rr = curr[0] + direction[0]
                    cc = curr[1] + direction[1]
                    if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and grid[rr][cc] == '1':
                        grid[rr][cc] = '0'
                        stack.append((rr,cc))
    print('output is', count)
    return count


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
grid2 = copy.deepcopy(grid)

assert num_of_islands(grid) == 3
assert num_of_islands_v2(grid2) == 3
