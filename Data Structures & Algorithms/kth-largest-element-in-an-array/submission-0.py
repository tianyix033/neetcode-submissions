import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k


        def quickselect(arr, left, right, k):
            pivotInd = random.randrange(left, right)
            pivot = arr[pivotInd]
            arr[pivotInd], arr[right - 1] = arr[right - 1], arr[pivotInd]
            p = left
            for i in range(left, right):
                if (arr[i] <= pivot):
                    arr[i], arr[p] = arr[p], arr[i]
                    p += 1
            p -= 1
            if (p == k):
                return pivot
            elif (p > k):
                return quickselect(arr, left, p, k)
            else:
                return quickselect(arr, p + 1, right, k)

        return quickselect(nums, 0, len(nums), k)
        
        