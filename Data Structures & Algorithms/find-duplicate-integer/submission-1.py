class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def count_smaller(nums, val):
            count = 0
            for num in nums:
                if num <= val:
                    count += 1
            return count

        left = 1
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if count_smaller(nums, mid) <= mid:
                left = mid + 1
            else:
                right = mid
        return left
