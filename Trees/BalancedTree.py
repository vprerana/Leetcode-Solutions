# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Description: Given a binary tree, determine if it is height balanced. 
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      def dfs(node): 
        if not node: 
          return 0 
        else: 
          # Calculate left and right height 
          lh = dfs(node.left)
          rh = dfs(node.right)
          # Propogate imbalance
          if lh < 0 or rh < 0 or abs(lh-rh) > 1: 
            return -1 
          # Tell the parent that node is balanced and the max height calculated for node. 
          return max(lh, rh) + 1 
      return dfs(root) >= 0 
