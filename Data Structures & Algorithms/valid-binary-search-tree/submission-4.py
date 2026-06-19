# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if root is None:
                return True
            if not left < root.val < right:
                return False
            left_valid = helper(root.left, left, root.val)
            right_valid = helper(root.right, root.val, right)
            return left_valid and right_valid

        return helper(root, -1001, 1001)