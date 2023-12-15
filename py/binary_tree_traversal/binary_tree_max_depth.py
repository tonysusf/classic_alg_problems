# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_depth(node):
    if node is None:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


root = Node(0)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3

node4 = Node(4)
node5 = Node(5)
node3.left = node4
node3.right = node5

assert(max_depth(root) == 3)