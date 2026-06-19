import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(k):
            res = 0
            for pile in piles:
                res += math.ceil((pile / k))
            return res

        min_k = max(sum(piles) // h, 1)
        max_k = max(piles)
        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            hours = get_hours(mid_k)
            if hours > h:
                min_k = mid_k + 1
            else:
                max_k = mid_k
                
        return max_k
