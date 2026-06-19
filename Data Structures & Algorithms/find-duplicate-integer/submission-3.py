class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = 0
        for i in range(16):
            pos = 1 << i
            supposed = sum((j & pos == pos) for j in range(1, len(nums)))
            actual = sum((num & pos == pos) for num in nums)
            if actual > supposed:
                res |= pos
        return res