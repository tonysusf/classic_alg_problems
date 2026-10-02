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
    def build_tree(self, preorder, inorder):
        inorder_lookup = {}
        preorder_index = 0
        for i in range(len(inorder)):
            inorder_lookup[inorder[i]] = i #key as val, val as index in inorder

        def create_tree_from_array(left, right, preorder):
            nonlocal preorder_index
            if left > right: return None

            node_value = preorder[preorder_index]
            node = Node(node_value)
            preorder_index += 1

            node.left = create_tree_from_array(left, inorder_lookup[node_value] - 1, preorder)
            node.right = create_tree_from_array(inorder_lookup[node_value] + 1, right, preorder)
            return node

        tree = create_tree_from_array(0, len(inorder) - 1, preorder)
        return tree.to_list()


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
assert Solution().build_tree(preorder, inorder) == [3,9,20,None,None,15,7]


preorder = [1]
inorder = [1]
assert Solution().build_tree(preorder, inorder) == [1]


