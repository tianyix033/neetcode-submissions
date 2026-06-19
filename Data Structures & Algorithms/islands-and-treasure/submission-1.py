class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        def helper(i, j, distance):
            if (not ( 0 <= i < rows and 0 <= j < cols)) or (grid[i][j] <= distance):
                return
            grid[i][j] = distance
            helper(i - 1, j, distance + 1)
            helper(i + 1, j, distance + 1)
            helper(i, j - 1, distance + 1)
            helper(i, j + 1, distance + 1)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    helper(i - 1, j, 1)
                    helper(i + 1, j, 1)
                    helper(i, j - 1, 1)
                    helper(i, j + 1, 1)