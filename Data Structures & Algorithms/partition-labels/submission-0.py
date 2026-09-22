class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i, char in enumerate(s):
            if char not in hashmap:
                hashmap[char] = [i, i]
            else:
                hashmap[char][1] = i
        sub_start = sub_end = 0
        res = []
        for start, end in sorted(hashmap.values()):
            if start <= sub_end:    # equality only possible for first entry
                sub_end = max(sub_end, end)
            else:
                res.append(sub_end - sub_start + 1)
                sub_start = start
                sub_end = end
        res.append(sub_end - sub_start + 1)
        return res
            