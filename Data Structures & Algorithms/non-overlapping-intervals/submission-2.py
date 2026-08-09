class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        cache = [0] * len(intervals)
        cache[0] = 1
        def helper(i):
            if cache[i] > 0:
                return cache[i]
            res = helper(i - 1)
            start = 0
            end = i
            while start < end:
                mid = (start + end) // 2
                if intervals[mid][1] > intervals[i][0]:
                    end = mid
                else:
                    start = mid + 1
            if start >= 1:
                res = max(res, 1 + cache[start - 1]) 
            cache[i] = res
            return res

        for i in range(len(intervals)):
            helper(i)
        return len(intervals) - cache[-1]
