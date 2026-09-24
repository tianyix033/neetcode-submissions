class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        res = 0
        curr_start = 0
        for i, char in enumerate(s):
            if char not in hashmap or hashmap[char] < curr_start:
                hashmap[char] = i
            else:
                res = max(res, i - curr_start)
                curr_start = hashmap[char] + 1
                hashmap[char] = i
        res = max(res, len(s) - curr_start)
        return res
            