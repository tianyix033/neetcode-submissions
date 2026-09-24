class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if x == -1:
            return -1 if n % 2 else 1
        def helper(n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            res = helper(n // 2)
            return res * res * helper(n % 2)

        return helper(n) if n >= 0 else 1 / helper(-n)
        