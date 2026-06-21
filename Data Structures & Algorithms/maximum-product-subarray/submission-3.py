class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ''' If you split the array at every zero, the maximum
            product subarray within any zero-free segment MUST 
            start at the very beginning of that segment (a prefix) 
            or end at the very end of that segment (a postfix). '''
        res = max(nums)
        prefix = postfix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            postfix = nums[len(nums) - 1 - i] * (postfix or 1)
            res = max(res, prefix, postfix)

        return res

