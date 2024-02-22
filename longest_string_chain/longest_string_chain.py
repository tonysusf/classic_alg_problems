# https://leetcode.com/problems/longest-string-chain/

def longest_str_chain(words):
    words.sort(key=len)
    dp = {}

    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev_word = word[:i] + word[i+1:]
            if prev_word in dp:
                dp[word] = max(dp[word], dp[prev_word] + 1)

    return max(dp.values())

words = ["a","b","ba","bca","bda","bdca"]
assert longest_str_chain(words) == 4


words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
assert longest_str_chain(words) == 5

words = ["abcd","dbqca"]
assert longest_str_chain(words) == 1
