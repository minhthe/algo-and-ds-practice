'''https://leetcode.com/problems/maximize-distance-to-closest-person/'''
class Solution:
	def maxDistToClosest(self, seats: List[int]) -> int:
		
		n = len(seats)
		
		x, y , z = 0 , 0 , 0 
		flag = False
		pre = -1
		for i, v in enumerate(seats):
			if v == 1 and flag == False:
				flag = True
				x = i 
				pre = i 
				z = n - 1 - i
				continue
			if v == 1 : 
				y = max(y, (i - pre) // 2  )
				pre = i 
				z = n - 1 - i
		rst = max(x,y,z)
		return rst