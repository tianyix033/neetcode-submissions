class Solution:
    def canJump(self, nums: List[int]) -> bool:

        memo = [-1] * len(nums)
        def helper(start):
            if start >= (len(nums) - 1):
                return True
            if memo[start] == 0:
                return False
            distance = nums[start]
            res = False
            for i in range(distance, 0, -1):
                if helper(start + i):
                    return True
            memo[start] = 0
            return False

        return helper(0)


