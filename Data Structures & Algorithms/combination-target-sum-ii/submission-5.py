from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        unique_nums = list(set(candidates))
        sublist = []
        res = []
        def helper(i, curr_sum):   
            if curr_sum == target:
                res.append(sublist.copy())
            elif i < len(unique_nums) and curr_sum < target:
                candidate = unique_nums[i]
                if counter[candidate] > 0:
                    counter[candidate] -= 1
                    sublist.append(candidate)
                    helper(i, curr_sum + candidate)
                    sublist.pop()
                    counter[candidate] += 1
                helper(i + 1, curr_sum)
            
        helper(0, 0)
        return res
