class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = [[] for i in range(n + 1)]
        for time in times:
            adj_map[time[0]].append((time[1], time[2]))
        shortest_times = [float('inf')] * (n + 1)
        shortest_times[0] = -1

        def dfs(node, time):
            if time >= shortest_times[node]:
                return
            shortest_times[node] = time
            for neighbor, weight in adj_map[node]:
                dfs(neighbor, time + weight)

        dfs(k, 0)
        res = max(shortest_times)
        return res if res != float('inf') else -1