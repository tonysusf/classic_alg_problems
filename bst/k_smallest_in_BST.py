# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def kth_smallest(node, k):
    stack = []
    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right



root = Node(2)
node2 = Node(1)
node3 = Node(3)
root.left = node2
root.right = node3
assert kth_smallest(root, 2) == 2

