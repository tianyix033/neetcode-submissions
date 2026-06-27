class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_start():
            left = 0
            right = len(nums) - 1
            while nums[left] > nums[right]:
                mid = (left + right) // 2
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid
            print(left)
            return left

        def binary_search(left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            if nums[left] == target:
                return left
            else:
                return -1


        start = find_start()
        if target <= nums[-1]:
            return binary_search(start, len(nums) - 1)
        else:
            return binary_search(0, start)

        