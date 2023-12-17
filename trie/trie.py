# https://leetcode.com/problems/implement-trie-prefix-tree/

# Implement a basic Trie data structure. Given a word to search if the word exists in the Trie

class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {} # char to list of Nodes mapping
        self.is_leaf = False

    def __str__(self):
        return 'Node %s, children %s, is_leaf %s' % (self.val, list(self.children.keys()), self.is_leaf)

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, w):
        curr = self.root
        for i in range(len(w)):
            if w[i] not in curr.children:
                curr.children[w[i]] = Node(w[i])
                curr.children[w[i]].is_leaf = (len(w) == i+1)
            curr = curr.children[w[i]]


    def search(self, w):
        curr = self.root
        for i in range(len(w)):
            if w[i] not in curr.children:
                return False
            else:
                curr = curr.children[w[i]]
        return curr.is_leaf



t = Trie()
t.insert('hello')
t.insert('house')
t.insert('world')
print(t.root)

assert t.search('hello') == True
assert t.search('he') == False
assert t.search('house') == True
assert t.search('world') == True
assert t.search('se') == False
assert t.search('') == False

