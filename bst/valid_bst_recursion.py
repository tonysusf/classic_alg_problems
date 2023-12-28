# https://leetcode.com/problems/validate-binary-search-tree/


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.last_visited_node = None

    def is_valid_bst(self, root):
        return self.dfs(root)

    def dfs(self, node): # in order left < self < right
        if node is None:
            return True
        # left
        if node.left and self.dfs(node.left) == False:
            return False

        # self
        if self.last_visited_node and node.val <= self.last_visited_node.val:
            return False

        self.last_visited_node = node

        # right
        if node.right and self.dfs(node.right) == False:
            return False

        return True

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

