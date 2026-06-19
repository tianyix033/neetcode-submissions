class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 1
        res = 0
        carry = 0
        while mask < 2 ** 32:
            a_digit = mask & a
            b_digit = mask & b
            if (a_digit and b_digit and carry):
                res |= mask
                carry = 1
            elif (a_digit and b_digit) or (a_digit and carry) or (b_digit and carry):
                carry = 1
            elif (a_digit or b_digit or carry):
                res |= mask
                carry = 0

            mask <<= 1
        
        # flip all bits 32 - 1, so now we only have the bit we need,
        # then we ~ it to flip everything and now it's considered
        # a negative number
        return res if res < 2 ** 31 else ~(res ^ (2 ** 32 - 1))
                
