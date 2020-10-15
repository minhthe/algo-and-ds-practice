'''https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/'''
import collections
class Solution:
	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:	
		mp  = collections.defaultdict(list)
		que = [(root, 0, 0 )] # x  y
		while que:
		
			tmp = []
			for item in que:
				u, x , y  = item
				mp[x].append( (-y , u.val) )
				if u.left: tmp.append((u.left, x - 1, y - 1 ))
				if u.right: tmp.append((u.right, x + 1, y -  1))
			que = tmp
	
		
		
		rst = []
		for item in sorted(mp.items(), key = lambda x: x[0]):
			tmp = []
			for u,v in sorted(item[1]):
				tmp.append(v)
			rst.append(tmp)
		return rst