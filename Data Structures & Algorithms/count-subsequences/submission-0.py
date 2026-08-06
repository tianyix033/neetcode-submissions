class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        cache = {}

        def helper(s_pos, t_pos):
            if t_pos == len(t):
                return 1
            if s_pos == len(s):
                return 0
            if (s_pos, t_pos) in cache:
                return cache[(s_pos, t_pos)]
            res = 0
            if s[s_pos] == t[t_pos]:
                res += helper(s_pos + 1, t_pos + 1)
            res += helper(s_pos + 1, t_pos)
            cache[(s_pos, t_pos)] = res
            return res

        return helper(0, 0)