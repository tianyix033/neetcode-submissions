class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        res = []
        sublist = []
        def helper(i, curr_sum):
            if curr_sum > target:
                return
            if i == len(candidates):
                if curr_sum == target:
                    res.append(sublist.copy())
            else:
                sublist.append(candidates[i])
                helper(i + 1, curr_sum + candidates[i])
                popped = sublist.pop()
                if not sublist or sublist[-1] != popped:
                    helper(i + 1, curr_sum)

        helper(0, 0)
        return res
