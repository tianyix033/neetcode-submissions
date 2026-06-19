class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while (right - left) > 1:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])