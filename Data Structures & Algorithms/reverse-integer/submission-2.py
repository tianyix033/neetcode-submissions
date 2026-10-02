class Solution:
    def reverse(self, x: int) -> int:
        signed = True if x < 0 else False
        x = abs(x)
        reversed_digits = []
        while x:
            digit = x % 10
            reversed_digits.append(digit)
            x = x // 10
        res = 0
        for i, digit in enumerate(reversed(reversed_digits)):
            res += digit * (10 ** i)
        if signed:
            res = -res
        if res > ((1 << 31) - 1) or res < -(1 << 31):
            return 0
        return res