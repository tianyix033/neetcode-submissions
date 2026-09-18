class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def helper(t):
            visited = set()
            stack = [(0, 0)]
            while stack:
                r, c = stack.pop()
                if r == (n - 1) and c == (n - 1):
                    return True
                visited.add((r, c))
                for r_dir, c_dir in directions:
                    new_r, new_c = r + r_dir, c + c_dir
                    if not (0 <= new_r < n and 0 <= new_c < n) or (new_r, new_c) in visited or grid[new_r][new_c] > t:
                        continue
                    stack.append((new_r, new_c))

            return False
        
        left = grid[0][0]
        right = -1
        for i in range(n):
            for j in range(n):
                right = max(right, grid[i][j])
        
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
                    
