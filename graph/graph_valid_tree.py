# https://leetcode.com/problems/graph-valid-tree/
# https://neetcode.io/problems/valid-tree

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether
# these edges make up a valid tree.

# graph is a valid tree if: (1) no circle, (2) all connected


def is_valid_tree(n, edges):
    if not n: return False
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    return dfs(0, -1, graph, visited) and len(visited) == n

def dfs(node, parent, graph, visited): # return false if circle found
    if node in visited: return False # circle found
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor == parent: continue
        if not dfs(neighbor, node, graph, visited): return False
    return True

n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
assert is_valid_tree(n, edges) == True


