'''
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

Two steps:
1 Build the heap -> O(n)
2 Get the result by the order priority -> O(log(n))
'''
import heapq
import collections
class Solution:
	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
		que = []
		heapq.heapify(que)		
		cur_node = [(0,0,root)]
		while cur_node:
		
			next_node = []
			for node in cur_node: 
				x,y,z = node
				heapq.heappush(que, (x , -y, z.val)  )
				if z.left: next_node.append((x-1, y -1, z.left))
				if z.right: next_node.append((x+1, y -1, z.right))
			cur_node = next_node
		mp = collections.defaultdict(list)
		rst = [] 
		child = []
		xx = None
		while que:
			x, y, z = heapq.heappop(que)
			if xx != x:
				if child: rst.append(child)
				child = []
				child.append(z)
				xx = x
			else:				
				child.append(z)
		if child: rst.append(child)				
		return rst