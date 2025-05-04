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
            if visit(row, col, word, m):
                return True
    return False

def visit(row, col, word, m, idx=0):
    if idx == len(word): return True

    if not 0 <= row < len(m) or not 0 <= col < len(m[0]): return False

    if m[row][col] != word[idx]: return False

    m[row][col] = None
    if visit(row+1, col, word, m, idx+1): return True
    if visit(row-1, col, word, m, idx+1): return True
    if visit(row, col+1, word, m, idx+1): return True
    if visit(row, col-1, word, m, idx+1): return True
    m[row][col] = word[idx]
    return False


matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
assert search_word(matrix, word) == True


matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
assert search_word(matrix, word) == True


matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
assert search_word(matrix, word) == False
