class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0:
            return x
        if x == -1:
            return -1 if n % 2 else 1
        if (n > (1 << 15)):
            if x > 1:
                return float('inf')
            elif -1 < x < 1:
                return 0
            else:
                return -float('inf')
        elif (-n > (1 << 15)):
            if x > 1 or x < -1:
                return 0
            elif 0 < x < 1:
                return float('inf')
            else:
                return -float('inf') if n % 2 else float('int')
        res = 1
        for i in range(abs(n)):
            res *= x
        return res if n >= 0 else 1 / res