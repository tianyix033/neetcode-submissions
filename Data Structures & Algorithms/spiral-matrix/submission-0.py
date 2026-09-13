class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        layers = (min(rows, cols) + 1) // 2
        for i in range(layers):
            if i == (rows - 1) / 2:
                for col in range(i, cols - i):
                    res.append(matrix[i][col]) 
            elif i == (cols - 1) / 2:
                for row in range(i, rows - i):
                    res.append(matrix[row][cols - i - 1])
            else:
                for col in range(i, cols - i - 1):
                    res.append(matrix[i][col])
                for row in range(i, rows - i - 1):
                    res.append(matrix[row][cols - i - 1])
                for col in range(cols - i - 1, i, -1):
                    res.append(matrix[rows - i - 1][col])
                for row in range(rows - i - 1, i, -1):
                    res.append(matrix[row][i])
        return res