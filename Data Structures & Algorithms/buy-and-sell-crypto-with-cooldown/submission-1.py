class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        can_buy1 = can_buy2 = can_sell1 = 0
        for i in range(len(prices) - 1, -1, -1):
            orig_can_buy1 = can_buy1
            can_buy1 = max(-prices[i] + can_sell1, can_buy1)
            can_sell1 = max(prices[i] + can_buy2, can_sell1)
            can_buy2 = orig_can_buy1
        return can_buy1