class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]

        max_len = 0
        resl, resr = -1, -1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if (j - i) < 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if (j - i + 1) > max_len:
                            max_len = j - i + 1
                            resl, resr = i, j
        return s[resl : resr + 1]
                    