class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] in ('A', 'X'):
                return 
            board[r][c] = 'A'
            for dir_r, dir_c in directions:
                dfs(r + dir_r, c + dir_c)

        def replace(prev, curr):
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == prev:
                        board[r][c] = curr

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        replace('O', 'X')
        replace('A', 'O')
        