class Solution:
	def maxAncestorDiff(self, root: TreeNode) -> int:
		
		
		rst = []
		def f(root, min_v, max_v, diff):
			
			if not root.left and not root.right: 
				return max(diff , max_v - min_v)
			l , r = 0 , 0	
			if root.left: l =  f(root.left , min(min_v, root.left.val), max(max_v, root.left.val), diff)
			if root.right: r = f(root.right, min(min_v, root.right.val), max(max_v, root.right.val), diff)
			return max(l, r)
		
		return f(root, root.val, root.val, 0)