'''https://leetcode.com/problems/binary-tree-postorder-traversal'''

class Solution:
	def postorderTraversal(self, root: TreeNode) -> List[int]:
		
		rst = []
		def f(root):
			if not root: return []
			return f(root.left) + f(root.right) + [root.val]
		return f(root)