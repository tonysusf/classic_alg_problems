# https://leetcode.com/problems/same-tree/


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def is_same_tree(a, b):
    if not a and not b: # both null
        return True
    elif a is None or b is None: # either one is null
        return False
    elif a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)



root1 = Node(0)
node2 = Node(2)
node3 = Node(3)
root1.left = node2
root1.right = node3

root2 = Node(0)
node4 = Node(2)
node5 = Node(3)
root2.left = node4
root2.right = node5

assert(is_same_tree(root1, root2) == True)



root3 = Node(0)
node12 = Node(2)
root3.left = node12

root4 = Node(0)
node13 = Node(2)
root4.right = node13

assert(is_same_tree(root3, root4) == False)
