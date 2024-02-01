# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

from collections import defaultdict
from collections import deque

def vertical_order(root):
    if root is None: return []

    lookup = defaultdict(list)
    left = right = 0
    queue = deque([(root, 0)])

    # breadth first traversal
    while queue:
        (node, idx) = queue.popleft()
        lookup[idx].append(node.val)

        left = min(left, idx)
        right = max(right, idx)

        if node.left: queue.append((node.left, idx - 1))
        if node.right: queue.append((node.right, idx + 1))

    return [lookup[i] for i in range(left, right+1)]



root = Node(3)
node2 = Node(9)
node3 = Node(20)
root.left = node2
root.right = node3
node4 = Node(15)
node5 = Node(7)
node3.left = node4
node3.right = node5

assert vertical_order(root) == [[9],[3,15],[20],[7]]
