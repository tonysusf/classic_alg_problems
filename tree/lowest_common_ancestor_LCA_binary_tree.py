# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor(node, p, q):
    if node is None or node.val == p or node.val == q: return node

    left = lowest_common_ancestor(node.left, p, q)
    right = lowest_common_ancestor(node.right, p, q)

    if left and right: return node # found it

    return left or right



root = Node(3)
node2 = Node(5)
node3 = Node(1)
root.left = node2
root.right = node3
node4 = Node(6)
node5 = Node(2)
node2.left = node4
node2.right = node5

assert lowest_common_ancestor(root, 5, 1).val == 3
