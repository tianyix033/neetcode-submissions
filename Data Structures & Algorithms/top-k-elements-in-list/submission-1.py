import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in count.items():
            bucket[val].append(key)
        idx = len(bucket) - 1
        res = []
        while k > 0:
            if (bucket[idx]):
                if (k < len(bucket[idx])):
                    while (k > 0):
                        res.append(bucket[idx].pop())
                        k -= 1
                else:
                    res.extend(bucket[idx])
                    k -= len(bucket[idx])
            idx -= 1
        return res
       
            
            
            
        