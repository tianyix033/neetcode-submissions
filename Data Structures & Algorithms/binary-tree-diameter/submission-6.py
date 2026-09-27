# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0, 0
            left_max, left_root_max = helper(root.left)
            right_max, right_root_max = helper(root.right)
            max_through_root = left_root_max + 1 + right_root_max
            max_on_root = max(left_root_max, right_root_max) + 1
            return max(left_max, right_max, max_through_root, max_on_root), max_on_root
        
        return helper(root)[0] - 1