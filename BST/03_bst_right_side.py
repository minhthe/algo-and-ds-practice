'''https://leetcode.com/problems/binary-tree-right-side-view/'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rst =  []
        if not root: return rst
        que = [root]
        while que:
            
            next_item = []
            for i, v in enumerate((que)):
                if i == len(que) -1:
                    rst.append(v.val)
                if v.left: next_item.append(v.left)
                if v.right: next_item.append(v.right)
            que = next_item
        
        return rst