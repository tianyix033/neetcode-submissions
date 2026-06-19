class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for row in board:
            visited = set()
            for val in row:
                if val != '.' and val in visited:
                    return False
                else:
                    visited.add(val)
        for col_idx in range(n):
            visited = set()
            for row_idx in range(n):
                val = board[row_idx][col_idx]
                if val != '.' and val in visited:
                    return False
                else:
                    visited.add(val)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                visited = set()
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        val = board[ii][jj]
                        if val != '.' and val in visited:
                            return False
                        else:
                            visited.add(val)
        return True

