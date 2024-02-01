# https://leetcode.com/problems/binary-tree-right-side-view/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def right_side_view(node):
    if not node: return []
    results = []
    def visit(node, level=0):
        if level == len(results):
            results.append(node.val)
        if node.right: visit(node.right, level + 1)
        if node.left: visit(node.left, level + 1)
    visit(node)
    return results



root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3
node4 = Node(5)
node5 = Node(4)
node2.right = node4
node3.right = node5

assert right_side_view(root) == [1,3,4]


root2 = Node(1)
node3 = Node(3)
root2.right = node3

assert right_side_view(root2) == [1,3]

assert right_side_view(None) == []