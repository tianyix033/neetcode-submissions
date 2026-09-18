import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], (0, 0))]
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            height, node = heapq.heappop(heap)
            if node[0] == (n - 1) and node[1] == (n - 1):
                return height                
            if node in visited:
                continue
            visited.add(node)
            for dir_r, dir_c in directions:
                new_r, new_c = dir_r + node[0], dir_c + node[1]
                if 0 <= new_r < n and 0 <= new_c < n and (new_r, new_c) not in visited:
                    heapq.heappush(heap, (max(height, grid[new_r][new_c]), (new_r, new_c)))
        return -1
        