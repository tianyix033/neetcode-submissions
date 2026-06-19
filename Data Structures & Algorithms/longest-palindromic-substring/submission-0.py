import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def centeredPalindrome(pos):
            if isinstance(pos, int):
                left = right = pos
            else:
                left = math.floor(pos)
                right = math.ceil(pos)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        max_len = 0
        resl, resr = -1, -1
        for i in range(len(s)):
            left, right = centeredPalindrome(i)
            if (right - left + 1) > max_len:
                max_len = right - left + 1
                resl, resr = left, right
            left, right = centeredPalindrome(i + 0.5)
            if (right - left + 1) > max_len:
                max_len = right - left + 1
                resl, resr = left, right

        return s[resl:resr + 1]