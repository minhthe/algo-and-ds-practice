'''https://leetcode.com/problems/symmetric-tree/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        
        def f(rootLeft , rootRight):
            if rootLeft is None and rootRight is None:
                return True
            if rootLeft and rootRight and rootLeft.val == rootRight.val:
                return f(rootLeft.left, rootRight.right) and f(rootLeft.right, rootRight.left)
            return False
            
        return f(root.left, root.right)
       