# https://leetcode.com/problems/longest-common-subsequence/


def longest_common_subsequence(str1, str2):
    dp = [[0] * (len(str2)+1)] * (len(str1)+1)
    for row in range(1, len(str1)+1):
        for col in range(1, len(str2)+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[-1][-1]


assert longest_common_subsequence('abcde', 'ace') == 3

assert longest_common_subsequence('abc', 'abc') == 3

assert longest_common_subsequence('abc', 'oiu') == 0

assert longest_common_subsequence('', '') == 0

assert longest_common_subsequence('a', '') == 0
