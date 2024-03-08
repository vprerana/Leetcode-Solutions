# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      res = 0 
      def dfs(node):
        nonlocal res 
        if not node: 
          #If last node, then return 0 - no child nodes
          return 0 
        else: 
          lh = dfs(node.left) 
          rh = dfs(node.right) 
          # Node has 2 decisions to make
          # Assume diameter passes through the node : res = max (res, lh+rh) 
          res = max(res, lh+rh) 
          # There might be more nodes at the top increasing the overall diameter 
          # Send max height at the node + edge connecting to the top. 
          return max(lh, rh) + 1
      dfs(root) 
      return res
      
      
