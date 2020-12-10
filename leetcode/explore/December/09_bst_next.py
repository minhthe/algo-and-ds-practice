# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    
    def traverse(self, node):
        if not node: return []
        return self.traverse(node.left) + [node.val] + self.traverse(node.right)
        
    def __init__(self, root: TreeNode):
        self.tree = root   
        self.arr = self.traverse(root)
        
        self.pointer = -1
        
        return None        

    def next(self) -> int:
        self.pointer += 1
        return self.arr[self.pointer]
    
    def hasNext(self) -> bool:
        return self.pointer < len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()