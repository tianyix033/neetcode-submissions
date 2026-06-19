class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = list(s)
        l = 0
        r = 0
        res = 0
        seen = {}
        while r < len(lst):
            while r < len(lst) and lst[r] not in seen:
                seen[lst[r]] = r
                r += 1
            res = max(res, r - l)
            if r < len(lst):
                newl = seen[lst[r]] + 1
                for i in range(l, newl):
                    del seen[lst[i]]
                l = newl
        return res



        