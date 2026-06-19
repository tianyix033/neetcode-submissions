"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(node):
            if node is None:
                return 
            if node in visited:
                return visited[node]
            new_node = Node(node.val)
            visited[node] = new_node
            new_neighbors = []
            for neighbor in node.neighbors:
                new_neighbors.append(dfs(neighbor))
            new_node.neighbors = new_neighbors
            visited[node] = new_node
            return new_node
        
        return dfs(node)
            
        