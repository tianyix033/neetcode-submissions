class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        COOLDOWN = 1

        # max profit given we start from index i and can buy or not (in which 
        # case we can sell)
        def helper(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in cache:
                return cache[(i, can_buy)]

            if can_buy:
                buy = helper(i + 1, False) - prices[i]
                hold = helper(i + 1, can_buy)
                cache[(i, can_buy)] = max(buy, hold)
            else:
                sell = helper(i + 1 + COOLDOWN, True) + prices[i]
                hold = helper(i + 1, can_buy)
                cache[(i, can_buy)] = max(sell, hold)

            return cache[(i, can_buy)]

        return helper(0, True)