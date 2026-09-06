class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = [[] for i in range(n + 1)]
        for time in times:
            adj_map[time[0]].append((time[1], time[2]))

        shortest_grid = [[float('inf')] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            shortest_grid[i][i] = 0
            for neighbor, time in adj_map[i]:
                shortest_grid[i][neighbor] = time
        
        for m in range(n + 1):
            for i in range(n + 1):
                for j in range(n + 1):
                    shortest_grid[i][j] = min(shortest_grid[i][j], shortest_grid[i][m] + shortest_grid[m][j])

        res = max(shortest_grid[k][1:])
        return res if res != float('inf') else -1