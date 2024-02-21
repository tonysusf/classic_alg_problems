# https://leetcode.com/problems/find-leaves-of-binary-tree/


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def find_leaves(root):
    results = []

    def dfs(node):
        nonlocal results
        if node is None: return -1
        current_height = max(dfs(node.left), dfs(node.right)) + 1
        if len(results) == current_height:
            results.append([])
        results[current_height].append(node.val)
        return current_height

    dfs(root)
    return results


root = Node(1)
node2 = Node(2)
node3 = Node(3)
root.left = node2
root.right = node3
node4 = Node(4)
node5 = Node(5)
node2.left = node4
node2.right = node5

assert find_leaves(root) == [[4,5,3],[2],[1]]

root = Node(1)
assert find_leaves(root) == [[1]]
