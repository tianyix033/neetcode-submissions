class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) - 2):
            temp = {}
            target = -nums[i]
            for cur in range(i + 1, len(nums)):
                val = nums[cur]
                if val in temp:
                    for entry in temp[val]:
                        res.append([nums[i], nums[entry], nums[cur]])
                if target - val in temp:
                    temp[target - val].append(cur)
                else:
                    temp[target - val] = [cur]

        return remove_dup(res)

def remove_dup(lst):
    seen = set(tuple(sorted(sublst)) for sublst in lst)
    return list(seen)
