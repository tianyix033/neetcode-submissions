import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.data = []
        i = 0
        while len(self.data) < k and i < len(nums):
            heapq.heappush(self.data, nums[i])
            i += 1
            # print(self.data)
        while i < len(nums):
            heapq.heappushpop(self.data, nums[i])
            i += 1
            # print("DONE", self.data)

    def add(self, val: int) -> int:
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
        else:
            heapq.heappushpop(self.data, val)
        return self.data[0]
        

        
        
