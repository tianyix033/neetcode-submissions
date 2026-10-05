from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        counter = Counter(nums)
        res = []
        for i in range(len(nums) - 2):
            counter[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                counter[nums[j]] -= 1
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                target = - nums[i] - nums[j]
                if target in counter and counter[target] > 0:
                    res.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums) - 1):
                counter[nums[j]] += 1
        return res

[-4, -1, -1, 0, 1, 2]
