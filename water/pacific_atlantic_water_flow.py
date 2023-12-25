# https://leetcode.com/problems/pacific-atlantic-water-flow/
# given a matrix, pacific left and top, atlantic right and bottom, return list of nodes both ocean water can reach


def dfs(row, col, visited, m, last_val=0):
    if row<0 or col<0 or row>=len(m) or col>=len(m[0]):
        return
    if (row, col) in visited:
        return
    if m[row][col] < last_val:
        return
    visited.add((row, col))
    dfs(row+1, col, visited, m, m[row][col])
    dfs(row-1, col, visited, m, m[row][col])
    dfs(row, col+1, visited, m, m[row][col])
    dfs(row, col-1, visited, m, m[row][col])

def pacific_atlantic(m):
    if not m or not m[0]:
        return []
    pacific_reachable = set()
    atlantic_reachable = set()

    for row in range(len(m)):
        dfs(row, 0, pacific_reachable, m)
        dfs(row, len(m[0]) - 1, atlantic_reachable, m)
    for col in range(len(m[0])):
        dfs(0, col, pacific_reachable, m)
        dfs(len(m) - 1, col, atlantic_reachable, m)

    result = list(pacific_reachable.intersection(atlantic_reachable))
    return [list(k) for k in result]

def _to_str(l):
    for row in l:
        row.sort()
        for i in range(len(row)):
            row[i] = str(row[i])
    l = [','.join(k) for k in l]
    l.sort()
    out = '|'.join(l)
    return out

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
assert _to_str(pacific_atlantic(heights)) == _to_str(expected)


heights = [[1]]
expected = [[0,0]]
assert _to_str(pacific_atlantic(heights)) == _to_str(expected)



heights = [[1], [1]]
expected = [[0,0], [1,0]]
assert _to_str(pacific_atlantic(heights)) == _to_str(expected)
