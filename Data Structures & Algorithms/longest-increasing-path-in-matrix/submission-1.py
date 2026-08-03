class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = [[0] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def helper(i, j):
            if cache[i][j]:
                return cache[i][j]
            cell_val = 1
            for x, y in directions:
                new_i, new_j = i + x, j + y
                if not ((0 <= new_i < rows) and (0 <= new_j < cols)):
                    continue
                if matrix[new_i][new_j] > matrix[i][j]:
                    cell_val = max(cell_val, 1 + helper(new_i, new_j))
            cache[i][j] = cell_val
            return cell_val

        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, helper(i, j))
        return res

        
