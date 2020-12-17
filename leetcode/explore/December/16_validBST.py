# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        que = [(root, -int(1e32), int(1e32))]
        while que:
            p, sub_l, sub_r = que.pop()
            if not( sub_l < p.val < sub_r ): return False
            if p.left : que.append((  p.left, sub_l , p.val    ))
            if p.right : que.append((  p.right, p.val , sub_r    ))
        return True