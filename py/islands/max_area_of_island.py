# https://leetcode.com/problems/max-area-of-island/submissions/

def max_area_of_islands(grid):
    print('grid is', grid)
    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                curr_area = visit(grid, row, col)
                max_area = max(max_area, curr_area)
    print('max_area is', max_area)
    return max_area

def visit(grid, row, col):
    if grid[row][col] != 1:
        return 0
    grid[row][col] = 0 # mark as visited
    s = 1
    if row > 0: # go up
        s += visit(grid, row-1, col)
    if col > 0: # go left
        s += visit(grid, row, col-1)
    if row < len(grid) - 1: # go down
        s += visit(grid, row+1, col)
    if col < len(grid[0]) - 1: # go right
        s += visit(grid, row, col+1)
    return s


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
assert max_area_of_islands(grid) == 6