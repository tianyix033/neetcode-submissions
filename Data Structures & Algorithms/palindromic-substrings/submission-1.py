class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        dp = [[False] * n for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                valid = (((j - i) < 2) or dp[i + 1][j - 1]) and (s[i] == s[j])
                if valid:
                    res += 1
                    dp[i][j] = True

        return res
        