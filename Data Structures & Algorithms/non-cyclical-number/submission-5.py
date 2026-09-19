class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(n):
            return sum([int(i) ** 2 for i in str(n)])
        fast = sum_of_squares(n)
        slow = n
        exp = 1
        count = 1

        while slow != fast:
            if count == exp:
                exp *= 2
                count = 0
                slow = fast
            fast = sum_of_squares(fast)
            if fast == 1:
                return True
            count += 1

        return fast == 1

