class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = -1
        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)

        for i in range(rows):
            for j in range(cols):
                res = max(res, dfs(i, j))
        return res