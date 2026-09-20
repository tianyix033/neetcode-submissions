class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        cache = {}

        def helper(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            ret = -1
            for i in range(left, right + 1):
                product = nums[left - 1] * nums[i] * nums[right + 1]
                ret = max(ret, product + helper(left, i - 1) + helper(i + 1, right))
            cache[(left, right)] = ret
            return ret

        return helper(1, len(nums) - 2)
        