# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        rst = 1
        que = [(root,rst)]
        while que:
            u, l = que.pop()
            rst = max(rst, l)
            if u.left: que.append((u.left, l + 1))
            if u.right: que.append((u.right, l + 1))
        
        return rst
        
        
        
        