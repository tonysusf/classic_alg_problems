# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import defaultdict


def dfs(adj, visited, node_idx):
    visited[node_idx] = True
    for i in range(len(adj[node_idx])):
        if not visited[adj[node_idx][i]]:
            dfs(adj, visited, adj[node_idx][i])


def count_components(n, edges):
    count = 0
    visited = [False] * n
    adj = defaultdict(list) # key as self node, value as neighbouring nodes

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(adj, visited, i)

    return count


n = 5
edges = [[0,1],[1,2],[3,4]]
assert count_components(n, edges) == 2


n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
assert count_components(n, edges) == 1
