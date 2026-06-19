import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        values = [-x for x in count.values()]
        heapq.heapify(values)
        target = []
        for i in range(k):
            target.append(-heapq.heappop(values))  
        res = []      
        for key, value in count.items():
            if (value in target):
                res.append(key)
        return res

       
            
            
            
        