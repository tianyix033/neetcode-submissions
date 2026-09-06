import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adj_map = [[] for i in range(n + 1)]
        for time in times:
            adj_map[time[0]].append((time[1], time[2]))
        events = [(0, k)]

        while events:
            time, node = heapq.heappop(events)
            if node in visited:
                continue
            visited.add(node)

            for adj_node, adj_time in adj_map[node]:
                if adj_node not in visited:
                    heapq.heappush(events, (time + adj_time, adj_node))
                            
            if len(visited) == n:
                return time

        return -1
        
            

