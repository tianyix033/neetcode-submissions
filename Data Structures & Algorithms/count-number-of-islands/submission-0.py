class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        groups = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    groups += 1
        return groups

        

        