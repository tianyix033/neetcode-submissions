class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # assume coins is sorted low to high
        coins.sort()

        cache = {}
        def helper(target, pos):
            if target < 0 or pos >= len(coins):
                return 0
            if target == 0:
                return 1
            if (target, pos) in cache:
                return cache[(target, pos)]
            # either take current coin or move on to the next
            res = 0
            if target >= coins[pos]:
                res += helper(target - coins[pos], pos) + helper(target, pos + 1)    
            cache[(target, pos)] = res
            return res

        return helper(amount, 0)

        