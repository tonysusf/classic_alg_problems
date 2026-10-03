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
        print(l)
        return l


class Solution:
    def build_tree(self, preorder, inorder):
        inorder_lookup = {value: i for i, value in enumerate(inorder)}
        roots = iter(preorder)

        def build(left, right):
            if left > right:
                return None
            value = next(roots)
            split_index = inorder_lookup[value]

            node = Node(value)
            node.left = build(left, split_index-1)
            node.right = build(split_index+1, right)

            return node

        tree = build(0, len(inorder)-1)
        return tree.to_list()


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
assert Solution().build_tree(preorder, inorder) == [3,9,20,None,None,15,7]


preorder = [1]
inorder = [1]
assert Solution().build_tree(preorder, inorder) == [1]


