class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def wordcmp(word, pos):
            if pos + len(word) > len(s):
                return False
            for i, c in enumerate(word):
                if c != s[pos + i]:
                    return False

            return True

        def helper(pos):
            if pos in cache:
                return cache[pos]
            if pos >= len(s):
                return True
            res = False
            for word in wordDict:
                if wordcmp(word, pos):
                    res = res or helper(pos + len(word))
            cache[pos] = res
            return res
            
        return helper(0)
        