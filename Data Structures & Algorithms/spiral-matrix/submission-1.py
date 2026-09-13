class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        def helper(direction, top, bottom, left, right):
            if (top <= bottom and left <= right):
                match direction:
                    case "right":
                        for col in range(left, right + 1):
                            res.append(matrix[top][col])
                        helper("down", top + 1, bottom, left, right)
                    case "down":
                        for row in range(top, bottom + 1):
                            res.append(matrix[row][right])
                        helper("left", top, bottom, left, right - 1)
                    case "left":
                        for col in range(right, left - 1, -1):
                            res.append(matrix[bottom][col])
                        helper("up", top, bottom - 1, left, right)
                    case "up":
                        for row in range(bottom, top - 1, -1):
                            res.append(matrix[row][left])
                        helper("right", top, bottom, left + 1, right)

        helper("right", 0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        return res
