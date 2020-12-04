# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def f(root):
            if not root: return []
            return f(root.left) + [root.val] + f(root.right)        
        rst = f(root)       
        root = TreeNode(rst[0])
        new_root = root
        for i, item in enumerate(rst):
            if i == 0: continue
            new_root.right = TreeNode(item)
            new_root = new_root.right      
        return root