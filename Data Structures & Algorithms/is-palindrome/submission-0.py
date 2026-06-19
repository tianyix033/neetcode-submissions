class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        l = 0
        while (l < len(s) - 1) and (not s[l].isalnum()):
            l += 1
        r = len(s) - 1
        while (r > 0) and (not s[r].isalnum()):
            r -= 1
        if l >= r:
            return True
        if s[l].lower() != s[r].lower():
            return False
        else:
            return self.isPalindrome(s[l + 1 : r])        