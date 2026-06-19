class Solution:
    def rob(self, nums: List[int]) -> int:
        do = dont = 0
        for num in nums:
            dont_new = max(do, dont)
            do_new = dont + num
            do = do_new
            dont = dont_new
        return max(do, dont)