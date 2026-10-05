class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2:
            num = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right and nums[right] >= 0:
                if nums[left] + nums[right] + num == 0:
                    res.append([nums[left], nums[right], num])
                    orig_left, orig_right = left, right
                    while left < len(nums) and nums[left] == nums[orig_left]:
                        left += 1
                    while right > 0 and nums[right] == nums[orig_right]:
                        right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    right -= 1
            while i < len(nums) and nums[i] == num:
                i += 1
        return res
                