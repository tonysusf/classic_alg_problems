# https://leetcode.com/problems/validate-binary-search-tree/


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None



def is_valid_bst(node):
    stack = []
    last_visited_node = None
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()

        if last_visited_node and node.val <= last_visited_node.val:
            return False
        last_visited_node = node
        node = node.right
    return True




root = Node(2)
node2 = Node(1)
node3 = Node(3)
root.left = node2
root.right = node3
assert is_valid_bst(root) == True


root = Node(5)
node2 = Node(1)
node3 = Node(4)
root.left = node2
root.right = node3
node4 = Node(3)
node5 = Node(6)
node3.left = node4
node3.right = node5

assert is_valid_bst(root) == False

