class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(start, end):
            prev_not_taken = prev_taken = 0
            for i in range(start, end):
                taken = prev_not_taken + nums[i]
                not_taken = max(prev_not_taken, prev_taken)
                prev_taken = taken
                prev_not_taken = not_taken
            return max(prev_taken, prev_not_taken)
            
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(simple_rob(1, len(nums)), simple_rob(2, len(nums) - 1) + nums[0])

