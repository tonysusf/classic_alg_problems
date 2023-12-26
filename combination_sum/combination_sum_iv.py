# https://leetcode.com/problems/combination-sum-iv/description/
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.


def comb_sum_count(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for comb_sum in range(target+1):
        for num in nums:
            if comb_sum - num >= 0:
                dp[comb_sum] += dp[comb_sum - num]
    return dp[target]


nums = [1,2,3]
target = 4
assert comb_sum_count(nums, target) == 7

nums = [3]
target = 14
assert comb_sum_count(nums, target) == 0