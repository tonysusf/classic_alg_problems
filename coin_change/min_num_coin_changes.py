# https://leetcode.com/problems/coin-change/
# given list of coins, return min num of coins summing up to the amount

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1) # float('inf') is super large
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]

coins = [1,2,5]
amount = 11
assert coin_change(coins, amount) == 3


coins = [2]
amount = 3
assert coin_change(coins, amount) == -1


coins = [2, 3]
amount = 10
assert coin_change(coins, amount) == 4

