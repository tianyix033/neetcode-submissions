class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for left in range(len(nums) - 2, 0, -1):
            for right in range(left, len(nums) - 1):
                for i in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], nums[left - 1] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right])

        return dp[1][len(nums) - 2]