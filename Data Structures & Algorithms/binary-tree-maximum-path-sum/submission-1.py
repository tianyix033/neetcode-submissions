# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def helper(root):
            nonlocal res
            if not root:
                return 0

            left_max = max(0, helper(root.left))
            right_max = max(0, helper(root.right))
            res = max(res, left_max + right_max + root.val)
            return root.val + max(left_max, right_max)

        helper(root)
        return res