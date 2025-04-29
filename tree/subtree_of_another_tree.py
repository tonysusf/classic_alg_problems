# https://leetcode.com/problems/subtree-of-another-tree/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def is_subtree(root, target_subtree):
    def hash_subtree(node, cache=None):
        if node is None: return 123
        left_hash = hash_subtree(node.left, cache)
        right_hash = hash_subtree(node.right, cache)
        node_hash = hash((left_hash, node.val, right_hash))
        if cache is not None: cache.add(node_hash)
        return node_hash

    memo = set()
    hash_subtree(root, memo)
    target = hash_subtree(target_subtree)
    return target in memo



root = Node(3)
node2 = Node(4)
node3 = Node(5)
root.left = node2
root.right = node3
node4 = Node(1)
node5 = Node(2)
node2.left = node4
node2.right = node5

target_tree = Node(4)
node10 = Node(1)
node11 = Node(2)
target_tree.left = node10
target_tree.right = node11

assert is_subtree(root, target_tree) == True

