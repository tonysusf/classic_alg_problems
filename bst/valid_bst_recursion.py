# https://leetcode.com/problems/validate-binary-search-tree/


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def is_valid_bst(self, root):
        last_node = None
        def dfs(node):
            nonlocal last_node
            if node is None: return True
            if dfs(node.left) == False: return False
            if last_node and node.val <= last_node.val: return False
            last_node = node
            if dfs(node.right) == False: return False
            return True

        return dfs(root)


root = Node(2)
node2 = Node(1)
node3 = Node(3)
root.left = node2
root.right = node3
assert Solution().is_valid_bst(root) == True


root = Node(5)
node2 = Node(1)
node3 = Node(4)
root.left = node2
root.right = node3
node4 = Node(3)
node5 = Node(6)
node3.left = node4
node3.right = node5

assert Solution().is_valid_bst(root) == False

