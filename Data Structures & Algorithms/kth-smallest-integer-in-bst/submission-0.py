# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class PersonalError(Exception):
    def __init__(self, val):
        self.val = val

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        def inorder(root):
            nonlocal counter
            if root is None:
                return
            inorder(root.left)
            counter += 1
            if counter == k:
                raise PersonalError(root.val)
            inorder(root.right)

        try:
            inorder(root)
        except PersonalError as e:
            return e.val
            

        