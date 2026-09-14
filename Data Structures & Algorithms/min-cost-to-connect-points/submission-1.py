class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        distances = [float('inf')] * n
        edges = 0
        curr_node = 0
        res = 0
        while edges != n - 1:
            visited[curr_node] = True
            next_node, cost = -1, float('inf')
            for point, coordinates in enumerate(points):
                if visited[point]:
                    continue
                curr_distance = abs(points[curr_node][0] - coordinates[0]) + abs(points[curr_node][1] - coordinates[1])
                distances[point] = min(distances[point], curr_distance)
                if distances[point] < cost:
                    cost = distances[point]
                    next_node = point
            res += cost
            curr_node = next_node
            edges += 1
        return res