import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        if not root: return root
        
        mp = collections.defaultdict(list)
        
        def getDepth(level, root, s):
            mp[level].append(s)
            if not root: return ""
            if root.left: getDepth(level+1, root.left, s + [str(root.left.val)])
            if root.right: getDepth(level+1, root.right, s + [str(root.right.val)])
            
            
        getDepth(0, root, [str(root.val)])
        
        # print(mp)
        def getSubtree(root):
            m  = max(mp.keys())
            paths = mp[m]
            
            # print(paths)
            pos = 0 
            flag = False
            while  pos < len(paths[0]):
                for i in range(1, len(paths)):
                    if paths[i][pos] != paths[i-1][pos]:
                        flag = True
                        break
                if flag: break
                pos += 1
            tmp = int(paths[0][pos-1]) if len(paths) != -1 else  int(paths[0][-1])
            pos = 0
            # print(tmp)
            while root.val != tmp:
                if root.left and root.left.val == int(paths[0][pos]):
                    root = root.left
                elif root.right and root.right.val == int(paths[0][pos]):
                    root = root.right
                pos+=1
            return root
            
        
        return getSubtree(root)
        ## mp ={ cnt_depth: "abc"}
        
        
        
        
        
