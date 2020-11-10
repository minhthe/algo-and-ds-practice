class Solution:
	def maxAncestorDiff(self, root: TreeNode) -> int:	
		rst = []		
		def f(tmp, root):			
			if not root.left and not root.right: rst.append(tmp)		
			if root.left: f(tmp + [root.left.val], root.left)
			if root.right: f(tmp + [root.right.val], root.right)
			return rst
		
		f([root.val],root)
		m = 0
		for item in rst:
			m = max(m, max(item) - min(item))
		return m 