from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        print(neighbors)
        
        trail = set()
        sequence = []
        res = []
        def dfs(node, prev):
            nonlocal res
            for neighbor in neighbors[node]:
                if neighbor != prev:
                    sequence.append(neighbor)
                    if neighbor in trail:
                        res = sequence.copy()
                        return 
                    trail.add(neighbor)
                    dfs(neighbor, node)
                    if res:
                        return
                    trail.remove(neighbor)
                    sequence.pop()
            return False

        trail.add(1)
        sequence.append(1)
        dfs(1, None)
        knot = res[-1]
        loop_start = res.index(knot)
        options = set()
        for i in range(loop_start, len(res) - 1):
            x, y = res[i], res[i + 1]
            options.add((x, y))
            options.add((y, x))
        for x, y in reversed(edges):
            if (x, y) in options or (y, x) in options:
                return [x, y]

        


