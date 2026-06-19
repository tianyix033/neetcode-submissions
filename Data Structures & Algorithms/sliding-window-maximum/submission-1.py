import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        neg_heap = [(-x, i) for i, x in enumerate(nums) if i < k]
        heapq.heapify(neg_heap)
        res = []
        res.append(-neg_heap[0][0])
        for i in range(k, len(nums)):
            while neg_heap and neg_heap[0][1] <= (i - k):
                heapq.heappop(neg_heap)
            heapq.heappush(neg_heap, (-nums[i], i))
            res.append(-neg_heap[0][0])
        return res