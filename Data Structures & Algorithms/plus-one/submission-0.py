class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - i - 1))
        num += 1
        num_str = str(num)
        return [int(digit) for digit in num_str]
        