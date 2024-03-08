# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Description: 
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #If current node is the target p or q, return current node
        if not root or root == p or root == q: 
            return root
        #Find p or q in left and right sub-trees
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        #If both left and right subtrees are present, then return root
        if l and r: 
            return root 
        #If only one sub tree is available, then both p and q are found in q, return the left/right subtree node accordingly. 
        return l if l else r 

