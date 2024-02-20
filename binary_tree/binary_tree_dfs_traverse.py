# Given a binary tree, traverse it using depth first traversal

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def dfs(root):
    if not root:
        return None
    result = []
    s = [root] # Stack
    while s:
        node = s.pop()
        result.append(node.val)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return result


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3

node4 = Node(4)
node5 = Node(5)
node3.left = node4
node3.right = node5

print(dfs(root))
