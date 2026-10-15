class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            filled = [0] * 10
            for val in row:
                if val == '.': 
                    continue
                val = int(val)
                if not filled[val]:
                    filled[val] = 1
                else:
                    return False
        for col in range(9):
            filled = [0] * 10
            for row in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                val = int(val)
                if not filled[val]:
                    filled[val] = 1
                else:
                    return False

        pivots = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
        for pivot_r, pivot_c in pivots:
            filled = [0] * 10
            for row in range(3):
                for col in range(3):
                    val = board[pivot_r + row][pivot_c + col]
                    if val == '.':
                        continue
                    val = int(val)
                    if not filled[val]:
                        filled[val] = 1
                    else:
                        return False
        
        return True
