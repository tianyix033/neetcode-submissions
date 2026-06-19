class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board_x, board_y, pos, visited):
            if pos >= len(word):
                return True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dir_x, dir_y in directions:
                new_cell_x, new_cell_y = board_x + dir_x, board_y + dir_y
                if (0 <= new_cell_x < len(board) and 0 <= new_cell_y < len(board[0]))\
                and (new_cell_x, new_cell_y) not in visited\
                and board[new_cell_x][new_cell_y] == word[pos]:
                    visited.add((new_cell_x, new_cell_y))
                    if dfs(new_cell_x, new_cell_y, pos + 1, visited):
                        return True
                    visited.remove((new_cell_x, new_cell_y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1, set([(i, j)])):
                        return True
        return False