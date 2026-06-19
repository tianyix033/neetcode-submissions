class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board_x, board_y, pos):
            if pos == len(word):
                return True

            if not (0 <= board_x < len(board) and 0 <= board_y < len(board[0])):
                return False

            if board[board_x][board_y] == word[pos]:
                board[board_x][board_y] = '#'
                res = dfs(board_x - 1, board_y, pos + 1) or\
                      dfs(board_x + 1, board_y, pos + 1) or\
                      dfs(board_x, board_y - 1, pos + 1) or\
                      dfs(board_x, board_y + 1, pos + 1)
                board[board_x][board_y] = word[pos]
                return res

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
