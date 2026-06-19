# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root is None:
            return 0, 0
        left_height, left_diameter = self.height(root.left)
        right_height, right_diameter = self.height(root.right)
        height = 1 + max(left_height, right_height)
        diameter = max(left_height + right_height, left_diameter, right_diameter)
        return height, diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.height(root)[1]