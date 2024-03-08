# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Description: 
# Given the root of a binary tree, invert the tree, and return its root.

class Solution:
    def invertTree(self, root):
        if not root: 
            return     
          
        #Recursively traverse tree node by node:
        self.invertTree(root.left)
        self.invertTree(root.right)

        # temp -> left ; left -> right ; right -> left 
        temp = root.left 
        root.left = root.right
        root.right = temp
        return root
