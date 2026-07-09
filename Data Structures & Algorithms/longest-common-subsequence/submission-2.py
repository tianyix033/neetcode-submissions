class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        curr = [0] * (len(text2) + 1)
        for i in range(1, len(text1) + 1):
            prev = 0
            for j in range(1, len(text2) + 1):
                temp_prev = curr[j]
                curr[j] = max(curr[j - 1], curr[j],\
                prev + int(text1[i - 1] == text2[j - 1]))
                prev = temp_prev
        return curr[-1]
            
