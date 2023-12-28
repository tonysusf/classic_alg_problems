# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from collections import deque

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def to_list(self):
        l = []
        queue = deque([self])
        bfs_length = 1
        while queue:
            current = queue.popleft()
            if current is None:
                l.append(None)
                continue
            l.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        while l[-1] is None:
            l.pop()
        return l


class Solution:
    def __init__(self):
        self.preorder_index = 0
        self.inorder_lookup = {}
        self.preorder = None

    def create_tree_from_array(self, left, right):
        if left > right: 
            return None

        node_value = self.preorder[self.preorder_index]
        node = Node(node_value)
        self.preorder_index += 1

        node.left = self.create_tree_from_array(left, self.inorder_lookup[node_value] - 1)
        node.right = self.create_tree_from_array(self.inorder_lookup[node_value] + 1, right)
        return node
        
    def build_tree(self, preorder, inorder):
        self.preorder = preorder
        for i in range(len(inorder)):
            self.inorder_lookup[inorder[i]] = i #key as val, val as index in inorder

        tree = self.create_tree_from_array(0, len(self.preorder) - 1)
        out = tree.to_list()
        return out


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
assert Solution().build_tree(preorder, inorder) == [3,9,20,None,None,15,7]


preorder = [1]
inorder = [1]
assert Solution().build_tree(preorder, inorder) == [1]


