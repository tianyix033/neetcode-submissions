class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = 101
        best_profit = 0
        for i in range(len(prices)):
            lowest_price = min(lowest_price, prices[i])
            best_profit = max(best_profit, prices[i] - lowest_price)

        return best_profit