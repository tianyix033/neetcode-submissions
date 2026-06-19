# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, root.val))
        res = 0
        while queue:
            node, path_max = queue.popleft()
            if node.val >= path_max:
                res += 1
                path_max = node.val
            if node.left:
                queue.append((node.left, path_max))
            if node.right:
                queue.append((node.right, path_max))
        return res