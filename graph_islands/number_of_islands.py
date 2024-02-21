# https://leetcode.com/problems/number-of-islands/

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
    return count


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

assert num_of_islands(grid) == 3
