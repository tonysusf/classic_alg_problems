# https://leetcode.com/problems/range-sum-of-bst/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root, low, high):
        if not root: return 0
        result = 0
        if low <= root.val <= high:
            result += root.val
        if root.val > low:
            result += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            result += self.rangeSumBST(root.right, low, high)
        return result


root = Node(2)
node2 = Node(1)
node3 = Node(3)
root.left = node2
root.right = node3
assert Solution().rangeSumBST(root, 1, 2) == 3
