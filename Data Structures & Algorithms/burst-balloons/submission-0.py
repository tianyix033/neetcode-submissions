class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        def helper(curr_nums):
            if not curr_nums:
                return 0
            tup_nums = tuple(curr_nums)
            if tup_nums in cache:
                return cache[tup_nums]
            res = -1
            for i in range(len(curr_nums)):
                copy = curr_nums.copy()
                popped_val = copy[i]
                if i > 0:
                    popped_val *= copy[i - 1]
                if i < len(curr_nums) - 1:
                    popped_val *= copy[i + 1]
                copy.pop(i)
                total_val = popped_val + helper(copy)
                if total_val > res:
                    res = total_val
            cache[tup_nums] = res
            return res

        return helper(nums)
