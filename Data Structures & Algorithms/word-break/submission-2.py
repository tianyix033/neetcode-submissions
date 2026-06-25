class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        wordSet = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i : j + 1] in wordSet and (j + 1 == len(s) or dp[j + 1]):
                    dp[i] = True
                    break
        return dp[0]