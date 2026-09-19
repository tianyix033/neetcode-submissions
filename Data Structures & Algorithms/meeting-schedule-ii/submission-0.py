"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x : x.start)
        endings = []
        curr_rooms = 0
        res = 0
        for interval in intervals:
            while endings and endings[0] <= interval.start:
                heapq.heappop(endings)
                curr_rooms -= 1
            heapq.heappush(endings, interval.end)
            curr_rooms += 1
            res = max(res, curr_rooms)
        return res
            