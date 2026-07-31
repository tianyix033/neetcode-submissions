class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = [[] for _ in range(n + 1)]
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        visited = [False] * (n + 1)
        loop_start = -1
        options = [False] * (n + 1)
        def dfs(node, prev):
            nonlocal loop_start
            if visited[node]:
                loop_start = node
                return True
            visited[node] = True
            for neighbor in neighbors[node]:
                if neighbor == prev:
                    continue
                found = dfs(neighbor, node)
                if loop_start > 0:
                    options[node] = True
                    if node == loop_start:
                        loop_start = -1
                if found:
                    return True
            return False

        dfs(1, None)
        for x, y in reversed(edges):
            if options[x] and options[y]:
                return [x, y]

                