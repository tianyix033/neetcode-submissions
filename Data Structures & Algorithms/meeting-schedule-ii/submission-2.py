"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        curr_rooms = 0
        res = 0
        for time in sorted(mp.keys()):
            curr_rooms += mp[time]
            res = max(res, curr_rooms)
        return res