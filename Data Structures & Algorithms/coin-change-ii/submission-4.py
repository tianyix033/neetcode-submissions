class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        for i in range(len(coins) + 1):
            dp[0][i] = 1
        for i in range(len(coins) - 1, -1, -1):
            for target in range(amount + 1):
                if target >= coins[i]:
                    dp[target][i] = dp[target - coins[i]][i] + dp[target][i + 1]

        return dp[amount][0]