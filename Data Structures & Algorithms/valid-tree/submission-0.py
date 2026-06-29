class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = [False] * n
        adj_lst = [[] for i in range(n)]
        for x, y in edges:
            adj_lst[x].append(y)
            adj_lst[y].append(x)
        # print(adj_lst)

        def dfs(i, pred):
            res = True
            seen[i] = True
            for neighbor in adj_lst[i]:
                if pred is not None and pred == neighbor:
                    continue
                if seen[neighbor]:
                    return False
                res = res and dfs(neighbor, i)
            return res

        no_cycle = dfs(0, None)
        # print(seen)
        return no_cycle and (False not in seen)
