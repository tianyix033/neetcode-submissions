class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start = end = -1
        res = []
        for curr_start, curr_end in intervals:
            if curr_start > end:
                if end >= 0:
                    res.append([start, end])
                start = curr_start
                end = curr_end
            else:
                end = max(end, curr_end)
        res.append([start, end])
        return res