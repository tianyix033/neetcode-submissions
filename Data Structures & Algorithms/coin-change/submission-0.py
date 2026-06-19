class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for target in range(1, amount + 1):
            min_nums = float('inf')
            for coin in coins:
                if coin > target:
                    continue
                min_nums = min(min_nums, dp[target - coin] + 1)
            dp[target] = min_nums
        # print(dp)
        return dp[amount] if dp[amount] < float('inf') else -1
