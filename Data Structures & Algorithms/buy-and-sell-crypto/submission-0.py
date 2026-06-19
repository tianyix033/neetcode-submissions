class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        buying = prices[:]
        for i in range(1, len(prices)):            
            buying[i] = min(buying[i], buying[i - 1])
        selling = prices[:]
        for i in range(len(prices) - 2, -1):
            selling[i] = max(selling[i], selling[i + 1])
        profit = 0
        for i in range(len(prices)):
            profit = max(profit, selling[i] - buying[i])
        return profit

        