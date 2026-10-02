class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False if x >= 0 else True
        x_str = str(abs(x))
        new_num = int("".join([x_str[i] for i in range(len(x_str) - 1, -1, -1)]))
        if is_neg:
            new_num = -new_num
        if new_num > ((1 << 31) - 1) or new_num < -(1 << 31):
            return 0
        else:
            return new_num