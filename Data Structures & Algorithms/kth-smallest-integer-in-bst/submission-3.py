# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        res = -1
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    res = curr.val
                curr = curr.right
            else:
                left_pred = curr.left
                while left_pred.right and left_pred.right != curr:
                    left_pred = left_pred.right
                if left_pred.right == curr:
                    k -= 1
                    if k == 0:
                        res = curr.val
                    left_pred.right = None
                    curr = curr.right
                else:
                    left_pred.right = curr
                    curr = curr.left

        return res