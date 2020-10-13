''''https://leetcode.com/problems/populating-next-right-pointers-in-each-node/'''
class Solution:
	def connect(self, root: 'Node') -> 'Node':
		current = [root]
		while root and current:
			next_point = []
			current[-1].next = None
			before = None
			for point in current:
				if before:
					before.next = point
				
				before = point
				if point.left: next_point.append(point.left)
				if point.right: next_point.append(point.right)
			current = next_point
		return root