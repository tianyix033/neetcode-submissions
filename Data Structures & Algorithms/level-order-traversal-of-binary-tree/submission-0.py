# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if root is None:
            return res
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            if len(res) > level:
                res[level].append(node.val)
            elif len(res) == level:
                res.append([node.val])
            else:
                raise Exception("This shouldn't happen.")
        
        return res
