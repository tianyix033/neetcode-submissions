from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_map = defaultdict(list)
        for src, dest in tickets:
            adj_map[src].append(dest)
        
        res = []

        def dfs(src):
            while adj_map[src]:
                dest = adj_map[src].pop()
                dfs(dest)
            res.append(src)

        dfs("JFK")
        return res[::-1]