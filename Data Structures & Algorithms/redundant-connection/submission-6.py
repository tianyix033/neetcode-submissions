class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n + 1)]
        ranks = [1] * (n + 1)

        def find(n):
            if parents[n] != n:
                parents[n] = find(parents[n])
            return parents[n]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if ranks[p1] <= ranks[p2]:
                parents[p1] = parents[p2]
            else:
                parents[p2] = parents[p1]
            ranks[p1], ranks[p2] = ranks[p1] + ranks[p2], ranks[p1] + ranks[p2]
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]