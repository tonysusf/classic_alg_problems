# https://leetcode.com/problems/diameter-of-binary-tree/description/

# diameter is the number of the edges


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(node) -> int:
    diameter = 0

    def depth(node):
        nonlocal diameter

        if not node: return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)

        return max(left, right) + 1

    depth(node)
    print('diameter is', diameter)
    return diameter


# Empty tree
assert diameter_of_binary_tree(None) == 0


# Single node
root = Node(1)
assert diameter_of_binary_tree(root) == 0


# Simple tree
#
#     1
#    / \
#   2   3
#
root = Node(1, Node(2), Node(3))
assert diameter_of_binary_tree(root) == 2


# LC example
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
root = Node(
    1,
    Node(2, Node(4), Node(5)),
    Node(3)
)
assert diameter_of_binary_tree(root) == 3


# Left-skewed tree
#
#   1
#  /
# 2
# /
#3
#/
#4
#
root = Node(
    1,
    Node(
        2,
        Node(
            3,
            Node(4)
        )
    )
)
assert diameter_of_binary_tree(root) == 3


# Diameter does NOT pass through root
#
#       1
#      /
#     2
#    / \
#   3   4
#  /     \
# 5       6
#
root = Node(
    1,
    Node(
        2,
        Node(3, Node(5)),
        Node(4, None, Node(6))
    )
)
assert diameter_of_binary_tree(root) == 4
