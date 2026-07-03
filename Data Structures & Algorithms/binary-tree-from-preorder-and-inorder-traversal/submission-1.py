# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: i for i, val in enumerate(inorder)}
        
        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_start >= preorder_end or inorder_start >= inorder_end:
                return None
            root = TreeNode(preorder[preorder_start])
            mid = hashmap[root.val] - inorder_start
            root.left = helper(preorder_start + 1, preorder_start + mid + 1, inorder_start, inorder_start + mid)
            root.right = helper(preorder_start + mid + 1, preorder_end, inorder_start + mid + 1, inorder_end)
            return root

        return helper(0, len(preorder), 0, len(inorder))

            