# https://leetcode.com/problems/word-break/

def word_break(s, word_dict):
    words = set(word_dict)
    dp = [True] + [False] * len(s)
    for i in range(1, len(s)+1):
        for k in range(i):
            if dp[k] and s[k:i] in words:
                dp[i] = True
                break
    return dp[-1]

s = "leetcode"
word_dict = ["leet","code"]
assert word_break(s, word_dict) == True


s = "catsandog"
word_dict = ["cats","dog","sand","and","cat"]
assert word_break(s, word_dict) == False
