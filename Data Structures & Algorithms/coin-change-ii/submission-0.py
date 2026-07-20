class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # assume coins is sorted low to high

        cache = {}
        def helper(target, start):
            if target < 0:
                return 0
            if target == 0:
                return 1
            if (target, start) in cache:
                return cache[(target, start)]
            res = 0
            for i in range(start, len(coins)):
                res += helper(target - coins[i], i)
            cache[(target, start)] = res
            return res

        return helper(amount, 0)

        