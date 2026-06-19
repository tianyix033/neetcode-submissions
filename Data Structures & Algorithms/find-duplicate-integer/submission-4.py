class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        ptr = 0
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]
        return ptr