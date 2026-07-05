class DSU:
    def __init__(self, n):
        self.leaders = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x):
        if x != self.leaders[x]:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x, y):
        x_leader = self.find(x)
        y_leader = self.find(y)
        if x_leader == y_leader:
            return False

        if self.sizes[x_leader] < self.sizes[y_leader]:
            self.leaders[x_leader] = y_leader
            self.sizes[y_leader] += self.sizes[x_leader]
        else:
            self.leaders[y_leader] = x_leader
            self.sizes[x_leader] += self.sizes[y_leader]

        return True        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for x, y in edges:
            if dsu.union(x, y):
                res -= 1

        return res
        