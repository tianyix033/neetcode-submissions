class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublist = nums.copy()
        def helper(pos):
            if pos == len(nums):
                res.append(sublist.copy())
                return
            for i in range(pos, len(nums)):
                sublist[pos], sublist[i] = sublist[i], sublist[pos]
                helper(pos + 1)
                sublist[pos], sublist[i] = sublist[i], sublist[pos]

        helper(0)
        return res