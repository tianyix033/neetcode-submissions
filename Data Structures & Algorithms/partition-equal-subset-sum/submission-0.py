class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        cache = set()
        def helper(start, curr_sum):
            if curr_sum * 2 == total:
                return True
            if start >= len(nums) or curr_sum * 2 > total:
                return False
            if (start, curr_sum) in cache:
                return False
            res = helper(start + 1, curr_sum + nums[start]) or helper(start + 1, curr_sum)
            if not res:
                cache.add((start, curr_sum))
            return res

        return helper(0, 0)