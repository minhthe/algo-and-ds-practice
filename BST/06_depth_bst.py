# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        current_node = [root]
        cnt = 0
        
        while current_node:
            cnt += 1
            next_node = []            
            for node in current_node:                
                if node.left: next_node.append(node.left)        
                if node.right: next_node.append(node.right)                    
            current_node = next_node 
            
        return cnt