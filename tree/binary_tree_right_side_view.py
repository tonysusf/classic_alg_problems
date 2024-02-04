# https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def right_side_view_dfs(node):
    if not node: return []
    results = []
    def visit(node, level=0):
        if level == len(results):
            results.append(node.val)
        # visit the right one 1st
        if node.right: visit(node.right, level + 1)
        if node.left: visit(node.left, level + 1)
    visit(node)
    return results

def right_side_view_bfs(root):
    if root is None: return []
    queue = deque([root])
    result = []

    while queue:
        level_len = len(queue)
        for i in range(level_len):
            node = queue.popleft()
            if i == level_len-1: result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return result


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3
node4 = Node(5)
node5 = Node(4)
node2.right = node4
node3.right = node5

assert right_side_view_dfs(root) == [1,3,4]
assert right_side_view_bfs(root) == [1,3,4]


root2 = Node(1)
node3 = Node(3)
root2.right = node3

assert right_side_view_dfs(root2) == [1,3]
assert right_side_view_bfs(root2) == [1,3]

assert right_side_view_dfs(None) == []
assert right_side_view_bfs(None) == []