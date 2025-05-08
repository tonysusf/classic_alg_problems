# https://leetcode.com/problems/implement-trie-prefix-tree/description/
# https://neetcode.io/problems/implement-prefix-tree
# assume all lower case letters

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]: return False
            node = node.children[idx]
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not node.children[idx]: return False
            node = node.children[idx]
        return True


trie = PrefixTree()

trie.insert("apple");
assert trie.search("apple") == True

assert trie.search("app") == False
assert trie.startsWith("app") == True

trie.insert("app")
assert trie.search("app") == True
