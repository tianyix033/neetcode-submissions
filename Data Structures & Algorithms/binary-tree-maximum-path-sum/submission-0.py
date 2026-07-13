# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # return: maxPathSum overall and maxPathSum if we must use root 
        # (thus allowing our parent to form a path with us)
        def helper(root):
            if root is None:
                return float('-inf'), float('-inf')
            left_max_overall, left_max_root = helper(root.left)
            right_max_overall, right_max_root = helper(root.right)
            max_root = max(root.val, left_max_root + root.val, right_max_root + root.val)                
            max_overall = max(max_root, left_max_overall, right_max_overall,\
                left_max_root + right_max_root + root.val)
            return max_overall, max_root

        return helper(root)[0]