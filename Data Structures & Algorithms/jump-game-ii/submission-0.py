class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float('inf')] * len(nums)
        jumps[0] = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, i + num + 1):
                if j < len(nums):
                    jumps[j] = min(jumps[i] + 1, jumps[j])
        return jumps[-1]