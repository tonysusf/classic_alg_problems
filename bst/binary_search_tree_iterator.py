# https://leetcode.com/problems/binary-search-tree-iterator/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        current = self.stack.pop()
        node = current.right
        while node:
            self.stack.append(node)
            node = node.left
        return current.val

    def hasNext(self):
        return bool(self.stack)


root = Node(4)
node2 = Node(2)
node3 = Node(5)
root.left = node2
root.right = node3
node21 = Node(1)
node22 = Node(3)
node2.left = node21
node2.right = node22

it = BSTIterator(root)
assert it.hasNext() == True
assert it.next() == 1
assert it.next() == 2
assert it.next() == 3
assert it.next() == 4
assert it.hasNext() == True
assert it.next() == 5
assert it.hasNext() == False
