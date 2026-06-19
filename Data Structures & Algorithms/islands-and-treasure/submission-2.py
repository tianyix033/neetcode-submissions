from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        
        while queue:
            i, j, distance = queue.popleft()    
            if grid[i][j] == -1:
                continue
            grid[i][j] = distance
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (0 <= nr < rows) and (0 <= nc < cols) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1))

        

        
