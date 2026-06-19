from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        res = ""
        def is_valid(freq):
            for char in target:
                if freq[char] < target[char]:
                    return False
            return True 

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
        freq = {chr(ord('A') + i) : 0 for i in range(26)}
        temp_freq = {chr(ord('a') + i) : 0 for i in range(26)}
        freq = freq | temp_freq
        min_length = len(s) + 1
        for r in range(len(s)):
            freq[s[r]] += 1
            if is_valid(freq):
                l = shrink(l, freq)
                if (r - l + 1) < min_length:
                    min_length = r - l + 1
                    res = s[l:r + 1]
        return res
