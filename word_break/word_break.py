# https://leetcode.com/problems/word-break/

def word_break(s, word_dict):
    dp = [False] * len(s)
    for i in range(len(s)):
        for w in word_dict:
            if i+1 < len(w):
                continue
            if (i == len(w)-1 or dp[i - len(w)]) and s[i-len(w)+1: i+1] == w:
                dp[i] = True
                break
    return dp[-1]


s = "leetcode"
word_dict = ["leet","code"]
assert word_break(s, word_dict) == True


s = "catsandog"
word_dict = ["cats","dog","sand","and","cat"]
assert word_break(s, word_dict) == False
