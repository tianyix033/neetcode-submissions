class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []
        for char in s:
            if char.isalnum():
                lst.append(char.lower())
        return lst == lst[::-1]