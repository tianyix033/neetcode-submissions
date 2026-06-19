class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def helper(nums, pos):
            if (pos == len(nums)):
                res.append(subset.copy())
                return
            subset.append(nums[pos])
            helper(nums, pos + 1)

            subset.pop()
            helper(nums, pos + 1)

        helper(nums, 0)
        return res
