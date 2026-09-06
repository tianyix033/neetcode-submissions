from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adj_map = [[] for i in range(n + 1)]
        for time in times:
            adj_map[time[0]].append((time[1], time[2]))
        curr_time = 0
        reachable = {}
        reachable[0] = [k]
        farthest_future = 0

        while farthest_future >= curr_time:
            
            if curr_time in reachable:
                for curr_node in reachable[curr_time]:
                    if curr_node in visited:
                        continue
                    visited.add(curr_node)

                    for adj_node, adj_time in adj_map[curr_node]:
                        if adj_node not in visited:
                            target_time = curr_time + adj_time
                            if target_time not in reachable:
                                reachable[target_time] = []
                            reachable[target_time].append(adj_node)
                            farthest_future = max(farthest_future, target_time)
            if len(visited) == n:
                return curr_time

            curr_time += 1


        return -1
        
            

