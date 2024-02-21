# https://leetcode.com/problems/detonate-the-maximum-bombs/

from collections import defaultdict

def maximum_detonation(bombs):
    graph = defaultdict(list)
    n = len(bombs)

    for i in range(n):
        for j in range(n):
            if i == j: continue
            xi, yi, ri = bombs[i]
            xj, yj, rj = bombs[j]
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    def dfs(cur, visited):
        visited.add(cur)
        for neighbor in graph[cur]:
            if neighbor not in visited:
                dfs(neighbor, visited)
        return len(visited)

    result = 0
    for i in range(n):
        result = max(result, dfs(i, set()))

    return result

bombs = [[2,1,3], [6,1,4]]
assert maximum_detonation(bombs) == 2

bombs = [[1,1,5],[10,10,5]]
assert maximum_detonation(bombs) == 1

bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
assert maximum_detonation(bombs) == 5

