class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total / 2
        visited = set([0])
        for num in nums:
            if target - num in visited:
                return True
            temp = set()
            for prev_sum in visited:
                temp.add(prev_sum + num)
            visited |= temp
        return False