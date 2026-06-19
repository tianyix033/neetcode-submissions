# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if root is None:
                return True, None, None
            left_valid, left_min, left_max = helper(root.left)
            right_valid, right_min, right_max = helper(root.right)
            left_true = left_max < root.val if left_max else True
            right_true = right_min > root.val if right_min else True
            if not (left_valid and right_valid and left_true and right_true):
                return False, None, None
            new_max = right_max if right_max else root.val
            new_min = left_min if left_min else root.val
            return True, new_min, new_max

        return helper(root)[0]
            