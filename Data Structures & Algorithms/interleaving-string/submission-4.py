class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def helper(pos1, pos2):
            if (pos1, pos2) in cache:
                return cache[(pos1, pos2)]
            if pos1 >= len(s1) and pos2 >= len(s2):
                return True
            if pos2 < len(s2) and s2[pos2] == s3[pos1 + pos2]:
                if helper(pos1, pos2 + 1):
                    cache[(pos1, pos2)] = True
                    return True
            elif pos1 < len(s1) and s1[pos1] == s3[pos1 + pos2]:
                if helper(pos1 + 1, pos2):
                    cache[(pos1, pos2)] = True
                    return True
            cache[(pos1, pos2)] = False
            return False

        return helper(0, 0)
