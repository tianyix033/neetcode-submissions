class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def helper(nums, pos):
            nonlocal res
            curr_len = len(res)
            for i in range(curr_len):
                new_sublist = res[i].copy()
                new_sublist.append(nums[pos])
                res.append(new_sublist)
            if pos < len(nums) - 1:
                helper(nums, pos + 1)

        helper(nums, 0)
        return res
        
        