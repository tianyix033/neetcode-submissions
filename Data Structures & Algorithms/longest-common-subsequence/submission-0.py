class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def helper(pos1, pos2):
            if pos1 < 0 or pos2 < 0:
                return 0
            if (pos1, pos2) in cache:
                return cache[(pos1, pos2)]
            res = max(helper(pos1 - 1, pos2 - 1) + int(text1[pos1] == text2[pos2]),\
                  helper(pos1 - 1, pos2), helper(pos1, pos2 - 1))
            cache[(pos1, pos2)] = res
            return res

        return helper(len(text1) - 1, len(text2) - 1)