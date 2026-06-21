class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = currMin = 1
        for num in nums:
            newMax = max(num * currMax, num * currMin, num)
            currMin = min(num * currMax, num * currMin, num)
            currMax = newMax
            res = max(res, currMax)

        return res