'''https://leetcode.com/problems/populating-next-right-pointers-in-each-node/'''
import collections
class Solution:
	def connect(self, root: 'Node') -> 'Node':
		mp = collections.defaultdict(list)
		que = [(root,0)]
		while root and que:
			point, level = que.pop(0)
			mp[level].append(point)
			if point.left :
				que.append( ( point.left, level + 1 ) )
			if point.right:
				que.append( ( point.right, level + 1 ) )
		
		for key in mp:
			for i,v in enumerate(mp[key]):
				if i == len(mp[key]) - 1 : 
					v.next = None
				else: v.next = mp[key][i+1]
				
		return root