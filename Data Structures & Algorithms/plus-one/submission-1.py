class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        num = int("".join(digits))
        num += 1
        num_str = str(num)
        return [int(digit) for digit in num_str]
        