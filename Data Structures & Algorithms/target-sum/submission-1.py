class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def ways_at_pos(pos, curr_sum):
            if pos == len(nums):
                return int(curr_sum == target)
            if (pos, curr_sum) in cache:
                return cache[(pos, curr_sum)]
            res = ways_at_pos(pos + 1, curr_sum + nums[pos]) + ways_at_pos(pos + 1, curr_sum - nums[pos])
            cache[(pos, curr_sum)] = res
            return res

        return ways_at_pos(0, 0)