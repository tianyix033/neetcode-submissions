from collections import defaultdict
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for start, end in intervals:
            mp[start] += 1
            mp[end] -= 1
        
        res = []
        curr_interval = []
        active_intervals = 0
        for key in sorted(mp):
            if not curr_interval:
                curr_interval.append(key)
            active_intervals += mp[key]
            if active_intervals == 0:
                curr_interval.append(key)
                res.append(curr_interval)
                curr_interval = []

        return res
