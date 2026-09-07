class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest_times = [float('inf')] * (n + 1)
        shortest_times[0] = -1
        shortest_times[k] = 0

        for i in range(n):
            for u, v, time in times:
                shortest_times[v] = min(shortest_times[v], shortest_times[u] + time)

        res = max(shortest_times)
        return res if res != float('inf') else -1