class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[-11] * len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j == i:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j - 1] * nums[j]
        res = -11
        for sublist in dp:
            for val in sublist:
                res = max(res, val)
        
        return res

