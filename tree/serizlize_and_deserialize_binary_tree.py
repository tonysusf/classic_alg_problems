# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def serialize(self, node):
        def _serialize(node, results):
            if node is None:
                results.append('None')
                return
            results.append(str(node.val))
            _serialize(node.left, results)
            _serialize(node.right, results)

        results = []
        _serialize(node, results)
        return ','.join(results)

    def deserialize(self, data):
        def _deserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            node = Node(int(l[0]))
            l.pop(0)
            node.left = _deserialize(l)
            node.right = _deserialize(l)
            return node

        return _deserialize(data.split(','))


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3
node4 = Node(4)
node5 = Node(5)
node3.left = node4
node3.right = node5

s = Solution()
serialized_tree_string = s.serialize(root)
print(serialized_tree_string)

node = s.deserialize(serialized_tree_string)

assert node.val == 1
assert node.left.val == 2
assert node.right.val == 3
assert node.right.left.val == 4
assert node.right.right.val == 5


