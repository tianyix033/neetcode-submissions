class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        digits[pos] += 1
        while digits[pos] == 10:
            digits[pos] = 0
            pos -= 1
            if pos >= 0:
                digits[pos] += 1
            else:
                digits.insert(0, 1)
                pos = 0
        return digits
        