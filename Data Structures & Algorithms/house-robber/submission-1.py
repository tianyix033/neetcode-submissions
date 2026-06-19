class Solution:
    def rob(self, nums: List[int]) -> int:

        # we return a tuple of max amount, one for if we rob house i 
        # and one for if we don't
        def recursive(i):
            if i == len(nums) - 1:
                return nums[i], 0
            do, dont = recursive(i + 1)
            return dont + nums[i], max(do, dont)

        return max(recursive(0))
        