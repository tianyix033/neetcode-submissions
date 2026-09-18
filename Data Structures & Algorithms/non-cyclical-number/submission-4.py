class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        fast = slow = n
        init = True
        
        while init or fast != slow:
            init = False
            slow = sum([int(i) ** 2 for i in str(slow)])
            fast = sum([int(i) ** 2 for i in str(fast)])
            fast = sum([int(i) ** 2 for i in str(fast)])
            if fast == 1 or slow == 1:
                return True

        return False
