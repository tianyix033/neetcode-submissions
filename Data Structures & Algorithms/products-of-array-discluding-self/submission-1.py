class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use prefix and suffix; for each idx we need the
        # product of everything before it and everything after it
        prefix = [1] * len(nums)
        suffix = prefix[:]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
        