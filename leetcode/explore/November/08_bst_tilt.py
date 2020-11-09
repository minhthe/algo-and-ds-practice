'''https://leetcode.com/problems/binary-tree-tilt/'''
class Solution:
	def findTilt(self, root: TreeNode) -> int:
		s =  []
		def f(root):
			if root is None: return 0
			l = f(root.left)
			r = f(root.right)
			s.append(abs(l-r))
			return l + r + root.val
			
		f(root)
		return sum(s)