class Solution:
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		stk =  [root]
		s = 0 
		
		while stk:
			u = stk.pop()
			if low <= u.val <= high: s += u.val
			if u.left and u.val > low: stk.append(u.left)
			if u.right and u.val < high: stk.append(u.right)
			
		return s