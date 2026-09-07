from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        cols = [False] * n
        diags_1 = defaultdict(bool)
        diags_2 = defaultdict(bool)
        diags_2 = [False] * (2 * n - 1)
        res = []
        def helper(r):
            if len(queens) == n:
                res.append(queens.copy())
                return
            for c in range(n):
                if (not cols[c]) and (not diags_1[r - c]) and (not diags_2[r + c]):
                    queens.append((r, c))
                    cols[c] = True
                    diags_1[r - c] = True
                    diags_2[r + c] = True
                    helper(r + 1)
                    cols[c] = False
                    diags_1[r - c] = False
                    diags_2[r + c] = False
                    queens.pop()
        
        helper(0)
        # print(res)
        ret = []
        for queens in res:
            grid = [["."] * n for _ in range(n)]
            for queen_r, queen_c in queens:
                grid[queen_r][queen_c] = "Q"
            grid = ["".join(row) for row in grid]
            ret.append(grid.copy())
        return ret