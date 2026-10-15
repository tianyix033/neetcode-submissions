class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                val = int(val)
                mask = 1 << (val - 1)
                if cols[col] & mask:
                    return False
                cols[col] |= mask
                if rows[row] & mask:
                    return False
                rows[row] |= mask
                box = row // 3 * 3 + col // 3
                if boxes[box] & mask:
                    return False
                boxes[box] |= mask
        return True
