class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        visited = [False] * n
        seen = [False] * n
        adj_lst = [[] for i in range(n)]
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)

        def dfs(node):
            visited[node] = True
            for neighbor in adj_lst[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        dfs(0)
        return (False not in visited)
            