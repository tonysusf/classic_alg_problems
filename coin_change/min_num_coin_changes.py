# https://leetcode.com/problems/coin-change/
# Given a list of coins, return min num of coins summing up to the amount

def minimum_num_of_coins_change(coins, amount):
    dp = [float('inf')] * (amount + 1) # float('inf') is infinity super large
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1


coins = [1,2,5]
amount = 11
assert minimum_num_of_coins_change(coins, amount) == 3


coins = [2]
amount = 3
assert minimum_num_of_coins_change(coins, amount) == -1


coins = [2, 3]
amount = 10
assert minimum_num_of_coins_change(coins, amount) == 4

