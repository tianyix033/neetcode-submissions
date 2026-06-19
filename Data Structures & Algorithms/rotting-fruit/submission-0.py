from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        queue = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        while queue:
            num_iters = len(queue)
            for iter in range(num_iters):
                rotten_cell = queue.popleft()
                for direction in directions:
                    new_cell_i, new_cell_j = rotten_cell[0] + direction[0], \
                                             rotten_cell[1] + direction[1]
                    if 0 <= new_cell_i < len(grid) and \
                    0 <= new_cell_j < len(grid[0]) and \
                    grid[new_cell_i][new_cell_j] == 1:
                        grid[new_cell_i][new_cell_j] = 2
                        queue.append((new_cell_i, new_cell_j))
            time += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(time - 1, 0)
        

