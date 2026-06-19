# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            else:
                return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        stack = [root]
        while stack:
            node = stack.pop()
            if isSameTree(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


            