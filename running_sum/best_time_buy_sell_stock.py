# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def max_profit(prices):
    cur_min = prices[0]
    max_pf = 0
    for i in range(1, len(prices)):
        cur_min = min(cur_min, prices[i-1])
        max_pf = max(max_pf, prices[i] - cur_min)
    return max_pf

prices = [7,1,5,3,6,4]
assert max_profit(prices) == 5

prices = [7,6,4,3,1]
assert max_profit(prices) == 0

prices = [1]
assert max_profit(prices) == 0

prices = [2, 1, 9]
assert max_profit(prices) == 8

