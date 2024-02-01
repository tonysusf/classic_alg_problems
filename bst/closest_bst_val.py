# https://leetcode.com/problems/closest-binary-search-tree-value/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def closest_value(node, target):
    current = node.val
    while node:
        # use tupple of diff and x itself to sort in case left/right same diff
        current = min(node.val, current, key=lambda x: (abs(target - x), x))
        node = node.left if target < node.val else node.right
    return current



root = Node(4)
node2 = Node(2)
node3 = Node(5)
root.left = node2
root.right = node3
node21 = Node(1)
node22 = Node(3)
node2.left = node21
node2.right = node22


assert closest_value(root, 3.714286) == 4

assert closest_value(root, 4.5) == 4

root2 = Node(1)
assert closest_value(root2, 4.428571) == 1
