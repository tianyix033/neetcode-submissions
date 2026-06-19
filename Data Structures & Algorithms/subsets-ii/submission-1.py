class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        prev_start = 0
        curr_size = len(res)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                for j in range(curr_size):
                    new_sublist = res[j].copy()
                    new_sublist.append(nums[i])
                    res.append(new_sublist)
            else:
                for j in range(prev_start, curr_size):
                    new_sublist = res[j].copy()
                    new_sublist.append(nums[i])
                    res.append(new_sublist)
            prev_start = curr_size
            curr_size = len(res)
        return res
