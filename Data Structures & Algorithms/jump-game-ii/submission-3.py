class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = next_end = 0
        for i in range(len(nums) - 1):
            next_end = max(i + nums[i], next_end)
            if i == curr_end:
                curr_end = next_end
                jumps += 1
        return jumps