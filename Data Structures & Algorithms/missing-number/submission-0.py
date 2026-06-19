class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        idx = 0
        while (idx < len(nums)):
            cur = int(nums[idx])
            if ((cur == -1) or (cur == idx) or (nums[cur] == cur)):
                idx += 1
            else:
                nums[cur], nums[idx] = nums[idx], nums[cur]
        for i in range(len(nums)):
            if (nums[i] == -1):
                return i
        return -1

        