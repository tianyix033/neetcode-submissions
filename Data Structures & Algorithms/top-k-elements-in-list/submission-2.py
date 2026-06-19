import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            bucket[val].append(key)
        idx = len(bucket) - 1
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res  # unnecessary
       
            
            
            
        