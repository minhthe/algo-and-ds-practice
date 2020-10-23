# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        min_v = 1
        if not root: return 0
        def f(root, l):
            if not root: return int(1e9)
            if not (root.right or root.left) : return l
            a =    f(root.left, l + 1)
            b =    f(root.right, l + 1)
            return min(a,b)
        return f(root, 1)