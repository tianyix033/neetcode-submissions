"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x : x.start)
        prev_end = -1
        for interval in intervals:
            if interval.start >= prev_end:
                prev_end = max(prev_end, interval.end)
            else:
                return False
        return True