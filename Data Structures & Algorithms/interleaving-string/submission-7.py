class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # make sure s2 is the shorter string
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        memo = [False] * (len(s2) + 1)

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i == len(s1) and j == len(s2):
                    memo[j] = True
                elif i == len(s1):
                    memo[j] = memo[j + 1] and (s2[j] == s3[i + j])
                elif j == len(s2):
                    memo[j] = memo[j] and (s1[i] == s3[i + j])
                else:
                    memo[j] = (memo[j + 1] and (s2[j] == s3[i + j])) or\
                                 (memo[j] and (s1[i] == s3[i + j]))

        return memo[0]