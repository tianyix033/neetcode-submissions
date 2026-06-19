class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left_max = [0] * n 
        right_max = [0] * n
        res = []
        for i in range(n):
            if i % k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i - 1], nums[i])
        for j in range(n - 1, -1, -1):
            if j == n - 1 or j % k == k - 1:
                right_max[j] = nums[j]
            else:
                right_max[j] = max(right_max[j + 1], nums[j])
        for i in range(n - k + 1):
            res.append(max(right_max[i], left_max[i + k - 1]))
        return res
