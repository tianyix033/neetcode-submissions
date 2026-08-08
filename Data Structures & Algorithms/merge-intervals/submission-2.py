class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = [-1] * (max(intervals)[0] + 1)
        for start, end in intervals:
            mp[start] = max(mp[start], end)
        
        res = []
        start = end = -1
        for curr_start, curr_end in enumerate(mp):
            if curr_start > end:
                if end >= 0:
                    res.append([start, end])
                start = curr_start
                end = curr_end
            else:
                end = max(end, curr_end)
        res.append([start, end])
        return res
            
