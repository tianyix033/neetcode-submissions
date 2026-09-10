class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_map = defaultdict(list)
        for src, dest in tickets:
            adj_map[src].append(dest)
        stack = ["JFK"]
        res = []
        while stack:
            pos = stack[-1]
            if not adj_map[pos]:
                res.append(stack.pop())
            else:
                stack.append(adj_map[pos].pop())

        return res[::-1]

        