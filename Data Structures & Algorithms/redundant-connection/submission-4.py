class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = [[] for _ in range(n + 1)]
        neighbors_count = [0] * (n + 1)
        for x, y in edges:
            neighbors[x].append(y)
            neighbors_count[x] += 1
            neighbors[y].append(x)
            neighbors_count[y] += 1

        remove_list = []
        for node, count in enumerate(neighbors_count):
            if count == 1:
                remove_list.append(node)

        while remove_list:
            node = remove_list.pop()
            neighbors_count[node] -= 1
            adjacents = neighbors[node]
            for adjacent in adjacents:
                neighbors_count[adjacent] -= 1
                if neighbors_count[adjacent] == 1:
                    remove_list.append(adjacent)

        for x, y in reversed(edges):
            if neighbors_count[x] == 2 and neighbors_count[y] == 2:
                return [x, y]