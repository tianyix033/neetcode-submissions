from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        indegree = [[0] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if not ((0 <= new_i < rows) and (0 <= new_j < cols)):
                        continue
                    if matrix[new_i][new_j] < matrix[i][j]:
                        indegree[i][j] += 1
        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if indegree[i][j] == 0:
                    queue.append((i, j))
        
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if not ((0 <= new_i < rows) and (0 <= new_j < cols)):
                        continue
                    if matrix[i][j] < matrix[new_i][new_j]:
                        indegree[new_i][new_j] -= 1
                        if indegree[new_i][new_j] == 0:
                            queue.append((new_i, new_j))
            
            level += 1
        return level

        