class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = (1 << 31) - 1
        signed = 1 if x < 0 else 0
        x = abs(x)
        res = 0
        while x:
            digit = x % 10
            if (MAX_INT + signed - digit) / 10 < res:
                return 0
            res = res * 10 + digit            
            x = x // 10
        if signed:
            res = -res
        return res