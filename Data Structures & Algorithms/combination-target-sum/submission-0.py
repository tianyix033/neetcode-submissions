class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort(reverse=True)
        res = []
        sublist = []

        def helper(pos, curr_sum):
            if curr_sum == target:
                res.append(sublist.copy())
            elif pos < len(nums) and curr_sum < target:
                sublist.append(nums[pos])
                helper(pos, curr_sum + nums[pos])
                sublist.pop()
                helper(pos + 1, curr_sum)

        helper(0, 0)
        return res

        