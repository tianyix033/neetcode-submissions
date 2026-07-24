from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1    
        for num in nums:
            next_dp = defaultdict(int)
            for prev_sum, num_of_ways in dp.items():
                next_dp[prev_sum + num] += num_of_ways
                next_dp[prev_sum - num] += num_of_ways
            dp = next_dp

        return dp[target]