import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        frontier = [(0, 0)] # heap: (cost, node)
        res = 0
        while len(visited) != len(points):
            cost, node = heapq.heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            res += cost
            for point, coordinates in enumerate(points):
                if point not in visited:
                    distance = abs(points[node][0] - coordinates[0]) + abs(points[node][1] - coordinates[1])
                    heapq.heappush(frontier, (distance, point))
        return res