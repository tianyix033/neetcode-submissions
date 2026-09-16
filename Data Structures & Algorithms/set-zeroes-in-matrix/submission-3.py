class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row1, zero_col1 = False, False
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        zero_row1 = True
                    if c == 0:
                        zero_col1 = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0
        
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0
        
        if zero_row1:
            for c in range(cols):
                matrix[0][c] = 0
        
        if zero_col1:
            for r in range(rows):
                matrix[r][0] = 0

        


        