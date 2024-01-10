# https://leetcode.com/problems/word-search-ii/

def find_words(board, words):
    trie = {}
    for word in words:
        node = trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = word
    results = []

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in trie:
                dfs(row, col, trie, board, results)
    return results


def dfs(row, col, trie_parent, board, results):
    ch = board[row][col]
    trie_node = trie_parent[ch]

    word_matched = trie_node.pop('$', False)
    if word_matched:
        print('word_matched', word_matched)
        results.append(word_matched)

    board[row][col] = '#' # mark as visited

    for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        newRow, newCol = row + rowOffset, col + colOffset
        if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]):
            continue
        if not board[newRow][newCol] in trie_node:
            continue
        dfs(newRow, newCol, trie_node, board, results)

    board[row][col] = ch # revert

    if not trie_node:
        trie_parent.pop(ch)


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
expected = ["eat","oath"]
assert sorted(find_words(board, words)) == sorted(expected)


# board = [["a","b"],["c","d"]]
# words = ["abcb"]
# expected = []
# assert find_words(board, words) == expected
