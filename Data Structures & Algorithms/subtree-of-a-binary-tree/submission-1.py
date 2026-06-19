# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = []
        serialized_subRoot = []
        def serialize(root, arr):
            if root is None:
                arr.append("#")
            else:
                arr.append(str(root.val))
                serialize(root.left, arr)
                serialize(root.right, arr)

        serialize(root, serialized_root)
        serialize(subRoot, serialized_subRoot)
        serialized_root = "$".join(serialized_root)
        serialized_subRoot = "$".join(serialized_subRoot)
        return serialized_subRoot in serialized_root