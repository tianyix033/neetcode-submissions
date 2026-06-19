class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        sublist = []
        def helper(pos):
            if pos >= len(nums):
                res.append(sublist.copy())
                return
            
            sublist.append(nums[pos]) 
            helper(pos + 1)
            last_val = sublist.pop()
            if not sublist or sublist[-1] != last_val:
                helper(pos + 1)
            
        helper(0)
        return res