'''https://leetcode.com/problems/symmetric-tree'''
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = collections.deque([root.left, root.right])
        while queue:
            
            t1 = queue.popleft()
            t2 = queue.popleft()
            if t1 is None and t2 is None:
                continue
            if t1 and t2 and t1.val == t2.val:
                queue.append(t1.left)
                queue.append(t2.right)
                queue.append(t1.right)
                queue.append(t2.left)
            else:
                return False
        return True
            