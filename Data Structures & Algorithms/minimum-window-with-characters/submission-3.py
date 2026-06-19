from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        res = ""

        def shrink(l, freq):
            # we start with a valid frequency and end with one
            while True:
                if s[l] in target and freq[s[l]] == target[s[l]]:
                    return l
                else:
                    freq[s[l]] -= 1
                    l += 1
        
        if len(s) < len(t):
            return res

        l = 0
        matched = 0
        needed = len(target)
        freq = defaultdict(int)
        min_length = len(s) + 1
        for r in range(len(s)):
            freq[s[r]] += 1
            if freq[s[r]] == target[s[r]]:
                matched += 1
            if matched == needed:
                l = shrink(l, freq)
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    res = s[l:r + 1]
        return res
