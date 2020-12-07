"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        cur = [root]
        while cur:
            nxt = []
            for i, node in enumerate(cur):
                
                if node.left:
                    nxt.append(node.left)
                
                if node.right:
                    nxt.append(node.right)
                    
                if i == len(cur) -1 :
                    break
                    
                node.next = cur[i+1]
            cur = nxt
                
        return root     