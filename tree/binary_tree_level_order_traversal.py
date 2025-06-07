# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import defaultdict, deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order(node):
    results = defaultdict(list)
    level = 0
    q = deque()
    while node:
        if node.left: q.append((node.left, level+1))
        if node.right: q.append((node.right, level+1))
        results[level].append(node.val)
        if not q:
            break
        node, level = q.popleft()
    out = list(results.values())
    print(out)
    return out



root = Node(3)
node2 = Node(9)
node3 = Node(20)
root.left = node2
root.right = node3

node4 = Node(15)
node5 = Node(7)
node3.left = node4
node3.right = node5

assert level_order(root) == [[3],[9, 20],[15, 7]]


root = Node(1)
assert level_order(root) == [[1]]

assert level_order([]) == []