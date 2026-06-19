import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = [row[-1] for row in matrix]
        column_pos = bisect.bisect(columns, target)
        if column_pos > 0 and columns[column_pos - 1] == target:
            return True
        elif column_pos >= len(matrix):
            return False
        target_row = matrix[column_pos]
        row_pos = bisect.bisect(target_row, target)
        if row_pos > 0 and target_row[row_pos - 1] == target:
            return True
        return False