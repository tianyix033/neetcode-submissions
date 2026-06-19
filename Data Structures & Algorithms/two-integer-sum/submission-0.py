class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        ind = 0
        while ind < len(nums):
            complement = target - nums[ind]
            if complement not in myDict:
                myDict[nums[ind]] = ind
                ind += 1
            else:
                first_ind = myDict[complement]
                second_ind = ind
                ind += len(nums)
        return [first_ind, second_ind]
        