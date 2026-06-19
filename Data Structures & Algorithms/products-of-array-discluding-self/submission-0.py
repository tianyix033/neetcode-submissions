from functools import reduce
from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        if counter[0] > 1:
            return [0] * len(nums)
        if counter[0] == 1:
            res = [0] * len(nums)
            prod = 1
            idx = -1
            for i in range(len(nums)):
                if nums[i] != 0:
                    prod *= nums[i]
                else:
                    idx = i
            res[idx] = prod
            return res
        product = reduce(lambda x, y : x * y, nums)
        return [int(product / x) for x in nums ]
        