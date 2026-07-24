class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def ways_at_pos(pos, curr_sum):
            if pos == len(nums):
                return int(curr_sum == target)
            return ways_at_pos(pos + 1, curr_sum + nums[pos]) + ways_at_pos(pos + 1, curr_sum - nums[pos])

        return ways_at_pos(0, 0)