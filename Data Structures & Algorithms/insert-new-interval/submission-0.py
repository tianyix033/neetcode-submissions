class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        breakpoint = len(intervals)
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                breakpoint = i
                break
        if breakpoint > 0 and intervals[breakpoint - 1][1] >= newInterval[0]:
            intervals[breakpoint - 1][1] = max(intervals[breakpoint - 1][1], newInterval[1])
            breakpoint -= 1
        else:
            intervals.insert(breakpoint, newInterval)
        for i in range(breakpoint + 1, len(intervals)):
            if intervals[i][0] <= intervals[breakpoint][1]:
                intervals[breakpoint][1] = max(intervals[breakpoint][1], intervals[i][1])
                intervals[i] = None
            else:
                break
        left = 0
        while left < len(intervals) and intervals[left] != None:
            left += 1
        if left < len(intervals):
            right = left
            while right < len(intervals) and intervals[right] == None:
                right += 1
            if right < len(intervals):
                while right < len(intervals):
                    intervals[left] = intervals[right]
                    intervals[right] = None
                    left += 1
                    right += 1
            while intervals[-1] == None:
                intervals.pop()

        return intervals

                    