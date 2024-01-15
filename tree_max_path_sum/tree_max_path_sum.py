# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = 0

    def get_max_path_sum(self, root):
        self.result = -float('inf')
        self._subtree_branch_sum(root)
        return self.result

    def _subtree_branch_sum(self, node): # get the max of left or right branch sum itself inclusive
        if not node: return 0
        sum_left_branch = max(self._subtree_branch_sum(node.left), 0) # if negative abandon it
        sum_right_branch = max(self._subtree_branch_sum(node.right), 0)
        # for final result
        self.result = max(self.result, sum_left_branch + sum_right_branch + node.val)
        return max(sum_left_branch + node.val, sum_right_branch + node.val)



root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3

assert Solution().get_max_path_sum(root) == 6



root2 = Node(-10)
node2 = Node(9)
node3 = Node(20)
root2.left = node2
root2.right = node3

node3 = Node(15)
node4 = Node(7)
node2.left = node3
node2.right = node4
assert Solution().get_max_path_sum(root) == 42
