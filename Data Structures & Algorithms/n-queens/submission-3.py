from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queens = []
        cols = 1 << (n + 1)
        diags_1 = 1 << (2 * n + 1)
        diags_2 = 1 << (2 * n + 1)
        res = []
        def helper(r):
            nonlocal cols, diags_1, diags_2
            if len(queens) == n:
                res.append(queens.copy())
                return
            for c in range(n):
                c_mask = 1 << c
                diags_1_mask = 1 << (r - c + n)
                diags_2_mask = 1 << (r + c)
                if (not cols & c_mask) and (not diags_1 & diags_1_mask) and (not diags_2 & diags_2_mask):
                    queens.append((r, c))
                    cols |= c_mask
                    diags_1 |= diags_1_mask
                    diags_2 |= diags_2_mask
                    helper(r + 1)
                    cols &= ~c_mask
                    diags_1 &= ~diags_1_mask
                    diags_2 &= ~diags_2_mask
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