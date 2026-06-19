class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        starts = set(num for num in all_nums if num - 1 not in all_nums)
        res = 0
        for start in starts:
            counter = 0
            while start in all_nums:
                counter += 1
                start += 1
            res = max(res, counter)
        return res

