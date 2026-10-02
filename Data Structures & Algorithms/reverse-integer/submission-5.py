class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = (1 << 31) - 1
        signed = 1 if x < 0 else 0
        x = abs(x)
        res = 0
        while x >= 10:
            digit = x % 10            
            res = res * 10 + digit            
            x = x // 10
        if (MAX_INT + signed) // 10 < res:
            return 0
        elif (MAX_INT + signed) // 10 == res and (MAX_INT + signed) % 10 < x:
            return 0
        res = res * 10 + x
        if signed:
            res = -res
        return res