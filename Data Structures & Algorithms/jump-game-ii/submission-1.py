class Solution:
    def jump(self, nums: List[int]) -> int:
        step_end = 0
        next_step_end = 0
        curr_steps = 0
        i = 0
        while i < len(nums):
            while i < len(nums) and i <= step_end:
                next_step_end = max(next_step_end, i + nums[i])
                i += 1
            step_end = next_step_end
            next_step_end = 0
            if i < len(nums):
                curr_steps += 1
        return curr_steps

