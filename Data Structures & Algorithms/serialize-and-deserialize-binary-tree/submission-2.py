# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')              
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = data.split(',')
        queue = deque()
        res = None
        for i, node_val in enumerate(lst):
            node = TreeNode(node_val) if node_val != 'None' else None
            if node:
                queue.append([node, False])
            if i == 0:
                res = node
                continue
            if queue[0][1]:
                parent, _ = queue.popleft()
                parent.right = node
            else:
                queue[0][0].left = node
                queue[0][1] = True

        return res



