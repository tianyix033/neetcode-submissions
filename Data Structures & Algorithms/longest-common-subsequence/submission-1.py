class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                curr[j] = max(curr[j - 1], prev[j],\
                prev[j - 1] + int(text1[i - 1] == text2[j - 1]))
            prev = curr
            curr = [0] * (len(text2) + 1)
        return prev[-1]
            
