from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        l = r = 0
        res = []
        while r < len(nums):
            while queue and queue[0] < l:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)
            
            if r - l == k - 1:
                res.append(nums[queue[0]])
                l += 1

            r += 1
        return res
        