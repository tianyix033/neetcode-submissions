from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()    
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[i][j] + 1
                    queue.append((nr, nc))

        

        
