# https://leetcode.com/problems/number-of-islands/

def num_of_islands(grid):
    print('grid is', grid)
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "1":
                count += 1
                visit(grid, row, col)
    print('num of islands is', count)
    return count

def visit(grid, row, col):
    if grid[row][col] != "1":
        return
    grid[row][col] = "0"
    if row > 0: # go up
        visit(grid, row-1, col)
    if col > 0: # go left
        visit(grid, row, col-1)
    if row < len(grid)-1: # go down
        visit(grid, row+1, col)
    if col < len(grid[0])-1: # go right
        visit(grid, row, col+1)


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

assert num_of_islands(grid) == 3
