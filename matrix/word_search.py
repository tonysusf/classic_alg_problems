# https://leetcode.com/problems/word-search/
# Given an m * n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#   A B C E
#   S F C S
#   A D E E


def search_word(m, word):
    for row in range(len(m)):
        for col in range(len(m[0])):
            if dfs(row, col, word, 0, m):
                return True
    return False

def dfs(row, col, word, idx, m):
    result = False

    if idx == len(word):
        return True

    if row < 0 or row >= len(m) or col < 0 or col >= len(m[0]):
        return False

    if m[row][col] != word[idx]:
        return False

    # mark as visited
    m[row][col] = None

    result = dfs(row+1, col, word, idx+1, m)
    if not result:
        result = dfs(row-1, col, word, idx+1, m)
    if not result:
        result = dfs(row, col+1, word, idx+1, m)
    if not result:
        result = dfs(row, col-1, word, idx+1, m)

    m[row][col] = word[idx]
    return result

matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
assert search_word(matrix, word) == True


matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
assert search_word(matrix, word) == True


matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
assert search_word(matrix, word) == False
