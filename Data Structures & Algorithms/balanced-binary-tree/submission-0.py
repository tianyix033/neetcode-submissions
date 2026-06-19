# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return 0, True
            left_height, left_balance = helper(root.left)
            right_height, right_balance = helper(root.right)
            if not (left_balance and right_balance):
                return -1, False
            else:
                return 1 + max(left_height, right_height), abs(left_height - right_height) <= 1
        return helper(root)[1]