class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in all_nums:
                counter = 0
                while num in all_nums:
                    counter += 1
                    num += 1
                res = max(res, counter)
        return res

