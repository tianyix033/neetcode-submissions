class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False] * n
        neighbors = [[] for _ in range(n)]
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        def dfs(node):
            visited[node] = True
            for neighbor in neighbors[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        counter = 0
        for i in range(n):
            if not visited[i]:
                counter += 1
                dfs(i)
        
        return counter
            
        