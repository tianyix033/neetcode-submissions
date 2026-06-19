class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = 1
        cache[1] = 1
        def helper(n):
            if cache[n]:
                return cache[n]
            else:
                res = helper(n - 1) + helper(n - 2)
                cache[n] = res
                return res

        return helper(n)
        