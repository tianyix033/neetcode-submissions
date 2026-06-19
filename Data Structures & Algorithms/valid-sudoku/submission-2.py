class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board) # 9
        rows = [0] * n
        columns = [0] * n
        squares = [[0] * int(n ** 0.5) for i in range(int(n ** 0.5))]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)
                mask = 1 << val
                square_i = i // 3
                square_j = j // 3
                if (rows[i] & mask) or (columns[j] & mask) or (squares[square_i][square_j] & mask):
                    return False
                else:
                    rows[i] |= mask
                    columns[j] |= mask
                    squares[square_i][square_j] |= mask
        
        return True