class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = 0
        res = []
        sublist = []
        def helper(picked):
            if len(sublist) == len(nums):
                res.append(sublist.copy())
                return
            for i, num in enumerate(nums):
                if (picked & (1 << i)) != 1 << i:
                    sublist.append(num)
                    picked |= (1 << i)
                    helper(picked)
                    sublist.pop()
                    picked &= ~(1 << i)

        helper(picked)
        return res
