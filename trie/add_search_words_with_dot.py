# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

class WordDict:
    def __init__(self):
        self.trie = {}

    def add_word(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def _search(self, w, node, start_idx=0):
        for i in range(start_idx, len(w)):
            if w[i] not in node:
                if w[i] == '.':
                    for x in node:
                        if x != '$' and self._search(w, node[x], i+1):
                            return True
                return False
            else:
                node = node[w[i]] # recursion
        return '$' in node

    def search(self, w: str) -> bool:
        return self._search(w, self.trie)


solution = WordDict()
solution.add_word('good')
solution.add_word('boy')
solution.add_word('go')

assert solution.search('go') == True
assert solution.search('goo') == False
assert solution.search('g.od') == True
assert solution.search('g.') == True


