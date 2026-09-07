from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = [[] for i in range(n + 1)]
        for time in times:
            adj_map[time[0]].append((time[1], time[2]))
        shortest_times = [float('inf')] * (n + 1)
        shortest_times[0] = -1
        shortest_times[k] = 0
        queue = deque()
        queue.append((k, 0))

        while queue:
            source, curr_time = queue.popleft()
            if shortest_times[source] < curr_time:
                continue
            for target, time_to_reach in adj_map[source]:
                new_time = time_to_reach + curr_time
                if new_time < shortest_times[target]:
                    shortest_times[target] = new_time
                    queue.append((target, new_time))

        res = max(shortest_times)
        return res if res != float('inf') else -1