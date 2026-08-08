class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        dp = [len(word2) - i for i in range(len(word2) + 1)]
        for i in range(len(word1) - 1, -1, -1):
            nextdp = dp[-1]
            dp[-1] = len(word1) - i
            for j in range(len(word2) - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = nextdp
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], nextdp)
                nextdp = temp
        return dp[0]