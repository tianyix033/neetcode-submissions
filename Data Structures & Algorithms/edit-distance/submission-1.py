class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def helper(pos1, pos2):
            res = -1
            if pos2 == len(word2):
                return len(word1) - pos1
            if pos1 == len(word1):
                return len(word2) - pos2            
            if (pos1, pos2) in cache:
                return cache[(pos1, pos2)]
            if word1[pos1] == word2[pos2]:
                res = helper(pos1 + 1, pos2 + 1)
                cache[(pos1, pos2)] = res
                return res
            
            res = 1 + min(helper(pos1 + 1, pos2), helper(pos1, pos2 + 1), helper(pos1 + 1, pos2 + 1))
            cache[(pos1, pos2)] = res
            return res
        
        return helper(0, 0)