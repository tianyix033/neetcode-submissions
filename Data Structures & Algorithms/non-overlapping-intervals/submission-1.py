class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = float('-inf')
        for start, end in intervals:
            if start < prev_end:
                res += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return res
