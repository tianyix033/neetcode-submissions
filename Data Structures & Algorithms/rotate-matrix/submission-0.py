class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n // 2):
            anchor = layer
            side = n - 2 * layer - 1
            print(anchor, side)
            for i in range(side):
                matrix[anchor][anchor + i], matrix[anchor + i][anchor + side], matrix[anchor + side][anchor + side - i], matrix[anchor + side - i][anchor] = matrix[anchor + side - i][anchor], matrix[anchor][anchor + i], matrix[anchor + i][anchor + side], matrix[anchor + side][anchor + side - i]
