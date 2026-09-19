"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = [] # timestamp, is_start
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, 0))
        events.sort()   # ending events get put first for the same timestamp
        curr_rooms = 0
        res = 0
        for event in events:
            if event[1]:
                curr_rooms += 1
                res = max(res, curr_rooms)
            else:
                curr_rooms -= 1
        return res