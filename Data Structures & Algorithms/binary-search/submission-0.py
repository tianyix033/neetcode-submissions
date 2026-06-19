class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            res = nums.index(target)
        except ValueError:
            return -1
        else:
            return res
        