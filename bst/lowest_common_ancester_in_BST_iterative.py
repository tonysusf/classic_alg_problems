# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def find_lowest_common_ancestor(node, p, q):
    s = [node]
    while s:
        current = s.pop()
        if p.val > current.val and q.val > current.val:
            s.append(current.right)
        elif p.val < current.val and q.val < current.val:
            s.append(current.left)
        else:
            return current

root = Node(2)
node2 = Node(1)
node3 = Node(3)
root.left = node2
root.right = node3
assert find_lowest_common_ancestor(root, node2, node3) == root


root = Node(5)
node2 = Node(1)
node3 = Node(7)
root.left = node2
root.right = node3
node4 = Node(6)
node5 = Node(8)
node3.left = node4
node3.right = node5

assert find_lowest_common_ancestor(root, node4, node5) == node3
assert find_lowest_common_ancestor(root, node3, node5) == node3


