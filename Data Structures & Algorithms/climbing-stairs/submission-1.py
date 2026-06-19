class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        def helper(n):
            if n in cache:
                return cache[n]
            else:
                res = helper(n - 1) + helper(n - 2)
                cache[n] = res
                return res

        return helper(n)
        