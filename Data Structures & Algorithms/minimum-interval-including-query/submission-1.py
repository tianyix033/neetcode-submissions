import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        hashmap = {}
        heap = []
        i = 0
        for query in sorted(queries):
            if query in hashmap:
                continue
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if not heap:
                hashmap[query] = -1
            else:
                hashmap[query] = heap[0][0]
        output = [hashmap[query] for query in queries]
        return output
