# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Description: 
# Given the root of a binary tree, return its maximum depth.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        else: 
            lh = self.maxDepth(root.left)
            rh = self.maxDepth(root.right)
            depth = max(lh, rh) + 1 
            return depth 
        
