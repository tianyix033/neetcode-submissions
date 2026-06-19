# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if root is None:
            return 0
        height = 1 + max(self.height(root.left), self.height(root.right))
        return height

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height + right_height, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
