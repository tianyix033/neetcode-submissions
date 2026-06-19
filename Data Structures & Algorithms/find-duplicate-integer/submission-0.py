class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            pos = 1 << num
            if mask & pos == pos:
                return num
            else:
                mask |= pos
        return -1

        